/***************** 
 * Crdm_Ado *
 *****************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'crdm_ado';  // from the Builder filename that created this script
let expInfo = {
    'participant': 'CRDM',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from crdm_instr1_JS
var exp_proceed = true;
var crdm_earnings = [];
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(crdm_instr1RoutineBegin());
flowScheduler.add(crdm_instr1RoutineEachFrame());
flowScheduler.add(crdm_instr1RoutineEnd());
flowScheduler.add(crdm_instr2RoutineBegin());
flowScheduler.add(crdm_instr2RoutineEachFrame());
flowScheduler.add(crdm_instr2RoutineEnd());
flowScheduler.add(crdm_instr3RoutineBegin());
flowScheduler.add(crdm_instr3RoutineEachFrame());
flowScheduler.add(crdm_instr3RoutineEnd());
flowScheduler.add(crdm_instr4RoutineBegin());
flowScheduler.add(crdm_instr4RoutineEachFrame());
flowScheduler.add(crdm_instr4RoutineEnd());
flowScheduler.add(crdm_instr5RoutineBegin());
flowScheduler.add(crdm_instr5RoutineEachFrame());
flowScheduler.add(crdm_instr5RoutineEnd());
flowScheduler.add(crdm_instr6RoutineBegin());
flowScheduler.add(crdm_instr6RoutineEachFrame());
flowScheduler.add(crdm_instr6RoutineEnd());
flowScheduler.add(crdm_instr7RoutineBegin());
flowScheduler.add(crdm_instr7RoutineEachFrame());
flowScheduler.add(crdm_instr7RoutineEnd());
flowScheduler.add(crdm_instr8RoutineBegin());
flowScheduler.add(crdm_instr8RoutineEachFrame());
flowScheduler.add(crdm_instr8RoutineEnd());
flowScheduler.add(crdm_pract1_instrRoutineBegin());
flowScheduler.add(crdm_pract1_instrRoutineEachFrame());
flowScheduler.add(crdm_pract1_instrRoutineEnd());
flowScheduler.add(crdm_pract_init_fixRoutineBegin());
flowScheduler.add(crdm_pract_init_fixRoutineEachFrame());
flowScheduler.add(crdm_pract_init_fixRoutineEnd());
const crdm_pract1_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crdm_pract1_trialsLoopBegin(crdm_pract1_trialsLoopScheduler));
flowScheduler.add(crdm_pract1_trialsLoopScheduler);
flowScheduler.add(crdm_pract1_trialsLoopEnd);



flowScheduler.add(crdm_qp_instrRoutineBegin());
flowScheduler.add(crdm_qp_instrRoutineEachFrame());
flowScheduler.add(crdm_qp_instrRoutineEnd());
const crdm_questplus_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crdm_questplus_trialsLoopBegin(crdm_questplus_trialsLoopScheduler));
flowScheduler.add(crdm_questplus_trialsLoopScheduler);
flowScheduler.add(crdm_questplus_trialsLoopEnd);



flowScheduler.add(crdm_schedule_genRoutineBegin());
flowScheduler.add(crdm_schedule_genRoutineEachFrame());
flowScheduler.add(crdm_schedule_genRoutineEnd());
flowScheduler.add(crdm_pract2_instrRoutineBegin());
flowScheduler.add(crdm_pract2_instrRoutineEachFrame());
flowScheduler.add(crdm_pract2_instrRoutineEnd());
flowScheduler.add(crdm_pract_init_fixRoutineBegin());
flowScheduler.add(crdm_pract_init_fixRoutineEachFrame());
flowScheduler.add(crdm_pract_init_fixRoutineEnd());
const crdm_pract2_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crdm_pract2_trialsLoopBegin(crdm_pract2_trialsLoopScheduler));
flowScheduler.add(crdm_pract2_trialsLoopScheduler);
flowScheduler.add(crdm_pract2_trialsLoopEnd);





flowScheduler.add(crdm_trial_instrRoutineBegin());
flowScheduler.add(crdm_trial_instrRoutineEachFrame());
flowScheduler.add(crdm_trial_instrRoutineEnd());
flowScheduler.add(crdm_init_fixRoutineBegin());
flowScheduler.add(crdm_init_fixRoutineEachFrame());
flowScheduler.add(crdm_init_fixRoutineEnd());
const crdm_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crdm_trialsLoopBegin(crdm_trialsLoopScheduler));
flowScheduler.add(crdm_trialsLoopScheduler);
flowScheduler.add(crdm_trialsLoopEnd);





flowScheduler.add(crdm_endRoutineBegin());
flowScheduler.add(crdm_endRoutineEachFrame());
flowScheduler.add(crdm_endRoutineEnd());
flowScheduler.add(crdm_bonusRoutineBegin());
flowScheduler.add(crdm_bonusRoutineEachFrame());
flowScheduler.add(crdm_bonusRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'crdm_practice1.csv', 'path': 'crdm_practice1.csv'},
    {'name': 'crdm_questplus_trials.csv', 'path': 'crdm_questplus_trials.csv'},
    {'name': 'crdm_practice2.csv', 'path': 'crdm_practice2.csv'},
    {'name': 'crdm_gen_trials_idx.csv', 'path': 'crdm_gen_trials_idx.csv'},
    {'name': 'images/risk_blue_75.bmp', 'path': 'images/risk_blue_75.bmp'},
    {'name': 'images/ambig_50.bmp', 'path': 'images/ambig_50.bmp'},
    {'name': 'images/2key.png', 'path': 'images/2key.png'},
    {'name': 'images/4key.png', 'path': 'images/4key.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'crdm_gen_test_idx.csv', 'path': 'crdm_gen_test_idx.csv'},
    {'name': 'crdm_practice2.csv', 'path': 'crdm_practice2.csv'},
    {'name': 'crdm_practice1.csv', 'path': 'crdm_practice1.csv'},
    {'name': 'crdm_gen_trials_idx.csv', 'path': 'crdm_gen_trials_idx.csv'},
    {'name': 'crdm_questplus_trials.csv', 'path': 'crdm_questplus_trials.csv'},
    {'name': 'images/risk_red_75.bmp', 'path': 'images/risk_red_75.bmp'},
    {'name': 'images/crdm_screen.png', 'path': 'images/crdm_screen.png'},
    {'name': 'images/ambig_24.bmp', 'path': 'images/ambig_24.bmp'},
    {'name': 'images/risk_red_25.bmp', 'path': 'images/risk_red_25.bmp'},
    {'name': 'images/response_box1-2.png', 'path': 'images/response_box1-2.png'},
    {'name': 'images/risk_blue_75.bmp', 'path': 'images/risk_blue_75.bmp'},
    {'name': 'images/FB_cert.png', 'path': 'images/FB_cert.png'},
    {'name': 'images/risk_blue_50.bmp', 'path': 'images/risk_blue_50.bmp'},
    {'name': 'images/2key.png', 'path': 'images/2key.png'},
    {'name': 'images/ambig_74.bmp', 'path': 'images/ambig_74.bmp'},
    {'name': 'images/FB_lott.png', 'path': 'images/FB_lott.png'},
    {'name': 'images/risk_blue_13.bmp', 'path': 'images/risk_blue_13.bmp'},
    {'name': 'images/risk_red_38.bmp', 'path': 'images/risk_red_38.bmp'},
    {'name': 'images/risk_red_50.bmp', 'path': 'images/risk_red_50.bmp'},
    {'name': 'images/risk_red_13.bmp', 'path': 'images/risk_red_13.bmp'},
    {'name': 'images/risk_blue_38.bmp', 'path': 'images/risk_blue_38.bmp'},
    {'name': 'images/risk_blue_25.bmp', 'path': 'images/risk_blue_25.bmp'},
    {'name': 'images/ambig_50.bmp', 'path': 'images/ambig_50.bmp'},
    {'name': 'images/fixTarget.bmp', 'path': 'images/fixTarget.bmp'},
    {'name': 'images/FB_nonresp.png', 'path': 'images/FB_nonresp.png'},
    {'name': 'images/4key.png', 'path': 'images/4key.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `/data/${expInfo["participant"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var crdm_instr1Clock;
var random;
var format;
var crdm_instr1_title_txt;
var crdm_instr1_txt;
var crdm_instr1_space_txt;
var crdm_instr1_resp;
var crdm_instr2Clock;
var crdm_instr2_lottname_txt;
var crdm_instr2_txt;
var crdm_instr2_img;
var crdm_instr2_lott0_txt;
var crdm_instr2_lott20_txt;
var crdm_instr2_space_txt;
var crdm_instr2_resp;
var crdm_instr3Clock;
var crdm_instr3_lottname_txt;
var crdm_instr3_txt;
var crdm_instr3_img;
var crdm_instr3_lott0_txt;
var crdm_instr3_lott20_txt;
var crdm_instr3_space_txt;
var crdm_instr3_resp;
var crdm_instr4Clock;
var crdm_instr4_lottname_txt;
var crdm_instr4_txt;
var crdm_instr4_img;
var crdm_instr4_lott0_txt;
var crdm_instr4_lott20_txt;
var crdm_instr4_space_txt;
var crdm_instr4_resp;
var crdm_instr5Clock;
var crdm_instr5_txt;
var crdm_instr5_img;
var crdm_instr5_lott_top_txt;
var crdm_instr5_lott_bot_txt;
var crdm_instr5_sure_txt;
var crdm_instr5_space_txt;
var crdm_instr5_resp;
var crdm_instr6Clock;
var crdm_instr6_txt;
var crdm_instr6_img;
var crdm_instr6_space_txt;
var crdm_instr6_resp;
var crdm_instr7Clock;
var crdm_instr7_txt;
var crdm_instr7_img;
var crdm_instr7_space_txt;
var crdm_instr7_resp;
var crdm_instr8Clock;
var crdm_instr8_title_txt;
var crdm_instr8_warn_txt;
var crdm_instr8_space_txt;
var crdm_instr8_resp;
var crdm_pract1_instrClock;
var crdm_pract1_instr_name_txt;
var crdm_pract1_instr_txt;
var crdm_pract1_instr_space_txt;
var crdm_pract1_instr_key;
var crdm_pract_init_fixClock;
var crdm_pract_init_fix_poly;
var crdm_pract1_trialClock;
var crdm_sure_pos1;
var crdm_sure_resp1;
var crdm_msg1;
var crdm_pos1;
var crdm_resp1;
var crdm_pract1_trial_img;
var crdm_pract1_trial_lott_top_txt;
var crdm_pract1_trial_lott_bot_txt;
var crdm_pract1_trial_sure_amt_txt;
var GRFX_fix4;
var crdm_pract1_trial_cue;
var crdm_pract1_trial_resp;
var crdm_pract1_feedbackClock;
var crdm_pract1_feedback_txt;
var crdm_qp_instrClock;
var crdm_qp_instr_title_txt;
var crdm_qp_instr_txt;
var crdm_qp_instr_space_txt;
var crdm_qp_instr_resp;
var crdm_questplusClock;
var crdm_sure_pos_qp;
var crdm_sure_resp_qp;
var crdm_msg_qp;
var crdm_pos_qp;
var crdm_resp_qp;
var weighted_avg;
var weighted_sd;
var crdm_value_space;
var crdm_ambiguity_space;
var crdm_probability_space;
var crdm_value_certain;
var crdm_alpha_space;
var crdm_beta_space;
var crdm_gamma_space;
var crdm_i;
var crdm_j;
var crdm_k;
var crdm_stim_space;
var crdm_gain_stim_space;
var crdm_loss_stim_space;
var crdm_params;
var crdm_response;
var crdm_contrast_idx_gain;
var crdm_contrast_idx_loss;
var crdm_func;
var crdm_q_gain;
var crdm_q_loss;
var crdm_questplus_img;
var crdm_questplus_trial_lott_top_txt;
var crdm_questplus_trial_lott_bot_txt;
var crdm_questplus_trial_sure_amt_txt;
var GRFX_fix3;
var crdm_questplus_trial_cue;
var crdm_questplus_trial_resp;
var crdm_qp_feedbackClock;
var crdm_qp_FB_txt;
var crdm_schedule_genClock;
var crdm_pract2_instrClock;
var crdm_pract2_instr_name_txt;
var crdm_pract2_instr_txt;
var crdm_pract2_instr_space_txt;
var crdm_pract2_instr_key;
var crdm_pract2_trialClock;
var crdm_sure_pos2;
var crdm_sure_resp2;
var crdm_crdm_msg2;
var crdm_pos2;
var crdm_resp2;
var crdm_pract2_trial_img;
var crdm_pract2_trial_lott_top_txt;
var crdm_pract2_trial_lott_bot_txt;
var crdm_pract2_trial_sure_amt_txt;
var GRFX_fix2;
var crdm_pract2_trial_cue;
var crdm_pract2_trial_resp;
var crdm_pract2_feedbackClock;
var crdm_pract2_feedback_txt;
var crdm_pract2_confClock;
var crdm_pract2_conf_txt;
var crdm_pract2_conf1;
var crdm_pract2_conf1_txt;
var crdm_pract2_conf2;
var crdm_pract2_conf2_txt;
var crdm_pract2_conf3;
var crdm_pract2_conf3_txt;
var crdm_pract2_conf4;
var crdm_pract2_conf4_txt;
var crdm_pract2_conf_resp;
var crdm_pract2_itiClock;
var crdm_pract2_iti_poly;
var crdm_trial_instrClock;
var crdm_trial_instr_title_txt;
var crdm_trial_instr_txt;
var crdm_trial_instr_space_txt;
var crdm_trial_instr_resp;
var crdm_init_fixClock;
var crdm_init_fix_poly;
var crdm_trialClock;
var crdm_delta_time;
var crdm_sure_pos;
var crdm_sure_resp;
var crdm_msg;
var crdm_pos;
var crdm_resp;
var crdm_task_nonresp_ct;
var crdm_conf_nonresp_ct;
var crdm_trial_img;
var crdm_trial_lott_top;
var crdm_trial_lott_bot;
var crdm_trial_sure_amt;
var GRFX_fix;
var crdm_trial_cue;
var crdm_trial_resp;
var crdm_feedbackClock;
var crdm_feedback_txt;
var crdm_confClock;
var crdm_conf_txt;
var crdm_conf1;
var crdm_conf1_txt;
var crdm_conf2;
var crdm_conf2_txt;
var crdm_conf3;
var crdm_conf3_txt;
var crdm_conf4;
var crdm_conf4_txt;
var crdm_conf_resp;
var crdm_trials_itiClock;
var crdm_trials_iti_poly;
var crdm_endClock;
var crdm_end_title_txt;
var crdm_end_txt_OFF;
var crdm_end_space_OFF;
var crdm_end_resp;
var crdm_bonusClock;
var crdm_bonus_thanks_txt;
var crdm_bonus_lott_top;
var crdm_bonus_img;
var crdm_bonus_lott_bot;
var crdm_bonus_sure_amt_txt;
var crdm_bonus_prompt_txt;
var crdm_bonus_choice_text_txt;
var crdm_bonus_choice_outcome_txt;
var crdm_bonus_drawn_txt;
var crdm_bonus_chip_poly;
var crdm_bonus_winnings_txt;
var crdm_bonus_space_txt;
var crdm_bonus_resp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "crdm_instr1"
  crdm_instr1Clock = new util.Clock();
  //function for random.random used in python
  random = {
  random: function(){return Math.random()}, 
  randint: function(start, end){return Math.round(Math.random() * (end - start) + start)}, 
  choices: function(items, weights){
      var i; 
      for (i = 0; i < weights.length; i++)
          weights[i] += weights[i - 1] || 0;
      var random = Math.random() * weights[weights.length - 1];
      for (i = 0; i < weights.length; i++)
          if (weights[i] > random)
              break;
      return items[i] }
  }
  
  const formatter = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  });
  
  format = formatter.format;
  
  crdm_instr1_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr1_title_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_instr1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr1_txt',
    text: 'In this decision making task, you will be asked to make economic choices between: \n\n\n- Gaining/losing a certain amount \nOR\n- Playing a lottery for the chance to win a larger gain or smaller loss ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr1_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr1_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_instr1_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr2"
  crdm_instr2Clock = new util.Clock();
  crdm_instr2_lottname_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr2_lottname_txt',
    text: '*Playing the Lottery*',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr2_txt',
    text: 'The lottery consists of an imaginary bag containing 100 poker chips, some red and some blue. To play, you pull a random chip from the bag.  \n\nThe figure on the right represents the proportion of blue and red chips in the imaginary bag. \n\nIn this example, most chips are blue (75 of 100) and fewer are red (25 of 100).',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_instr2_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr2_img', units : 'height', 
    image : 'images/risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  crdm_instr2_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr2_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_instr2_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr2_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_instr2_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr2_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_instr2_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr3"
  crdm_instr3Clock = new util.Clock();
  crdm_instr3_lottname_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr3_lottname_txt',
    text: '*Playing the Lottery*',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr3_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr3_txt',
    text: 'Given information about the number of blue and red chips in the bag, you can decide whether you would prefer a certain monetary outcome or if you would rather play the lottery for a chance to win a different outcome\n\nIn this example, you have a 75% chance of pulling a blue chip and winning $20. Conversely, you have a 25% chance of pulling a red chip and receiving $0.\n\nThe value for each color will change from bag to bag. Read the $ amount above the red and below the blue to know the value of each chip color.',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_instr3_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr3_img', units : undefined, 
    image : 'images/risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  crdm_instr3_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr3_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_instr3_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr3_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_instr3_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr3_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_instr3_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr4"
  crdm_instr4Clock = new util.Clock();
  crdm_instr4_lottname_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr4_lottname_txt',
    text: '*Playing the Lottery*',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr4_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr4_txt',
    text: 'For some lotteries, information about the contents of the bag may be partially hidden. \n\nIn this example, the bag has at least 25 blue chips and 25 red chips. However, the color of the remaining 50 chips is unknown. The remaining 50 chips could be all red, all blue, or any combination of the two. ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_instr4_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr4_img', units : undefined, 
    image : 'images/ambig_50.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  crdm_instr4_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr4_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_instr4_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr4_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_instr4_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr4_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_instr4_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr5"
  crdm_instr5Clock = new util.Clock();
  crdm_instr5_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr5_txt',
    text: 'The lottery bag will appear in the center of the screen. The certain dollar amount will be presented on either the right or left side of the bag. In this example, the certain $5 would be the left option, and the lottery would be the right option:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.035,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr5_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr5_img', units : undefined, 
    image : 'images/risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.05)], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_instr5_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr5_lott_top_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr5_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr5_lott_bot_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_instr5_sure_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr5_sure_txt',
    text: '$5',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.5), (- 0.05)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_instr5_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr5_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_instr5_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr6"
  crdm_instr6Clock = new util.Clock();
  crdm_instr6_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr6_txt',
    text: 'When the green circle appears, use the number keys at the top of your keyboard to indicate your choice:\n\nPress 1 to select the left option\nPress 2 to select the right option \n\n\n\n\n\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr6_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr6_img', units : undefined, 
    image : 'images/2key.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.1)], size : [0.6, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_instr6_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr6_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr6_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr7"
  crdm_instr7Clock = new util.Clock();
  crdm_instr7_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr7_txt',
    text: "After each choice, you will be asked to rate your choice confidence. \n1 indicates you couldn't decide which option you preferred and chose at random, while 4 indicates total certainty in your choice. Use the number keys at the top of your keyboard to indicate your confidence: \n\nPress 1 - Not at all confident\nPress 2 - Less confident\nPress 3 - Somewhat confident\nPress 4 - Very confident\n\n\n\n\n\n\n\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.35, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr7_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_instr7_img', units : undefined, 
    image : 'images/4key.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.15)], size : [0.6, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_instr7_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr7_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr7_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instr8"
  crdm_instr8Clock = new util.Clock();
  crdm_instr8_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr8_title_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_instr8_warn_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr8_warn_txt',
    text: 'You must answer both the initial question and confidence prompts to complete each trial. The experiment will end if you (1) miss more than 4 trials, or (2) provide responses which indicate you did not understand, or are not following, task instructions. If this happens, you will not be eligible to receive a *bonus earnings*. \n\nPlease remain engaged throughout the experiment and provide earnest, sincere responses for each trial. Remember, your choices could help you walk away with an additional bonus ranging from $2 to $65, depending on the seleced *bonus earnings* trial!\n\nThank you for your participation!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_instr8_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr8_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr8_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract1_instr"
  crdm_pract1_instrClock = new util.Clock();
  crdm_pract1_instr_name_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_instr_name_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_pract1_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_instr_txt',
    text: "In this first section, you will only be asked to indicate your choice between the certain outcome and the lottery. You will not be asked to rate your choice confidence.\n\nWhen the green circle appears, indicate your decision by pressing YELLOW for the left option and GREEN for the right option. \n\nLet's practice!",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_pract1_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract1_instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract_init_fix"
  crdm_pract_init_fixClock = new util.Clock();
  crdm_pract_init_fix_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_pract_init_fix_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "crdm_pract1_trial"
  crdm_pract1_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from crdm_pract1_trial_code
  crdm_sure_pos1 = [];
  crdm_sure_resp1 = [];
  crdm_msg1 = "";
  crdm_pos1 = [[(- 0.5), 0], [0.5, 0]];
  crdm_resp1 = ["1", "2"];
  
  crdm_pract1_trial_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_pract1_trial_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_pract1_trial_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_trial_lott_top_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract1_trial_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_trial_lott_bot_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_pract1_trial_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_trial_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  GRFX_fix4 = new visual.Rect ({
    win: psychoJS.window, name: 'GRFX_fix4', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  crdm_pract1_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_pract1_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_pract1_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract1_feedback"
  crdm_pract1_feedbackClock = new util.Clock();
  crdm_pract1_feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract1_feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crdm_qp_instr"
  crdm_qp_instrClock = new util.Clock();
  crdm_qp_instr_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_qp_instr_title_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_qp_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_qp_instr_txt',
    text: "Now that you've practiced, we'll begin the first section of the task.\n\nYou will have 3 seconds to consider and 2 seconds to respond for each trial. Please make your choice when the green circle appears on the screen. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_qp_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_qp_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_qp_instr_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_questplus"
  crdm_questplusClock = new util.Clock();
  // Run 'Begin Experiment' code from crdm_questplus_JS
  crdm_sure_pos_qp = [];
  crdm_sure_resp_qp = [];
  crdm_msg_qp = "";
  crdm_pos_qp = [[(- 0.5), 0], [0.5, 0]];
  crdm_resp_qp = ["1", "2"];
  
  weighted_avg = function(q) {
      var fits = [];
      var weight = 0;
      // q.param_domain, q.posterior
      var i, l;
      l = q.param_domain[0].length;
      while (fits.length < l) {
          fits.push(0);
      }
      for (i = 0; i < q.posterior.length; i++) {
          for (l = 0; l < fits.length; l++) {
              fits[l] += q.param_domain[i][l] * q.posterior[i];
          }
          weight += q.posterior[i];
      }
      for (l = 0; l < fits.length; l++) {
          fits[l] /= weight;
      }
      return fits;
  }
  
  // Sqrt(sum(w * (x - wm)^2) / sum(w))
  weighted_sd = function(q) {
      var fits = [];
      var weight = 0;
      var i, l;
      var wm = weighted_avg(q);
      l = q.param_domain[0].length;
      while (fits.length < l) {
          fits.push(0);
      }
      for (i = 0; i < q.posterior.length; i++) {
          for (l = 0; l < fits.length; l++) {
              fits[l] += q.posterior[i] * Math.pow((q.param_domain[i][l] - wm[l]), 2);
          }
          weight += q.posterior[i];
      }
      for (l = 0; l < fits.length; l++) {
          fits[l] /= weight;
          fits[l] = Math.sqrt(fits[l])
      }
      return fits;
  }
  
  crdm_value_space = [5, 8, 20, 40, 50];
  crdm_ambiguity_space = [0, 0.24, 0.5, 0.74];
  crdm_probability_space = [0.13, 0.25, 0.38, 0.5, 0.75];
  crdm_value_certain = 5;
  
  // parameter space 
  crdm_alpha_space = arange_round(0.1, 3.1, 0.1);
  crdm_beta_space =  arange_round(-1.3, 1.31, 0.1);
  crdm_gamma_space =  arange_round(0.5, 5.1, 0.5);
  
  crdm_i = 0;
  crdm_j = 0;
  crdm_k = 0;
  crdm_stim_space = []; // set for gain domain
  for (crdm_i = 0; crdm_i < crdm_value_space.length; crdm_i++) {
      for (crdm_j = 0; crdm_j < crdm_ambiguity_space.length; crdm_j++) {
          for (crdm_k = 0; crdm_k < crdm_probability_space.length; crdm_k++) {
              if (!crdm_ambiguity_space[crdm_j] || crdm_probability_space[crdm_k] == 0.5) {
                  crdm_stim_space.push([crdm_value_space[crdm_i], crdm_ambiguity_space[crdm_j], crdm_probability_space[crdm_k], crdm_value_certain]);
              }
          }
      }
  }
  crdm_gain_stim_space = crdm_stim_space;
  
  crdm_stim_space = []; // reset for loss domain
  for (crdm_i = 0; crdm_i < crdm_value_space.length; crdm_i++) {
      for (crdm_j = 0; crdm_j < crdm_ambiguity_space.length; crdm_j++) {
          for (crdm_k = 0; crdm_k < crdm_probability_space.length; crdm_k++) {
              if (!crdm_ambiguity_space[crdm_j] || crdm_probability_space[crdm_k] == 0.5) {
                  crdm_stim_space.push([-crdm_value_space[crdm_i], crdm_ambiguity_space[crdm_j], crdm_probability_space[crdm_k], -crdm_value_certain]);
              }
          }
      }
  }
  crdm_loss_stim_space = crdm_stim_space;
  
  crdm_params = [crdm_alpha_space, crdm_beta_space, crdm_gamma_space];
  crdm_response = true;
  
  // risk and ambiguity model
  function SV_option_RA(stimulus_values, params) {
      var prob;
      var objective_value = stimulus_values[0];
      var ambiguity = stimulus_values[1];
      var probability = stimulus_values[2];
      var value_certain = stimulus_values[3];
      var alpha_subject_risk_aversion = params[0];
      var beta_ambiguity_aversion = params[1];
      var sv_reward, sv_null, tmp;
      sv_reward = Math.sign(objective_value) * (probability - beta_ambiguity_aversion * (ambiguity/2)) * Math.pow(Math.abs(objective_value), alpha_subject_risk_aversion);
      sv_null = Math.sign(objective_value) * Math.pow(Math.abs(value_certain), alpha_subject_risk_aversion);
      var gamma = params[2];
      prob = 1. / (1 + Math.exp(-gamma * (sv_reward - sv_null)));
      return prob;
  }
  
  // subjective value decision
  function draw_from(stimulus_value, params, func) {
      var prob = func(stimulus_value, params);
      if (Math.random() < prob)
          return 1;
      else
          return 0;
  }
  
  // # uses contrast_idx instead of contrast for efficiency
  crdm_contrast_idx_gain = parseInt(Math.random() * crdm_stim_space.length);
  crdm_contrast_idx_loss = parseInt(Math.random() * crdm_stim_space.length);
  
  crdm_func = SV_option_RA;
  crdm_q_gain = new QuestPlus(crdm_stim_space, crdm_params, crdm_func);
  crdm_q_loss = new QuestPlus(crdm_stim_space, crdm_params, crdm_func);
  crdm_questplus_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_questplus_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_questplus_trial_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_questplus_trial_lott_top_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_questplus_trial_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_questplus_trial_lott_bot_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_questplus_trial_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_questplus_trial_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  GRFX_fix3 = new visual.Rect ({
    win: psychoJS.window, name: 'GRFX_fix3', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  crdm_questplus_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_questplus_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_questplus_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_qp_feedback"
  crdm_qp_feedbackClock = new util.Clock();
  crdm_qp_FB_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_qp_FB_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crdm_schedule_gen"
  crdm_schedule_genClock = new util.Clock();
  // Initialize components for Routine "crdm_pract2_instr"
  crdm_pract2_instrClock = new util.Clock();
  crdm_pract2_instr_name_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_instr_name_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_pract2_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_instr_txt',
    text: "In this second section, you will now be asked to provide a confidence rating after your choice.\n\nWhen the green circle appears, indicate your decision by pressing YELLOW for the left option and GREEN for the right option. Next, you will rate your choice confidence. Please be sure to answer both the task and confidence questions!\n\nLet's practice!",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_pract2_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract2_instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract2_trial"
  crdm_pract2_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from crdm_pract2_trial_code
  crdm_sure_pos2 = [];
  crdm_sure_resp2 = [];
  crdm_crdm_msg2 = "";
  crdm_pos2 = [[(- 0.5), 0], [0.5, 0]];
  crdm_resp2 = ["1", "2"];
  
  crdm_pract2_trial_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_pract2_trial_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_pract2_trial_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_trial_lott_top_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract2_trial_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_trial_lott_bot_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_pract2_trial_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_trial_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  GRFX_fix2 = new visual.Rect ({
    win: psychoJS.window, name: 'GRFX_fix2', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  crdm_pract2_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_pract2_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_pract2_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract2_feedback"
  crdm_pract2_feedbackClock = new util.Clock();
  crdm_pract2_feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crdm_pract2_conf"
  crdm_pract2_confClock = new util.Clock();
  crdm_pract2_conf_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_conf_txt',
    text: 'How confident are you in your choice?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_pract2_conf1 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract2_conf1', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.6), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  crdm_pract2_conf1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_conf1_txt',
    text: 'Not at all\nconfident\n\n1',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.6), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_pract2_conf2 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract2_conf2', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.2), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  crdm_pract2_conf2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_conf2_txt',
    text: 'Less\nconfident\n\n2',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_pract2_conf3 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract2_conf3', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.2, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_pract2_conf3_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_conf3_txt',
    text: 'Somewhat\nconfident\n\n3',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  crdm_pract2_conf4 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract2_conf4', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.6, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  crdm_pract2_conf4_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract2_conf4_txt',
    text: 'Very\nconfident\n\n4',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  crdm_pract2_conf_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract2_iti"
  crdm_pract2_itiClock = new util.Clock();
  crdm_pract2_iti_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_pract2_iti_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "crdm_trial_instr"
  crdm_trial_instrClock = new util.Clock();
  crdm_trial_instr_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_instr_title_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_trial_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_instr_txt',
    text: "Now that you've practiced, we'll begin the second section of the task.\n\nYou will have 3 seconds to view and consider the certain and lottery options, and 2 seconds to choose once the green circle appears. You will then have 3 seconds to rate your confidence.",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_trial_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_trial_instr_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_init_fix"
  crdm_init_fixClock = new util.Clock();
  crdm_init_fix_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_init_fix_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "crdm_trial"
  crdm_trialClock = new util.Clock();
  //var crdm_sure_amt, crdm_sure_p, crdm_lott_top, crdm_lott_bot, crdm_lott_p, crdm_amb_lev, crdm_domain, crdm_img;
  //var delta_time, sure_pos, sure_resp, crdm_msg, pos, resp, task_nonresp_ct, conf_nonresp_ct;
  
  crdm_delta_time = 0; //used in variable ITI
  crdm_sure_pos = []; //position of certain option
  crdm_sure_resp = []; //response key for certain option
  crdm_msg = ""; //feedback message string
  crdm_pos = [[(- 0.5), 0], [0.5, 0]]; //left/right screen locations
  crdm_resp = ["1", "2"]; //1 = left, 2 = right
  crdm_task_nonresp_ct = 0;
  crdm_conf_nonresp_ct = 0;
  crdm_trial_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_trial_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_trial_lott_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_lott_top',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_trial_lott_bot = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_lott_bot',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_trial_sure_amt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_sure_amt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  GRFX_fix = new visual.Rect ({
    win: psychoJS.window, name: 'GRFX_fix', 
    width: [2, 2][0], height: [2, 2][1],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([0, 0, 0]),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  crdm_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_feedback"
  crdm_feedbackClock = new util.Clock();
  crdm_feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crdm_conf"
  crdm_confClock = new util.Clock();
  crdm_conf_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_conf_txt',
    text: 'How confident are you in your choice?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_conf1 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_conf1', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.6), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  crdm_conf1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_conf1_txt',
    text: 'Not at all\nconfident\n\n1',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.6), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_conf2 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_conf2', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.2), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  crdm_conf2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_conf2_txt',
    text: 'Less\nconfident\n\n2',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_conf3 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_conf3', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.2, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_conf3_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_conf3_txt',
    text: 'Somewhat\nconfident\n\n3',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  crdm_conf4 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_conf4', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.6, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  crdm_conf4_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_conf4_txt',
    text: 'Very\nconfident\n\n4',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  crdm_conf_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_trials_iti"
  crdm_trials_itiClock = new util.Clock();
  crdm_trials_iti_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_trials_iti_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "crdm_end"
  crdm_endClock = new util.Clock();
  crdm_end_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_end_title_txt',
    text: '* Risk & Ambiguity Task *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_end_txt_OFF = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_end_txt_OFF',
    text: 'You have completed the Risky & Ambiguity Task!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: 1.35, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_end_space_OFF = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_end_space_OFF',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_end_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_bonus"
  crdm_bonusClock = new util.Clock();
  crdm_bonus_thanks_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_thanks_txt',
    text: 'Your randomly selected *bonus earnings trial* is from the\nRisk & Ambiguity Task!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: 1.35, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_bonus_lott_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_lott_top',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_bonus_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_bonus_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.6, (- 0.1)], size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  crdm_bonus_lott_bot = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_lott_bot',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_bonus_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.375, (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_bonus_prompt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_prompt_txt',
    text: 'In this trial, you chose:',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.2], height: 0.04,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  crdm_bonus_choice_text_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_choice_text_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.1], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  crdm_bonus_choice_outcome_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_choice_outcome_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  crdm_bonus_drawn_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_drawn_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.1)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  crdm_bonus_chip_poly = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_bonus_chip_poly', 
    edges: 100, size:[0.075, 0.075],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -10, interpolate: true,
  });
  
  crdm_bonus_winnings_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_winnings_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.2)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -11.0 
  });
  
  crdm_bonus_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_space_txt',
    text: 'Press SPACE to end.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -12.0 
  });
  
  crdm_bonus_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var crdm_practice_loop1_name;
var crdm_questplus_loop_name;
var crdm_practice_loop2_name;
var crdm_loop_name;
var _crdm_instr1_resp_allKeys;
var crdm_instr1Components;
function crdm_instr1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr1' ---
    t = 0;
    crdm_instr1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr1.started', globalClock.getTime());
    crdm_practice_loop1_name = "crdm_pract1_trials";
    crdm_questplus_loop_name = "crdm_questplus_trials";
    crdm_practice_loop2_name = "crdm_pract2_trials";
    crdm_loop_name = "crdm_trials";
    crdm_instr1_resp.keys = undefined;
    crdm_instr1_resp.rt = undefined;
    _crdm_instr1_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr1Components = [];
    crdm_instr1Components.push(crdm_instr1_title_txt);
    crdm_instr1Components.push(crdm_instr1_txt);
    crdm_instr1Components.push(crdm_instr1_space_txt);
    crdm_instr1Components.push(crdm_instr1_resp);
    
    for (const thisComponent of crdm_instr1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr1' ---
    // get current time
    t = crdm_instr1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr1_title_txt* updates
    if (t >= 0.0 && crdm_instr1_title_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr1_title_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr1_title_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr1_title_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr1_txt* updates
    if (t >= 0.0 && crdm_instr1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr1_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr1_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr1_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr1_space_txt* updates
    if (t >= 0.0 && crdm_instr1_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr1_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr1_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr1_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr1_resp* updates
    if (t >= 0.0 && crdm_instr1_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr1_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr1_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr1_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr1_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr1_resp.clearEvents(); });
    }
    
    if (crdm_instr1_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr1_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr1_resp_allKeys = _crdm_instr1_resp_allKeys.concat(theseKeys);
      if (_crdm_instr1_resp_allKeys.length > 0) {
        crdm_instr1_resp.keys = _crdm_instr1_resp_allKeys[_crdm_instr1_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr1_resp.rt = _crdm_instr1_resp_allKeys[_crdm_instr1_resp_allKeys.length - 1].rt;
        crdm_instr1_resp.duration = _crdm_instr1_resp_allKeys[_crdm_instr1_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr1' ---
    for (const thisComponent of crdm_instr1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr1.stopped', globalClock.getTime());
    crdm_instr1_resp.stop();
    // the Routine "crdm_instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr2_resp_allKeys;
var crdm_instr2Components;
function crdm_instr2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr2' ---
    t = 0;
    crdm_instr2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr2.started', globalClock.getTime());
    crdm_instr2_resp.keys = undefined;
    crdm_instr2_resp.rt = undefined;
    _crdm_instr2_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr2Components = [];
    crdm_instr2Components.push(crdm_instr2_lottname_txt);
    crdm_instr2Components.push(crdm_instr2_txt);
    crdm_instr2Components.push(crdm_instr2_img);
    crdm_instr2Components.push(crdm_instr2_lott0_txt);
    crdm_instr2Components.push(crdm_instr2_lott20_txt);
    crdm_instr2Components.push(crdm_instr2_space_txt);
    crdm_instr2Components.push(crdm_instr2_resp);
    
    for (const thisComponent of crdm_instr2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr2' ---
    // get current time
    t = crdm_instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr2_lottname_txt* updates
    if (t >= 0.0 && crdm_instr2_lottname_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_lottname_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_lottname_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_lottname_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_txt* updates
    if (t >= 0.0 && crdm_instr2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_img* updates
    if (t >= 0.0 && crdm_instr2_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_lott0_txt* updates
    if (t >= 0.0 && crdm_instr2_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_lott0_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_lott0_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_lott0_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_lott20_txt* updates
    if (t >= 0.0 && crdm_instr2_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_lott20_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_lott20_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_lott20_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_space_txt* updates
    if (t >= 0.0 && crdm_instr2_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr2_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr2_resp* updates
    if (t >= 0.0 && crdm_instr2_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr2_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr2_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr2_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr2_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr2_resp.clearEvents(); });
    }
    
    if (crdm_instr2_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr2_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr2_resp_allKeys = _crdm_instr2_resp_allKeys.concat(theseKeys);
      if (_crdm_instr2_resp_allKeys.length > 0) {
        crdm_instr2_resp.keys = _crdm_instr2_resp_allKeys[_crdm_instr2_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr2_resp.rt = _crdm_instr2_resp_allKeys[_crdm_instr2_resp_allKeys.length - 1].rt;
        crdm_instr2_resp.duration = _crdm_instr2_resp_allKeys[_crdm_instr2_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr2' ---
    for (const thisComponent of crdm_instr2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr2.stopped', globalClock.getTime());
    crdm_instr2_resp.stop();
    // the Routine "crdm_instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr3_resp_allKeys;
var crdm_instr3Components;
function crdm_instr3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr3' ---
    t = 0;
    crdm_instr3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr3.started', globalClock.getTime());
    crdm_instr3_resp.keys = undefined;
    crdm_instr3_resp.rt = undefined;
    _crdm_instr3_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr3Components = [];
    crdm_instr3Components.push(crdm_instr3_lottname_txt);
    crdm_instr3Components.push(crdm_instr3_txt);
    crdm_instr3Components.push(crdm_instr3_img);
    crdm_instr3Components.push(crdm_instr3_lott0_txt);
    crdm_instr3Components.push(crdm_instr3_lott20_txt);
    crdm_instr3Components.push(crdm_instr3_space_txt);
    crdm_instr3Components.push(crdm_instr3_resp);
    
    for (const thisComponent of crdm_instr3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr3' ---
    // get current time
    t = crdm_instr3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr3_lottname_txt* updates
    if (t >= 0.0 && crdm_instr3_lottname_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_lottname_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_lottname_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_lottname_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_txt* updates
    if (t >= 0.0 && crdm_instr3_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_img* updates
    if (t >= 0.0 && crdm_instr3_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_lott0_txt* updates
    if (t >= 0.0 && crdm_instr3_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_lott0_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_lott0_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_lott0_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_lott20_txt* updates
    if (t >= 0.0 && crdm_instr3_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_lott20_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_lott20_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_lott20_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_space_txt* updates
    if (t >= 0.0 && crdm_instr3_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr3_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr3_resp* updates
    if (t >= 0.0 && crdm_instr3_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr3_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr3_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr3_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr3_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr3_resp.clearEvents(); });
    }
    
    if (crdm_instr3_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr3_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr3_resp_allKeys = _crdm_instr3_resp_allKeys.concat(theseKeys);
      if (_crdm_instr3_resp_allKeys.length > 0) {
        crdm_instr3_resp.keys = _crdm_instr3_resp_allKeys[_crdm_instr3_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr3_resp.rt = _crdm_instr3_resp_allKeys[_crdm_instr3_resp_allKeys.length - 1].rt;
        crdm_instr3_resp.duration = _crdm_instr3_resp_allKeys[_crdm_instr3_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr3' ---
    for (const thisComponent of crdm_instr3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr3.stopped', globalClock.getTime());
    crdm_instr3_resp.stop();
    // the Routine "crdm_instr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr4_resp_allKeys;
var crdm_instr4Components;
function crdm_instr4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr4' ---
    t = 0;
    crdm_instr4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr4.started', globalClock.getTime());
    crdm_instr4_resp.keys = undefined;
    crdm_instr4_resp.rt = undefined;
    _crdm_instr4_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr4Components = [];
    crdm_instr4Components.push(crdm_instr4_lottname_txt);
    crdm_instr4Components.push(crdm_instr4_txt);
    crdm_instr4Components.push(crdm_instr4_img);
    crdm_instr4Components.push(crdm_instr4_lott0_txt);
    crdm_instr4Components.push(crdm_instr4_lott20_txt);
    crdm_instr4Components.push(crdm_instr4_space_txt);
    crdm_instr4Components.push(crdm_instr4_resp);
    
    for (const thisComponent of crdm_instr4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr4' ---
    // get current time
    t = crdm_instr4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr4_lottname_txt* updates
    if (t >= 0.0 && crdm_instr4_lottname_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_lottname_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_lottname_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_lottname_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_txt* updates
    if (t >= 0.0 && crdm_instr4_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_img* updates
    if (t >= 0.0 && crdm_instr4_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_lott0_txt* updates
    if (t >= 0.0 && crdm_instr4_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_lott0_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_lott0_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_lott0_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_lott20_txt* updates
    if (t >= 0.0 && crdm_instr4_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_lott20_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_lott20_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_lott20_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_space_txt* updates
    if (t >= 0.0 && crdm_instr4_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr4_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr4_resp* updates
    if (t >= 0.0 && crdm_instr4_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr4_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr4_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr4_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr4_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr4_resp.clearEvents(); });
    }
    
    if (crdm_instr4_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr4_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr4_resp_allKeys = _crdm_instr4_resp_allKeys.concat(theseKeys);
      if (_crdm_instr4_resp_allKeys.length > 0) {
        crdm_instr4_resp.keys = _crdm_instr4_resp_allKeys[_crdm_instr4_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr4_resp.rt = _crdm_instr4_resp_allKeys[_crdm_instr4_resp_allKeys.length - 1].rt;
        crdm_instr4_resp.duration = _crdm_instr4_resp_allKeys[_crdm_instr4_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr4' ---
    for (const thisComponent of crdm_instr4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr4.stopped', globalClock.getTime());
    crdm_instr4_resp.stop();
    // the Routine "crdm_instr4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr5_resp_allKeys;
var crdm_instr5Components;
function crdm_instr5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr5' ---
    t = 0;
    crdm_instr5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr5.started', globalClock.getTime());
    crdm_instr5_resp.keys = undefined;
    crdm_instr5_resp.rt = undefined;
    _crdm_instr5_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr5Components = [];
    crdm_instr5Components.push(crdm_instr5_txt);
    crdm_instr5Components.push(crdm_instr5_img);
    crdm_instr5Components.push(crdm_instr5_lott_top_txt);
    crdm_instr5Components.push(crdm_instr5_lott_bot_txt);
    crdm_instr5Components.push(crdm_instr5_sure_txt);
    crdm_instr5Components.push(crdm_instr5_space_txt);
    crdm_instr5Components.push(crdm_instr5_resp);
    
    for (const thisComponent of crdm_instr5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr5' ---
    // get current time
    t = crdm_instr5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr5_txt* updates
    if (t >= 0.0 && crdm_instr5_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_img* updates
    if (t >= 0.0 && crdm_instr5_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_lott_top_txt* updates
    if (t >= 0.0 && crdm_instr5_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_lott_top_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_lott_bot_txt* updates
    if (t >= 0.0 && crdm_instr5_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_lott_bot_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_sure_txt* updates
    if (t >= 0.0 && crdm_instr5_sure_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_sure_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_sure_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_sure_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_space_txt* updates
    if (t >= 0.0 && crdm_instr5_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr5_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr5_resp* updates
    if (t >= 0.0 && crdm_instr5_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr5_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr5_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr5_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr5_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr5_resp.clearEvents(); });
    }
    
    if (crdm_instr5_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr5_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr5_resp_allKeys = _crdm_instr5_resp_allKeys.concat(theseKeys);
      if (_crdm_instr5_resp_allKeys.length > 0) {
        crdm_instr5_resp.keys = _crdm_instr5_resp_allKeys[_crdm_instr5_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr5_resp.rt = _crdm_instr5_resp_allKeys[_crdm_instr5_resp_allKeys.length - 1].rt;
        crdm_instr5_resp.duration = _crdm_instr5_resp_allKeys[_crdm_instr5_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr5' ---
    for (const thisComponent of crdm_instr5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr5.stopped', globalClock.getTime());
    crdm_instr5_resp.stop();
    // the Routine "crdm_instr5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr6_resp_allKeys;
var crdm_instr6Components;
function crdm_instr6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr6' ---
    t = 0;
    crdm_instr6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr6.started', globalClock.getTime());
    crdm_instr6_resp.keys = undefined;
    crdm_instr6_resp.rt = undefined;
    _crdm_instr6_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr6Components = [];
    crdm_instr6Components.push(crdm_instr6_txt);
    crdm_instr6Components.push(crdm_instr6_img);
    crdm_instr6Components.push(crdm_instr6_space_txt);
    crdm_instr6Components.push(crdm_instr6_resp);
    
    for (const thisComponent of crdm_instr6Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr6' ---
    // get current time
    t = crdm_instr6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr6_txt* updates
    if (t >= 0.0 && crdm_instr6_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr6_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr6_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr6_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr6_img* updates
    if (t >= 0.0 && crdm_instr6_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr6_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr6_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr6_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr6_space_txt* updates
    if (t >= 0.0 && crdm_instr6_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr6_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr6_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr6_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr6_resp* updates
    if (t >= 0.0 && crdm_instr6_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr6_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr6_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr6_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr6_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr6_resp.clearEvents(); });
    }
    
    if (crdm_instr6_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr6_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr6_resp_allKeys = _crdm_instr6_resp_allKeys.concat(theseKeys);
      if (_crdm_instr6_resp_allKeys.length > 0) {
        crdm_instr6_resp.keys = _crdm_instr6_resp_allKeys[_crdm_instr6_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr6_resp.rt = _crdm_instr6_resp_allKeys[_crdm_instr6_resp_allKeys.length - 1].rt;
        crdm_instr6_resp.duration = _crdm_instr6_resp_allKeys[_crdm_instr6_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr6Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr6' ---
    for (const thisComponent of crdm_instr6Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr6.stopped', globalClock.getTime());
    crdm_instr6_resp.stop();
    // the Routine "crdm_instr6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr7_resp_allKeys;
var crdm_instr7Components;
function crdm_instr7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr7' ---
    t = 0;
    crdm_instr7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr7.started', globalClock.getTime());
    crdm_instr7_resp.keys = undefined;
    crdm_instr7_resp.rt = undefined;
    _crdm_instr7_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr7Components = [];
    crdm_instr7Components.push(crdm_instr7_txt);
    crdm_instr7Components.push(crdm_instr7_img);
    crdm_instr7Components.push(crdm_instr7_space_txt);
    crdm_instr7Components.push(crdm_instr7_resp);
    
    for (const thisComponent of crdm_instr7Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr7' ---
    // get current time
    t = crdm_instr7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr7_txt* updates
    if (t >= 0.0 && crdm_instr7_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr7_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr7_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr7_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr7_img* updates
    if (t >= 0.0 && crdm_instr7_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr7_img.tStart = t;  // (not accounting for frame time here)
      crdm_instr7_img.frameNStart = frameN;  // exact frame index
      
      crdm_instr7_img.setAutoDraw(true);
    }
    
    
    // *crdm_instr7_space_txt* updates
    if (t >= 0.0 && crdm_instr7_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr7_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr7_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr7_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr7_resp* updates
    if (t >= 0.0 && crdm_instr7_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr7_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr7_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr7_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr7_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr7_resp.clearEvents(); });
    }
    
    if (crdm_instr7_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr7_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr7_resp_allKeys = _crdm_instr7_resp_allKeys.concat(theseKeys);
      if (_crdm_instr7_resp_allKeys.length > 0) {
        crdm_instr7_resp.keys = _crdm_instr7_resp_allKeys[_crdm_instr7_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr7_resp.rt = _crdm_instr7_resp_allKeys[_crdm_instr7_resp_allKeys.length - 1].rt;
        crdm_instr7_resp.duration = _crdm_instr7_resp_allKeys[_crdm_instr7_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr7Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr7' ---
    for (const thisComponent of crdm_instr7Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr7.stopped', globalClock.getTime());
    crdm_instr7_resp.stop();
    // the Routine "crdm_instr7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_instr8_resp_allKeys;
var crdm_instr8Components;
function crdm_instr8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instr8' ---
    t = 0;
    crdm_instr8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_instr8.started', globalClock.getTime());
    crdm_instr8_resp.keys = undefined;
    crdm_instr8_resp.rt = undefined;
    _crdm_instr8_resp_allKeys = [];
    // keep track of which components have finished
    crdm_instr8Components = [];
    crdm_instr8Components.push(crdm_instr8_title_txt);
    crdm_instr8Components.push(crdm_instr8_warn_txt);
    crdm_instr8Components.push(crdm_instr8_space_txt);
    crdm_instr8Components.push(crdm_instr8_resp);
    
    for (const thisComponent of crdm_instr8Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_instr8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instr8' ---
    // get current time
    t = crdm_instr8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instr8_title_txt* updates
    if (t >= 0.0 && crdm_instr8_title_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr8_title_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr8_title_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr8_title_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr8_warn_txt* updates
    if (t >= 0.0 && crdm_instr8_warn_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr8_warn_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr8_warn_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr8_warn_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr8_space_txt* updates
    if (t >= 0.0 && crdm_instr8_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr8_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_instr8_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_instr8_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_instr8_resp* updates
    if (t >= 0.0 && crdm_instr8_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instr8_resp.tStart = t;  // (not accounting for frame time here)
      crdm_instr8_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_instr8_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr8_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_instr8_resp.clearEvents(); });
    }
    
    if (crdm_instr8_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_instr8_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_instr8_resp_allKeys = _crdm_instr8_resp_allKeys.concat(theseKeys);
      if (_crdm_instr8_resp_allKeys.length > 0) {
        crdm_instr8_resp.keys = _crdm_instr8_resp_allKeys[_crdm_instr8_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_instr8_resp.rt = _crdm_instr8_resp_allKeys[_crdm_instr8_resp_allKeys.length - 1].rt;
        crdm_instr8_resp.duration = _crdm_instr8_resp_allKeys[_crdm_instr8_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_instr8Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_instr8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instr8' ---
    for (const thisComponent of crdm_instr8Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_instr8.stopped', globalClock.getTime());
    crdm_instr8_resp.stop();
    // the Routine "crdm_instr8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_pract1_instr_key_allKeys;
var crdm_pract1_instrComponents;
function crdm_pract1_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract1_instr' ---
    t = 0;
    crdm_pract1_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract1_instr.started', globalClock.getTime());
    crdm_pract1_instr_key.keys = undefined;
    crdm_pract1_instr_key.rt = undefined;
    _crdm_pract1_instr_key_allKeys = [];
    // keep track of which components have finished
    crdm_pract1_instrComponents = [];
    crdm_pract1_instrComponents.push(crdm_pract1_instr_name_txt);
    crdm_pract1_instrComponents.push(crdm_pract1_instr_txt);
    crdm_pract1_instrComponents.push(crdm_pract1_instr_space_txt);
    crdm_pract1_instrComponents.push(crdm_pract1_instr_key);
    
    for (const thisComponent of crdm_pract1_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract1_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract1_instr' ---
    // get current time
    t = crdm_pract1_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract1_instr_name_txt* updates
    if (t >= 0.0 && crdm_pract1_instr_name_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_instr_name_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_instr_name_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_instr_name_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract1_instr_txt* updates
    if (t >= 0.0 && crdm_pract1_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_instr_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_instr_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_instr_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract1_instr_space_txt* updates
    if (t >= 0.0 && crdm_pract1_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract1_instr_key* updates
    if (t >= 0.0 && crdm_pract1_instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_instr_key.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract1_instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract1_instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract1_instr_key.clearEvents(); });
    }
    
    if (crdm_pract1_instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract1_instr_key.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_pract1_instr_key_allKeys = _crdm_pract1_instr_key_allKeys.concat(theseKeys);
      if (_crdm_pract1_instr_key_allKeys.length > 0) {
        crdm_pract1_instr_key.keys = _crdm_pract1_instr_key_allKeys[_crdm_pract1_instr_key_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract1_instr_key.rt = _crdm_pract1_instr_key_allKeys[_crdm_pract1_instr_key_allKeys.length - 1].rt;
        crdm_pract1_instr_key.duration = _crdm_pract1_instr_key_allKeys[_crdm_pract1_instr_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract1_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract1_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract1_instr' ---
    for (const thisComponent of crdm_pract1_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract1_instr.stopped', globalClock.getTime());
    crdm_pract1_instr_key.stop();
    // the Routine "crdm_pract1_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract_init_fixComponents;
function crdm_pract_init_fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_init_fix' ---
    t = 0;
    crdm_pract_init_fixClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract_init_fix.started', globalClock.getTime());
    // keep track of which components have finished
    crdm_pract_init_fixComponents = [];
    crdm_pract_init_fixComponents.push(crdm_pract_init_fix_poly);
    
    for (const thisComponent of crdm_pract_init_fixComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function crdm_pract_init_fixRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_init_fix' ---
    // get current time
    t = crdm_pract_init_fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract_init_fix_poly* updates
    if (t >= 0.0 && crdm_pract_init_fix_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_init_fix_poly.tStart = t;  // (not accounting for frame time here)
      crdm_pract_init_fix_poly.frameNStart = frameN;  // exact frame index
      
      crdm_pract_init_fix_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_init_fix_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_init_fix_poly.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract_init_fixComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract_init_fixRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_init_fix' ---
    for (const thisComponent of crdm_pract_init_fixComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract_init_fix.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract1_trials;
function crdm_pract1_trialsLoopBegin(crdm_pract1_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crdm_pract1_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crdm_practice1.csv',
      seed: undefined, name: 'crdm_pract1_trials'
    });
    psychoJS.experiment.addLoop(crdm_pract1_trials); // add the loop to the experiment
    currentLoop = crdm_pract1_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrdm_pract1_trial of crdm_pract1_trials) {
      snapshot = crdm_pract1_trials.getSnapshot();
      crdm_pract1_trialsLoopScheduler.add(importConditions(snapshot));
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_trialRoutineBegin(snapshot));
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_trialRoutineEachFrame());
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_trialRoutineEnd(snapshot));
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_feedbackRoutineBegin(snapshot));
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_feedbackRoutineEachFrame());
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_feedbackRoutineEnd(snapshot));
      crdm_pract1_trialsLoopScheduler.add(crdm_pract1_trialsLoopEndIteration(crdm_pract1_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crdm_pract1_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crdm_pract1_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crdm_pract1_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var crdm_questplus_trials;
function crdm_questplus_trialsLoopBegin(crdm_questplus_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crdm_questplus_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crdm_questplus_trials.csv',
      seed: undefined, name: 'crdm_questplus_trials'
    });
    psychoJS.experiment.addLoop(crdm_questplus_trials); // add the loop to the experiment
    currentLoop = crdm_questplus_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrdm_questplus_trial of crdm_questplus_trials) {
      snapshot = crdm_questplus_trials.getSnapshot();
      crdm_questplus_trialsLoopScheduler.add(importConditions(snapshot));
      crdm_questplus_trialsLoopScheduler.add(crdm_questplusRoutineBegin(snapshot));
      crdm_questplus_trialsLoopScheduler.add(crdm_questplusRoutineEachFrame());
      crdm_questplus_trialsLoopScheduler.add(crdm_questplusRoutineEnd(snapshot));
      crdm_questplus_trialsLoopScheduler.add(crdm_qp_feedbackRoutineBegin(snapshot));
      crdm_questplus_trialsLoopScheduler.add(crdm_qp_feedbackRoutineEachFrame());
      crdm_questplus_trialsLoopScheduler.add(crdm_qp_feedbackRoutineEnd(snapshot));
      crdm_questplus_trialsLoopScheduler.add(crdm_questplus_trialsLoopEndIteration(crdm_questplus_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crdm_questplus_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crdm_questplus_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crdm_questplus_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var crdm_pract2_trials;
function crdm_pract2_trialsLoopBegin(crdm_pract2_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crdm_pract2_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crdm_practice2.csv',
      seed: undefined, name: 'crdm_pract2_trials'
    });
    psychoJS.experiment.addLoop(crdm_pract2_trials); // add the loop to the experiment
    currentLoop = crdm_pract2_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrdm_pract2_trial of crdm_pract2_trials) {
      snapshot = crdm_pract2_trials.getSnapshot();
      crdm_pract2_trialsLoopScheduler.add(importConditions(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_trialRoutineBegin(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_trialRoutineEachFrame());
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_trialRoutineEnd(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_feedbackRoutineBegin(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_feedbackRoutineEachFrame());
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_feedbackRoutineEnd(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_confRoutineBegin(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_confRoutineEachFrame());
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_confRoutineEnd(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_itiRoutineBegin(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_itiRoutineEachFrame());
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_itiRoutineEnd(snapshot));
      crdm_pract2_trialsLoopScheduler.add(crdm_pract2_trialsLoopEndIteration(crdm_pract2_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crdm_pract2_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crdm_pract2_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crdm_pract2_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var crdm_trials;
function crdm_trialsLoopBegin(crdm_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crdm_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crdm_gen_trials_idx.csv',
      seed: undefined, name: 'crdm_trials'
    });
    psychoJS.experiment.addLoop(crdm_trials); // add the loop to the experiment
    currentLoop = crdm_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrdm_trial of crdm_trials) {
      snapshot = crdm_trials.getSnapshot();
      crdm_trialsLoopScheduler.add(importConditions(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trialRoutineBegin(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trialRoutineEachFrame());
      crdm_trialsLoopScheduler.add(crdm_trialRoutineEnd(snapshot));
      crdm_trialsLoopScheduler.add(crdm_feedbackRoutineBegin(snapshot));
      crdm_trialsLoopScheduler.add(crdm_feedbackRoutineEachFrame());
      crdm_trialsLoopScheduler.add(crdm_feedbackRoutineEnd(snapshot));
      crdm_trialsLoopScheduler.add(crdm_confRoutineBegin(snapshot));
      crdm_trialsLoopScheduler.add(crdm_confRoutineEachFrame());
      crdm_trialsLoopScheduler.add(crdm_confRoutineEnd(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trials_itiRoutineBegin(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trials_itiRoutineEachFrame());
      crdm_trialsLoopScheduler.add(crdm_trials_itiRoutineEnd(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trialsLoopEndIteration(crdm_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crdm_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crdm_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crdm_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var my_loop;
var crdm_idx1;
var _crdm_pract1_trial_resp_allKeys;
var crdm_pract1_trialComponents;
function crdm_pract1_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract1_trial' ---
    t = 0;
    crdm_pract1_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract1_trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract1_trial_code
    my_loop = eval(crdm_practice_loop1_name);
    
    crdm_idx1 = random.randint(0, 1);
    crdm_sure_pos1 = crdm_pos1[crdm_idx1];
    crdm_sure_resp1 = crdm_resp1[crdm_idx1];
    crdm_pract1_trial_img.setImage(("images/" + crdm_img1));
    crdm_pract1_trial_lott_top_txt.setText(("$" + format(crdm_lott_top1).toString()).toString());
    crdm_pract1_trial_lott_bot_txt.setText(("$" + format(crdm_lott_bot1).toString()).toString());
    crdm_pract1_trial_sure_amt_txt.setPos(crdm_sure_pos1);
    crdm_pract1_trial_sure_amt_txt.setText(("$" + format(crdm_sure_amt1).toString()).toString());
    crdm_pract1_trial_resp.keys = undefined;
    crdm_pract1_trial_resp.rt = undefined;
    _crdm_pract1_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_pract1_trialComponents = [];
    crdm_pract1_trialComponents.push(crdm_pract1_trial_img);
    crdm_pract1_trialComponents.push(crdm_pract1_trial_lott_top_txt);
    crdm_pract1_trialComponents.push(crdm_pract1_trial_lott_bot_txt);
    crdm_pract1_trialComponents.push(crdm_pract1_trial_sure_amt_txt);
    crdm_pract1_trialComponents.push(GRFX_fix4);
    crdm_pract1_trialComponents.push(crdm_pract1_trial_cue);
    crdm_pract1_trialComponents.push(crdm_pract1_trial_resp);
    
    for (const thisComponent of crdm_pract1_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract1_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract1_trial' ---
    // get current time
    t = crdm_pract1_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract1_trial_img* updates
    if (t >= 0.0 && crdm_pract1_trial_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_img.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_img.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_trial_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_img.setAutoDraw(false);
    }
    
    // *crdm_pract1_trial_lott_top_txt* updates
    if (t >= 0.0 && crdm_pract1_trial_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_trial_lott_top_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_lott_top_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_lott_top_txt.setAutoDraw(false);
    }
    
    // *crdm_pract1_trial_lott_bot_txt* updates
    if (t >= 0.0 && crdm_pract1_trial_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_trial_lott_bot_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_lott_bot_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_lott_bot_txt.setAutoDraw(false);
    }
    
    // *crdm_pract1_trial_sure_amt_txt* updates
    if (t >= 0.0 && crdm_pract1_trial_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_trial_sure_amt_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_sure_amt_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_sure_amt_txt.setAutoDraw(false);
    }
    
    // *GRFX_fix4* updates
    if (t >= 3 && GRFX_fix4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix4.tStart = t;  // (not accounting for frame time here)
      GRFX_fix4.frameNStart = frameN;  // exact frame index
      
      GRFX_fix4.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix4.setAutoDraw(false);
    }
    
    // *crdm_pract1_trial_cue* updates
    if (t >= 3 && crdm_pract1_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_pract1_trial_resp* updates
    if (t >= 3 && crdm_pract1_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract1_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract1_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract1_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_pract1_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract1_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_pract1_trial_resp_allKeys = _crdm_pract1_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_pract1_trial_resp_allKeys.length > 0) {
        crdm_pract1_trial_resp.keys = _crdm_pract1_trial_resp_allKeys[0].name;  // just the first key pressed
        crdm_pract1_trial_resp.rt = _crdm_pract1_trial_resp_allKeys[0].rt;
        crdm_pract1_trial_resp.duration = _crdm_pract1_trial_resp_allKeys[0].duration;
        // was this correct?
        if (crdm_pract1_trial_resp.keys == crdm_sure_resp1) {
            crdm_pract1_trial_resp.corr = 1;
        } else {
            crdm_pract1_trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract1_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var crdm_pract1_key;
var crdm_pract1_sure_key;
function crdm_pract1_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract1_trial' ---
    for (const thisComponent of crdm_pract1_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract1_trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from crdm_pract1_trial_code
    crdm_pract1_key = crdm_pract1_trial_resp.keys;
    crdm_pract1_sure_key = crdm_pract1_trial_resp.corr;
    my_loop.addData("crdm_trial_type", "practice1");
    
    // was no response the correct answer?!
    if (crdm_pract1_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(crdm_sure_resp1)) {
         crdm_pract1_trial_resp.corr = 1;  // correct non-response
      } else {
         crdm_pract1_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_pract1_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_pract1_trial_resp.keys', crdm_pract1_trial_resp.keys);
    psychoJS.experiment.addData('crdm_pract1_trial_resp.corr', crdm_pract1_trial_resp.corr);
    if (typeof crdm_pract1_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_pract1_trial_resp.rt', crdm_pract1_trial_resp.rt);
        psychoJS.experiment.addData('crdm_pract1_trial_resp.duration', crdm_pract1_trial_resp.duration);
        routineTimer.reset();
        }
    
    crdm_pract1_trial_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract1_feedbackComponents;
function crdm_pract1_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract1_feedback' ---
    t = 0;
    crdm_pract1_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract1_feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract1_feedback_code
    if ((crdm_pract1_key === undefined)) {
        crdm_msg1 = "NO RESPONSE";
    } else {
        if (crdm_pract1_sure_key) {
            crdm_msg1 = ("CERTAIN $" + format(crdm_sure_amt1.toString()));
        } else {
            crdm_msg1 = "LOTTERY";
        }
    }
    
    crdm_pract1_feedback_txt.setText(crdm_msg1);
    // keep track of which components have finished
    crdm_pract1_feedbackComponents = [];
    crdm_pract1_feedbackComponents.push(crdm_pract1_feedback_txt);
    
    for (const thisComponent of crdm_pract1_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract1_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract1_feedback' ---
    // get current time
    t = crdm_pract1_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract1_feedback_txt* updates
    if (t >= 0.0 && crdm_pract1_feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract1_feedback_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract1_feedback_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract1_feedback_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract1_feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract1_feedback_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract1_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract1_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract1_feedback' ---
    for (const thisComponent of crdm_pract1_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract1_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_qp_instr_resp_allKeys;
var crdm_qp_instrComponents;
function crdm_qp_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_qp_instr' ---
    t = 0;
    crdm_qp_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_qp_instr.started', globalClock.getTime());
    crdm_qp_instr_resp.keys = undefined;
    crdm_qp_instr_resp.rt = undefined;
    _crdm_qp_instr_resp_allKeys = [];
    // keep track of which components have finished
    crdm_qp_instrComponents = [];
    crdm_qp_instrComponents.push(crdm_qp_instr_title_txt);
    crdm_qp_instrComponents.push(crdm_qp_instr_txt);
    crdm_qp_instrComponents.push(crdm_qp_instr_space_txt);
    crdm_qp_instrComponents.push(crdm_qp_instr_resp);
    
    for (const thisComponent of crdm_qp_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_qp_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_qp_instr' ---
    // get current time
    t = crdm_qp_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_qp_instr_title_txt* updates
    if (t >= 0.0 && crdm_qp_instr_title_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_qp_instr_title_txt.tStart = t;  // (not accounting for frame time here)
      crdm_qp_instr_title_txt.frameNStart = frameN;  // exact frame index
      
      crdm_qp_instr_title_txt.setAutoDraw(true);
    }
    
    
    // *crdm_qp_instr_txt* updates
    if (t >= 0.0 && crdm_qp_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_qp_instr_txt.tStart = t;  // (not accounting for frame time here)
      crdm_qp_instr_txt.frameNStart = frameN;  // exact frame index
      
      crdm_qp_instr_txt.setAutoDraw(true);
    }
    
    
    // *crdm_qp_instr_space_txt* updates
    if (t >= 0.0 && crdm_qp_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_qp_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_qp_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_qp_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_qp_instr_resp* updates
    if (t >= 0.0 && crdm_qp_instr_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_qp_instr_resp.tStart = t;  // (not accounting for frame time here)
      crdm_qp_instr_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_qp_instr_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_qp_instr_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_qp_instr_resp.clearEvents(); });
    }
    
    if (crdm_qp_instr_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_qp_instr_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_qp_instr_resp_allKeys = _crdm_qp_instr_resp_allKeys.concat(theseKeys);
      if (_crdm_qp_instr_resp_allKeys.length > 0) {
        crdm_qp_instr_resp.keys = _crdm_qp_instr_resp_allKeys[_crdm_qp_instr_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_qp_instr_resp.rt = _crdm_qp_instr_resp_allKeys[_crdm_qp_instr_resp_allKeys.length - 1].rt;
        crdm_qp_instr_resp.duration = _crdm_qp_instr_resp_allKeys[_crdm_qp_instr_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_qp_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_qp_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_qp_instr' ---
    for (const thisComponent of crdm_qp_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_qp_instr.stopped', globalClock.getTime());
    crdm_qp_instr_resp.stop();
    // the Routine "crdm_qp_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_idx_qp;
var crdm_sure_amt_qp;
var crdm_ambiguity;
var crdm_probability;
var crdm_lott_top_qp;
var crdm_lott_bot_qp;
var crdm_img_qp;
var _crdm_questplus_trial_resp_allKeys;
var crdm_questplusComponents;
function crdm_questplusRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_questplus' ---
    t = 0;
    crdm_questplusClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_questplus.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_questplus_JS
    my_loop = eval(crdm_questplus_loop_name);
    crdm_idx_qp = random.randint(0, 1);
    crdm_sure_pos_qp = crdm_pos_qp[crdm_idx_qp];
    crdm_sure_resp_qp = crdm_resp_qp[crdm_idx_qp];
    
    if (crdm_domain_type == 'gain') { //GAINS - get ambiguity, probability, and lott top & bottom
        crdm_sure_amt_qp = crdm_gain_stim_space[crdm_contrast_idx_gain][3];
        crdm_ambiguity = crdm_gain_stim_space[crdm_contrast_idx_gain][1];
        if (!crdm_ambiguity) {
            crdm_probability = crdm_gain_stim_space[crdm_contrast_idx_gain][2];
        } else {
            crdm_probability = 0.5;
        }
        if (crdm_nonzero_side == 'top') {
            crdm_lott_top_qp = crdm_gain_stim_space[crdm_contrast_idx_gain][0];
            crdm_lott_bot_qp = 0;
        } else {
            crdm_lott_top_qp = 0;
            crdm_lott_bot_qp = crdm_gain_stim_space[crdm_contrast_idx_gain][0];
        }
    } else { //LOSSES - get ambiguity, probability, and lott top & bottom
        crdm_sure_amt_qp = crdm_loss_stim_space[crdm_contrast_idx_loss][3];
        crdm_ambiguity = crdm_loss_stim_space[crdm_contrast_idx_loss][1];
        if (!crdm_ambiguity) {
            crdm_probability = crdm_loss_stim_space[crdm_contrast_idx_loss][2];
        } else {
            crdm_probability = 0.5;
        }
        if (crdm_nonzero_side == 'top') {
            crdm_lott_top_qp = crdm_loss_stim_space[crdm_contrast_idx_loss][0];
            crdm_lott_bot_qp = 0;
        } else {
            crdm_lott_top_qp = 0;
            crdm_lott_bot_qp = crdm_loss_stim_space[crdm_contrast_idx_loss][0];
        }
    }
    
    if (crdm_ambiguity) { //set current image
        crdm_img_qp = 'ambig_' + parseInt(crdm_ambiguity * 100) + '.bmp';
    } else {
        if (crdm_lott_top_qp != 0) {
            crdm_img_qp = 'risk_red_' + parseInt(crdm_probability * 100) + '.bmp'
        } else {
            crdm_img_qp = 'risk_blue_' + parseInt(crdm_probability * 100) + '.bmp'
        }
    }
    crdm_questplus_img.setImage(("images/" + crdm_img_qp));
    crdm_questplus_trial_lott_top_txt.setText(("$" + format(crdm_lott_top_qp).toString()).toString());
    crdm_questplus_trial_lott_bot_txt.setText(("$" + format(crdm_lott_bot_qp).toString()).toString());
    crdm_questplus_trial_sure_amt_txt.setPos(crdm_sure_pos_qp);
    crdm_questplus_trial_sure_amt_txt.setText(("$" + format(crdm_sure_amt_qp).toString()).toString());
    crdm_questplus_trial_resp.keys = undefined;
    crdm_questplus_trial_resp.rt = undefined;
    _crdm_questplus_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_questplusComponents = [];
    crdm_questplusComponents.push(crdm_questplus_img);
    crdm_questplusComponents.push(crdm_questplus_trial_lott_top_txt);
    crdm_questplusComponents.push(crdm_questplus_trial_lott_bot_txt);
    crdm_questplusComponents.push(crdm_questplus_trial_sure_amt_txt);
    crdm_questplusComponents.push(GRFX_fix3);
    crdm_questplusComponents.push(crdm_questplus_trial_cue);
    crdm_questplusComponents.push(crdm_questplus_trial_resp);
    
    for (const thisComponent of crdm_questplusComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_questplusRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_questplus' ---
    // get current time
    t = crdm_questplusClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_questplus_img* updates
    if (t >= 0.0 && crdm_questplus_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_img.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_img.frameNStart = frameN;  // exact frame index
      
      crdm_questplus_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_img.setAutoDraw(false);
    }
    
    // *crdm_questplus_trial_lott_top_txt* updates
    if (t >= 0.0 && crdm_questplus_trial_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_trial_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_trial_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      crdm_questplus_trial_lott_top_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_trial_lott_top_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_trial_lott_top_txt.setAutoDraw(false);
    }
    
    // *crdm_questplus_trial_lott_bot_txt* updates
    if (t >= 0.0 && crdm_questplus_trial_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_trial_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_trial_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      crdm_questplus_trial_lott_bot_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_trial_lott_bot_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_trial_lott_bot_txt.setAutoDraw(false);
    }
    
    // *crdm_questplus_trial_sure_amt_txt* updates
    if (t >= 0.0 && crdm_questplus_trial_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_trial_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_trial_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      crdm_questplus_trial_sure_amt_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_trial_sure_amt_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_trial_sure_amt_txt.setAutoDraw(false);
    }
    
    // *GRFX_fix3* updates
    if (t >= 3 && GRFX_fix3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix3.tStart = t;  // (not accounting for frame time here)
      GRFX_fix3.frameNStart = frameN;  // exact frame index
      
      GRFX_fix3.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix3.setAutoDraw(false);
    }
    
    // *crdm_questplus_trial_cue* updates
    if (t >= 3 && crdm_questplus_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_questplus_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_questplus_trial_resp* updates
    if (t >= 3 && crdm_questplus_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_questplus_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_questplus_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_questplus_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_questplus_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_questplus_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_questplus_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_questplus_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_questplus_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_questplus_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_questplus_trial_resp_allKeys = _crdm_questplus_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_questplus_trial_resp_allKeys.length > 0) {
        crdm_questplus_trial_resp.keys = _crdm_questplus_trial_resp_allKeys[0].name;  // just the first key pressed
        crdm_questplus_trial_resp.rt = _crdm_questplus_trial_resp_allKeys[0].rt;
        crdm_questplus_trial_resp.duration = _crdm_questplus_trial_resp_allKeys[0].duration;
        // was this correct?
        if (crdm_questplus_trial_resp.keys == crdm_sure_resp_qp) {
            crdm_questplus_trial_resp.corr = 1;
        } else {
            crdm_questplus_trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_questplusComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var crdm_qp_key;
var crdm_qp_sure_key;
var crdm_post_mean;
var crdm_post_sd;
function crdm_questplusRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_questplus' ---
    for (const thisComponent of crdm_questplusComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_questplus.stopped', globalClock.getTime());
    // Run 'End Routine' code from crdm_questplus_JS
    crdm_qp_key = crdm_questplus_trial_resp.keys;
    crdm_qp_sure_key = crdm_questplus_trial_resp.corr;
    
    crdm_response = !crdm_qp_sure_key;
    if (crdm_domain_type == 'gain'){
        // update posterior
        crdm_q_gain.update(crdm_contrast_idx_gain, crdm_response);
        // find next contrast index
        crdm_contrast_idx_gain = crdm_q_gain.next_contrast();
        crdm_post_mean = weighted_avg(crdm_q_gain);
        crdm_post_sd = weighted_sd(crdm_q_gain);
    } else {
        crdm_q_loss.update(crdm_contrast_idx_loss, crdm_response);
        crdm_contrast_idx_loss = crdm_q_loss.next_contrast();
        crdm_post_mean = weighted_avg(crdm_q_loss);
        crdm_post_sd = weighted_sd(crdm_q_loss);
    }
    
    my_loop.addData("crdm_trial_type", "questplus");
    my_loop.addData("crdm_response", crdm_response);
    my_loop.addData("crdm_mean_alpha", crdm_post_mean[0]);
    my_loop.addData("crdm_mean_beta", crdm_post_mean[1]);
    my_loop.addData("crdm_mean_gamma", crdm_post_mean[2]);
    my_loop.addData("crdm_sd_alpha", crdm_post_sd[0]); 
    my_loop.addData("crdm_sd_beta", crdm_post_sd[1]);
    my_loop.addData("crdm_sd_gamma", crdm_post_sd[2]);
    my_loop.addData("crdm_lott_reward", crdm_lott_top_qp + crdm_lott_bot_qp);
    my_loop.addData("crdm_lott_prob", Number.parseInt((crdm_probability * 100)));
    my_loop.addData("crdm_ambig_level", Number.parseInt((crdm_ambiguity * 100)));
    // was no response the correct answer?!
    if (crdm_questplus_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(crdm_sure_resp_qp)) {
         crdm_questplus_trial_resp.corr = 1;  // correct non-response
      } else {
         crdm_questplus_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_questplus_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_questplus_trial_resp.keys', crdm_questplus_trial_resp.keys);
    psychoJS.experiment.addData('crdm_questplus_trial_resp.corr', crdm_questplus_trial_resp.corr);
    if (typeof crdm_questplus_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_questplus_trial_resp.rt', crdm_questplus_trial_resp.rt);
        psychoJS.experiment.addData('crdm_questplus_trial_resp.duration', crdm_questplus_trial_resp.duration);
        routineTimer.reset();
        }
    
    crdm_questplus_trial_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_qp_feedbackComponents;
function crdm_qp_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_qp_feedback' ---
    t = 0;
    crdm_qp_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_qp_feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_qp_FB_code
    if ((crdm_qp_key === undefined)) {
        crdm_msg_qp = "NO RESPONSE";
    } else {
        if (crdm_qp_sure_key) {
            crdm_msg_qp  = ("CERTAIN $" + format(crdm_sure_amt_qp.toString()));
        } else {
            crdm_msg_qp  = "LOTTERY";
        }
    }
    
    crdm_qp_FB_txt.setText(crdm_msg_qp);
    // keep track of which components have finished
    crdm_qp_feedbackComponents = [];
    crdm_qp_feedbackComponents.push(crdm_qp_FB_txt);
    
    for (const thisComponent of crdm_qp_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_qp_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_qp_feedback' ---
    // get current time
    t = crdm_qp_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_qp_FB_txt* updates
    if (t >= 0.0 && crdm_qp_FB_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_qp_FB_txt.tStart = t;  // (not accounting for frame time here)
      crdm_qp_FB_txt.frameNStart = frameN;  // exact frame index
      
      crdm_qp_FB_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_qp_FB_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_qp_FB_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_qp_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_qp_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_qp_feedback' ---
    for (const thisComponent of crdm_qp_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_qp_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var range;
var arange;
var clone;
var sum;
var crdm_fit_gain;
var crdm_fit_loss;
var alpha_gain;
var alpha_loss;
var beta_gain;
var beta_loss;
var prob;
var amb;
var crdm_steps;
var append_trial;
var lottery2sv;
var round2fiddy;
var safe2sv;
var sort_it;
var sv2money;
var make_sample_sv_ranges;
var crdm_trials_dict;
var generate_trials;
var crdm_schedule_genComponents;
function crdm_schedule_genRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_schedule_gen' ---
    t = 0;
    crdm_schedule_genClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_schedule_gen.started', globalClock.getTime());
    //# because Pavlovia doesn't auto-convert append or extend to push, 
    //#  make the same functions work for any javascript array by affecting the prototype
    Array.prototype.append = Array.prototype.push
    Array.prototype.extend = function(arr){this.push(...arr)};
    
    //# avoid using the "function name(){}" syntax
    //#  to account for Pavlovia's scope problems.
    
    range = function(start_stop, post_stop, step=1) {
        //# create a list sequence with a starting point, stopping point, and step size
        //#  the step size is assumed 1 if not provided
        //#  the first value is considered the stopping point if the second value is not given,
        //#   in which case the starting point is assumed to be 0.
        //#  post_stop is the non-inclusive end point.
        var arr = [];
        if (post_stop != undefined) {
            for (var i = start_stop; i < post_stop; i += step) {
                arr.push(i);
            }
        } else {
            for (var i = 0; i < start_stop; i += step) {
                arr.push(i);
            }
        }
        return arr;
    }
    
    arange = function(start_stop, post_stop, step=1, rounding=2) {
        //# same as range(), but with rounding built-in
        //# create a list sequence with a starting point, stopping point, and step size
        //#  the step size is assumed 1 if not provided
        //#  the first value is considered the stopping point if the second value is not given,
        //#   in which case the starting point is assumed to be 0.
        //#  post_stop is the non-inclusive end point.
        var arr = [];
        if (post_stop != undefined) {
            if (post_stop < start_stop) {
                for (var i = start_stop; i > post_stop; i += step) {
                    arr.push(round(i, rounding))
                } 
            } else {
                for (var i = start_stop; i < post_stop; i += step) {
                    arr.push(round(i, rounding))
                } 
            }
        } else {
            if (start_stop < 0) {
                for (var i = 0; i > start_stop; i += step) {
                    arr.push(round(i, rounding))
                }
            } else {
                for (var i = 0; i < start_stop; i += step) {
                    arr.push(round(i, rounding))
                }
            }
        }
        return arr;
    }
    
    clone = function(arr) {
        //# recursive function to deep copy arrays and dictionaries    
        var loops, tmp;
        //# see if it is an array
        //#  check a couple of things to try to avoid objects with these keys
        if (Array.isArray(arr)) {
            loops = arr;
            tmp = [];
        } else {
            loops = Object.keys(arr);
            tmp = {};
        }
        loops.forEach(function(val) {
            var value;
            //# if the looped items are the array, push() to a list
            if (loops === arr) {
                value = val;
                if (typeof(value) == "object") {
                    //# if the subelement is another complex object, 
                    //#  then clone it as well.
                    tmp.push(clone(value));
                } else {
                    tmp.push(value);
                }
            } else { //# if the looped items are the dictionary
                     //#  add them with the key
                value = arr[val];
                if (typeof(value) == "object") {
                    //# if the subelement is another complex object, 
                    //#  then clone it as well.
                    tmp[val] = clone(value);
                } else {
                    tmp[val] = value;
                }
            }
        })
        return tmp;
    }
    
    sum = function(arr){return arr.reduce((partialSum, a) => partialSum + a, 0)}
    
    
    random = {
        //# contains useful random number generation functions
        "random" : function(start_stop=1, post_stop=undefined, count=1) {
            var results = [];
            range(count).forEach(function() {
                if (post_stop != undefined) {
                    if (post_stop < start_stop) {
                        var tmp = post_stop;
                        post_stop = start_stop;
                        start_stop = tmp;
                    }
                    results.push((start_stop + Math.random() * (post_stop - start_stop)));
                } else {
                    //# if post_stop is not defined, start_stop is the non-inclusive max value.
                    results.push((Math.random() * start_stop));
                }
            });
            if (count == 1)
                return results[0];
                return results;       
        },
        
        "randint" : function(start_stop, post_stop, count=1) {
            var results = [];
            range(count).forEach(function() {
                //# Math.random() never gives exactly 1, so it
                //#  never reaches the provided max value.
                if (post_stop != undefined) {
                    if (post_stop < start_stop) {
                        var tmp = post_stop;
                        post_stop = start_stop;
                        start_stop = tmp;
                    }
                    results.push(parseInt(start_stop + Math.random() * (post_stop - start_stop)));
                } else {
                    //# if post_stop is not defined, start_stop is non-inclusive max value
                    results.push(parseInt(Math.random() * start_stop));
                }
            });
            if (count == 1)
                return results[0];
                return results;
        },
        
        "choice" : function(arr, count=1, with_replacement=true) {
            var results = [];
            if (with_replacement) {
                range(count).forEach(function() {
                    results.push(arr[random.randint(arr.length)]);
                });
            } else {
                //# make shallow copy to choose from.
                //#  you can always clone returned result if you want unique copies,
                //#  and it makes no difference for arrays of primitives 
                //#  (like numeric indices or string keys).
                var tmp = [...arr];
                range(count).forEach(function() {
                    if (tmp.length == 0)
                        //# refill array
                        tmp = [...arr];
                        results.push(tmp.splice(random.randint(tmp.length), 1));
                });
            }
            if (count == 1)
                return results[0];
                return results;
        }
    }
    
    
    
    crdm_fit_gain = weighted_avg(crdm_q_gain) //# parameters for gains
    crdm_fit_loss = weighted_avg(crdm_q_loss) //# parameters for losses
    
    //# global variables
    alpha_gain = crdm_fit_gain[0];
    alpha_loss = crdm_fit_loss[0];
    beta_gain = crdm_fit_gain[1];
    beta_loss = crdm_fit_loss[1];
    prob = 0.5;
    amb = 0; 
    crdm_steps = 4;
    //# domain: gain = 1, loss = -1
    
    append_trial = function(trials, safe_sv, lott_sv, lott, safe, prob, amb, sv_half, domain) {
        //# appends trial info for presentation and output
        trials["crdm_safe_sv"].append(safe_sv);
        trials["crdm_lott_sv"].append(safe_sv);
        trials["crdm_lott"].append(lott);
        trials["crdm_sure_amt"].append(safe);
        trials["crdm_lott_p"].append(prob);
        trials["crdm_amb_lev"].append(amb);
        trials["crdm_delta_sv"].append(lott_sv - safe_sv);
        trials["crdm_domain"].append(domain);
    }
    
    lottery2sv = function(objective_value, alpha_risk_aversion, beta_ambiguity_aversion, probability, ambiguity) {
        //# converts lottery option value from money space --> subjective value space
        //# domain considered where function is called
        return Math.sign(objective_value) * (probability - beta_ambiguity_aversion * (ambiguity/2)) 
               * Math.pow(Math.abs(objective_value), alpha_risk_aversion);
    }
    
    round2fiddy = function(number) {
        //# rounding all money values to nearest $0.50
        return Math.round(number * 2)/2;
    }
    
    safe2sv = function(subjective_value, alpha) { //# deprecated
        //# converts safe option value from money space --> subjective value space
        return Math.sign(subjective_value) * Math.pow(Math.abs(subjective_value), alpha);
    }
    
    sort_it = function(arr) {
        //# sort ascending (used for SVs)
        arr.sort(function(a, b){return a - b});
    }
    
    sv2money = function(subjective_value, domain, alpha, beta, prob, amb) { 
        //# based on whether you provide beta, converts each value in the 
        //#  subjective value (safe & lottery) range --> money spaces
        var money;
        if (beta === undefined) { //# beta isn't used for safe money
            //# compute safe money using inverse of SV formula
            //#  gain - money(V) = 1*SV**1/alpha
            //#  loss - money(V) = -1*SV**1/alpha
            money = round2fiddy(domain * Math.pow(Math.abs(subjective_value), 1/alpha)); 
        } else {
            //# compute lottery money using inverse of SV formula
            //#  gain - money(V) = 1*(SV/P-B*A/2)**1/alpha
            //#  loss - money(V) = -1*(SV/P-B*A/2)**1/alpha
            money = round2fiddy(domain * Math.pow(Math.abs(subjective_value)/(prob - beta * amb/2), 1/alpha));
        }
        //# constrains min and max lottery $ and ensure correct sign for gain/loss
        money = domain * Math.min(50, Math.max(0.5, Math.abs(money)));
        return money
    }
    
    make_sample_sv_ranges = function(domain, alpha, beta, prob, amb, steps) {
        //# calculates SVdeltas and corresponding monetary values
        var sv_max = domain * lottery2sv(50, alpha, beta, prob, amb); //# maximum possible lottery value ($ --> SV space)
        var sv_min = 0; //# domain * safe2sv(0.5, alpha); //#minimum possible lottery value ($ --> SV space)
        var sv_half = sv_max/2; //# SV of trial halfway between 0 and max lottery gain (true center)
        var step_size = (sv_max - sv_min)/(2 * steps - 1);
        var space = arange(sv_min, sv_max + step_size/2, step_size);
        return [space, sv_half];
    }
    
    crdm_trials_dict = {"crdm_safe_sv":[], "crdm_lott_sv":[], "crdm_lott":[], "crdm_sure_amt":[], //# dict for trial variables
                        "crdm_lott_p":[], "crdm_amb_lev":[], "crdm_delta_sv":[], "crdm_domain":[]};
    
    generate_trials = function(trials, domain, alpha, beta, steps) {
        //# creates trial schedule for each domain (gain/loss)
        var amb_space = [0.24, 0.5, 0.74]; //# possible ambiguity values
        var prob_space = [0.13, 0.25, 0.38, 0.5, 0.75]; //# possible probability values
        var trials_per = 9; //# number of trials per unique prob/amb option
        var choice_idxs = [0,1,2,3,3.5,4,5,6,7];
        var delta_idx = range(8); //# index of trials_remaining_per_sv_delta array
    
        prob_space.forEach(function(prob) {
            //# non-ambiguity trials
            var tmp = make_sample_sv_ranges(domain, alpha, beta, prob, 0, steps);
            var svs = tmp[0]; //# get list of SV quadrants
            var sv_half = tmp[1]; //# get SV_half
            range(trials_per).forEach(function(_, tidx) { //# for each of 9 trials per prob
                var choice_idx = choice_idxs[tidx]; //# current sample index
                if (choice_idx != parseInt(choice_idx)) { //# if not an integer
                    var inty = parseInt(choice_idx); //# turn it into integer
                    choice_idx = random.randint(inty, inty + 2); //# randomly sample within two steps
                }
                var subspace_sv = svs[choice_idx]; //# specific random SV for curr quad
                var lott = sv2money(subspace_sv, domain, alpha, beta, prob, 0); //# specific lottery $ for curr quad
                var safe = sv2money(sv_half, domain, alpha); //# specific safe $ for curr quad
                append_trial(trials, sv_half, subspace_sv, lott, safe, prob, 0, sv_half, domain); //# save to trials dict
            });
    
        });
    
        amb_space.forEach(function(amb) {
            //# ambiguity trials
            var tmp = make_sample_sv_ranges(domain, alpha, beta, 0.5, amb, steps);
            var svs = tmp[0]; //# get list of SV quadrants
            var sv_half = tmp[1]; //# get SV_half
            range(trials_per).forEach(function(_, tidx) { //# for each of 9 trials per amb
                var choice_idx = choice_idxs[tidx]; //# current sample index
                if (choice_idx != parseInt(choice_idx)) { //# if not an integer
                    var inty = parseInt(choice_idx); //# turn it into integer
                    choice_idx = random.randint(inty, inty + 2); //# randomly sample within two steps
                }
                var subspace_sv = svs[choice_idx]; //# specific random SV for curr quad
                var lott = sv2money(subspace_sv, domain, alpha, beta, 0.5, amb); //# specific lottery $ for curr quad
                var safe = sv2money(sv_half, domain, alpha); //# specific safe $ for curr quad
                append_trial(trials, sv_half, subspace_sv, lott, safe, 0.5, amb, sv_half, domain); //# save to trials dict
            });
    
        });
    }
    
    //# generate schedule for each domain
    generate_trials(crdm_trials_dict, 1, alpha_gain, beta_gain, crdm_steps); //# gain trials
    generate_trials(crdm_trials_dict, -1, alpha_loss, beta_loss, crdm_steps); //# loss trials
    // keep track of which components have finished
    crdm_schedule_genComponents = [];
    
    for (const thisComponent of crdm_schedule_genComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_schedule_genRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_schedule_gen' ---
    // get current time
    t = crdm_schedule_genClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_schedule_genComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_schedule_genRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_schedule_gen' ---
    for (const thisComponent of crdm_schedule_genComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_schedule_gen.stopped', globalClock.getTime());
    // the Routine "crdm_schedule_gen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_pract2_instr_key_allKeys;
var crdm_pract2_instrComponents;
function crdm_pract2_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract2_instr' ---
    t = 0;
    crdm_pract2_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract2_instr.started', globalClock.getTime());
    crdm_pract2_instr_key.keys = undefined;
    crdm_pract2_instr_key.rt = undefined;
    _crdm_pract2_instr_key_allKeys = [];
    // keep track of which components have finished
    crdm_pract2_instrComponents = [];
    crdm_pract2_instrComponents.push(crdm_pract2_instr_name_txt);
    crdm_pract2_instrComponents.push(crdm_pract2_instr_txt);
    crdm_pract2_instrComponents.push(crdm_pract2_instr_space_txt);
    crdm_pract2_instrComponents.push(crdm_pract2_instr_key);
    
    for (const thisComponent of crdm_pract2_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract2_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract2_instr' ---
    // get current time
    t = crdm_pract2_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract2_instr_name_txt* updates
    if (t >= 0.0 && crdm_pract2_instr_name_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_instr_name_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_instr_name_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_instr_name_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract2_instr_txt* updates
    if (t >= 0.0 && crdm_pract2_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_instr_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_instr_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_instr_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract2_instr_space_txt* updates
    if (t >= 0.0 && crdm_pract2_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract2_instr_key* updates
    if (t >= 0.0 && crdm_pract2_instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_instr_key.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract2_instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_instr_key.clearEvents(); });
    }
    
    if (crdm_pract2_instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract2_instr_key.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_pract2_instr_key_allKeys = _crdm_pract2_instr_key_allKeys.concat(theseKeys);
      if (_crdm_pract2_instr_key_allKeys.length > 0) {
        crdm_pract2_instr_key.keys = _crdm_pract2_instr_key_allKeys[_crdm_pract2_instr_key_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract2_instr_key.rt = _crdm_pract2_instr_key_allKeys[_crdm_pract2_instr_key_allKeys.length - 1].rt;
        crdm_pract2_instr_key.duration = _crdm_pract2_instr_key_allKeys[_crdm_pract2_instr_key_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract2_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract2_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract2_instr' ---
    for (const thisComponent of crdm_pract2_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract2_instr.stopped', globalClock.getTime());
    crdm_pract2_instr_key.stop();
    // the Routine "crdm_pract2_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_idx2;
var _crdm_pract2_trial_resp_allKeys;
var crdm_pract2_trialComponents;
function crdm_pract2_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract2_trial' ---
    t = 0;
    crdm_pract2_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract2_trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract2_trial_code
    my_loop = eval(crdm_practice_loop2_name);
    crdm_idx2 = random.randint(0, 1);
    crdm_sure_pos2 = crdm_pos2[crdm_idx2];
    crdm_sure_resp2 = crdm_resp2[crdm_idx2];
    crdm_pract2_trial_img.setImage(("images/" + crdm_img2));
    crdm_pract2_trial_lott_top_txt.setText(("$" + format(crdm_lott_top2).toString()).toString());
    crdm_pract2_trial_lott_bot_txt.setText(("$" + format(crdm_lott_bot2).toString()).toString());
    crdm_pract2_trial_sure_amt_txt.setPos(crdm_sure_pos2);
    crdm_pract2_trial_sure_amt_txt.setText(("$" + format(crdm_sure_amt2).toString()).toString());
    crdm_pract2_trial_resp.keys = undefined;
    crdm_pract2_trial_resp.rt = undefined;
    _crdm_pract2_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_pract2_trialComponents = [];
    crdm_pract2_trialComponents.push(crdm_pract2_trial_img);
    crdm_pract2_trialComponents.push(crdm_pract2_trial_lott_top_txt);
    crdm_pract2_trialComponents.push(crdm_pract2_trial_lott_bot_txt);
    crdm_pract2_trialComponents.push(crdm_pract2_trial_sure_amt_txt);
    crdm_pract2_trialComponents.push(GRFX_fix2);
    crdm_pract2_trialComponents.push(crdm_pract2_trial_cue);
    crdm_pract2_trialComponents.push(crdm_pract2_trial_resp);
    
    for (const thisComponent of crdm_pract2_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract2_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract2_trial' ---
    // get current time
    t = crdm_pract2_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract2_trial_img* updates
    if (t >= 0.0 && crdm_pract2_trial_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_img.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_img.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_trial_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_img.setAutoDraw(false);
    }
    
    // *crdm_pract2_trial_lott_top_txt* updates
    if (t >= 0.0 && crdm_pract2_trial_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_trial_lott_top_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_lott_top_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_lott_top_txt.setAutoDraw(false);
    }
    
    // *crdm_pract2_trial_lott_bot_txt* updates
    if (t >= 0.0 && crdm_pract2_trial_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_trial_lott_bot_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_lott_bot_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_lott_bot_txt.setAutoDraw(false);
    }
    
    // *crdm_pract2_trial_sure_amt_txt* updates
    if (t >= 0.0 && crdm_pract2_trial_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_trial_sure_amt_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_sure_amt_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_sure_amt_txt.setAutoDraw(false);
    }
    
    // *GRFX_fix2* updates
    if (t >= 3 && GRFX_fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix2.tStart = t;  // (not accounting for frame time here)
      GRFX_fix2.frameNStart = frameN;  // exact frame index
      
      GRFX_fix2.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix2.setAutoDraw(false);
    }
    
    // *crdm_pract2_trial_cue* updates
    if (t >= 3 && crdm_pract2_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_pract2_trial_resp* updates
    if (t >= 3 && crdm_pract2_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract2_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_pract2_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract2_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_pract2_trial_resp_allKeys = _crdm_pract2_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_pract2_trial_resp_allKeys.length > 0) {
        crdm_pract2_trial_resp.keys = _crdm_pract2_trial_resp_allKeys[0].name;  // just the first key pressed
        crdm_pract2_trial_resp.rt = _crdm_pract2_trial_resp_allKeys[0].rt;
        crdm_pract2_trial_resp.duration = _crdm_pract2_trial_resp_allKeys[0].duration;
        // was this correct?
        if (crdm_pract2_trial_resp.keys == crdm_sure_resp2) {
            crdm_pract2_trial_resp.corr = 1;
        } else {
            crdm_pract2_trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract2_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var crdm_pract2_key;
var crdm_pract2_sure_key;
function crdm_pract2_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract2_trial' ---
    for (const thisComponent of crdm_pract2_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract2_trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from crdm_pract2_trial_code
    crdm_pract2_key = crdm_pract2_trial_resp.keys;
    crdm_pract2_sure_key = crdm_pract2_trial_resp.corr;
    my_loop.addData("crdm_trial_type", "practice2");
    
    // was no response the correct answer?!
    if (crdm_pract2_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(crdm_sure_resp2)) {
         crdm_pract2_trial_resp.corr = 1;  // correct non-response
      } else {
         crdm_pract2_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_pract2_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_pract2_trial_resp.keys', crdm_pract2_trial_resp.keys);
    psychoJS.experiment.addData('crdm_pract2_trial_resp.corr', crdm_pract2_trial_resp.corr);
    if (typeof crdm_pract2_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_pract2_trial_resp.rt', crdm_pract2_trial_resp.rt);
        psychoJS.experiment.addData('crdm_pract2_trial_resp.duration', crdm_pract2_trial_resp.duration);
        routineTimer.reset();
        }
    
    crdm_pract2_trial_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_msg2;
var crdm_pract2_feedbackComponents;
function crdm_pract2_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract2_feedback' ---
    t = 0;
    crdm_pract2_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract2_feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract2_feedback_code
    if ((crdm_pract2_key === undefined)) {
        crdm_msg2 = "NO RESPONSE";
    } else {
        if (crdm_pract2_sure_key) {
            crdm_msg2 = ("CERTAIN $" + format(crdm_sure_amt2.toString()));
        } else {
            crdm_msg2 = "LOTTERY";
        }
    }
    
    crdm_pract2_feedback_txt.setText(crdm_msg2);
    // keep track of which components have finished
    crdm_pract2_feedbackComponents = [];
    crdm_pract2_feedbackComponents.push(crdm_pract2_feedback_txt);
    
    for (const thisComponent of crdm_pract2_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract2_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract2_feedback' ---
    // get current time
    t = crdm_pract2_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract2_feedback_txt* updates
    if (t >= 0.0 && crdm_pract2_feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_feedback_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_feedback_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_feedback_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_feedback_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract2_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract2_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract2_feedback' ---
    for (const thisComponent of crdm_pract2_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract2_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var conf1_color;
var conf2_color;
var conf3_color;
var conf4_color;
var _crdm_pract2_conf_resp_allKeys;
var crdm_pract2_confComponents;
function crdm_pract2_confRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract2_conf' ---
    t = 0;
    crdm_pract2_confClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract2_conf.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract2_conf_code
    if ((crdm_pract2_key === undefined))  {
        continueRoutine = false;
    }
    conf1_color = [0, 0, 0];
    conf2_color = [0, 0, 0];
    conf3_color = [0, 0, 0];
    conf4_color = [0, 0, 0];
    
    crdm_pract2_conf_resp.keys = undefined;
    crdm_pract2_conf_resp.rt = undefined;
    _crdm_pract2_conf_resp_allKeys = [];
    // keep track of which components have finished
    crdm_pract2_confComponents = [];
    crdm_pract2_confComponents.push(crdm_pract2_conf_txt);
    crdm_pract2_confComponents.push(crdm_pract2_conf1);
    crdm_pract2_confComponents.push(crdm_pract2_conf1_txt);
    crdm_pract2_confComponents.push(crdm_pract2_conf2);
    crdm_pract2_confComponents.push(crdm_pract2_conf2_txt);
    crdm_pract2_confComponents.push(crdm_pract2_conf3);
    crdm_pract2_confComponents.push(crdm_pract2_conf3_txt);
    crdm_pract2_confComponents.push(crdm_pract2_conf4);
    crdm_pract2_confComponents.push(crdm_pract2_conf4_txt);
    crdm_pract2_confComponents.push(crdm_pract2_conf_resp);
    
    for (const thisComponent of crdm_pract2_confComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract_conf_key;
function crdm_pract2_confRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract2_conf' ---
    // get current time
    t = crdm_pract2_confClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from crdm_pract2_conf_code
    crdm_pract_conf_key = crdm_pract2_conf_resp.keys;
    if (!(crdm_pract_conf_key == undefined) && (crdm_pract_conf_key.length === 1)) {
        if ((crdm_pract_conf_key === "1")) {
            conf1_color = "darkgray";
            conf2_color = [0, 0, 0];
            conf3_color = [0, 0, 0];
            conf4_color = [0, 0, 0];
        } else {
            if ((crdm_pract_conf_key === "2")) {
                conf1_color = [0, 0, 0];
                conf2_color = "darkgray";
                conf3_color = [0, 0, 0];
                conf4_color = [0, 0, 0];
            } else {
                if ((crdm_pract_conf_key === "3")) {
                    conf1_color = [0, 0, 0];
                    conf2_color = [0, 0, 0];
                    conf3_color = "darkgray";
                    conf4_color = [0, 0, 0];
                } else {
                    if ((crdm_pract_conf_key === "4")) {
                        conf1_color = [0, 0, 0];
                        conf2_color = [0, 0, 0];
                        conf3_color = [0, 0, 0];
                        conf4_color = "darkgray";
                    }
                }
            }
        }
    }
    
    
    // *crdm_pract2_conf_txt* updates
    if (t >= 0.0 && crdm_pract2_conf_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf_txt.setAutoDraw(false);
    }
    
    if (crdm_pract2_conf1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract2_conf1.setFillColor(new util.Color(conf1_color), false);
    }
    
    // *crdm_pract2_conf1* updates
    if (t >= 0.0 && crdm_pract2_conf1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf1.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf1.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf1.setAutoDraw(false);
    }
    
    // *crdm_pract2_conf1_txt* updates
    if (t >= 0.0 && crdm_pract2_conf1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf1_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf1_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf1_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf1_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf1_txt.setAutoDraw(false);
    }
    
    if (crdm_pract2_conf2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract2_conf2.setFillColor(new util.Color(conf2_color), false);
    }
    
    // *crdm_pract2_conf2* updates
    if (t >= 0.0 && crdm_pract2_conf2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf2.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf2.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf2.setAutoDraw(false);
    }
    
    // *crdm_pract2_conf2_txt* updates
    if (t >= 0.0 && crdm_pract2_conf2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf2_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf2_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf2_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf2_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf2_txt.setAutoDraw(false);
    }
    
    if (crdm_pract2_conf3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract2_conf3.setFillColor(new util.Color(conf3_color), false);
    }
    
    // *crdm_pract2_conf3* updates
    if (t >= 0.0 && crdm_pract2_conf3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf3.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf3.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf3.setAutoDraw(false);
    }
    
    // *crdm_pract2_conf3_txt* updates
    if (t >= 0.0 && crdm_pract2_conf3_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf3_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf3_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf3_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf3_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf3_txt.setAutoDraw(false);
    }
    
    if (crdm_pract2_conf4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract2_conf4.setFillColor(new util.Color(conf4_color), false);
    }
    
    // *crdm_pract2_conf4* updates
    if (t >= 0.0 && crdm_pract2_conf4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf4.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf4.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf4.setAutoDraw(false);
    }
    
    // *crdm_pract2_conf4_txt* updates
    if (t >= 0.0 && crdm_pract2_conf4_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf4_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf4_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_conf4_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf4_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf4_txt.setAutoDraw(false);
    }
    
    // *crdm_pract2_conf_resp* updates
    if (t >= 0.0 && crdm_pract2_conf_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_conf_resp.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_conf_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract2_conf_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_conf_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract2_conf_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_conf_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_conf_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_pract2_conf_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract2_conf_resp.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _crdm_pract2_conf_resp_allKeys = _crdm_pract2_conf_resp_allKeys.concat(theseKeys);
      if (_crdm_pract2_conf_resp_allKeys.length > 0) {
        crdm_pract2_conf_resp.keys = _crdm_pract2_conf_resp_allKeys[_crdm_pract2_conf_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract2_conf_resp.rt = _crdm_pract2_conf_resp_allKeys[_crdm_pract2_conf_resp_allKeys.length - 1].rt;
        crdm_pract2_conf_resp.duration = _crdm_pract2_conf_resp_allKeys[_crdm_pract2_conf_resp_allKeys.length - 1].duration;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract2_confComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract2_confRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract2_conf' ---
    for (const thisComponent of crdm_pract2_confComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract2_conf.stopped', globalClock.getTime());
    conf1_color = [0, 0, 0];
    conf2_color = [0, 0, 0];
    conf3_color = [0, 0, 0];
    conf4_color = [0, 0, 0];
    
    crdm_conf1.setFillColor(new util.Color(conf1_color), false);
    crdm_conf2.setFillColor(new util.Color(conf2_color), false);
    crdm_conf3.setFillColor(new util.Color(conf3_color), false);
    crdm_conf4.setFillColor(new util.Color(conf4_color), false);
    
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_pract2_conf_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_pract2_conf_resp.keys', crdm_pract2_conf_resp.keys);
    if (typeof crdm_pract2_conf_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_pract2_conf_resp.rt', crdm_pract2_conf_resp.rt);
        psychoJS.experiment.addData('crdm_pract2_conf_resp.duration', crdm_pract2_conf_resp.duration);
        }
    
    crdm_pract2_conf_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract2_itiComponents;
function crdm_pract2_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract2_iti' ---
    t = 0;
    crdm_pract2_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_pract2_iti.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_pract2_iti_code
    if (!(crdm_pract2_trials.thisTrialN == undefined) && (crdm_pract2_trials.thisTrialN === 5)) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    crdm_pract2_itiComponents = [];
    crdm_pract2_itiComponents.push(crdm_pract2_iti_poly);
    
    for (const thisComponent of crdm_pract2_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract2_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract2_iti' ---
    // get current time
    t = crdm_pract2_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract2_iti_poly* updates
    if (t >= 0.0 && crdm_pract2_iti_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract2_iti_poly.tStart = t;  // (not accounting for frame time here)
      crdm_pract2_iti_poly.frameNStart = frameN;  // exact frame index
      
      crdm_pract2_iti_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract2_iti_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract2_iti_poly.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_pract2_itiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_pract2_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract2_iti' ---
    for (const thisComponent of crdm_pract2_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_pract2_iti.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_task_resps;
var crdm_conf_resps;
var crdm_catch_trials;
var crdm_iti_list;
var crdm_s;
var _crdm_trial_instr_resp_allKeys;
var crdm_trial_instrComponents;
function crdm_trial_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_trial_instr' ---
    t = 0;
    crdm_trial_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_trial_instr.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_trial_instr_code
    crdm_task_resps = [];
    crdm_conf_resps = [];
    crdm_catch_trials = [];
    crdm_iti_list = function () {
        var _pj_a = [], _pj_b = util.range(144);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(random.random());
        }
        return _pj_a;
    }
    .call(this);
    crdm_s = util.sum(crdm_iti_list);
    crdm_iti_list = function () {
        var _pj_a = [], _pj_b = crdm_iti_list;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(((i * 144) / crdm_s));
        }
        return _pj_a;
    }
    .call(this);
    
    crdm_trial_instr_resp.keys = undefined;
    crdm_trial_instr_resp.rt = undefined;
    _crdm_trial_instr_resp_allKeys = [];
    // keep track of which components have finished
    crdm_trial_instrComponents = [];
    crdm_trial_instrComponents.push(crdm_trial_instr_title_txt);
    crdm_trial_instrComponents.push(crdm_trial_instr_txt);
    crdm_trial_instrComponents.push(crdm_trial_instr_space_txt);
    crdm_trial_instrComponents.push(crdm_trial_instr_resp);
    
    for (const thisComponent of crdm_trial_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_trial_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_trial_instr' ---
    // get current time
    t = crdm_trial_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_trial_instr_title_txt* updates
    if (t >= 0.0 && crdm_trial_instr_title_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_instr_title_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_instr_title_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_instr_title_txt.setAutoDraw(true);
    }
    
    
    // *crdm_trial_instr_txt* updates
    if (t >= 0.0 && crdm_trial_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_instr_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_instr_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_instr_txt.setAutoDraw(true);
    }
    
    
    // *crdm_trial_instr_space_txt* updates
    if (t >= 0.0 && crdm_trial_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_trial_instr_resp* updates
    if (t >= 0.0 && crdm_trial_instr_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_instr_resp.tStart = t;  // (not accounting for frame time here)
      crdm_trial_instr_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_trial_instr_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_instr_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_instr_resp.clearEvents(); });
    }
    
    if (crdm_trial_instr_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_trial_instr_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_trial_instr_resp_allKeys = _crdm_trial_instr_resp_allKeys.concat(theseKeys);
      if (_crdm_trial_instr_resp_allKeys.length > 0) {
        crdm_trial_instr_resp.keys = _crdm_trial_instr_resp_allKeys[_crdm_trial_instr_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_trial_instr_resp.rt = _crdm_trial_instr_resp_allKeys[_crdm_trial_instr_resp_allKeys.length - 1].rt;
        crdm_trial_instr_resp.duration = _crdm_trial_instr_resp_allKeys[_crdm_trial_instr_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_trial_instrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_trial_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_trial_instr' ---
    for (const thisComponent of crdm_trial_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_trial_instr.stopped', globalClock.getTime());
    crdm_trial_instr_resp.stop();
    // the Routine "crdm_trial_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_init_fixComponents;
function crdm_init_fixRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_init_fix' ---
    t = 0;
    crdm_init_fixClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_init_fix.started', globalClock.getTime());
    // keep track of which components have finished
    crdm_init_fixComponents = [];
    crdm_init_fixComponents.push(crdm_init_fix_poly);
    
    for (const thisComponent of crdm_init_fixComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_init_fixRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_init_fix' ---
    // get current time
    t = crdm_init_fixClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_init_fix_poly* updates
    if (t >= 0.0 && crdm_init_fix_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_init_fix_poly.tStart = t;  // (not accounting for frame time here)
      crdm_init_fix_poly.frameNStart = frameN;  // exact frame index
      
      crdm_init_fix_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_init_fix_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_init_fix_poly.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_init_fixComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_init_fixRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_init_fix' ---
    for (const thisComponent of crdm_init_fixComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_init_fix.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_stop_timer;
var crdm_stopped_time;
var crdm_lott_outcome;
var crdm_conf_key;
var crdm_idx;
var crdm_sure_amt;
var crdm_sure_p;
var crdm_lott_p;
var crdm_amb_lev;
var crdm_domain;
var crdm_lott_top;
var crdm_lott_bot;
var crdm_img;
var _crdm_trial_resp_allKeys;
var crdm_trialComponents;
function crdm_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_trial' ---
    t = 0;
    crdm_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_trial.started', globalClock.getTime());
    my_loop = eval(crdm_loop_name);
    crdm_stop_timer = null;
    crdm_stopped_time = 0;
    crdm_lott_outcome = 0;
    crdm_conf_key = [];
    crdm_idx = random.randint(0, 1);
    crdm_sure_pos = crdm_pos[crdm_idx];
    crdm_sure_resp = crdm_resp[crdm_idx];
    
    
    //crdm_trials_dict = {"crdm_safe_sv":[], "crdm_lott_sv":[], "crdm_lott":[], "crdm_sure_amt":[], //#dict for trial variables
    //                    "crdm_lott_p":[], "crdm_amb_lev":[], "crdm_delta_sv":[], "crdm_domain":[]};
    //assign QuestPlus generated variables for trial presentation
    crdm_sure_amt = crdm_trials_dict["crdm_sure_amt"][crdm_trial_idx];
    crdm_sure_p = 100;
    crdm_lott_p = crdm_trials_dict["crdm_lott_p"][crdm_trial_idx];
    crdm_amb_lev = crdm_trials_dict["crdm_amb_lev"][crdm_trial_idx];
    crdm_domain = crdm_trials_dict["crdm_domain"][crdm_trial_idx];
    crdm_lott_top = "";
    crdm_lott_bot = "";
    crdm_img = "";
    
    if (crdm_nonzero_side == "top") {
        crdm_lott_top = crdm_trials_dict["crdm_lott"][crdm_trial_idx];
        crdm_lott_bot = 0;
        if (crdm_trials_dict["crdm_amb_lev"][crdm_trial_idx] != 0) { //check if ambiguity trial
            crdm_img = "ambig_" + parseInt(crdm_trials_dict["crdm_amb_lev"][crdm_trial_idx] * 100) + ".bmp";
        } else { 
            crdm_img = "risk_red_" + parseInt(crdm_trials_dict["crdm_lott_p"][crdm_trial_idx] * 100) + ".bmp";
        }
    } else {
        crdm_lott_top = 0 
        crdm_lott_bot = crdm_trials_dict["crdm_lott"][crdm_trial_idx];
        if (crdm_trials_dict["crdm_amb_lev"][crdm_trial_idx] != 0) { //check if ambiguity trial
            crdm_img = "ambig_" + parseInt(crdm_trials_dict["crdm_amb_lev"][crdm_trial_idx] * 100) + ".bmp";
        } else { 
            crdm_img = "risk_blue_" + parseInt(crdm_trials_dict["crdm_lott_p"][crdm_trial_idx] * 100) + ".bmp";
        }
    }
    
    //save QuestPlus generated variables to output csv
    my_loop.addData("crdm_sure_amt", crdm_sure_amt);
    my_loop.addData("crdm_lott_top", crdm_lott_top);
    my_loop.addData("crdm_lott_bot", crdm_lott_bot);
    my_loop.addData("crdm_sure_p", crdm_sure_p);
    my_loop.addData("crdm_lott_p", crdm_lott_p);
    my_loop.addData("crdm_amb_lev", crdm_amb_lev);
    my_loop.addData("crdm_domain", crdm_domain);
    my_loop.addData("crdm_img", crdm_img);
    crdm_trial_img.setImage(("images/" + crdm_img));
    crdm_trial_lott_top.setText(("$" + format(crdm_lott_top).toString()).toString());
    crdm_trial_lott_bot.setText(("$" + format(crdm_lott_bot).toString()).toString());
    crdm_trial_sure_amt.setPos(crdm_sure_pos);
    crdm_trial_sure_amt.setText(("$" + format(crdm_sure_amt).toString()).toString());
    crdm_trial_resp.keys = undefined;
    crdm_trial_resp.rt = undefined;
    _crdm_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_trialComponents = [];
    crdm_trialComponents.push(crdm_trial_img);
    crdm_trialComponents.push(crdm_trial_lott_top);
    crdm_trialComponents.push(crdm_trial_lott_bot);
    crdm_trialComponents.push(crdm_trial_sure_amt);
    crdm_trialComponents.push(GRFX_fix);
    crdm_trialComponents.push(crdm_trial_cue);
    crdm_trialComponents.push(crdm_trial_resp);
    
    for (const thisComponent of crdm_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_trial' ---
    // get current time
    t = crdm_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from crdm_trial_JS
    if (!(crdm_trial_resp.keys == undefined) && (crdm_trial_resp.keys.length === 1)) {
        if ((crdm_stop_timer === null)) {
            crdm_stop_timer = new util.Clock();
        } else {
            if ((crdm_stop_timer.getTime() >= 0.5)) {
                continueRoutine = false;
            }
        }
    }
    
    // *crdm_trial_img* updates
    if (t >= 0.0 && crdm_trial_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_img.tStart = t;  // (not accounting for frame time here)
      crdm_trial_img.frameNStart = frameN;  // exact frame index
      
      crdm_trial_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_img.setAutoDraw(false);
    }
    
    // *crdm_trial_lott_top* updates
    if (t >= 0.0 && crdm_trial_lott_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_lott_top.tStart = t;  // (not accounting for frame time here)
      crdm_trial_lott_top.frameNStart = frameN;  // exact frame index
      
      crdm_trial_lott_top.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_lott_top.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_lott_top.setAutoDraw(false);
    }
    
    // *crdm_trial_lott_bot* updates
    if (t >= 0.0 && crdm_trial_lott_bot.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_lott_bot.tStart = t;  // (not accounting for frame time here)
      crdm_trial_lott_bot.frameNStart = frameN;  // exact frame index
      
      crdm_trial_lott_bot.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_lott_bot.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_lott_bot.setAutoDraw(false);
    }
    
    // *crdm_trial_sure_amt* updates
    if (t >= 0.0 && crdm_trial_sure_amt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_sure_amt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_sure_amt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_sure_amt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_sure_amt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_sure_amt.setAutoDraw(false);
    }
    
    // *GRFX_fix* updates
    if (t >= 3 && GRFX_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix.tStart = t;  // (not accounting for frame time here)
      GRFX_fix.frameNStart = frameN;  // exact frame index
      
      GRFX_fix.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix.setAutoDraw(false);
    }
    
    // *crdm_trial_cue* updates
    if (t >= 3 && crdm_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_trial_resp* updates
    if (t >= 3 && crdm_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_trial_resp_allKeys = _crdm_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_trial_resp_allKeys.length > 0) {
        crdm_trial_resp.keys = _crdm_trial_resp_allKeys[0].name;  // just the first key pressed
        crdm_trial_resp.rt = _crdm_trial_resp_allKeys[0].rt;
        crdm_trial_resp.duration = _crdm_trial_resp_allKeys[0].duration;
        // was this correct?
        if (crdm_trial_resp.keys == crdm_sure_resp) {
            crdm_trial_resp.corr = 1;
        } else {
            crdm_trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var crdm_key;
var crdm_sure_key;
var lott_outcome;
function crdm_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_trial' ---
    for (const thisComponent of crdm_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_trial.stopped', globalClock.getTime());
    crdm_key = crdm_trial_resp.keys;
    crdm_sure_key = crdm_trial_resp.corr;
    my_loop.addData("crdm_trial_type", "task");
    lott_outcome = 0;
    if ((((crdm_trial_resp.rt) === undefined) || (crdm_trial_resp.rt >= (2 - 0.5)))) {
        crdm_delta_time = 0;
    } else {
        crdm_delta_time = Math.max(0, (2 - (crdm_trial_resp.rt + crdm_stopped_time)));
    }
    if (!(crdm_key === undefined) && (crdm_key.length === 1)) {
        if ((crdm_sure_key === 1)) {
            crdm_earnings.push(["sure", crdm_sure_amt, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, (- 1), crdm_nonzero_side, crdm_domain]);
            my_loop.addData("crdm_choice", 0);
            my_loop.addData("crdm_choice2", "sure");
            my_loop.addData("crdm_lott", "");
            my_loop.addData("crdm_lott2", "");
        } else {
            lott_outcome = random.choice([0, 1], [100 - Number.parseInt(crdm_lott_p), Number.parseInt(crdm_lott_p)]);
            my_loop.addData("crdm_choice", 1);
            my_loop.addData("crdm_choice2", "lott");
            my_loop.addData("crdm_lott", lott_outcome);
            if ((lott_outcome === 1)) {
                my_loop.addData("crdm_lott2", "win");
                if ((crdm_domain === "gain")) {
                    if ((Number.parseInt(crdm_lott_top) !== 0)) {
                        crdm_earnings.push(["lott", crdm_lott_top, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    } else {
                        crdm_earnings.push(["lott", crdm_lott_bot, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    }
                } else {
                    if ((crdm_domain === "loss")) {
                        if ((Number.parseInt(crdm_lott_top) === 0)) {
                            crdm_earnings.push(["lott", crdm_lott_top, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        } else {
                            crdm_earnings.push(["lott", crdm_lott_bot, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        }
                    }
                }
            } else {
                my_loop.addData("crdm_lott2", "lose");
                if ((crdm_domain === "gain")) {
                    if ((Number.parseInt(crdm_lott_top) === 0)) {
                        crdm_earnings.push(["lott", crdm_lott_top, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    } else {
                        crdm_earnings.push(["lott", crdm_lott_bot, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    }
                } else {
                    if ((crdm_domain === "loss")) {
                        if ((Number.parseInt(crdm_lott_top) < 0)) {
                            crdm_earnings.push(["lott", crdm_lott_top, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        } else {
                            crdm_earnings.push(["lott", crdm_lott_bot, crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        }
                    }
                }
            }
        }
    }
    // was no response the correct answer?!
    if (crdm_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(crdm_sure_resp)) {
         crdm_trial_resp.corr = 1;  // correct non-response
      } else {
         crdm_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_trial_resp.keys', crdm_trial_resp.keys);
    psychoJS.experiment.addData('crdm_trial_resp.corr', crdm_trial_resp.corr);
    if (typeof crdm_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_trial_resp.rt', crdm_trial_resp.rt);
        psychoJS.experiment.addData('crdm_trial_resp.duration', crdm_trial_resp.duration);
        routineTimer.reset();
        }
    
    crdm_trial_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_feedbackComponents;
function crdm_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_feedback' ---
    t = 0;
    crdm_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_feedback.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_feedback_code
    if ((crdm_key === undefined)) {
        crdm_msg = "NO RESPONSE";
    } else {
        if (crdm_sure_key) {
            crdm_msg = ("CERTAIN $" + format(crdm_sure_amt.toString()));
        } else {
            crdm_msg = "LOTTERY";
        }
    }
    
    crdm_feedback_txt.setText(crdm_msg);
    // keep track of which components have finished
    crdm_feedbackComponents = [];
    crdm_feedbackComponents.push(crdm_feedback_txt);
    
    for (const thisComponent of crdm_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_feedback' ---
    // get current time
    t = crdm_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_feedback_txt* updates
    if (t >= 0.0 && crdm_feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_feedback_txt.tStart = t;  // (not accounting for frame time here)
      crdm_feedback_txt.frameNStart = frameN;  // exact frame index
      
      crdm_feedback_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_feedback_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_feedback' ---
    for (const thisComponent of crdm_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_conf_resp_allKeys;
var crdm_confComponents;
function crdm_confRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_conf' ---
    t = 0;
    crdm_confClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_conf.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_conf_code
    if ((crdm_key === undefined)) {
        continueRoutine = false;
    }
    conf1_color = [0, 0, 0];
    conf2_color = [0, 0, 0];
    conf3_color = [0, 0, 0];
    conf4_color = [0, 0, 0];
    
    crdm_conf_resp.keys = undefined;
    crdm_conf_resp.rt = undefined;
    _crdm_conf_resp_allKeys = [];
    // keep track of which components have finished
    crdm_confComponents = [];
    crdm_confComponents.push(crdm_conf_txt);
    crdm_confComponents.push(crdm_conf1);
    crdm_confComponents.push(crdm_conf1_txt);
    crdm_confComponents.push(crdm_conf2);
    crdm_confComponents.push(crdm_conf2_txt);
    crdm_confComponents.push(crdm_conf3);
    crdm_confComponents.push(crdm_conf3_txt);
    crdm_confComponents.push(crdm_conf4);
    crdm_confComponents.push(crdm_conf4_txt);
    crdm_confComponents.push(crdm_conf_resp);
    
    for (const thisComponent of crdm_confComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_confRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_conf' ---
    // get current time
    t = crdm_confClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from crdm_conf_code
    crdm_conf_key = crdm_conf_resp.keys;
    if (!(crdm_conf_key == undefined) && (crdm_conf_key.length === 1)) {
        if ((crdm_conf_key === "1")) {
            conf1_color = "darkgray";
            conf2_color = [0, 0, 0];
            conf3_color = [0, 0, 0];
            conf4_color = [0, 0, 0];
        } else {
            if ((crdm_conf_key === "2")) {
                conf1_color = [0, 0, 0];
                conf2_color = "darkgray";
                conf3_color = [0, 0, 0];
                conf4_color = [0, 0, 0];
            } else {
                if ((crdm_conf_key === "3")) {
                    conf1_color = [0, 0, 0];
                    conf2_color = [0, 0, 0];
                    conf3_color = "darkgray";
                    conf4_color = [0, 0, 0];
                } else {
                    if ((crdm_conf_key === "4")) {
                        conf1_color = [0, 0, 0];
                        conf2_color = [0, 0, 0];
                        conf3_color = [0, 0, 0];
                        conf4_color = "darkgray";
                    }
                }
            }
        }
    }
    
    
    // *crdm_conf_txt* updates
    if (t >= 0.0 && crdm_conf_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf_txt.tStart = t;  // (not accounting for frame time here)
      crdm_conf_txt.frameNStart = frameN;  // exact frame index
      
      crdm_conf_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf_txt.setAutoDraw(false);
    }
    
    if (crdm_conf1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_conf1.setFillColor(new util.Color(conf1_color), false);
    }
    
    // *crdm_conf1* updates
    if (t >= 0.0 && crdm_conf1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf1.tStart = t;  // (not accounting for frame time here)
      crdm_conf1.frameNStart = frameN;  // exact frame index
      
      crdm_conf1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf1.setAutoDraw(false);
    }
    
    // *crdm_conf1_txt* updates
    if (t >= 0.0 && crdm_conf1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf1_txt.tStart = t;  // (not accounting for frame time here)
      crdm_conf1_txt.frameNStart = frameN;  // exact frame index
      
      crdm_conf1_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf1_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf1_txt.setAutoDraw(false);
    }
    
    if (crdm_conf2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_conf2.setFillColor(new util.Color(conf2_color), false);
    }
    
    // *crdm_conf2* updates
    if (t >= 0.0 && crdm_conf2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf2.tStart = t;  // (not accounting for frame time here)
      crdm_conf2.frameNStart = frameN;  // exact frame index
      
      crdm_conf2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf2.setAutoDraw(false);
    }
    
    // *crdm_conf2_txt* updates
    if (t >= 0.0 && crdm_conf2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf2_txt.tStart = t;  // (not accounting for frame time here)
      crdm_conf2_txt.frameNStart = frameN;  // exact frame index
      
      crdm_conf2_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf2_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf2_txt.setAutoDraw(false);
    }
    
    if (crdm_conf3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_conf3.setFillColor(new util.Color(conf3_color), false);
    }
    
    // *crdm_conf3* updates
    if (t >= 0.0 && crdm_conf3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf3.tStart = t;  // (not accounting for frame time here)
      crdm_conf3.frameNStart = frameN;  // exact frame index
      
      crdm_conf3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf3.setAutoDraw(false);
    }
    
    // *crdm_conf3_txt* updates
    if (t >= 0.0 && crdm_conf3_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf3_txt.tStart = t;  // (not accounting for frame time here)
      crdm_conf3_txt.frameNStart = frameN;  // exact frame index
      
      crdm_conf3_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf3_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf3_txt.setAutoDraw(false);
    }
    
    if (crdm_conf4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_conf4.setFillColor(new util.Color(conf4_color), false);
    }
    
    // *crdm_conf4* updates
    if (t >= 0.0 && crdm_conf4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf4.tStart = t;  // (not accounting for frame time here)
      crdm_conf4.frameNStart = frameN;  // exact frame index
      
      crdm_conf4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf4.setAutoDraw(false);
    }
    
    // *crdm_conf4_txt* updates
    if (t >= 0.0 && crdm_conf4_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf4_txt.tStart = t;  // (not accounting for frame time here)
      crdm_conf4_txt.frameNStart = frameN;  // exact frame index
      
      crdm_conf4_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf4_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf4_txt.setAutoDraw(false);
    }
    
    // *crdm_conf_resp* updates
    if (t >= 0.0 && crdm_conf_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_conf_resp.tStart = t;  // (not accounting for frame time here)
      crdm_conf_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_conf_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_conf_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_conf_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_conf_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_conf_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_conf_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_conf_resp.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _crdm_conf_resp_allKeys = _crdm_conf_resp_allKeys.concat(theseKeys);
      if (_crdm_conf_resp_allKeys.length > 0) {
        crdm_conf_resp.keys = _crdm_conf_resp_allKeys[_crdm_conf_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_conf_resp.rt = _crdm_conf_resp_allKeys[_crdm_conf_resp_allKeys.length - 1].rt;
        crdm_conf_resp.duration = _crdm_conf_resp_allKeys[_crdm_conf_resp_allKeys.length - 1].duration;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_confComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_confRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_conf' ---
    for (const thisComponent of crdm_confComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_conf.stopped', globalClock.getTime());
    // Run 'End Routine' code from crdm_conf_code
    my_loop.addData("crdm_conf", crdm_conf_key);
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_conf_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_conf_resp.keys', crdm_conf_resp.keys);
    if (typeof crdm_conf_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_conf_resp.rt', crdm_conf_resp.rt);
        psychoJS.experiment.addData('crdm_conf_resp.duration', crdm_conf_resp.duration);
        }
    
    crdm_conf_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_iti_time;
var crdm_trials_itiComponents;
function crdm_trials_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_trials_iti' ---
    t = 0;
    crdm_trials_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_trials_iti.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_trials_iti_code
    crdm_iti_time = (crdm_iti_list[my_loop.thisIndex] + crdm_delta_time);
    if (!(crdm_trials.thisTrialN == undefined) && (crdm_trials.thisTrialN === 143)) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    crdm_trials_itiComponents = [];
    crdm_trials_itiComponents.push(crdm_trials_iti_poly);
    
    for (const thisComponent of crdm_trials_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_trials_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_trials_iti' ---
    // get current time
    t = crdm_trials_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_trials_iti_poly* updates
    if (t >= 0.0 && crdm_trials_iti_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trials_iti_poly.tStart = t;  // (not accounting for frame time here)
      crdm_trials_iti_poly.frameNStart = frameN;  // exact frame index
      
      crdm_trials_iti_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + crdm_iti_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trials_iti_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trials_iti_poly.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_trials_itiComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_trials_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_trials_iti' ---
    for (const thisComponent of crdm_trials_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_trials_iti.stopped', globalClock.getTime());
    // Run 'End Routine' code from crdm_trials_iti_code
    my_loop.addData("crdm_delta_time", crdm_delta_time);
    my_loop.addData("crdm_iti_time", crdm_iti_time);
    
    // the Routine "crdm_trials_iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_end_resp_allKeys;
var crdm_endComponents;
function crdm_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_end' ---
    t = 0;
    crdm_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_end.started', globalClock.getTime());
    crdm_end_resp.keys = undefined;
    crdm_end_resp.rt = undefined;
    _crdm_end_resp_allKeys = [];
    // keep track of which components have finished
    crdm_endComponents = [];
    crdm_endComponents.push(crdm_end_title_txt);
    crdm_endComponents.push(crdm_end_txt_OFF);
    crdm_endComponents.push(crdm_end_space_OFF);
    crdm_endComponents.push(crdm_end_resp);
    
    for (const thisComponent of crdm_endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_end' ---
    // get current time
    t = crdm_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_end_title_txt* updates
    if (t >= 0.0 && crdm_end_title_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_end_title_txt.tStart = t;  // (not accounting for frame time here)
      crdm_end_title_txt.frameNStart = frameN;  // exact frame index
      
      crdm_end_title_txt.setAutoDraw(true);
    }
    
    
    // *crdm_end_txt_OFF* updates
    if (t >= 0.0 && crdm_end_txt_OFF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_end_txt_OFF.tStart = t;  // (not accounting for frame time here)
      crdm_end_txt_OFF.frameNStart = frameN;  // exact frame index
      
      crdm_end_txt_OFF.setAutoDraw(true);
    }
    
    
    // *crdm_end_space_OFF* updates
    if (t >= 0.0 && crdm_end_space_OFF.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_end_space_OFF.tStart = t;  // (not accounting for frame time here)
      crdm_end_space_OFF.frameNStart = frameN;  // exact frame index
      
      crdm_end_space_OFF.setAutoDraw(true);
    }
    
    
    // *crdm_end_resp* updates
    if (t >= 0.0 && crdm_end_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_end_resp.tStart = t;  // (not accounting for frame time here)
      crdm_end_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_end_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_end_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_end_resp.clearEvents(); });
    }
    
    if (crdm_end_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_end_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_end_resp_allKeys = _crdm_end_resp_allKeys.concat(theseKeys);
      if (_crdm_end_resp_allKeys.length > 0) {
        crdm_end_resp.keys = _crdm_end_resp_allKeys[_crdm_end_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_end_resp.rt = _crdm_end_resp_allKeys[_crdm_end_resp_allKeys.length - 1].rt;
        crdm_end_resp.duration = _crdm_end_resp_allKeys[_crdm_end_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_end' ---
    for (const thisComponent of crdm_endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_end.stopped', globalClock.getTime());
    crdm_end_resp.stop();
    // the Routine "crdm_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var exp;
var choice;
var money;
var trial_img;
var top;
var bottom;
var outcome;
var nonzero_side;
var domain;
var sure_amt;
var earnings_text;
var choice_text;
var outcome_color;
var chip_color;
var chip_text;
var choice_outcome;
var money_outcome;
var idx;
var red_nonzero;
var _crdm_bonus_resp_allKeys;
var crdm_bonusComponents;
function crdm_bonusRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_bonus' ---
    t = 0;
    crdm_bonusClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('crdm_bonus.started', globalClock.getTime());
    // Run 'Begin Routine' code from crdm_bonus_code
    exp = [];
    choice = [];
    money = [];
    trial_img = [];
    top = [];
    bottom = [];
    outcome = [];
    nonzero_side = [];
    domain = [];
    sure_amt = "";
    earnings_text = "";
    choice_text = "";
    outcome_color = [0, 0, 0];
    chip_color = [0, 0, 0];
    chip_text = "";
    choice_outcome = "";
    money_outcome = "";
    idx = Number.parseInt((random.random() * crdm_earnings.length));
    [choice, money, sure_amt, trial_img, top, bottom, outcome, nonzero_side, domain] = crdm_earnings[idx];
    money = format(money);
    my_loop.addData("crdm_bonus_choice", choice);
    my_loop.addData("crdm_bonus_amt", money);
    red_nonzero = false;
    if ((nonzero_side === "top")) {
        red_nonzero = true;
    }
    if ((choice === "sure")) {
        choice_text = "*CERTAIN*";
        outcome_color = [0.7098, 0.2941, (- 0.749)];
        chip_color = [0, 0, 0];
        chip_text = "";
        choice_outcome = ("$" + money.toString());
        money_outcome = "";
    } else {
        choice_text = "*PLAY THE LOTTERY*";
        if ((red_nonzero === true)) {
            if (((outcome === 1) && (domain === "gain"))) {
                outcome_color = [0.9608, 0.0039, (- 0.1059)];
                chip_color = [0.9608, 0.0039, (- 0.1059)];
                choice_outcome = "A red chip";
                chip_text = "was drawn and the outcome was";
                money_outcome = ("$" + money.toString());
            } else {
                if (((outcome === 1) && (domain === "loss"))) {
                    outcome_color = [(- 0.2157), 0.1686, 0.8588];
                    chip_color = [(- 0.2157), 0.1686, 0.8588];
                    choice_outcome = "A blue chip";
                    chip_text = "was drawn and the outcome was";
                    money_outcome = ("$" + money.toString());
                } else {
                    if (((outcome === 0) && (domain === "gain"))) {
                        outcome_color = [(- 0.2157), 0.1686, 0.8588];
                        chip_color = [(- 0.2157), 0.1686, 0.8588];
                        choice_outcome = "A blue chip";
                        chip_text = "was drawn and the outcome was";
                        money_outcome = ("$" + money.toString());
                    } else {
                        if (((outcome === 0) && (domain === "loss"))) {
                            outcome_color = [0.9608, 0.0039, (- 0.1059)];
                            chip_color = [0.9608, 0.0039, (- 0.1059)];
                            choice_outcome = "A red chip";
                            chip_text = "was drawn and the outcome was";
                            money_outcome = ("$" + money.toString());
                        }
                    }
                }
            }
        } else {
            if (((outcome === 1) && (domain === "gain"))) {
                outcome_color = [(- 0.2157), 0.1686, 0.8588];
                chip_color = [(- 0.2157), 0.1686, 0.8588];
                choice_outcome = "A blue chip";
                chip_text = "was drawn and the outcome was";
                money_outcome = ("$" + money.toString());
            } else {
                if (((outcome === 1) && (domain === "loss"))) {
                    outcome_color = [0.9608, 0.0039, (- 0.1059)];
                    chip_color = [0.9608, 0.0039, (- 0.1059)];
                    choice_outcome = "A red chip";
                    chip_text = "was drawn and the outcome was";
                    money_outcome = ("$" + money.toString());
                } else {
                    if (((outcome === 0) && (domain === "gain"))) {
                        outcome_color = [0.9608, 0.0039, (- 0.1059)];
                        chip_color = [0.9608, 0.0039, (- 0.1059)];
                        choice_outcome = "A red chip";
                        chip_text = "was drawn and the outcome was";
                        money_outcome = ("$" + money.toString());
                    } else {
                        if (((outcome === 0) && (domain === "loss"))) {
                            outcome_color = [(- 0.2157), 0.1686, 0.8588];
                            chip_color = [(- 0.2157), 0.1686, 0.8588];
                            choice_outcome = "A blue chip";
                            chip_text = "was drawn and the outcome was";
                            money_outcome = ("$" + money.toString());
                        }
                    }
                }
            }
        }
    }
    
    crdm_bonus_lott_top.setText(("$" + format(top).toString()).toString());
    crdm_bonus_img.setImage(("images/" + trial_img));
    crdm_bonus_lott_bot.setText(("$" + format(bottom).toString()).toString());
    crdm_bonus_sure_amt_txt.setText(("$" + format(sure_amt).toString()).toString());
    crdm_bonus_choice_text_txt.setText(choice_text);
    crdm_bonus_choice_outcome_txt.setColor(new util.Color(outcome_color));
    crdm_bonus_choice_outcome_txt.setText(choice_outcome);
    crdm_bonus_drawn_txt.setText(chip_text);
    crdm_bonus_chip_poly.setFillColor(new util.Color(chip_color));
    crdm_bonus_chip_poly.setLineColor(new util.Color(chip_color));
    crdm_bonus_winnings_txt.setText(money_outcome);
    crdm_bonus_resp.keys = undefined;
    crdm_bonus_resp.rt = undefined;
    _crdm_bonus_resp_allKeys = [];
    // keep track of which components have finished
    crdm_bonusComponents = [];
    crdm_bonusComponents.push(crdm_bonus_thanks_txt);
    crdm_bonusComponents.push(crdm_bonus_lott_top);
    crdm_bonusComponents.push(crdm_bonus_img);
    crdm_bonusComponents.push(crdm_bonus_lott_bot);
    crdm_bonusComponents.push(crdm_bonus_sure_amt_txt);
    crdm_bonusComponents.push(crdm_bonus_prompt_txt);
    crdm_bonusComponents.push(crdm_bonus_choice_text_txt);
    crdm_bonusComponents.push(crdm_bonus_choice_outcome_txt);
    crdm_bonusComponents.push(crdm_bonus_drawn_txt);
    crdm_bonusComponents.push(crdm_bonus_chip_poly);
    crdm_bonusComponents.push(crdm_bonus_winnings_txt);
    crdm_bonusComponents.push(crdm_bonus_space_txt);
    crdm_bonusComponents.push(crdm_bonus_resp);
    
    for (const thisComponent of crdm_bonusComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_bonusRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_bonus' ---
    // get current time
    t = crdm_bonusClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_bonus_thanks_txt* updates
    if (t >= 0.0 && crdm_bonus_thanks_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_thanks_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_thanks_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_thanks_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_lott_top* updates
    if (t >= 0.0 && crdm_bonus_lott_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_lott_top.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_lott_top.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_lott_top.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_img* updates
    if (t >= 0.0 && crdm_bonus_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_img.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_img.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_img.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_lott_bot* updates
    if (t >= 0.0 && crdm_bonus_lott_bot.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_lott_bot.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_lott_bot.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_lott_bot.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_sure_amt_txt* updates
    if (t >= 0.0 && crdm_bonus_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_sure_amt_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_prompt_txt* updates
    if (t >= 0.0 && crdm_bonus_prompt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_prompt_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_prompt_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_prompt_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_choice_text_txt* updates
    if (t >= 0.0 && crdm_bonus_choice_text_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_choice_text_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_choice_text_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_choice_text_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_choice_outcome_txt* updates
    if (t >= 0.0 && crdm_bonus_choice_outcome_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_choice_outcome_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_choice_outcome_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_choice_outcome_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_drawn_txt* updates
    if (t >= 0.0 && crdm_bonus_drawn_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_drawn_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_drawn_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_drawn_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_chip_poly* updates
    if (t >= 0.0 && crdm_bonus_chip_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_chip_poly.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_chip_poly.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_chip_poly.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_winnings_txt* updates
    if (t >= 0.0 && crdm_bonus_winnings_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_winnings_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_winnings_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_winnings_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_space_txt* updates
    if (t >= 0.0 && crdm_bonus_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_resp* updates
    if (t >= 0.0 && crdm_bonus_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_resp.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_bonus_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_bonus_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_bonus_resp.clearEvents(); });
    }
    
    if (crdm_bonus_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_bonus_resp.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_bonus_resp_allKeys = _crdm_bonus_resp_allKeys.concat(theseKeys);
      if (_crdm_bonus_resp_allKeys.length > 0) {
        crdm_bonus_resp.keys = _crdm_bonus_resp_allKeys[_crdm_bonus_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_bonus_resp.rt = _crdm_bonus_resp_allKeys[_crdm_bonus_resp_allKeys.length - 1].rt;
        crdm_bonus_resp.duration = _crdm_bonus_resp_allKeys[_crdm_bonus_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crdm_bonusComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crdm_bonusRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_bonus' ---
    for (const thisComponent of crdm_bonusComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crdm_bonus.stopped', globalClock.getTime());
    crdm_bonus_resp.stop();
    // the Routine "crdm_bonus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
