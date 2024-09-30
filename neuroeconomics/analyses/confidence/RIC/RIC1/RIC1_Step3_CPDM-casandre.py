"""
===================
Mandy Renfro (2024)
===================
"""

from glob import glob
import ipyparallel as ipp
#import matplotlib.pyplot as plt
import numpy as np
from numpy import exp, linspace, log, sqrt, sum
np.seterr(all = "ignore")
import os
from os.path import join
import pandas as pd
from scipy import stats
from scipy.optimize import minimize
from scipy.special import erfcinv
normcdf = stats.norm.cdf
#import seaborn as sns
#sns.set_theme(style="white", palette="muted")
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
import time

base_proj_dir = "Z:/data/RIC" ## base project directory
data_dir      = "Z:/data/RIC/sourcedata/RIC1" ## directory containing data
save_proj_dir = os.path.join(base_proj_dir, "derivatives/RIC1/parameter_estimation/cpdm") ## output directory
n_cores = 14 ## number of processing cores (14 Ss at a time)

## CASANDRE parameters
cruns         = 10   ## CASANDRE runs per Ss
sample_rate   = 30   ## higher values produce slower, more precise estimates
delta         = 5    ## SDs below and above mean, computes confidence variable distributions
noise_sens    = 1    ## if sensory noise == 1, distributions of decision variable and confidence variable can be compared directly
## CASANDRE options
options       = dict(maxiter = 250, disp = False) ## primary factor influencing runtime


def casandre_fit(guess_rate, stim_sens, stim_crit, meta_uncert, conf_crit, stim_vals):
    """ Compute llh of each response alternative
        Step 1 - sample decision variable denominator in steps of constant cumulative density.
        Step 2 - compute choice distribution under each scaled sensory distribution.
        Step 3 - average across all scaled sensory distributions to get likelihood functions.
        **Linear transformation of normal variable is itself normal variable.
        **Inverse of denominator used here to work with products instead of ratios.
        INPUT
        - params:    CASANDRE parameters [guessRate, stimSens, stimCrit, uncMeta, confCrit]
        - stim_vals: stimulus conditions in units of stimulus magnitude
        OUTPUT
        - choice_ll: likelihood of each choice (2 x # confidence levels x N stim_vals) 
    """
    np                  = numpy
    sens_mean           = stim_vals * stim_sens ## ??? piece of numerator (SNR) with unknown specific name
    sens_crit           = stim_crit * stim_sens ## second piece of numerator (SNR)
    x                   = [-conf_crit, 0, conf_crit] ## bounds splitting conf space into four quadrants (determined by conf levs)
    guess_rate_weight   = guess_rate / (len(x) + 1) ## weigh by number of regions in confidence space
    choice_llh          = np.zeros((len(x) + 1, len(stim_vals))) ## setting up short vector of 4 x conditions (or trials?)
    sample_rate_div     = 0.5 / sample_rate ## optimization
    meta_power          = meta_uncert**2 ## optimization
    mu_log_n            = log((noise_sens**2) / sqrt(meta_power + noise_sens**2)) ## mean of prob space accounting for metauncertainty
    sigma_log_n         = sqrt(log((meta_power) / (noise_sens**2) + 1)) ## SD of prob space accounting for metauncertainty
    ## inverse of sensitivity to decision reliability (denominator of SNR)
    dv_Den_x            = 1 / logninv(linspace(sample_rate_div, 1 - sample_rate_div, sample_rate),  mu_log_n, sigma_log_n).reshape(-1, 1)
    sigma               = dv_Den_x * noise_sens ## SD of confidence space
    
    for stim_idx in range(len(stim_vals)): ## iterates through trials for given contrast
        ## incorporated 1/denominator above loop to improve computational efficiency
        mu = dv_Den_x * (sens_mean[stim_idx] - sens_crit) ## 1/denominator * numerator (SNR)
        p  = normcdf(repeat_matrix_function_2D(x, sample_rate, 1), ## cumsum at each bound of x
                    repeat_matrix_function_2D(mu, 1, len(x)), 
                    repeat_matrix_function_2D(sigma, 1, len(x)))
        ratio_dist_p = np.mean(p, axis = 0) ## gets avg cumsum up to each x bound
        #### Get probabilities of each quad and weight them by guessrate to use as likelihoods
        ## delta cumsum of mid-quadrants to get specific probabilities
        choice_llh[1:-1, stim_idx] = guess_rate_weight + (1 - guess_rate) * (ratio_dist_p[1:] - ratio_dist_p[:-1])
        ## cumsum of first quadrant
        choice_llh[   0, stim_idx] = guess_rate_weight + (1 - guess_rate) * (ratio_dist_p[0])
        ## cumsum of last quadrant
        choice_llh[  -1, stim_idx] = guess_rate_weight + (1 - guess_rate) * (1 - ratio_dist_p[-1])
    return choice_llh


def _logninv(p):
    """ Returns log inverse only when mu = 0 and sigma = 1.
        INPUT
        - p: one or more cumsums of log normal distribution
        OUTPUT
        - log inverse
    """
    return exp(-sqrt(2) * erfcinv(2 * p))


def logninv(p, mu, sigma):
    """ Returns log inverse not only for mu = 0 and sigma = 1.
        If you want to get the log normal inverse of a cumsum (p),
        you can use a definitional trick to compute it with a function that 
        only provides the inverse with mu = 0 and sigma = 1 because:
        --> log(logninv(p, mu, sigma)) == mu + sigma * log(logninv(p, 0, 1))
        the inverse of the natural log is exp()
        --> exp(log(logninv(p, mu, sigma))) == logninv(p, mu, sigma)
        INPUT
        - p: one or more cumsums of log normal distribution
        - mu: avg of distribution
        - sigma: SD of distribution
        OUTPUT
        - log inverse
    """
    return exp(mu + sigma * log(_logninv(p)))


def neg_ll(params_vec, stim_vals, choices, all_run_idx, all_contrast_idx, neg_llh_size):
    """ Returns negative log likelihood for entire parameter vector.
        INPUT
        - param_vec: list of all modeling parameters
        - stim_vals: list of stimulus orientations grouped by condition and contrast
        - choices: list of Ss choice grouped by condition and contrast
        - all_run_idx: np.where results identifying locations of trials within each run
        - all_contrast_idx: np.where results identifying locations of trials within each contrast
        - neg_llh_size: precounted number of summed log likelihoods
        OUTPUT
        - returns final sum of negative log likelihood for model parameters across contrasts 
        and runs (called up to 250 times per crun)
    """
    np               = numpy
    max_contrast_len = 0 ## optimization
    for key in all_contrast_idx: ## optimization
        max_contrast_len = max(max_contrast_len, len(all_contrast_idx[key])) ## optimization
    max_contrast_len1 = 1 + max_contrast_len ## optimization
    max_contrast_len2 = max_contrast_len1 + max_contrast_len ## optimization
    max_contrast_len3 = max_contrast_len2 + len(all_run_idx) ## optimization
    neg_llh           = np.zeros(neg_llh_size) ## empt array to hold negative LLHs
    counter           = 0 ## keep track of where to store each LLH
    for idx_run in range(len(all_run_idx)): ## each condition run
        run_stim_vals = stim_vals[all_run_idx[idx_run]] ## stim vals for current run
        run_choices   = choices[all_run_idx[idx_run]] ## choices for current run
        for idx_contrast in range(len(all_contrast_idx[idx_run])): ## each contrast for current run
            ## CASANDRE parameters
            guess_rate, stim_sens, stim_crit, meta_uncert, conf_crit = params_vec[(np.array([0, 
                                                                                    1 + idx_contrast,
                                                                                    max_contrast_len1 + idx_contrast,  
                                                                                    max_contrast_len2 + idx_run, 
                                                                                    max_contrast_len3 + idx_run]))]
            unique_stim_choices = run_choices[all_contrast_idx[idx_run][idx_contrast]] ## corresponding choices for each stimulus
            choice_llh          = casandre_fit(guess_rate, stim_sens, stim_crit, meta_uncert, conf_crit, ## executing CASANDRE
                                                run_stim_vals[all_contrast_idx[idx_run][idx_contrast]])
            neg_llh[counter]    = -sum(unique_stim_choices * log(choice_llh.T)) ## summed negative LLHs of choices for current contrast and run
            counter += 1 ## increment index in neg_llh
    return np.nansum(neg_llh)


def random_bounded(bounds):
    """ Generate random value within parameter range.
        INPUT
        - bounds: tuple containing minimum and maximum values of parameter range.
        OUTPUT
        - returns random value within bounded range.
    """
    np = numpy
    return np.random.random() * (bounds[1] - bounds[0]) + bounds[0]


def repeat_matrix_function_2D(arr, x, y = 1):
    """ Python implementation of MATLAB's repmat().
        INPUT
        - arr: array to be copied
        - x:   number of rows
        - y:   number of columns
        OUTPUT
        - new_arr: new array 
    """
    np      = numpy
    new_arr = arr.copy()
    for i in range(1, x):
        new_arr = np.vstack((new_arr, arr))
    arr_h   = new_arr.copy()
    for i in range(1, y):
        new_arr = np.hstack((new_arr, arr_h))
    return new_arr


def sub_func(idx, sub): ## iterate through Ss IDs
    np = numpy
    pd = pandas
    if idx + 1 <= skip_num: ## checks if current Ss has already been run
        return ## go to next Ss
    sub_files = sorted(glob(os.path.join(data_dir, "2*_IDM_{0}.csv".format(sub)))) ## grab all IDM task csvs
    sub_cols  = ["run_dims", "orient", "contrast", "acc", "conf", "choice"] ## trial/Ss resp elements
    sub_df    = pd.DataFrame(columns = sub_cols) ## Ss-specific dataframe w/ preset columns
    raw_df    = pd.read_csv(sub_files[0]) ## open current data file
    df        = raw_df.loc[(raw_df["cpdm_trial_type"] == "task") & (raw_df["cpdm_trial_resp.keys"].notnull())] ## only CPDM task trials w/ responses
    sub_df["run_dims"] = df["cpdm_run_dimension"] ## dimensions for current trial (volatility/risk levels = number/difficulty of orientations/contrasts)
    sub_df["orient"]   = df["cpdm_gabor_orient"] ## orientation of stimulus (gabor patch)
    sub_df["contrast"] = df["cpdm_gabor_contrast"] ## contrast of stimulus (gabor patch)
    sub_df["acc"]      = df["cpdm_acc"] ## Ss accuracy
    sub_df["conf"]     = df["cpdm_conf"] ## Ss confidence in perceptual accuracy
    sub_df["choice"]   = df["cpdm_trial_resp.keys"] ## trial choice (q=high conf/left tilt; a=low conf/left tilt; p=high conf/right tilt; l=low conf/right tilt)
    choice_dict        = {'q':-2, 'a':-1, 'l':1, 'p':2} ## remap CPDM choice responses 
    sub_df["choice"]   = df["cpdm_trial_resp.keys"].replace(choice_dict) ## replace old choices with remapped values
    stim_vals     = sub_df["orient"].values ## all stimulus orientations for current sub
    contrast_vals = sub_df["contrast"].values ## all stimulus contrast values for current sub
    choices       = sub_df["choice"].values ## all choice decisions for current sub
    math_choices  = np.zeros((len(choices), len(choice_dict.keys()))) ## zeros matrix to contain choice arrays
    math_choices[np.where(choices ==  2)] = np.array([0, 0, 0, 1]) ## choice array for high conf/right tilt
    math_choices[np.where(choices ==  1)] = np.array([0, 0, 1, 0]) ## choice array for low conf/right tilt
    math_choices[np.where(choices == -1)] = np.array([0, 1, 0, 0]) ## choice array for low conf/left tilt
    math_choices[np.where(choices == -2)] = np.array([1, 0, 0, 0]) ## choice array for high conf/left tilt
    all_run_idx      = [] ## list of list of trial indices by condition [low_vol_no_risk, low_vol_low_risk, low_vol_high_risk]
    all_contrast_idx = {} ## dictionary containing tuples of arrays for indices of contrasts organized by run (keys)
    nll_counter      = 0 ## number of times LL is placed in NLL array
    for idx_run, run_label in enumerate(sorted(sub_df["run_dims"].unique())): ## iterate through conditions (runs)
        trial_idx  = np.where(sub_df["run_dims"].values == run_label) ## current run indices
        all_run_idx.append(trial_idx) ## append current run index list to all_run_idx
        run_contrast_vals = contrast_vals[trial_idx] ## contrast values for current run indices
        all_contrast_idx[idx_run] = [] ## create key and empty value array for current run
        for unique_contrast in sorted(np.unique(run_contrast_vals)): ## iterate through unique stimulus contrast values
            unique_contrast_idx = np.where(run_contrast_vals == unique_contrast) ## indices for current contrast within current run
            all_contrast_idx[idx_run].append(unique_contrast_idx) ## add unique contrast indices to all_contrast_idx under appropriate key
            nll_counter += len(unique_contrast_idx) ## increment nll_counter by number of current contrast trials
    best_param_est = None ## set empty best params variable
    best_nll = None
    run_labels     = dict(low_vol_low_risk = "LVLR", low_vol_high_risk = "LVHR", 
                            high_vol_low_risk = "HVLR", high_vol_high_risk = "HVHR") ## output column identifiers
    for crun in range(cruns): ## CASANDRE runs
        #crun_start_time = time.time()
        ## prints current Ss number and current CASANDRE run
        #print("-------------> Currently running sub-{0}".format(sub), "on CASANDRE Run #", "{0:02d}".format(crun+1), end = "")
        search_start = [random_bounded(guess_rate_bounds)] ## starting point for current CASANDRE run
        bounds       = [guess_rate_bounds] ## list containing parameter bounds (starting points for each param space added below)
        column_names = ["subID", "Guess Rate"] ## parameter output column names
        for curr_contrast in sorted(np.unique(contrast_vals)): ## for each level of contrast
            search_start.append(random_bounded(stim_sens_bounds)) ## random stimulus sensitivity starting point (bounded)
            bounds.append(stim_sens_bounds) ## stimulus sensitivity bounds
            column_names.append("Stimulus Sensitivity {}".format(curr_contrast)) ## stimulus sensitivity column label
        for curr_contrast in sorted(np.unique(contrast_vals)): ## for each level of contrast
            search_start.append(random_bounded(stim_crit_bounds)) ## random stimulus criterion starting point (bounded)
            bounds.append(stim_crit_bounds) ## stimulus criterion bounds
            column_names.append("Stimulus Criterion {}".format(curr_contrast)) ## stimulus criterion column label
        for curr_run in sorted(sub_df["run_dims"].unique()): ## for each conditional run
            search_start.append(random_bounded(meta_uncert_bounds)) ## random meta uncertainty starting point (bounded)
            bounds.append(meta_uncert_bounds) ## meta uncertainty bounds
            column_names.append("Meta Uncertainty {}".format(run_labels[curr_run])) ## meta uncertainly column label
        for curr_run in sorted(sub_df["run_dims"].unique()): ## for each conditional run
            search_start.append(random_bounded(conf_crit_bounds)) ## random confidence criterion starting point (bounded)
            bounds.append(conf_crit_bounds) ## confidence criterion bounds
            column_names.append("Confidence Criterion {}".format(run_labels[curr_run])) ## confidence criterion column label
        search_start = np.array(search_start) ## convert to numpy array
        estimate = minimize(neg_ll, 
                            x0      = search_start, ## optimizer starting point
                            method  = "L-BFGS-B", ## descent direction by preconditioning gradient with curvature info (b = boundary limits)
                            bounds  = bounds, ## dimensional bounds for each parameter
                            args    = (stim_vals, math_choices, all_run_idx, all_contrast_idx, nll_counter), 
                            options = options) ## number of maxiters
        if best_nll is None or estimate.fun < best_nll:
        #crun_end_time = time.time()
        ## prints number of iters required for convergence of --previous-- CASANDRE run
        #print(" | Last crun iters: {0:03d} | Last crun time: {1:03d}".format(estimate.nit, int(crun_end_time-crun_start_time)), end = "\r") 
            best_nll = estimate.fun
            best_param_est = np.hstack((sub, estimate.x)) ## horizonally add ID to subject row containing best parameter estimates for each crun
    return best_param_est, column_names



guess_rate_bounds  = (   0, 0.075)
stim_sens_bounds   = (0.01,    10)
stim_crit_bounds   = (  -3,     3)
meta_uncert_bounds = ( 0.1,     3)
conf_crit_bounds   = (0.01,   5.1)
subs               = [] ## list of Ss IDs
all_sub_params     = [] ## list containing all Ss extimated CASANDRE parameters
column_names = None

files = sorted(glob(os.path.join(data_dir, "2*_IDM_*.csv"))) ## grab all Ss datafiles
for curr_file in files: ## iterate through globbed files and save Ss ID to a list
    sub_id = os.path.basename(curr_file)[7:11] ## grab first 5 indices of filename string
    if not sub_id in subs: ## check if already in list
        subs.append(sub_id) ## if not, append new Ss ID to list

skip_num = 0 ## counter used to allow continuation of writing CASANDRE param output across Ss if something breaks
if os.path.exists(join(save_proj_dir, "ric1-cpdm_best-params-est.csv")): ## checks for previous best params file
    existing_df          = pd.read_csv(join(save_proj_dir, "ric1-cpdm_best-params-est.csv")) ## make new Ss save directory
    existing_df["subID"] = [val[2:-1] for val in existing_df["subID"]] ## gets subID accounting for padding
    skip_num             = len(existing_df["subID"].values) ## current number of completed Ss
    all_sub_params       = existing_df.values.tolist() ## new output df with current Ss

with ipp.Cluster(n = n_cores) as rc: ## 14 cores (starts and connects to the local cluster)
    with rc[:].sync_imports():
        from glob import glob
        import numpy as np
        from numpy import exp, linspace, log, sqrt, sum
        import os
        from os.path import join
        import pandas as pd
        from scipy import stats
        from scipy.optimize import minimize
        from scipy.special import erfcinv
        import sys
        import time
    rc[:].push(dict(casandre_fit = casandre_fit, ## pushed functions
                    _logninv = _logninv,
                    logninv = logninv,
                    neg_ll = neg_ll, 
                    normcdf = stats.norm.cdf,
                    random_bounded = random_bounded, 
                    repeat_matrix_function_2D = repeat_matrix_function_2D))
    rc[:].push(dict(cruns = cruns, ## pushed ttributes
                    sample_rate = sample_rate,
                    delta = delta,
                    noise_sens = noise_sens, 
                    options = options,
                    skip_num = skip_num,
                    guess_rate_bounds = guess_rate_bounds,
                    stim_sens_bounds = stim_sens_bounds,
                    stim_crit_bounds = stim_crit_bounds,
                    meta_uncert_bounds = meta_uncert_bounds,
                    conf_crit_bounds = conf_crit_bounds,
                    data_dir = data_dir))
    clean_batches = len(subs) // n_cores
    unclean_batch = len(subs) % n_cores ## modulus (remainder after division)
    batches = clean_batches
    if unclean_batch != 0:
        batches += 1
    for batch in range(batches):
        batch_start_time = time.time()
        print("-------------> Currently running Batch {0} of {1}".format(batch + 1, batches), end = "")
        cap = n_cores
        if batch == batches - 1:
            cap = unclean_batch
        ## slice == len of n_cores, unless final batch
        res = rc[: cap].map_sync(sub_func, range(cap), subs[batch * n_cores : batch * n_cores + cap])
        for row in res:
            if row is None:
                continue
            if column_names is None:
                column_names = row[1]
            all_sub_params.append(row[0])
        batch_end_time = time.time()
        print(" | Last batch runtime: {0:03d}".format(int(batch_end_time - batch_start_time)), end = "\r")

## final save of complete CASANDRE parameters csv with CRDM alpha parameter

crdm_params_file          = os.path.join(base_proj_dir, "derivatives/RIC1/parameter_estimation/crdm/softmax/ric1-crdm-sm_modelfit.csv")
crdm_params_df            = pd.read_csv(crdm_params_file) ## crdm params
estimate_df               = pd.DataFrame(np.array(all_sub_params), columns = column_names) ## conversion of complete param estimates to dataframe
estimate_df["subID"]      = estimate_df["subID"].apply('="{}"'.format) ## force zero padding to final output csv
estimate_df["CRDM Alpha"] = crdm_params_df["Alpha"] ## add CRDM alpha to final CASANDRE output
estimate_df.to_csv(join(save_proj_dir, "ric1-cpdm_best-params-est.csv"), index = False) ## save completed dataframe w/ CRDM alpha