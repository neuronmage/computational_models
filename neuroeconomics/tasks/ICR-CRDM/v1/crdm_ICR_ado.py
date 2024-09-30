#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Sep  5 13:21:13 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from crdm_instr1_py
###code written by Mandy Renfro (2023)###
import random
import os
exp_proceed = True
earnings = []

import ricardo_gain as rg
import ricardo_loss as rl
#ADO Step 0
g_log_lik, g_ent, g_log_post, g_sets = rg.step0() #gains
l_log_lik, l_ent, l_log_post, l_sets = rl.step0() #losses

confkey_map = {"2": "1", "3": "2", "j": "3", "k": "4", None: None} #for Cedrus box code mapping


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'CRDM_ICR'  # from the Builder filename that created this script
expInfo = {
    'participant': 'NIH',
    'session': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s/session%s/%s_S%s_%s' % (expInfo['participant'], expInfo['session'], expInfo['participant'], expInfo['session'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/UCDN/code/CRDM_ICR/crdm_ICR_ado.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1728, 1117], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "crdm_instr1" ---
# Run 'Begin Experiment' code from crdm_instr1_py
import os
from datetime import datetime
subid = expInfo["participant"]
epoch = datetime.utcfromtimestamp(0)

if not os.path.exists("data/{0}".format(subid)): #does subject exist
    os.mkdir("data/{0}".format(subid))
if not os.path.exists("data/{0}/session{1}".format(subid, expInfo["session"])): #does session exist
    os.mkdir("data/{0}/session{1}".format(subid, expInfo["session"]))

if os.path.exists("data/{0}/session{1}/session.log".format(subid, expInfo["session"])):
    os.remove("data/{0}/session{1}/session.log".format(subid, expInfo["session"]))

def log_out(subid, *args):
    # "a" is append
    # "w" overwrites whatever previously existed
    with open("data/{0}/session{1}/session.log".format(subid, expInfo["session"]), "a") as f:
        for i in args:
            f.write(str(i)+ "\t")
        f.write("\n")

utc_start = int((datetime.utcnow() - epoch).total_seconds()*1000)
log_out(subid, utc_start, 0, "log starts", "Task", "Conf", "Domain", "Stim", "Lott_Top", "Lott_Bot", "Trialx")
crdm_instr1_title_txt = visual.TextStim(win=win, name='crdm_instr1_title_txt',
    text='* Risk & Ambiguity Task *',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_instr1_txt = visual.TextStim(win=win, name='crdm_instr1_txt',
    text='In this decision making task, you will be asked to make economic choices between: \n\n\n- Gaining/losing a certain amount \nOR\n- Playing a lottery for the chance to win a larger gain or smaller loss ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.25, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_instr1_space_txt = visual.TextStim(win=win, name='crdm_instr1_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr1_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr2" ---
crdm_instr2_lottname_txt = visual.TextStim(win=win, name='crdm_instr2_lottname_txt',
    text='*Playing the Lottery*',
    font='Arial',
    pos=(-0.2, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr2_txt = visual.TextStim(win=win, name='crdm_instr2_txt',
    text='The lottery consists of an imaginary bag containing 100 poker chips, some red and some blue. To play, you pull a random chip from the bag.  \n\nThe figure on the right represents the proportion of blue and red chips in the imaginary bag. \n\nIn this example, most chips are blue (75 of 100) and fewer are red (25 of 100).',
    font='Arial',
    pos=(-0.2, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_instr2_img = visual.ImageStim(
    win=win,
    name='crdm_instr2_img', units='height', 
    image='images/risk_blue_75.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0.6, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
crdm_instr2_lott0_txt = visual.TextStim(win=win, name='crdm_instr2_lott0_txt',
    text='$0',
    font='Arial',
    pos=(0.6, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr2_lott20_txt = visual.TextStim(win=win, name='crdm_instr2_lott20_txt',
    text='$20',
    font='Arial',
    pos=(0.6, -0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_instr2_space_txt = visual.TextStim(win=win, name='crdm_instr2_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_instr2_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr3" ---
crdm_instr3_lottname_txt = visual.TextStim(win=win, name='crdm_instr3_lottname_txt',
    text='*Playing the Lottery*',
    font='Arial',
    pos=(-0.2, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr3_txt = visual.TextStim(win=win, name='crdm_instr3_txt',
    text='Given information about the number of blue and red chips in the bag, you can decide whether you would prefer a certain monetary outcome or if you would rather play the lottery for a chance to win a different outcome\n\nIn this example, you have a 75% chance of pulling a blue chip and winning $20. Conversely, you have a 25% chance of pulling a red chip and receiving $0.\n\nThe value for each color will change from bag to bag. Read the $ amount above the red and below the blue to know the value of each chip color.',
    font='Arial',
    pos=(-0.2, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_instr3_img = visual.ImageStim(
    win=win,
    name='crdm_instr3_img', 
    image='images/risk_blue_75.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0.6, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
crdm_instr3_lott0_txt = visual.TextStim(win=win, name='crdm_instr3_lott0_txt',
    text='$0',
    font='Arial',
    pos=(0.6, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr3_lott20_txt = visual.TextStim(win=win, name='crdm_instr3_lott20_txt',
    text='$20',
    font='Arial',
    pos=(0.6, -0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_instr3_space_txt = visual.TextStim(win=win, name='crdm_instr3_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_instr3_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr4" ---
crdm_instr4_lottname_txt = visual.TextStim(win=win, name='crdm_instr4_lottname_txt',
    text='*Playing the Lottery*',
    font='Arial',
    pos=(-0.2, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr4_txt = visual.TextStim(win=win, name='crdm_instr4_txt',
    text='For some lotteries, information about the contents of the bag may be partially hidden. \n\nIn this example, the bag has at least 25 blue chips and 25 red chips. However, the color of the remaining 50 chips is unknown. The remaining 50 chips could be all red, all blue, or any combination of the two. ',
    font='Arial',
    pos=(-0.2, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_instr4_img = visual.ImageStim(
    win=win,
    name='crdm_instr4_img', 
    image='images/ambig_50.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0.6, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
crdm_instr4_lott0_txt = visual.TextStim(win=win, name='crdm_instr4_lott0_txt',
    text='$0',
    font='Arial',
    pos=(0.6, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr4_lott20_txt = visual.TextStim(win=win, name='crdm_instr4_lott20_txt',
    text='$20',
    font='Arial',
    pos=(0.6, -0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_instr4_space_txt = visual.TextStim(win=win, name='crdm_instr4_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_instr4_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr5" ---
crdm_instr5_txt = visual.TextStim(win=win, name='crdm_instr5_txt',
    text='The lottery bag will appear in the center of the screen. The certain dollar amount will be presented on either the right or left side of the bag. In this example, the certain $5 would be the left option, and the lottery would be the right option:',
    font='Arial',
    pos=(0, 0.35), height=0.035, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr5_img = visual.ImageStim(
    win=win,
    name='crdm_instr5_img', 
    image='images/risk_blue_75.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_instr5_lott_top_txt = visual.TextStim(win=win, name='crdm_instr5_lott_top_txt',
    text='$0',
    font='Arial',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_instr5_lott_bot_txt = visual.TextStim(win=win, name='crdm_instr5_lott_bot_txt',
    text='$20',
    font='Arial',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr5_sure_txt = visual.TextStim(win=win, name='crdm_instr5_sure_txt',
    text='$5',
    font='Arial',
    pos=(-0.5, -0.05), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_instr5_space_txt = visual.TextStim(win=win, name='crdm_instr5_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_instr5_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr6" ---
crdm_instr6_txt = visual.TextStim(win=win, name='crdm_instr6_txt',
    text='When the green circle appears, use the color buttons on the response pad to indicate your choice:\n\nPress YELLOW to select the left option\nPress GREEN to select the right option \n\n\n\n\n\n\n\n',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=1.25, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr6_img = visual.ImageStim(
    win=win,
    name='crdm_instr6_img', 
    image='images/response_box1-2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_instr6_space_txt = visual.TextStim(win=win, name='crdm_instr6_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_instr6_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_instr7" ---
crdm_instr7_txt = visual.TextStim(win=win, name='crdm_instr7_txt',
    text="After each choice, you will be asked to rate your choice confidence. \n1 indicates you couldn't decide which option you preferred and chose at random, while 4 indicates total certainty in your choice. Use the number keys on the response pad to indicate your confidence: \n\n\n\n\n\n\n\n\n\n\n",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.35, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_instr7_img = visual.ImageStim(
    win=win,
    name='crdm_instr7_img', 
    image='images/response_box1-2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.15), size=(0.6, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_instr7_left_txt = visual.TextStim(win=win, name='crdm_instr7_left_txt',
    text='1 - Not at all confident\n 2 - Less confident',
    font='Arial',
    pos=(-0.575, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_instr7_right_txt = visual.TextStim(win=win, name='crdm_instr7_right_txt',
    text='3 - Somewhat confident\n 4 - Very confident',
    font='Arial',
    pos=(0.575, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_instr7_space_txt = visual.TextStim(win=win, name='crdm_instr7_space_txt',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_instr7_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_pract_instr" ---
crdm_pract_instr_name_txt = visual.TextStim(win=win, name='crdm_pract_instr_name_txt',
    text='* Risk & Ambiguity Task *',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_pract_instr_txt = visual.TextStim(win=win, name='crdm_pract_instr_txt',
    text="Let's practice!\n\nWhen the green circle appears, indicate your decision by pressing YELLOW for the left option and GREEN for the right option. Next, you will rate your choice confidence. \n\nPlease be sure to answer both the task and confidence prompts or the trial will be considered incomplete. ",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=1.25, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_pract_instr_space_txt = visual.TextStim(win=win, name='crdm_pract_instr_space_txt',
    text='Press SPACE to begin.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_pract_instr_key = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_pract_init_fix" ---
crdm_init_fix_poly_2 = visual.ShapeStim(
    win=win, name='crdm_init_fix_poly_2', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "crdm_pract_trial" ---
# Run 'Begin Experiment' code from crdm_pract_trial_py
#position of certain amount option
sure_pos = [] 
sure_resp = []
crdm_msg = ""

#stimuli positions and respective responses
#left/right screen locations
pos = [[-0.5, 0], [0.5, 0]] 
resp = ["4", "5"] #4 = left, 5 = right
crdm_pract_trial_img = visual.ImageStim(
    win=win,
    name='crdm_pract_trial_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_pract_trial_lott_top_txt = visual.TextStim(win=win, name='crdm_pract_trial_lott_top_txt',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_pract_trial_lott_bot_txt = visual.TextStim(win=win, name='crdm_pract_trial_lott_bot_txt',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_pract_trial_sure_amt_txt = visual.TextStim(win=win, name='crdm_pract_trial_sure_amt_txt',
    text='',
    font='Arial',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
GRFX_fix2 = visual.Rect(
    win=win, name='GRFX_fix2',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-5.0, interpolate=True)
crdm_pract_trial_cue = visual.ShapeStim(
    win=win, name='crdm_pract_trial_cue',
    size=(0.04, 0.04), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
crdm_pract_trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_pract_feedback" ---
crdm_pract_feedback_txt = visual.TextStim(win=win, name='crdm_pract_feedback_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "crdm_pract_conf" ---
crdm_pract_conf_txt = visual.TextStim(win=win, name='crdm_pract_conf_txt',
    text='How confident are you in your choice?',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_pract_conf1 = visual.Rect(
    win=win, name='crdm_pract_conf1',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.6, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
crdm_pract_conf1_txt = visual.TextStim(win=win, name='crdm_pract_conf1_txt',
    text='Not at all\nconfident\n\n1',
    font='Arial',
    pos=(-0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_pract_conf2 = visual.Rect(
    win=win, name='crdm_pract_conf2',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.2, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
crdm_pract_conf2_txt = visual.TextStim(win=win, name='crdm_pract_conf2_txt',
    text='Less\nconfident\n\n2',
    font='Arial',
    pos=(-0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_pract_conf3 = visual.Rect(
    win=win, name='crdm_pract_conf3',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.2, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
crdm_pract_conf3_txt = visual.TextStim(win=win, name='crdm_pract_conf3_txt',
    text='Somewhat\nconfident\n\n3',
    font='Arial',
    pos=(0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
crdm_pract_conf4 = visual.Rect(
    win=win, name='crdm_pract_conf4',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.6, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
crdm_pract_conf4_txt = visual.TextStim(win=win, name='crdm_pract_conf4_txt',
    text='Very\nconfident\n\n4',
    font='Arial',
    pos=(0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
crdm_pract_conf_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_pract_iti" ---
crdm_pract_iti1_poly = visual.ShapeStim(
    win=win, name='crdm_pract_iti1_poly', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "crdm_QP_instr" ---
crdm_QP_instr_title_txt = visual.TextStim(win=win, name='crdm_QP_instr_title_txt',
    text='* Risk & Ambiguity Task *',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
crdm_QP_instr_txt = visual.TextStim(win=win, name='crdm_QP_instr_txt',
    text='In the first part of the task, you will be asked to make your choice between a certain monetary outcome and a lottery. For these trials, you will not be asked to rate your choice confidence. \n\nYou will have 4 seconds to consider and 3 seconds to respond. Please make your choice when the green circle appears on the screen. ',
    font='Arial',
    pos=(0, -0.05), height=0.04, wrapWidth=1.25, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_QP_instr_space_txt = visual.TextStim(win=win, name='crdm_QP_instr_space_txt',
    text='Press SPACE to begin.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_QP_instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_questplus" ---
# Run 'Begin Experiment' code from crdm_questplus_py
#position of certain amount option
sure_pos = [] 
sure_resp = []
crdm_msg = ""

#stimuli positions and respective responses
pos = [[-0.5, 0], [0.5, 0]] #left/right screen locations
resp = ["4", "5"] #4 = left, 5 = right
crdm_questplus_img = visual.ImageStim(
    win=win,
    name='crdm_questplus_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_questplus_trial_lott_top_txt = visual.TextStim(win=win, name='crdm_questplus_trial_lott_top_txt',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_questplus_trial_lott_bot_txt = visual.TextStim(win=win, name='crdm_questplus_trial_lott_bot_txt',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_questplus_trial_sure_amt_txt = visual.TextStim(win=win, name='crdm_questplus_trial_sure_amt_txt',
    text='',
    font='Arial',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
GRFX_fix3 = visual.Rect(
    win=win, name='GRFX_fix3',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-5.0, interpolate=True)
crdm_questplus_trial_cue = visual.ShapeStim(
    win=win, name='crdm_questplus_trial_cue',
    size=(0.04, 0.04), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
crdm_questplus_trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_qp_feedback" ---
crdm_QP_FB_txt = visual.TextStim(win=win, name='crdm_QP_FB_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "crdm_generatecsv" ---
# Run 'Begin Experiment' code from crdm_generatecsv_py
#Import the relevant libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
import numpy as np

#First, let's read the ADO output for gains and losses and make it DataFrames
patient_code = expInfo['participant'] #This is to keep the CSV in the same directories as the patient's data
post_mean_gain = rg.get_post_mean(np.exp(g_log_post), g_sets.param)
post_mean_loss = rl.get_post_mean(np.exp(l_log_post), l_sets.param)

#Parameters for the gains
alpha_pos, beta_pos = post_mean_gain[0], post_mean_gain[1]
#Parameters for the losses
alpha_neg, beta_neg = post_mean_loss[0], post_mean_loss[1]

#Declare the variables
p_options = [0.75, 0.5, 0.38, 0.25, 0.13]
amb_options = [0.24, 0.5, 0.74]
A_null = 0.0 # no ambiguity
Vmax = 50.0 #The maximum amount we can pay to participants
Vmin = -50.0 #The minimum amount we can take from participants
Vsafe_pos = 5.0 # The old safe option in positive trials
Vsafe_neg = -5.0 # The old safe option in negative trials

empty_df = pd.DataFrame([],columns=['category','p_reward', 'value_reward'])

def get_extreme(p_options, trials='gains'):
    extr = {} #Create an empty dict
    V = Vmax
    if trials=='losses': #If trials are losses, assign them -50
        V = Vmin
    for p in p_options: #Iterate through the probability levels
        extr[p] = V #Assign them the 50 dollars value
    return extr

extrpos = get_extreme(p_options)
extrneg = get_extreme(p_options,trials='losses')

#From the dictionaries, we create DataFrames to work with
def get_extr_df(extr_dict,trials='gains'):
    df_app = pd.DataFrame(extr_dict.items(), columns=['p_reward', 'value_reward'])
    Extr_df = pd.concat([empty_df, df_app], ignore_index=True)
    category = 'Extr_pos'
    if trials=='losses':
        category = 'Extr_neg'
    Extr_df['category'] = category
    Extr_df['ambiguity'] = A_null
    return Extr_df

def add_ambig_extr(df,amb_options,Vmax=50,prob_amb=0.50,trials='gains'):
    amb_dict = {prob_amb:amb_options}
    df_app = pd.DataFrame(amb_dict.items(), columns=['p_reward', 'ambiguity'])
    df_app = df_app.explode('ambiguity')
    df_app['category'] = df['category']
    df_app['value_reward'] = Vmax
    df = pd.concat([df,df_app],ignore_index=True)
    return df


#We define a function to calculate the SV of the lotteries given ADO's alpha and beta
def append_SVreward(df,alpha,beta,trials='gains'):
    Amp = 1.0
    if trials == 'losses':
        Amp = -1.0
    df['SV_reward'] = (df['p_reward'] - beta*df['ambiguity']/2)*Amp*(abs(df['value_reward']))**alpha
    return df

#We define a function to calculate the SV of the safe options of the trials given the 
#participant's alpha and beta
def append_Vsafe(df,alpha,beta,trials='gains'): 
    Amp = 1.0
    if trials == 'losses':
        Amp = -1.0
    df['SV_New_Safe'] = 0.5*df['SV_reward']
    df['value_lott_SE'] = Amp*(abs(df['SV_New_Safe']) / (df['p_reward']-beta*df['ambiguity']/2)) ** (1 / alpha)
    df['value_safe'] = Amp*(abs(df['SV_New_Safe'])) ** (1 / alpha)
    return df
#Define the data frames
df_pos = get_extr_df(extrpos)
df_pos = add_ambig_extr(df_pos,amb_options)

df_neg = get_extr_df(extrneg,trials='losses')
df_neg = add_ambig_extr(df_neg,amb_options,Vmax=Vmin,trials='losses')


#Add the SV of lottery and safe trials
df_pos = append_SVreward(df_pos,alpha_pos,beta_pos)
df_pos = append_Vsafe(df_pos,alpha_pos,beta_pos)

df_neg = append_SVreward(df_neg,alpha_neg,beta_neg,trials='losses')
df_neg = append_Vsafe(df_neg,alpha_neg,beta_neg,trials='losses')

# Safe option dataframe to use when merging multiple dataframes
df_safe_pos = df_pos[['p_reward','ambiguity','SV_New_Safe','value_lott_SE','value_safe']].copy()
df_safe_neg = df_neg[['p_reward','ambiguity','SV_New_Safe','value_lott_SE','value_safe']].copy()
##Define the trials of subjective equality

#For gains
df_SE_pos = df_pos[['category','p_reward','ambiguity','value_lott_SE', 'SV_New_Safe']].copy()
df_SE_pos['category'] = 'SE_pos'
df_SE_pos = df_SE_pos.rename(columns={'value_lott_SE':'value_reward'})
df_SE_pos['value_safe'] = df_safe_pos['value_safe']
df_SE_pos = df_SE_pos.rename(columns={'SV_New_Safe':'SV_reward'})

#For losses
df_SE_neg = df_neg[['category','p_reward','ambiguity','value_lott_SE', 'SV_New_Safe']].copy()
df_SE_neg['category'] = 'SE_neg'
df_SE_neg = df_SE_neg.rename(columns={'value_lott_SE':'value_reward'})
df_SE_neg['value_safe'] = df_safe_neg['value_safe']
df_SE_neg = df_SE_neg.rename(columns={'SV_New_Safe':'SV_reward'})
##Centered around SE

#For gains
df_cent_pos= df_SE_pos.copy()
df_cent_pos['category'] = 'Cent_SE_pos'

#New dfs
df_adjusted_pos = df_cent_pos.copy()
df_adjusted_pos['value_reward'] = df_adjusted_pos['value_reward'] +2.0
df_adjusted_neg = df_cent_pos.copy()
df_adjusted_neg['value_reward'] = df_adjusted_neg['value_reward'] - 2.0

df_cent_pos = pd.concat([df_cent_pos, df_adjusted_pos, df_adjusted_neg], ignore_index=True)

#Centered around SE DF
df_cent_pos = append_SVreward(df_cent_pos,alpha_pos,beta_pos)

# Filter out rows with negative SV_reward values to avoid complex numbers in value of lottery
df_cent_pos = df_cent_pos[df_cent_pos['SV_reward'] >= 0] #This conditional statement may drop trials. 
df_cent_pos = df_cent_pos.round(2)
#For losses
df_cent_neg= df_SE_neg.copy()
df_cent_neg['category'] = 'Cent_SE_neg'

#New dfs
df1_adjusted_pos = df_cent_neg.copy()
df1_adjusted_pos['value_reward'] = df1_adjusted_pos['value_reward'] +2.0
df1_adjusted_neg = df_cent_neg.copy()
df1_adjusted_neg['value_reward'] = df1_adjusted_neg['value_reward'] - 2.0

df_cent_neg = pd.concat([df_cent_neg, df1_adjusted_pos, df1_adjusted_neg], ignore_index=True)

#Centered around SE DF
df_cent_neg = append_SVreward(df_cent_neg,alpha_neg,beta_neg,trials='losses')

#Selecting our SVdiff sampling. We are doing this by ojo of which SVdiff allows more sampling.
#We need to create a more systematic method. 

#For Gains
df_pos = df_pos.sort_values('SV_reward', ascending=False).reset_index(drop=True)
# fourth ranked SV_reward
index = 3
# SV_reward
col = 4
SV_max_pos = df_pos.iloc[index,col]
_SV_safe = df_pos.iloc[index,col+1]
# sampling here
_delta_SV = SV_max_pos - _SV_safe
# second sampling
_delta_SV2 = 0.5 * _delta_SV
#For Losses

df_neg = df_neg.sort_values('SV_reward', ascending=True).reset_index(drop=True)
# fourth ranked SV_reward
neg_index = 4
# SV_reward
neg_col = 4
SV_min_neg = df_neg.iloc[neg_index,neg_col]
neg_SV_safe = df_neg.iloc[neg_index,neg_col+1]
# sampling here
neg_delta_SV = SV_min_neg - neg_SV_safe
# second sampling
neg_delta_SV2 = 0.5 * neg_delta_SV
#Creating the Neg target SVdeltas and SV_rewards
neg_df1 = df_neg[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
neg_df1['category'] = 'MaxSVdelta_Loss'
neg_df1['deltaSV'] = neg_delta_SV
neg_df1['SV_reward'] = neg_df1['deltaSV'] + neg_df1['SV_New_Safe']
#new_df1
neg_df2 = df_neg[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
neg_df2['category'] = 'Neg_Half_maxSV_delta'
neg_df2['deltaSV'] = neg_delta_SV2
neg_df2['SV_reward'] = neg_df2['deltaSV'] + neg_df2['SV_New_Safe']
neg_df2

#neg_df3 = pd.concat([neg_df1,neg_df2], ignore_index=True)

neg_df3 = df_neg[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
neg_df3['category'] = 'MinSVdelta'
neg_df3['deltaSV'] = -1.0*neg_delta_SV
neg_df3['SV_reward'] = neg_df3['deltaSV'] + neg_df3['SV_New_Safe']


neg_df4 = df_neg[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
neg_df4['category'] = 'Neg_Half_minSV_delta'
neg_df4['deltaSV'] = -1.0*neg_delta_SV2
neg_df4['SV_reward'] = neg_df4['deltaSV'] + neg_df4['SV_New_Safe']
#new_df4 = pd.concat([min_df1,min_df2], ignore_index=True)
neg_df = pd.concat([neg_df1,neg_df2,neg_df3,neg_df4], ignore_index=True) 
#Creating the Gains target SVdeltas and SV_rewards
new_df1 = df_pos[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
new_df1['category'] = 'MaxSVdelta'
new_df1['deltaSV'] = _delta_SV
new_df1['SV_reward'] = new_df1['deltaSV'] + new_df1['SV_New_Safe']
#new_df1

new_df2 = df_pos[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
new_df2['category'] = 'half_maxSV_delta'
new_df2['deltaSV'] = _delta_SV2
new_df2['SV_reward'] = new_df2['deltaSV'] + new_df2['SV_New_Safe']
new_df3 = pd.concat([new_df1,new_df2], ignore_index=True)

min_df1 = df_pos[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
min_df1['category'] = 'MinSVdelta'
min_df1['deltaSV'] = -1.0*_delta_SV
min_df1['SV_reward'] = min_df1['deltaSV'] + min_df1['SV_New_Safe']


min_df2 = df_pos[['category','p_reward', 'ambiguity', 'value_safe', 'SV_New_Safe']].copy()
min_df2['category'] = 'Half_minSV_delta'
min_df2['deltaSV'] = -1.0*_delta_SV2
min_df2['SV_reward'] = min_df2['deltaSV'] + min_df2['SV_New_Safe']
new_df4 = pd.concat([min_df1,min_df2], ignore_index=True)
new_df5 = pd.concat([new_df3, new_df4], ignore_index=True) 
#Calculate the Value of the lotteries for the New SV that give the same SVdelta

def calculate_value_reward(df, alpha, beta):
    new_rows = []
    for index,row in df.iterrows(): #loop to go through each row in the input DataFrame (df)
                                # and extract the relevant values to calculate value_reward
        SV = row['SV_reward']  #The SV of the given row
        value_safe = row['value_safe'] #To keep value_safe constant
        p= row['p_reward']
        #value_safe = 5.0
        A = row['ambiguity'] 
        if A!= 0:
            p=0.50
        if SV<0.0: 
            continue    
        value_reward = (SV/(p-beta*A/2))**(1/alpha) #Having issues with this beta. 
        if (value_reward <100) and (value_reward>=0.0):
            new_rows.append({'category': row['category'], 'SV_reward': SV, 'p_reward': p, 'ambiguity':A, 'value_safe': value_safe, 'value_reward': value_reward}) 
            
            #All the calculated values are used to create a new dictionary for each combination.
            #The dictionaries are collected in a new rows list. 
            new_df = pd.DataFrame(new_rows,columns=['category','p_reward','ambiguity', 'value_reward', 'SV_reward', 'value_safe']) #A new DF from the list
            new_df = new_df.round(2) 
    return new_df

df_SVdeltas_gains = calculate_value_reward(new_df5, alpha_pos, beta_pos)
def calculate_value_reward_losses(df, alpha, beta):
    new_rows = []
    for index,row in df.iterrows(): #loop to go through each row in the input DataFrame (df)
                                # and extract the relevant values to calculate value_reward
        SV = row['SV_reward']  #The SV of the given row
        value_safe = row['value_safe'] #To keep value_safe constant
        p= row['p_reward']
        #value_safe = 5.0
        A = row['ambiguity'] 
        if A!= 0:
            p=0.50
        if SV>0.0: 
            continue    
        value_reward = -((abs(SV)/(p-beta*A/2))**(1/alpha))
        if (value_reward >-100) and (value_reward<=0.0):
            new_rows.append({'category': row['category'], 'SV_reward': SV, 'p_reward': p, 'ambiguity':A, 'value_safe': value_safe, 'value_reward': value_reward}) 
            
            #All the calculated values are used to create a new dictionary for each combination.
            #The dictionaries are collected in a new rows list. 
            new_df = pd.DataFrame(new_rows,columns=['category','p_reward','ambiguity', 'value_reward', 'SV_reward', 'value_safe']) #A new DF from the list
            new_df = new_df.round(2) 
    return new_df

df_SVdeltas_losses =  calculate_value_reward_losses(neg_df, alpha_neg, beta_neg)
df_SVdeltas_losses

df_Trials_gains = pd.concat([df_SVdeltas_gains, df_cent_pos],ignore_index=True)
df_Trials_gains['SV_New_Safe'] = df_Trials_gains['value_safe']**alpha_pos
df_Trials_gains['deltaSV'] = df_Trials_gains['SV_reward'] - df_Trials_gains['SV_New_Safe']
#df_Trials_gains = df_Trials_gains.drop(columns=['value_lott_SE'])

#Convert selected columns to numeric values to be able to round
columns_to_convert = ['value_reward', 'value_safe', 'SV_reward', 'deltaSV']
df_Trials_gains[columns_to_convert] = df_Trials_gains[columns_to_convert].apply(pd.to_numeric, errors='coerce')
df_Trials_gains = df_Trials_gains.round(2)



desired_trials = 50

# Check if the current number of trials is less than the desired number

if len(df_Trials_gains) < desired_trials:
    
    trials_needed = desired_trials - len(df_Trials_gains)
    
    # Calculate the number of additional trials for each category (gains and losses)
    trials_needed_gains = math.ceil(trials_needed)  # Round up to the nearest integer

    # Add new trials from the extremes reward or loss
    additional_trials_gains = df_pos.sample(n=trials_needed_gains, replace=True)

    # Concatenate the additional trials to your existing DataFrame
    df_Trials_gains = pd.concat([df_Trials_gains, additional_trials_gains], ignore_index=True)
    df_Trials_gains = df_Trials_gains.drop(columns=['value_lott_SE'])

# Check if the current number of trials is greater than 50
if len(df_Trials_gains) > desired_trials:
    trials_to_delete = len(df_Trials_gains) - desired_trials
    
    # Randomly sample rows to delete
    rows_to_delete = df_Trials_gains[df_Trials_gains['category'] == 'Cent_SE_pos'].sample(n=trials_to_delete)
    
    # Remove the sampled rows from the DataFrame
    df_Trials_gains = df_Trials_gains.drop(rows_to_delete.index)

#Rounding to the nearest 50 cents
df_Trials_gains['value_reward'] = df_Trials_gains['value_reward'].apply(lambda x: round(x * 2) / 2)
df_Trials_gains['value_safe'] = df_Trials_gains['value_safe'].apply(lambda x: round(x * 2) / 2)


#Update value_safe and value_reward when it's 0. Note that the SV_reward for those trials will stay as previously calculate as 0.0
df_Trials_gains.loc[df_Trials_gains['value_safe']==0, 'value_safe'] = 0.5
df_Trials_gains.loc[df_Trials_gains['value_reward']==0, 'value_reward'] = 0.5

df_Trials_gains

df_Trials_losses = pd.concat([df_SVdeltas_losses, df_cent_neg],ignore_index=True)
df_Trials_losses['SV_New_Safe'] = -abs(df_Trials_losses['value_safe'])**alpha_neg
df_Trials_losses['deltaSV'] = df_Trials_losses['SV_reward'] - df_Trials_losses['SV_New_Safe']
#df_Trials_gains = df_Trials_gains.drop(columns=['value_lott_SE'])

#Convert selected columns to numeric values to be able to round
columns_to_convert = ['value_reward', 'value_safe', 'SV_reward']
df_Trials_losses[columns_to_convert] = df_Trials_losses[columns_to_convert].apply(pd.to_numeric, errors='coerce')
df_Trials_losses = df_Trials_losses.round(2)

desired_trials = 50

# Check if the current number of trials is less than the desired number

if len(df_Trials_losses) < desired_trials:
    trials_needed = desired_trials - len(df_Trials_losses)
    # Calculate the number of additional trials for each category (gains and losses)
    trials_needed_losses = math.floor(trials_needed)  # Round down to the nearest integer

    # Add new trials from the extremes reward or loss
    additional_trials_losses = df_neg.sample(n=trials_needed_gains, replace=True)

    # Concatenate the additional trials to your existing DataFrame
    df_Trials_losses = pd.concat([df_Trials_losses, additional_trials_losses], ignore_index=True)
    df_Trials_losses = df_Trials_losses.drop(columns=['value_lott_SE'])

# Check if the current number of trials is greater than 50
if len(df_Trials_losses) > desired_trials:
    trials_to_delete = len(df_Trials_losses) - desired_trials
    
    # Randomly sample rows to delete
    rows_to_delete = df_Trials_losses[df_Trials_losses['category'] == 'Cent_SE_neg'].sample(n=trials_to_delete)
    
    # Remove the sampled rows from the DataFrame
    df_Trials_losses = df_Trials_losses.drop(rows_to_delete.index)


#Reset the index
df_Trials_losses = df_Trials_losses.reset_index(drop=True)

#Rounding to the nearest 50 cents
df_Trials_losses['value_reward'] = df_Trials_losses['value_reward'].apply(lambda x: round(x * 2) / 2)
df_Trials_losses['value_safe'] = df_Trials_losses['value_safe'].apply(lambda x: round(x * 2) / 2)

#avoiding 0
df_Trials_losses.loc[df_Trials_losses['value_safe']==0, 'value_safe'] = 0.5
df_Trials_losses.loc[df_Trials_losses['value_reward']==0, 'value_reward'] = 0.5

df_Trials_losses

#We define the list of image filenames. 
#For now, it is hardcoded. I need to work in soft coding it from 
#the participant's output csv 'crdm_img' column. 
 
   #risk images filenames
rimages = [ 'risk_blue_75.bmp','risk_blue_50.bmp', 'risk_blue_38.bmp','risk_blue_25.bmp', 'risk_blue_13.bmp',
           'risk_red_75.bmp','risk_red_50.bmp',  'risk_red_38.bmp', 'risk_red_25.bmp', 'risk_red_13.bmp']
    #Ambiguity images filenames
aimages = ['ambig_24.bmp', 'ambig_50.bmp','ambig_74.bmp']


p_options_100 = [int(p * 100) for p in p_options] #We define the probabilities as integers. This is to be consistent with the output csv format
risk_images = {} #Empty dict to store the results. 

for p in p_options_100: #Iterate through each probability
    #For each probability value, we start with an empty list named 
    # matching_images to hold the filenames that match the current probability 
    matching_images = [img for img in rimages if isinstance(img, str) and f"_{p}" in img]
    #For each image filename, we check if it's a string 
    # and if the formatted probability (like "_75") is present in the filename.
    #If both conditions are true, the image filename is added to the list. 
    risk_images[p] = matching_images #After iterating through the file names,we assign the list
    #to the risk_images dictionary using p as a key. 

amb_options = [0.24, 0.5, 0.74]
amb_options_100 = [int(a * 100) for a in amb_options]
amb_images = {}

for a in amb_options_100:
    matching_images = [img for img in aimages if isinstance(img, str) and f"ambig_{a}" in img]
    amb_images[a] = matching_images

#Making it into the raw CSV
raw_trials = 'csv/{}_raw_trials.csv'.format(patient_code)

#Let's reformat to match the psychopy CSV input
crdm_trials_gains = df_Trials_gains.copy()

crdm_trials_gains['category'] = 'gain'
crdm_trials_gains = crdm_trials_gains.sort_values('p_reward', ascending=True).reset_index(drop=True)
crdm_trials_gains = crdm_trials_gains.drop(columns=['SV_reward', 'SV_New_Safe','deltaSV'])
crdm_trials_gains['ambiguity'] = (crdm_trials_gains['ambiguity']*100).astype(int)
crdm_trials_gains['p_reward'] = (crdm_trials_gains['p_reward']*100).astype(int)
crdm_trials_gains = crdm_trials_gains.rename(columns={
    'value_safe':'crdm_sure_amt',
    'value_reward':'crdm_lott',
    'ambiguity': 'crdm_amb_lev',
    'p_reward':'crdm_lott_p', 
    'category':'crdm_domain'})
crdm_trials_gains['crdm_sure_p'] = 100
# Reordering columns
column_order = [
    'crdm_sure_amt', 'crdm_sure_p', 'crdm_lott', 'crdm_lott_p', 'crdm_amb_lev', 'crdm_domain'
]
crdm_trials_gains = crdm_trials_gains[column_order]

# Sort the DataFrame first by 'crdm_lott_p' and then by 'crdm_amb_lev
crdm_trials_gains = crdm_trials_gains.sort_values(by=['crdm_lott_p', 'crdm_amb_lev'], ascending=[True,True])

# Separate rows with 'crdm_amb_lev' different from zero to the end
zero_ambiguity_rows = crdm_trials_gains[crdm_trials_gains['crdm_amb_lev'] == 0]
non_zero_ambiguity_rows = crdm_trials_gains[crdm_trials_gains['crdm_amb_lev'] != 0]

# Concatenate the DataFrames to put rows with 'crdm_amb_lev' different from zero at the end
crdm_trials_gains = pd.concat([zero_ambiguity_rows, non_zero_ambiguity_rows], ignore_index=True)

# Randomly assign values to crdm_lott_top or crdm_lott_bot
# randomly select whether each value should go to the crdm_lott_top or crdm_lott_bot column
random_assignments = np.random.choice(['crdm_lott_top', 'crdm_lott_bot'], size=len(crdm_trials_gains))

# np.where to conditionally assign values from the crdm_lott column to the appropriate 
# columns based on the random selections
crdm_trials_gains['crdm_lott_top'] = np.where(random_assignments == 'crdm_lott_top', crdm_trials_gains['crdm_lott'], 0)
crdm_trials_gains['crdm_lott_bot'] = np.where(random_assignments == 'crdm_lott_bot', crdm_trials_gains['crdm_lott'], 0)
column_order = ['crdm_sure_amt', 'crdm_sure_p', 'crdm_lott_top', 'crdm_lott_bot', 'crdm_lott_p', 'crdm_amb_lev', 'crdm_domain']
crdm_trials_gain = crdm_trials_gains[column_order]

#Let's reformat to match the psychopy CSV input
crdm_trials_losses = df_Trials_losses.copy()
crdm_trials_losses = crdm_trials_losses.sort_values('p_reward', ascending=True).reset_index(drop=True)
crdm_trials_losses['category'] = 'loss'
crdm_trials_losses = crdm_trials_losses.drop(columns=['SV_reward', 'SV_New_Safe','deltaSV'])
crdm_trials_losses['ambiguity'] = (crdm_trials_losses['ambiguity']*100).astype(int)
crdm_trials_losses['p_reward'] = (crdm_trials_losses['p_reward']*100).astype(int)
crdm_trials_losses = crdm_trials_losses.rename(columns={
    'value_safe':'crdm_sure_amt',
    'value_reward':'crdm_lott',
    'ambiguity': 'crdm_amb_lev',
    'p_reward':'crdm_lott_p', 
    'category':'crdm_domain'})
crdm_trials_losses['crdm_sure_p'] = 100
# Reordering columns
column_order = ['crdm_sure_amt', 'crdm_sure_p', 'crdm_lott', 'crdm_lott_p', 'crdm_amb_lev', 'crdm_domain'
]
crdm_trials_losses = crdm_trials_losses[column_order]
#crdm_trials_losses =crdm_trials_losses.sort_values(by=['crdm_lott_p', 'crdm_amb_lev'], ascending=True).reset_index(drop=True)

# Sort the DataFrame first by 'crdm_lott_p' and then by 'crdm_amb_lev
crdm_trials_losses = crdm_trials_losses.sort_values(by=['crdm_lott_p', 'crdm_amb_lev'], ascending=[True,True])

# Separate rows with 'crdm_amb_lev' different from zero to the end
zero_ambiguity_rows_loss = crdm_trials_losses[crdm_trials_losses['crdm_amb_lev'] == 0]
non_zero_ambiguity_rows_loss = crdm_trials_losses[crdm_trials_losses['crdm_amb_lev'] != 0]

# Concatenate the DataFrames to put rows with 'crdm_amb_lev' different from zero at the end
crdm_trials_losses = pd.concat([zero_ambiguity_rows_loss, non_zero_ambiguity_rows_loss], ignore_index=True)
# Randomly assign values to crdm_lott_top or crdm_lott_bot
# randomly select whether each value should go to the crdm_lott_top or crdm_lott_bot column
random_assignments = np.random.choice(['crdm_lott_top', 'crdm_lott_bot'], size=len(crdm_trials_losses))

# np.where to conditionally assign values from the crdm_lott column to the appropriate 
# columns based on the random selections
crdm_trials_losses['crdm_lott_top'] = np.where(random_assignments == 'crdm_lott_top', crdm_trials_losses['crdm_lott'], 0)
crdm_trials_losses['crdm_lott_bot'] = np.where(random_assignments == 'crdm_lott_bot', crdm_trials_losses['crdm_lott'], 0)
column_order = [
    'crdm_sure_amt', 'crdm_sure_p', 'crdm_lott_top', 'crdm_lott_bot', 'crdm_lott_p', 'crdm_amb_lev', 'crdm_domain'
]
crdm_trials_loss = crdm_trials_losses[column_order]
crdm_trials = pd.concat([crdm_trials_gain,crdm_trials_loss],ignore_index=True)
#crdm_trials['crdm_win_side'] = 'bottom'
#crdm_trials.loc[crdm_trials['crdm_lott_top'] !=0.00, 'crdm_win_side'] = 'top'  
#Creating the crdm_win_side column

def determine_win_side(row): #Function the determine the wining side of the lottery. 
    if row['crdm_lott_top'] != 0.00:
        return 'top'
    else:
        return 'bottom'
    
# Apply the function to create the 'crdm_win_side' column
crdm_trials['crdm_win_side'] = crdm_trials.apply(determine_win_side, axis=1)
#crdm_trials

#Function to created crdm_image
def determine_risk_image_file(row):
    for p, f in risk_images.items():
        if row['crdm_lott_p'] == p and row['crdm_win_side'] == 'top':
            return  f[1] #using the 2nd item in the dictionary for red images
        elif row['crdm_lott_p'] == p and row['crdm_win_side'] == 'bottom':
            return f[0] #Using the first item of the dict as blue
crdm_trials['crdm_img'] = crdm_trials.apply(determine_risk_image_file,axis =1)

column_order = ['crdm_sure_amt', 'crdm_sure_p', 'crdm_lott_top', 'crdm_lott_bot', 'crdm_lott_p', 'crdm_amb_lev', 'crdm_domain', 'crdm_img', 'crdm_win_side']
crdm_trials = crdm_trials[column_order]

#Rounding to the nearest 50 cents

crdm_trials_csv = 'adaptive_schedules/{}_trials.csv'.format(patient_code)
crdm_trials.to_csv(crdm_trials_csv,float_format='%.2f',index=False)

# --- Initialize components for Routine "crdm_trial_instr" ---
crdm_trial_instr_title_txt = visual.TextStim(win=win, name='crdm_trial_instr_title_txt',
    text='* Risk & Ambiguity Task *',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_trial_instr_txt = visual.TextStim(win=win, name='crdm_trial_instr_txt',
    text='In the second part of the task, you will also be asked to make your choice between the certain monetary outcome and lottery. However, for these trials, you will be asked to rate your choice confidence.\n\nYou will have 4 seconds to view and consider the certain and lottery options, and 3 seconds to choose once the green circle appears. You will then have 4 seconds to rate your confidence.',
    font='Arial',
    pos=(0, -0.05), height=0.04, wrapWidth=1.25, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_trial_instr_space_txt = visual.TextStim(win=win, name='crdm_trial_instr_space_txt',
    text='Press SPACE to begin.',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_trial_instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_init_fix" ---
crdm_init_fix_poly = visual.ShapeStim(
    win=win, name='crdm_init_fix_poly', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "crdm_trial" ---
# Run 'Begin Experiment' code from crdm_trial_py
delta_time = 0 #used in variable ITI
sure_pos = [] #position of certain amount option
sure_resp = [] 
crdm_msg = "" #feedback message string

#stimuli positions and respective responses
pos = [[-0.5, 0], [0.5, 0]] #left/right screen locations
resp = ["4", "5"] #4 = left, 5 = right
crdm_trial_img = visual.ImageStim(
    win=win,
    name='crdm_trial_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_trial_lott_top = visual.TextStim(win=win, name='crdm_trial_lott_top',
    text='',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_trial_lott_bot = visual.TextStim(win=win, name='crdm_trial_lott_bot',
    text='',
    font='Arial',
    pos=(0, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_trial_sure_amt = visual.TextStim(win=win, name='crdm_trial_sure_amt',
    text='',
    font='Arial',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
GRFX_fix = visual.Rect(
    win=win, name='GRFX_fix',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-5.0, interpolate=True)
crdm_trial_cue = visual.ShapeStim(
    win=win, name='crdm_trial_cue',
    size=(0.04, 0.04), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, 1.0000, -1.0000], fillColor=[-1.0000, 1.0000, -1.0000],
    opacity=None, depth=-6.0, interpolate=True)
crdm_trial_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_feedback" ---
crdm_feedback_txt = visual.TextStim(win=win, name='crdm_feedback_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "crdm_conf" ---
crdm_conf_txt = visual.TextStim(win=win, name='crdm_conf_txt',
    text='How confident are you in your choice?',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
crdm_conf1 = visual.Rect(
    win=win, name='crdm_conf1',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.6, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
crdm_conf1_txt = visual.TextStim(win=win, name='crdm_conf1_txt',
    text='Not at all\nconfident\n\n1',
    font='Arial',
    pos=(-0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_conf2 = visual.Rect(
    win=win, name='crdm_conf2',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.2, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
crdm_conf2_txt = visual.TextStim(win=win, name='crdm_conf2_txt',
    text='Less\nconfident\n\n2',
    font='Arial',
    pos=(-0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_conf3 = visual.Rect(
    win=win, name='crdm_conf3',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.2, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
crdm_conf3_txt = visual.TextStim(win=win, name='crdm_conf3_txt',
    text='Somewhat\nconfident\n\n3',
    font='Arial',
    pos=(0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
crdm_conf4 = visual.Rect(
    win=win, name='crdm_conf4',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.6, -0.3), anchor='center',
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
crdm_conf4_txt = visual.TextStim(win=win, name='crdm_conf4_txt',
    text='Very\nconfident\n\n4',
    font='Arial',
    pos=(0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
crdm_conf_resp = keyboard.Keyboard()

# --- Initialize components for Routine "crdm_trials_iti" ---
crdm_trials_iti1_poly = visual.ShapeStim(
    win=win, name='crdm_trials_iti1_poly', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# --- Initialize components for Routine "crdm_bonus" ---
crdm_bonus_img = visual.ImageStim(
    win=win,
    name='crdm_bonus_img', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.6, -0.1), size=(0.3, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
crdm_bonus_thanks_txt = visual.TextStim(win=win, name='crdm_bonus_thanks_txt',
    text='Thank you for participating in the Risk & Ambiguity Task!',
    font='Arial',
    pos=(0, 0.35), height=0.05, wrapWidth=1.5, ori=0.0, 
    color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
crdm_bonus_box = visual.TextStim(win=win, name='crdm_bonus_box',
    text='',
    font='Arial',
    pos=(-0.20, -0.05), height=0.04, wrapWidth=1.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
crdm_bonus_lott_top = visual.TextStim(win=win, name='crdm_bonus_lott_top',
    text='',
    font='Arial',
    pos=(0.6, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
crdm_bonus_lott_bot = visual.TextStim(win=win, name='crdm_bonus_lott_bot',
    text='',
    font='Arial',
    pos=(0.6, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
crdm_bonus_space_txt = visual.TextStim(win=win, name='crdm_bonus_space_txt',
    text='Press SPACE to end',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
crdm_bonus_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "crdm_instr1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from crdm_instr1_py
#provides specific loop names for each of two interations of CRDM
#to provide flexibility of crdm_pract_trial and crdm_trial routines
practice_loop_name = "crdm_pract_trials"
loop_name = "crdm_trials"
crdm_instr1_resp.keys = []
crdm_instr1_resp.rt = []
_crdm_instr1_resp_allKeys = []
# keep track of which components have finished
crdm_instr1Components = [crdm_instr1_title_txt, crdm_instr1_txt, crdm_instr1_space_txt, crdm_instr1_resp]
for thisComponent in crdm_instr1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr1_title_txt* updates
    if crdm_instr1_title_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr1_title_txt.frameNStart = frameN  # exact frame index
        crdm_instr1_title_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr1_title_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr1_title_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr1_title_txt.setAutoDraw(True)
    
    # *crdm_instr1_txt* updates
    if crdm_instr1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr1_txt.frameNStart = frameN  # exact frame index
        crdm_instr1_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr1_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr1_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr1_txt.setAutoDraw(True)
    
    # *crdm_instr1_space_txt* updates
    if crdm_instr1_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr1_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr1_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr1_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr1_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr1_space_txt.setAutoDraw(True)
    
    # *crdm_instr1_resp* updates
    waitOnFlip = False
    if crdm_instr1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr1_resp.frameNStart = frameN  # exact frame index
        crdm_instr1_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr1_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr1_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr1_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr1_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr1_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr1_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr1_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr1_resp_allKeys):
            crdm_instr1_resp.keys = _crdm_instr1_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr1_resp.rt = _crdm_instr1_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr1" ---
for thisComponent in crdm_instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr2_resp.keys = []
crdm_instr2_resp.rt = []
_crdm_instr2_resp_allKeys = []
# keep track of which components have finished
crdm_instr2Components = [crdm_instr2_lottname_txt, crdm_instr2_txt, crdm_instr2_img, crdm_instr2_lott0_txt, crdm_instr2_lott20_txt, crdm_instr2_space_txt, crdm_instr2_resp]
for thisComponent in crdm_instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr2_lottname_txt* updates
    if crdm_instr2_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_lottname_txt.frameNStart = frameN  # exact frame index
        crdm_instr2_lottname_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr2_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_lottname_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_lottname_txt.setAutoDraw(True)
    
    # *crdm_instr2_txt* updates
    if crdm_instr2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_txt.frameNStart = frameN  # exact frame index
        crdm_instr2_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr2_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_txt.setAutoDraw(True)
    
    # *crdm_instr2_img* updates
    if crdm_instr2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_img.frameNStart = frameN  # exact frame index
        crdm_instr2_img.tStart = t  # local t and not account for scr refresh
        crdm_instr2_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_img.setAutoDraw(True)
    
    # *crdm_instr2_lott0_txt* updates
    if crdm_instr2_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_lott0_txt.frameNStart = frameN  # exact frame index
        crdm_instr2_lott0_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr2_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_lott0_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_lott0_txt.setAutoDraw(True)
    
    # *crdm_instr2_lott20_txt* updates
    if crdm_instr2_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_lott20_txt.frameNStart = frameN  # exact frame index
        crdm_instr2_lott20_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr2_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_lott20_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_lott20_txt.setAutoDraw(True)
    
    # *crdm_instr2_space_txt* updates
    if crdm_instr2_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr2_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr2_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_space_txt.setAutoDraw(True)
    
    # *crdm_instr2_resp* updates
    waitOnFlip = False
    if crdm_instr2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr2_resp.frameNStart = frameN  # exact frame index
        crdm_instr2_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr2_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr2_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr2_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr2_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr2_resp_allKeys):
            crdm_instr2_resp.keys = _crdm_instr2_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr2_resp.rt = _crdm_instr2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr2" ---
for thisComponent in crdm_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr3_resp.keys = []
crdm_instr3_resp.rt = []
_crdm_instr3_resp_allKeys = []
# keep track of which components have finished
crdm_instr3Components = [crdm_instr3_lottname_txt, crdm_instr3_txt, crdm_instr3_img, crdm_instr3_lott0_txt, crdm_instr3_lott20_txt, crdm_instr3_space_txt, crdm_instr3_resp]
for thisComponent in crdm_instr3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr3_lottname_txt* updates
    if crdm_instr3_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_lottname_txt.frameNStart = frameN  # exact frame index
        crdm_instr3_lottname_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr3_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_lottname_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_lottname_txt.setAutoDraw(True)
    
    # *crdm_instr3_txt* updates
    if crdm_instr3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_txt.frameNStart = frameN  # exact frame index
        crdm_instr3_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr3_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_txt.setAutoDraw(True)
    
    # *crdm_instr3_img* updates
    if crdm_instr3_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_img.frameNStart = frameN  # exact frame index
        crdm_instr3_img.tStart = t  # local t and not account for scr refresh
        crdm_instr3_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_img.setAutoDraw(True)
    
    # *crdm_instr3_lott0_txt* updates
    if crdm_instr3_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_lott0_txt.frameNStart = frameN  # exact frame index
        crdm_instr3_lott0_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr3_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_lott0_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_lott0_txt.setAutoDraw(True)
    
    # *crdm_instr3_lott20_txt* updates
    if crdm_instr3_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_lott20_txt.frameNStart = frameN  # exact frame index
        crdm_instr3_lott20_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr3_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_lott20_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_lott20_txt.setAutoDraw(True)
    
    # *crdm_instr3_space_txt* updates
    if crdm_instr3_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr3_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr3_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_space_txt.setAutoDraw(True)
    
    # *crdm_instr3_resp* updates
    waitOnFlip = False
    if crdm_instr3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr3_resp.frameNStart = frameN  # exact frame index
        crdm_instr3_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr3_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr3_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr3_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr3_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr3_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr3_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr3_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr3_resp_allKeys):
            crdm_instr3_resp.keys = _crdm_instr3_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr3_resp.rt = _crdm_instr3_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr3" ---
for thisComponent in crdm_instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr4_resp.keys = []
crdm_instr4_resp.rt = []
_crdm_instr4_resp_allKeys = []
# keep track of which components have finished
crdm_instr4Components = [crdm_instr4_lottname_txt, crdm_instr4_txt, crdm_instr4_img, crdm_instr4_lott0_txt, crdm_instr4_lott20_txt, crdm_instr4_space_txt, crdm_instr4_resp]
for thisComponent in crdm_instr4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr4_lottname_txt* updates
    if crdm_instr4_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_lottname_txt.frameNStart = frameN  # exact frame index
        crdm_instr4_lottname_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr4_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_lottname_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_lottname_txt.setAutoDraw(True)
    
    # *crdm_instr4_txt* updates
    if crdm_instr4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_txt.frameNStart = frameN  # exact frame index
        crdm_instr4_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr4_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_txt.setAutoDraw(True)
    
    # *crdm_instr4_img* updates
    if crdm_instr4_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_img.frameNStart = frameN  # exact frame index
        crdm_instr4_img.tStart = t  # local t and not account for scr refresh
        crdm_instr4_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_img.setAutoDraw(True)
    
    # *crdm_instr4_lott0_txt* updates
    if crdm_instr4_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_lott0_txt.frameNStart = frameN  # exact frame index
        crdm_instr4_lott0_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr4_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_lott0_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_lott0_txt.setAutoDraw(True)
    
    # *crdm_instr4_lott20_txt* updates
    if crdm_instr4_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_lott20_txt.frameNStart = frameN  # exact frame index
        crdm_instr4_lott20_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr4_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_lott20_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_lott20_txt.setAutoDraw(True)
    
    # *crdm_instr4_space_txt* updates
    if crdm_instr4_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr4_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr4_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_space_txt.setAutoDraw(True)
    
    # *crdm_instr4_resp* updates
    waitOnFlip = False
    if crdm_instr4_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr4_resp.frameNStart = frameN  # exact frame index
        crdm_instr4_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr4_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr4_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr4_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr4_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr4_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr4_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr4_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr4_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr4_resp_allKeys):
            crdm_instr4_resp.keys = _crdm_instr4_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr4_resp.rt = _crdm_instr4_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr4" ---
for thisComponent in crdm_instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr5_resp.keys = []
crdm_instr5_resp.rt = []
_crdm_instr5_resp_allKeys = []
# keep track of which components have finished
crdm_instr5Components = [crdm_instr5_txt, crdm_instr5_img, crdm_instr5_lott_top_txt, crdm_instr5_lott_bot_txt, crdm_instr5_sure_txt, crdm_instr5_space_txt, crdm_instr5_resp]
for thisComponent in crdm_instr5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr5_txt* updates
    if crdm_instr5_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_txt.frameNStart = frameN  # exact frame index
        crdm_instr5_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr5_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_txt.setAutoDraw(True)
    
    # *crdm_instr5_img* updates
    if crdm_instr5_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_img.frameNStart = frameN  # exact frame index
        crdm_instr5_img.tStart = t  # local t and not account for scr refresh
        crdm_instr5_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_img.setAutoDraw(True)
    
    # *crdm_instr5_lott_top_txt* updates
    if crdm_instr5_lott_top_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_lott_top_txt.frameNStart = frameN  # exact frame index
        crdm_instr5_lott_top_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr5_lott_top_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_lott_top_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_lott_top_txt.setAutoDraw(True)
    
    # *crdm_instr5_lott_bot_txt* updates
    if crdm_instr5_lott_bot_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_lott_bot_txt.frameNStart = frameN  # exact frame index
        crdm_instr5_lott_bot_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr5_lott_bot_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_lott_bot_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_lott_bot_txt.setAutoDraw(True)
    
    # *crdm_instr5_sure_txt* updates
    if crdm_instr5_sure_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_sure_txt.frameNStart = frameN  # exact frame index
        crdm_instr5_sure_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr5_sure_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_sure_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_sure_txt.setAutoDraw(True)
    
    # *crdm_instr5_space_txt* updates
    if crdm_instr5_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr5_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr5_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_space_txt.setAutoDraw(True)
    
    # *crdm_instr5_resp* updates
    waitOnFlip = False
    if crdm_instr5_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr5_resp.frameNStart = frameN  # exact frame index
        crdm_instr5_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr5_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr5_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr5_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr5_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr5_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr5_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr5_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr5_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr5_resp_allKeys):
            crdm_instr5_resp.keys = _crdm_instr5_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr5_resp.rt = _crdm_instr5_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr5" ---
for thisComponent in crdm_instr5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr6_resp.keys = []
crdm_instr6_resp.rt = []
_crdm_instr6_resp_allKeys = []
# keep track of which components have finished
crdm_instr6Components = [crdm_instr6_txt, crdm_instr6_img, crdm_instr6_space_txt, crdm_instr6_resp]
for thisComponent in crdm_instr6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr6_txt* updates
    if crdm_instr6_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr6_txt.frameNStart = frameN  # exact frame index
        crdm_instr6_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr6_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr6_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr6_txt.setAutoDraw(True)
    
    # *crdm_instr6_img* updates
    if crdm_instr6_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr6_img.frameNStart = frameN  # exact frame index
        crdm_instr6_img.tStart = t  # local t and not account for scr refresh
        crdm_instr6_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr6_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr6_img.setAutoDraw(True)
    
    # *crdm_instr6_space_txt* updates
    if crdm_instr6_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr6_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr6_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr6_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr6_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr6_space_txt.setAutoDraw(True)
    
    # *crdm_instr6_resp* updates
    waitOnFlip = False
    if crdm_instr6_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr6_resp.frameNStart = frameN  # exact frame index
        crdm_instr6_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr6_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr6_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr6_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr6_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr6_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr6_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr6_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr6_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr6_resp_allKeys):
            crdm_instr6_resp.keys = _crdm_instr6_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr6_resp.rt = _crdm_instr6_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr6" ---
for thisComponent in crdm_instr6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_instr7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_instr7_resp.keys = []
crdm_instr7_resp.rt = []
_crdm_instr7_resp_allKeys = []
# keep track of which components have finished
crdm_instr7Components = [crdm_instr7_txt, crdm_instr7_img, crdm_instr7_left_txt, crdm_instr7_right_txt, crdm_instr7_space_txt, crdm_instr7_resp]
for thisComponent in crdm_instr7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_instr7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_instr7_txt* updates
    if crdm_instr7_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_txt.frameNStart = frameN  # exact frame index
        crdm_instr7_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr7_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_txt.setAutoDraw(True)
    
    # *crdm_instr7_img* updates
    if crdm_instr7_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_img.frameNStart = frameN  # exact frame index
        crdm_instr7_img.tStart = t  # local t and not account for scr refresh
        crdm_instr7_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_img, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_img.setAutoDraw(True)
    
    # *crdm_instr7_left_txt* updates
    if crdm_instr7_left_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_left_txt.frameNStart = frameN  # exact frame index
        crdm_instr7_left_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr7_left_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_left_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_left_txt.setAutoDraw(True)
    
    # *crdm_instr7_right_txt* updates
    if crdm_instr7_right_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_right_txt.frameNStart = frameN  # exact frame index
        crdm_instr7_right_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr7_right_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_right_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_right_txt.setAutoDraw(True)
    
    # *crdm_instr7_space_txt* updates
    if crdm_instr7_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_space_txt.frameNStart = frameN  # exact frame index
        crdm_instr7_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_instr7_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_space_txt.setAutoDraw(True)
    
    # *crdm_instr7_resp* updates
    waitOnFlip = False
    if crdm_instr7_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_instr7_resp.frameNStart = frameN  # exact frame index
        crdm_instr7_resp.tStart = t  # local t and not account for scr refresh
        crdm_instr7_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_instr7_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_instr7_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_instr7_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_instr7_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_instr7_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_instr7_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_instr7_resp_allKeys.extend(theseKeys)
        if len(_crdm_instr7_resp_allKeys):
            crdm_instr7_resp.keys = _crdm_instr7_resp_allKeys[-1].name  # just the last key pressed
            crdm_instr7_resp.rt = _crdm_instr7_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_instr7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_instr7" ---
for thisComponent in crdm_instr7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_instr7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_pract_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_pract_instr_key.keys = []
crdm_pract_instr_key.rt = []
_crdm_pract_instr_key_allKeys = []
# keep track of which components have finished
crdm_pract_instrComponents = [crdm_pract_instr_name_txt, crdm_pract_instr_txt, crdm_pract_instr_space_txt, crdm_pract_instr_key]
for thisComponent in crdm_pract_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_pract_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_pract_instr_name_txt* updates
    if crdm_pract_instr_name_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_pract_instr_name_txt.frameNStart = frameN  # exact frame index
        crdm_pract_instr_name_txt.tStart = t  # local t and not account for scr refresh
        crdm_pract_instr_name_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_pract_instr_name_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_pract_instr_name_txt.setAutoDraw(True)
    
    # *crdm_pract_instr_txt* updates
    if crdm_pract_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_pract_instr_txt.frameNStart = frameN  # exact frame index
        crdm_pract_instr_txt.tStart = t  # local t and not account for scr refresh
        crdm_pract_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_pract_instr_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_pract_instr_txt.setAutoDraw(True)
    
    # *crdm_pract_instr_space_txt* updates
    if crdm_pract_instr_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_pract_instr_space_txt.frameNStart = frameN  # exact frame index
        crdm_pract_instr_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_pract_instr_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_pract_instr_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_pract_instr_space_txt.setAutoDraw(True)
    
    # *crdm_pract_instr_key* updates
    waitOnFlip = False
    if crdm_pract_instr_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_pract_instr_key.frameNStart = frameN  # exact frame index
        crdm_pract_instr_key.tStart = t  # local t and not account for scr refresh
        crdm_pract_instr_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_pract_instr_key, 'tStartRefresh')  # time at next scr refresh
        crdm_pract_instr_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_pract_instr_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_pract_instr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_pract_instr_key.status == STARTED and not waitOnFlip:
        theseKeys = crdm_pract_instr_key.getKeys(keyList=['space'], waitRelease=False)
        _crdm_pract_instr_key_allKeys.extend(theseKeys)
        if len(_crdm_pract_instr_key_allKeys):
            crdm_pract_instr_key.keys = _crdm_pract_instr_key_allKeys[-1].name  # just the last key pressed
            crdm_pract_instr_key.rt = _crdm_pract_instr_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_pract_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_pract_instr" ---
for thisComponent in crdm_pract_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_pract_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_pract_init_fix" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
crdm_pract_init_fixComponents = [crdm_init_fix_poly_2]
for thisComponent in crdm_pract_init_fixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_pract_init_fix" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_init_fix_poly_2* updates
    if crdm_init_fix_poly_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_init_fix_poly_2.frameNStart = frameN  # exact frame index
        crdm_init_fix_poly_2.tStart = t  # local t and not account for scr refresh
        crdm_init_fix_poly_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_init_fix_poly_2, 'tStartRefresh')  # time at next scr refresh
        crdm_init_fix_poly_2.setAutoDraw(True)
    if crdm_init_fix_poly_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > crdm_init_fix_poly_2.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            crdm_init_fix_poly_2.tStop = t  # not accounting for scr refresh
            crdm_init_fix_poly_2.frameNStop = frameN  # exact frame index
            crdm_init_fix_poly_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_pract_init_fixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_pract_init_fix" ---
for thisComponent in crdm_pract_init_fixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
crdm_pract_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('crdm_practice.xlsx'),
    seed=None, name='crdm_pract_trials')
thisExp.addLoop(crdm_pract_trials)  # add the loop to the experiment
thisCrdm_pract_trial = crdm_pract_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCrdm_pract_trial.rgb)
if thisCrdm_pract_trial != None:
    for paramName in thisCrdm_pract_trial:
        exec('{} = thisCrdm_pract_trial[paramName]'.format(paramName))

for thisCrdm_pract_trial in crdm_pract_trials:
    currentLoop = crdm_pract_trials
    # abbreviate parameter names if possible (e.g. rgb = thisCrdm_pract_trial.rgb)
    if thisCrdm_pract_trial != None:
        for paramName in thisCrdm_pract_trial:
            exec('{} = thisCrdm_pract_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "crdm_pract_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_pract_trial_py
    my_loop = eval(practice_loop_name)
    
    #random index for certain outcome position and response
    idx = random.randint(0,1) 
    sure_pos = pos[idx] 
    sure_resp = resp[idx]
    crdm_pract_trial_img.setImage("images/" + crdm_img)
    crdm_pract_trial_lott_top_txt.setText(str("$"+str(crdm_lott_top)))
    crdm_pract_trial_lott_bot_txt.setText(str("$"+str(crdm_lott_bot)))
    crdm_pract_trial_sure_amt_txt.setPos(sure_pos)
    crdm_pract_trial_sure_amt_txt.setText(str("$"+str(crdm_sure_amt))
)
    crdm_pract_trial_resp.keys = []
    crdm_pract_trial_resp.rt = []
    _crdm_pract_trial_resp_allKeys = []
    # keep track of which components have finished
    crdm_pract_trialComponents = [crdm_pract_trial_img, crdm_pract_trial_lott_top_txt, crdm_pract_trial_lott_bot_txt, crdm_pract_trial_sure_amt_txt, GRFX_fix2, crdm_pract_trial_cue, crdm_pract_trial_resp]
    for thisComponent in crdm_pract_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_pract_trial" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_pract_trial_img* updates
        if crdm_pract_trial_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_img.frameNStart = frameN  # exact frame index
            crdm_pract_trial_img.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_img, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_img.setAutoDraw(True)
        if crdm_pract_trial_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_img.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_img.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_img.frameNStop = frameN  # exact frame index
                crdm_pract_trial_img.setAutoDraw(False)
        
        # *crdm_pract_trial_lott_top_txt* updates
        if crdm_pract_trial_lott_top_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_lott_top_txt.frameNStart = frameN  # exact frame index
            crdm_pract_trial_lott_top_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_lott_top_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_lott_top_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_lott_top_txt.setAutoDraw(True)
        if crdm_pract_trial_lott_top_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_lott_top_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_lott_top_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_lott_top_txt.frameNStop = frameN  # exact frame index
                crdm_pract_trial_lott_top_txt.setAutoDraw(False)
        
        # *crdm_pract_trial_lott_bot_txt* updates
        if crdm_pract_trial_lott_bot_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_lott_bot_txt.frameNStart = frameN  # exact frame index
            crdm_pract_trial_lott_bot_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_lott_bot_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_lott_bot_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_lott_bot_txt.setAutoDraw(True)
        if crdm_pract_trial_lott_bot_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_lott_bot_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_lott_bot_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_lott_bot_txt.frameNStop = frameN  # exact frame index
                crdm_pract_trial_lott_bot_txt.setAutoDraw(False)
        
        # *crdm_pract_trial_sure_amt_txt* updates
        if crdm_pract_trial_sure_amt_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_sure_amt_txt.frameNStart = frameN  # exact frame index
            crdm_pract_trial_sure_amt_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_sure_amt_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_sure_amt_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_sure_amt_txt.setAutoDraw(True)
        if crdm_pract_trial_sure_amt_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_sure_amt_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_sure_amt_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_sure_amt_txt.frameNStop = frameN  # exact frame index
                crdm_pract_trial_sure_amt_txt.setAutoDraw(False)
        
        # *GRFX_fix2* updates
        if GRFX_fix2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            GRFX_fix2.frameNStart = frameN  # exact frame index
            GRFX_fix2.tStart = t  # local t and not account for scr refresh
            GRFX_fix2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GRFX_fix2, 'tStartRefresh')  # time at next scr refresh
            GRFX_fix2.setAutoDraw(True)
        if GRFX_fix2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GRFX_fix2.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                GRFX_fix2.tStop = t  # not accounting for scr refresh
                GRFX_fix2.frameNStop = frameN  # exact frame index
                GRFX_fix2.setAutoDraw(False)
        
        # *crdm_pract_trial_cue* updates
        if crdm_pract_trial_cue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_cue.frameNStart = frameN  # exact frame index
            crdm_pract_trial_cue.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_cue, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_cue.setAutoDraw(True)
        if crdm_pract_trial_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_cue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_cue.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_cue.frameNStop = frameN  # exact frame index
                crdm_pract_trial_cue.setAutoDraw(False)
        
        # *crdm_pract_trial_resp* updates
        waitOnFlip = False
        if crdm_pract_trial_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_trial_resp.frameNStart = frameN  # exact frame index
            crdm_pract_trial_resp.tStart = t  # local t and not account for scr refresh
            crdm_pract_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_trial_resp, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_pract_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_pract_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_pract_trial_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_trial_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_trial_resp.tStop = t  # not accounting for scr refresh
                crdm_pract_trial_resp.frameNStop = frameN  # exact frame index
                crdm_pract_trial_resp.status = FINISHED
        if crdm_pract_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_pract_trial_resp.getKeys(keyList=["4", "5"], waitRelease=False)
            _crdm_pract_trial_resp_allKeys.extend(theseKeys)
            if len(_crdm_pract_trial_resp_allKeys):
                crdm_pract_trial_resp.keys = _crdm_pract_trial_resp_allKeys[0].name  # just the first key pressed
                crdm_pract_trial_resp.rt = _crdm_pract_trial_resp_allKeys[0].rt
                # was this correct?
                if (crdm_pract_trial_resp.keys == str(sure_resp)) or (crdm_pract_trial_resp.keys == sure_resp):
                    crdm_pract_trial_resp.corr = 1
                else:
                    crdm_pract_trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_pract_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_pract_trial" ---
    for thisComponent in crdm_pract_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from crdm_pract_trial_py
    pract_key = crdm_pract_trial_resp.keys
    pract_sure_key = crdm_pract_trial_resp.corr
    
    my_loop.addData("crdm_trial_type", "practice")
    # check responses
    if crdm_pract_trial_resp.keys in ['', [], None]:  # No response was made
        crdm_pract_trial_resp.keys = None
        # was no response the correct answer?!
        if str(sure_resp).lower() == 'none':
           crdm_pract_trial_resp.corr = 1;  # correct non-response
        else:
           crdm_pract_trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for crdm_pract_trials (TrialHandler)
    crdm_pract_trials.addData('crdm_pract_trial_resp.keys',crdm_pract_trial_resp.keys)
    crdm_pract_trials.addData('crdm_pract_trial_resp.corr', crdm_pract_trial_resp.corr)
    if crdm_pract_trial_resp.keys != None:  # we had a response
        crdm_pract_trials.addData('crdm_pract_trial_resp.rt', crdm_pract_trial_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "crdm_pract_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_pract_feedback_py
    if len(pract_key) == 0: #Ss did not respond
        crdm_msg = "NO RESPONSE"
    elif pract_sure_key: #Ss chose sure amt
        crdm_msg = "CERTAIN $" + str(crdm_sure_amt)
    else: #Ss chose lottery
        crdm_msg = "LOTTERY"
    crdm_pract_feedback_txt.setText(crdm_msg)
    # keep track of which components have finished
    crdm_pract_feedbackComponents = [crdm_pract_feedback_txt]
    for thisComponent in crdm_pract_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_pract_feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_pract_feedback_txt* updates
        if crdm_pract_feedback_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_feedback_txt.frameNStart = frameN  # exact frame index
            crdm_pract_feedback_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_feedback_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_feedback_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_feedback_txt.setAutoDraw(True)
        if crdm_pract_feedback_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_feedback_txt.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_feedback_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_feedback_txt.frameNStop = frameN  # exact frame index
                crdm_pract_feedback_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_pract_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_pract_feedback" ---
    for thisComponent in crdm_pract_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "crdm_pract_conf" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_pract_conf_py
    #Ss did not respond
    if len(pract_key) == 0: 
        continueRoutine = False
    
    #set default gray for all four response boxes
    conf1_color = [0, 0, 0] 
    conf2_color = [0, 0, 0]
    conf3_color = [0, 0, 0]
    conf4_color = [0, 0, 0]
    crdm_pract_conf_resp.keys = []
    crdm_pract_conf_resp.rt = []
    _crdm_pract_conf_resp_allKeys = []
    # keep track of which components have finished
    crdm_pract_confComponents = [crdm_pract_conf_txt, crdm_pract_conf1, crdm_pract_conf1_txt, crdm_pract_conf2, crdm_pract_conf2_txt, crdm_pract_conf3, crdm_pract_conf3_txt, crdm_pract_conf4, crdm_pract_conf4_txt, crdm_pract_conf_resp]
    for thisComponent in crdm_pract_confComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_pract_conf" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from crdm_pract_conf_py
        #resp is received
        pract_conf_key = crdm_pract_conf_resp.keys
        if len(pract_conf_key) == 1:
            pract_conf_key = confkey_map[pract_conf_key[-1]]
            #not at all confident
            if pract_conf_key == "1":
                #change box color to indicate selection
                conf1_color = "darkgray" 
                conf2_color = [0,0,0]
                conf3_color = [0,0,0]
                conf4_color = [0,0,0]
            #less confident
            elif pract_conf_key == "2": 
                conf1_color = [0,0,0]
                conf2_color = "darkgray"
                conf3_color = [0,0,0]
                conf4_color = [0,0,0]
            #somewhat confident
            elif pract_conf_key == "3": 
                conf1_color = [0,0,0]
                conf2_color = [0,0,0]
                conf3_color = "darkgray"
                conf4_color = [0,0,0]
            #very confident
            elif pract_conf_key == "4": 
                conf1_color = [0,0,0]
                conf2_color = [0,0,0]
                conf3_color = [0,0,0]
                conf4_color = "darkgray"
        
        # *crdm_pract_conf_txt* updates
        if crdm_pract_conf_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf_txt.frameNStart = frameN  # exact frame index
            crdm_pract_conf_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf_txt.setAutoDraw(True)
        if crdm_pract_conf_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_conf_txt.frameNStop = frameN  # exact frame index
                crdm_pract_conf_txt.setAutoDraw(False)
        
        # *crdm_pract_conf1* updates
        if crdm_pract_conf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf1.frameNStart = frameN  # exact frame index
            crdm_pract_conf1.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf1, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf1.setAutoDraw(True)
        if crdm_pract_conf1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf1.tStop = t  # not accounting for scr refresh
                crdm_pract_conf1.frameNStop = frameN  # exact frame index
                crdm_pract_conf1.setAutoDraw(False)
        if crdm_pract_conf1.status == STARTED:  # only update if drawing
            crdm_pract_conf1.setFillColor(conf1_color, log=False)
        
        # *crdm_pract_conf1_txt* updates
        if crdm_pract_conf1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf1_txt.frameNStart = frameN  # exact frame index
            crdm_pract_conf1_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf1_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf1_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf1_txt.setAutoDraw(True)
        if crdm_pract_conf1_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf1_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf1_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_conf1_txt.frameNStop = frameN  # exact frame index
                crdm_pract_conf1_txt.setAutoDraw(False)
        
        # *crdm_pract_conf2* updates
        if crdm_pract_conf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf2.frameNStart = frameN  # exact frame index
            crdm_pract_conf2.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf2, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf2.setAutoDraw(True)
        if crdm_pract_conf2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf2.tStop = t  # not accounting for scr refresh
                crdm_pract_conf2.frameNStop = frameN  # exact frame index
                crdm_pract_conf2.setAutoDraw(False)
        if crdm_pract_conf2.status == STARTED:  # only update if drawing
            crdm_pract_conf2.setFillColor(conf2_color, log=False)
        
        # *crdm_pract_conf2_txt* updates
        if crdm_pract_conf2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf2_txt.frameNStart = frameN  # exact frame index
            crdm_pract_conf2_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf2_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf2_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf2_txt.setAutoDraw(True)
        if crdm_pract_conf2_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf2_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf2_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_conf2_txt.frameNStop = frameN  # exact frame index
                crdm_pract_conf2_txt.setAutoDraw(False)
        
        # *crdm_pract_conf3* updates
        if crdm_pract_conf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf3.frameNStart = frameN  # exact frame index
            crdm_pract_conf3.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf3, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf3.setAutoDraw(True)
        if crdm_pract_conf3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf3.tStop = t  # not accounting for scr refresh
                crdm_pract_conf3.frameNStop = frameN  # exact frame index
                crdm_pract_conf3.setAutoDraw(False)
        if crdm_pract_conf3.status == STARTED:  # only update if drawing
            crdm_pract_conf3.setFillColor(conf3_color, log=False)
        
        # *crdm_pract_conf3_txt* updates
        if crdm_pract_conf3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf3_txt.frameNStart = frameN  # exact frame index
            crdm_pract_conf3_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf3_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf3_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf3_txt.setAutoDraw(True)
        if crdm_pract_conf3_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf3_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf3_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_conf3_txt.frameNStop = frameN  # exact frame index
                crdm_pract_conf3_txt.setAutoDraw(False)
        
        # *crdm_pract_conf4* updates
        if crdm_pract_conf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf4.frameNStart = frameN  # exact frame index
            crdm_pract_conf4.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf4, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf4.setAutoDraw(True)
        if crdm_pract_conf4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf4.tStop = t  # not accounting for scr refresh
                crdm_pract_conf4.frameNStop = frameN  # exact frame index
                crdm_pract_conf4.setAutoDraw(False)
        if crdm_pract_conf4.status == STARTED:  # only update if drawing
            crdm_pract_conf4.setFillColor(conf4_color, log=False)
        
        # *crdm_pract_conf4_txt* updates
        if crdm_pract_conf4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf4_txt.frameNStart = frameN  # exact frame index
            crdm_pract_conf4_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf4_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf4_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf4_txt.setAutoDraw(True)
        if crdm_pract_conf4_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf4_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf4_txt.tStop = t  # not accounting for scr refresh
                crdm_pract_conf4_txt.frameNStop = frameN  # exact frame index
                crdm_pract_conf4_txt.setAutoDraw(False)
        
        # *crdm_pract_conf_resp* updates
        waitOnFlip = False
        if crdm_pract_conf_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_conf_resp.frameNStart = frameN  # exact frame index
            crdm_pract_conf_resp.tStart = t  # local t and not account for scr refresh
            crdm_pract_conf_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_conf_resp, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_conf_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_pract_conf_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_pract_conf_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_pract_conf_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_conf_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_conf_resp.tStop = t  # not accounting for scr refresh
                crdm_pract_conf_resp.frameNStop = frameN  # exact frame index
                crdm_pract_conf_resp.status = FINISHED
        if crdm_pract_conf_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_pract_conf_resp.getKeys(keyList=['2', '3', 'j', 'k'], waitRelease=False)
            _crdm_pract_conf_resp_allKeys.extend(theseKeys)
            if len(_crdm_pract_conf_resp_allKeys):
                crdm_pract_conf_resp.keys = _crdm_pract_conf_resp_allKeys[-1].name  # just the last key pressed
                crdm_pract_conf_resp.rt = _crdm_pract_conf_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_pract_confComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_pract_conf" ---
    for thisComponent in crdm_pract_confComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if crdm_pract_conf_resp.keys in ['', [], None]:  # No response was made
        crdm_pract_conf_resp.keys = None
    crdm_pract_trials.addData('crdm_pract_conf_resp.keys',crdm_pract_conf_resp.keys)
    if crdm_pract_conf_resp.keys != None:  # we had a response
        crdm_pract_trials.addData('crdm_pract_conf_resp.rt', crdm_pract_conf_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "crdm_pract_iti" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_pract_iti1_py
    #3 CRDM practice trials
    if crdm_pract_trials.thisTrialN == 5:
        continueRoutine = False
    # keep track of which components have finished
    crdm_pract_itiComponents = [crdm_pract_iti1_poly]
    for thisComponent in crdm_pract_itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_pract_iti" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_pract_iti1_poly* updates
        if crdm_pract_iti1_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_iti1_poly.frameNStart = frameN  # exact frame index
            crdm_pract_iti1_poly.tStart = t  # local t and not account for scr refresh
            crdm_pract_iti1_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_iti1_poly, 'tStartRefresh')  # time at next scr refresh
            crdm_pract_iti1_poly.setAutoDraw(True)
        if crdm_pract_iti1_poly.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_iti1_poly.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_iti1_poly.tStop = t  # not accounting for scr refresh
                crdm_pract_iti1_poly.frameNStop = frameN  # exact frame index
                crdm_pract_iti1_poly.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_pract_itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_pract_iti" ---
    for thisComponent in crdm_pract_itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'crdm_pract_trials'


# --- Prepare to start Routine "crdm_QP_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
crdm_QP_instr_resp.keys = []
crdm_QP_instr_resp.rt = []
_crdm_QP_instr_resp_allKeys = []
# keep track of which components have finished
crdm_QP_instrComponents = [crdm_QP_instr_title_txt, crdm_QP_instr_txt, crdm_QP_instr_space_txt, crdm_QP_instr_resp]
for thisComponent in crdm_QP_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_QP_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_QP_instr_title_txt* updates
    if crdm_QP_instr_title_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_QP_instr_title_txt.frameNStart = frameN  # exact frame index
        crdm_QP_instr_title_txt.tStart = t  # local t and not account for scr refresh
        crdm_QP_instr_title_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_QP_instr_title_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_QP_instr_title_txt.setAutoDraw(True)
    
    # *crdm_QP_instr_txt* updates
    if crdm_QP_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_QP_instr_txt.frameNStart = frameN  # exact frame index
        crdm_QP_instr_txt.tStart = t  # local t and not account for scr refresh
        crdm_QP_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_QP_instr_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_QP_instr_txt.setAutoDraw(True)
    
    # *crdm_QP_instr_space_txt* updates
    if crdm_QP_instr_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_QP_instr_space_txt.frameNStart = frameN  # exact frame index
        crdm_QP_instr_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_QP_instr_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_QP_instr_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_QP_instr_space_txt.setAutoDraw(True)
    
    # *crdm_QP_instr_resp* updates
    waitOnFlip = False
    if crdm_QP_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_QP_instr_resp.frameNStart = frameN  # exact frame index
        crdm_QP_instr_resp.tStart = t  # local t and not account for scr refresh
        crdm_QP_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_QP_instr_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_QP_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_QP_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_QP_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_QP_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_QP_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_QP_instr_resp_allKeys.extend(theseKeys)
        if len(_crdm_QP_instr_resp_allKeys):
            crdm_QP_instr_resp.keys = _crdm_QP_instr_resp_allKeys[-1].name  # just the last key pressed
            crdm_QP_instr_resp.rt = _crdm_QP_instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_QP_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_QP_instr" ---
for thisComponent in crdm_QP_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_QP_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
questplus_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('questplus_trials.csv'),
    seed=None, name='questplus_trials')
thisExp.addLoop(questplus_trials)  # add the loop to the experiment
thisQuestplus_trial = questplus_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisQuestplus_trial.rgb)
if thisQuestplus_trial != None:
    for paramName in thisQuestplus_trial:
        exec('{} = thisQuestplus_trial[paramName]'.format(paramName))

for thisQuestplus_trial in questplus_trials:
    currentLoop = questplus_trials
    # abbreviate parameter names if possible (e.g. rgb = thisQuestplus_trial.rgb)
    if thisQuestplus_trial != None:
        for paramName in thisQuestplus_trial:
            exec('{} = thisQuestplus_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "crdm_questplus" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_questplus_py
    my_loop = eval("questplus_trials")
    
    #random index for certain outcome position and response
    idx = random.randint(0,1) 
    sure_pos = pos[idx] 
    sure_resp = resp[idx]
    ado_lott_top = ""
    ado_lott_bot = ""
    ado_img = ""
    
    if trial_type == "gain":
        log_lik, ent, log_post, sets = g_log_lik, g_ent, g_log_post, g_sets
        mutual_info = rg.get_MI(log_lik,ent,log_post)
    else: #losses
        log_lik, ent, log_post, sets = l_log_lik, l_ent, l_log_post, l_sets
        mutual_info = rl.get_MI(log_lik,ent,log_post)
        
    
    # GET_DESIGN based on maximum Mutual information
    idx_design = np.argmax(mutual_info)
    cur_design = sets.choice.iloc[idx_design].to_dict()
    
    if nonzero_side == "top": #red side of lotto
        ado_lott_top = cur_design["value_reward"] #nonzero value on top (red)
        ado_lott_bot = 0
        if cur_design["amb_level"] == 0: #risk trial
            ado_img = "risk_red_{0}.bmp".format(int(cur_design["p_reward"]*100))
        else: #ambiguity trial
            ado_img = "ambig_{0}.bmp".format(int(cur_design["amb_level"]*100))
    else: #blue side of lotto
        ado_lott_top = 0
        ado_lott_bot = cur_design["value_reward"] #nonzero value on bottom (blue)
        if cur_design["amb_level"] == 0: #risk trial
            ado_img = "risk_blue_{0}.bmp".format(int(cur_design["p_reward"]*100))
        else: #ambiguity trial
            ado_img = "ambig_{0}.bmp".format(int(cur_design["amb_level"]*100))
    ado_sure_amt = cur_design["value_null"]
    crdm_questplus_img.setImage("images/" + ado_img)
    crdm_questplus_trial_lott_top_txt.setText(str("$"+str(ado_lott_top)))
    crdm_questplus_trial_lott_bot_txt.setText(str("$"+str(ado_lott_bot)))
    crdm_questplus_trial_sure_amt_txt.setPos(sure_pos)
    crdm_questplus_trial_sure_amt_txt.setText(str("$"+str(ado_sure_amt))
)
    crdm_questplus_trial_resp.keys = []
    crdm_questplus_trial_resp.rt = []
    _crdm_questplus_trial_resp_allKeys = []
    # keep track of which components have finished
    crdm_questplusComponents = [crdm_questplus_img, crdm_questplus_trial_lott_top_txt, crdm_questplus_trial_lott_bot_txt, crdm_questplus_trial_sure_amt_txt, GRFX_fix3, crdm_questplus_trial_cue, crdm_questplus_trial_resp]
    for thisComponent in crdm_questplusComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_questplus" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_questplus_img* updates
        if crdm_questplus_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_img.frameNStart = frameN  # exact frame index
            crdm_questplus_img.tStart = t  # local t and not account for scr refresh
            crdm_questplus_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_img, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_img.setAutoDraw(True)
        if crdm_questplus_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_img.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_img.tStop = t  # not accounting for scr refresh
                crdm_questplus_img.frameNStop = frameN  # exact frame index
                crdm_questplus_img.setAutoDraw(False)
        
        # *crdm_questplus_trial_lott_top_txt* updates
        if crdm_questplus_trial_lott_top_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_trial_lott_top_txt.frameNStart = frameN  # exact frame index
            crdm_questplus_trial_lott_top_txt.tStart = t  # local t and not account for scr refresh
            crdm_questplus_trial_lott_top_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_trial_lott_top_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_trial_lott_top_txt.setAutoDraw(True)
        if crdm_questplus_trial_lott_top_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_trial_lott_top_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_trial_lott_top_txt.tStop = t  # not accounting for scr refresh
                crdm_questplus_trial_lott_top_txt.frameNStop = frameN  # exact frame index
                crdm_questplus_trial_lott_top_txt.setAutoDraw(False)
        
        # *crdm_questplus_trial_lott_bot_txt* updates
        if crdm_questplus_trial_lott_bot_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_trial_lott_bot_txt.frameNStart = frameN  # exact frame index
            crdm_questplus_trial_lott_bot_txt.tStart = t  # local t and not account for scr refresh
            crdm_questplus_trial_lott_bot_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_trial_lott_bot_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_trial_lott_bot_txt.setAutoDraw(True)
        if crdm_questplus_trial_lott_bot_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_trial_lott_bot_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_trial_lott_bot_txt.tStop = t  # not accounting for scr refresh
                crdm_questplus_trial_lott_bot_txt.frameNStop = frameN  # exact frame index
                crdm_questplus_trial_lott_bot_txt.setAutoDraw(False)
        
        # *crdm_questplus_trial_sure_amt_txt* updates
        if crdm_questplus_trial_sure_amt_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_trial_sure_amt_txt.frameNStart = frameN  # exact frame index
            crdm_questplus_trial_sure_amt_txt.tStart = t  # local t and not account for scr refresh
            crdm_questplus_trial_sure_amt_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_trial_sure_amt_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_trial_sure_amt_txt.setAutoDraw(True)
        if crdm_questplus_trial_sure_amt_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_trial_sure_amt_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_trial_sure_amt_txt.tStop = t  # not accounting for scr refresh
                crdm_questplus_trial_sure_amt_txt.frameNStop = frameN  # exact frame index
                crdm_questplus_trial_sure_amt_txt.setAutoDraw(False)
        
        # *GRFX_fix3* updates
        if GRFX_fix3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            GRFX_fix3.frameNStart = frameN  # exact frame index
            GRFX_fix3.tStart = t  # local t and not account for scr refresh
            GRFX_fix3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GRFX_fix3, 'tStartRefresh')  # time at next scr refresh
            GRFX_fix3.setAutoDraw(True)
        if GRFX_fix3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GRFX_fix3.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                GRFX_fix3.tStop = t  # not accounting for scr refresh
                GRFX_fix3.frameNStop = frameN  # exact frame index
                GRFX_fix3.setAutoDraw(False)
        
        # *crdm_questplus_trial_cue* updates
        if crdm_questplus_trial_cue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_trial_cue.frameNStart = frameN  # exact frame index
            crdm_questplus_trial_cue.tStart = t  # local t and not account for scr refresh
            crdm_questplus_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_trial_cue, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_trial_cue.setAutoDraw(True)
        if crdm_questplus_trial_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_trial_cue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_trial_cue.tStop = t  # not accounting for scr refresh
                crdm_questplus_trial_cue.frameNStop = frameN  # exact frame index
                crdm_questplus_trial_cue.setAutoDraw(False)
        
        # *crdm_questplus_trial_resp* updates
        waitOnFlip = False
        if crdm_questplus_trial_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_questplus_trial_resp.frameNStart = frameN  # exact frame index
            crdm_questplus_trial_resp.tStart = t  # local t and not account for scr refresh
            crdm_questplus_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_questplus_trial_resp, 'tStartRefresh')  # time at next scr refresh
            crdm_questplus_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_questplus_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_questplus_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_questplus_trial_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_questplus_trial_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_questplus_trial_resp.tStop = t  # not accounting for scr refresh
                crdm_questplus_trial_resp.frameNStop = frameN  # exact frame index
                crdm_questplus_trial_resp.status = FINISHED
        if crdm_questplus_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_questplus_trial_resp.getKeys(keyList=["4", "5"], waitRelease=False)
            _crdm_questplus_trial_resp_allKeys.extend(theseKeys)
            if len(_crdm_questplus_trial_resp_allKeys):
                crdm_questplus_trial_resp.keys = _crdm_questplus_trial_resp_allKeys[0].name  # just the first key pressed
                crdm_questplus_trial_resp.rt = _crdm_questplus_trial_resp_allKeys[0].rt
                # was this correct?
                if (crdm_questplus_trial_resp.keys == str(sure_resp)) or (crdm_questplus_trial_resp.keys == sure_resp):
                    crdm_questplus_trial_resp.corr = 1
                else:
                    crdm_questplus_trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_questplusComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_questplus" ---
    for thisComponent in crdm_questplusComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from crdm_questplus_py
    qp_key = crdm_questplus_trial_resp.keys
    qp_sure_key = crdm_questplus_trial_resp.corr
    my_loop.addData("crdm_trial_type", "questplus")
    
    cur_response = not qp_sure_key #flips .corr convention
    if trial_type == "gain":
        mutual_info, log_post = rg.update_MI(sets.choice, sets.response, cur_design, cur_response, log_lik, ent, log_post)
        post_mean = rg.get_post_mean(np.exp(log_post), sets.param)
        post_sd = rg.get_post_sd(np.exp(log_post), sets.param)
        g_log_lik, g_ent, g_log_post, g_sets = log_lik, ent, log_post, sets
    else: #losses
        mutual_info, log_post = rl.update_MI(sets.choice, sets.response, cur_design, cur_response, log_lik, ent, log_post)
        post_mean = rl.get_post_mean(np.exp(log_post), sets.param)
        post_sd = rl.get_post_sd(np.exp(log_post), sets.param)
        l_log_lik, l_ent, l_log_post, l_sets = log_lik, ent, log_post, sets
    
    my_loop.addData("response", cur_response)
    my_loop.addData('mean_alpha', post_mean[0])
    my_loop.addData('mean_beta', post_mean[1])
    my_loop.addData('mean_gamma', post_mean[2])
    my_loop.addData('sd_alpha', post_sd[0])
    my_loop.addData('sd_beta', post_sd[1])
    my_loop.addData('sd_gamma', post_sd[2])
    my_loop.addData("lott_reward", cur_design["value_reward"])
    my_loop.addData("lott_prob", int(cur_design["p_reward"]*100))
    my_loop.addData("ambig_level", int(cur_design["amb_level"]*100))
    # check responses
    if crdm_questplus_trial_resp.keys in ['', [], None]:  # No response was made
        crdm_questplus_trial_resp.keys = None
        # was no response the correct answer?!
        if str(sure_resp).lower() == 'none':
           crdm_questplus_trial_resp.corr = 1;  # correct non-response
        else:
           crdm_questplus_trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for questplus_trials (TrialHandler)
    questplus_trials.addData('crdm_questplus_trial_resp.keys',crdm_questplus_trial_resp.keys)
    questplus_trials.addData('crdm_questplus_trial_resp.corr', crdm_questplus_trial_resp.corr)
    if crdm_questplus_trial_resp.keys != None:  # we had a response
        questplus_trials.addData('crdm_questplus_trial_resp.rt', crdm_questplus_trial_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "crdm_qp_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_QP_FB_py
    if len(qp_key) == 0: #Ss did not respond
        crdm_msg = "No Response"
    elif qp_sure_key: #Ss chose sure amt
        crdm_msg = "You chose: CERTAIN $" + str(cur_design["value_null"])
    else: #Ss chose lottery
        crdm_msg = "You chose: LOTTERY"
    crdm_QP_FB_txt.setText(crdm_msg)
    # keep track of which components have finished
    crdm_qp_feedbackComponents = [crdm_QP_FB_txt]
    for thisComponent in crdm_qp_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_qp_feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_QP_FB_txt* updates
        if crdm_QP_FB_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_QP_FB_txt.frameNStart = frameN  # exact frame index
            crdm_QP_FB_txt.tStart = t  # local t and not account for scr refresh
            crdm_QP_FB_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_QP_FB_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_QP_FB_txt.setAutoDraw(True)
        if crdm_QP_FB_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_QP_FB_txt.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                crdm_QP_FB_txt.tStop = t  # not accounting for scr refresh
                crdm_QP_FB_txt.frameNStop = frameN  # exact frame index
                crdm_QP_FB_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_qp_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_qp_feedback" ---
    for thisComponent in crdm_qp_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'questplus_trials'


# --- Prepare to start Routine "crdm_generatecsv" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
crdm_generatecsvComponents = []
for thisComponent in crdm_generatecsvComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_generatecsv" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_generatecsvComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_generatecsv" ---
for thisComponent in crdm_generatecsvComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_generatecsv" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_trial_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from crdm_trial_instr_py
task_resps = []
conf_resps = []

iti_list = [random.random() for i in range(100)] # create list of random floats (0-1) which is length of trial schedule
s = sum(iti_list) #sum list of rnadom floats
iti_list = [i*100/s for i in iti_list] #for each item in iti_list: multiple by list length, then divide by list sum
crdm_trial_instr_resp.keys = []
crdm_trial_instr_resp.rt = []
_crdm_trial_instr_resp_allKeys = []
# keep track of which components have finished
crdm_trial_instrComponents = [crdm_trial_instr_title_txt, crdm_trial_instr_txt, crdm_trial_instr_space_txt, crdm_trial_instr_resp]
for thisComponent in crdm_trial_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_trial_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_trial_instr_title_txt* updates
    if crdm_trial_instr_title_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_trial_instr_title_txt.frameNStart = frameN  # exact frame index
        crdm_trial_instr_title_txt.tStart = t  # local t and not account for scr refresh
        crdm_trial_instr_title_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_trial_instr_title_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_trial_instr_title_txt.setAutoDraw(True)
    
    # *crdm_trial_instr_txt* updates
    if crdm_trial_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_trial_instr_txt.frameNStart = frameN  # exact frame index
        crdm_trial_instr_txt.tStart = t  # local t and not account for scr refresh
        crdm_trial_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_trial_instr_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_trial_instr_txt.setAutoDraw(True)
    
    # *crdm_trial_instr_space_txt* updates
    if crdm_trial_instr_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_trial_instr_space_txt.frameNStart = frameN  # exact frame index
        crdm_trial_instr_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_trial_instr_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_trial_instr_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_trial_instr_space_txt.setAutoDraw(True)
    
    # *crdm_trial_instr_resp* updates
    waitOnFlip = False
    if crdm_trial_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_trial_instr_resp.frameNStart = frameN  # exact frame index
        crdm_trial_instr_resp.tStart = t  # local t and not account for scr refresh
        crdm_trial_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_trial_instr_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_trial_instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_trial_instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_trial_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_trial_instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_trial_instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_trial_instr_resp_allKeys.extend(theseKeys)
        if len(_crdm_trial_instr_resp_allKeys):
            crdm_trial_instr_resp.keys = _crdm_trial_instr_resp_allKeys[-1].name  # just the last key pressed
            crdm_trial_instr_resp.rt = _crdm_trial_instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_trial_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_trial_instr" ---
for thisComponent in crdm_trial_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_trial_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "crdm_init_fix" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from crdm_init_fix_py
utc_iti = int((datetime.utcnow() - epoch).total_seconds()*1000)
log_out(subid, utc_iti, 1, "Rand_ITIFix", -1, -1, "xxxx", "xxxxxxxxx", -1, -1, 1)
# keep track of which components have finished
crdm_init_fixComponents = [crdm_init_fix_poly]
for thisComponent in crdm_init_fixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_init_fix" ---
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_init_fix_poly* updates
    if crdm_init_fix_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_init_fix_poly.frameNStart = frameN  # exact frame index
        crdm_init_fix_poly.tStart = t  # local t and not account for scr refresh
        crdm_init_fix_poly.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_init_fix_poly, 'tStartRefresh')  # time at next scr refresh
        crdm_init_fix_poly.setAutoDraw(True)
    if crdm_init_fix_poly.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > crdm_init_fix_poly.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            crdm_init_fix_poly.tStop = t  # not accounting for scr refresh
            crdm_init_fix_poly.frameNStop = frameN  # exact frame index
            crdm_init_fix_poly.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_init_fixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_init_fix" ---
for thisComponent in crdm_init_fixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
crdm_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(crdm_trials_csv),
    seed=None, name='crdm_trials')
thisExp.addLoop(crdm_trials)  # add the loop to the experiment
thisCrdm_trial = crdm_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCrdm_trial.rgb)
if thisCrdm_trial != None:
    for paramName in thisCrdm_trial:
        exec('{} = thisCrdm_trial[paramName]'.format(paramName))

for thisCrdm_trial in crdm_trials:
    currentLoop = crdm_trials
    # abbreviate parameter names if possible (e.g. rgb = thisCrdm_trial.rgb)
    if thisCrdm_trial != None:
        for paramName in thisCrdm_trial:
            exec('{} = thisCrdm_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "crdm_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_trial_py
    utc_trial = int((datetime.utcnow() - epoch).total_seconds()*1000) #output log variable for Ss trial onset
    log_out(subid, utc_trial, 1, "Task_Stim", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    log_out(subid, utc_trial+4000, 1, "Task_Cue", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    
    my_loop = eval(loop_name) #variable for saving data
    stop_timer = None 
    stopped_time = 0
    lott_outcome = 0
    
    #random index for certain outcome position and response
    idx = random.randint(0,1) 
    sure_pos = pos[idx] 
    sure_resp = resp[idx]
    crdm_trial_img.setImage("images/" + crdm_img)
    crdm_trial_lott_top.setText(str("$"+str(crdm_lott_top)))
    crdm_trial_lott_bot.setText(str("$"+str(crdm_lott_bot)))
    crdm_trial_sure_amt.setPos(sure_pos)
    crdm_trial_sure_amt.setText(str("$"+str(crdm_sure_amt)))
    crdm_trial_resp.keys = []
    crdm_trial_resp.rt = []
    _crdm_trial_resp_allKeys = []
    # keep track of which components have finished
    crdm_trialComponents = [crdm_trial_img, crdm_trial_lott_top, crdm_trial_lott_bot, crdm_trial_sure_amt, GRFX_fix, crdm_trial_cue, crdm_trial_resp]
    for thisComponent in crdm_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_trial" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from crdm_trial_py
        if len(crdm_trial_resp.keys) == 1: #Ss responded
            if stop_timer == None: 
                stop_timer = core.Clock() 
            else:
                if stop_timer.getTime() >= 0.5:
                    continueRoutine = False
        
        # *crdm_trial_img* updates
        if crdm_trial_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_img.frameNStart = frameN  # exact frame index
            crdm_trial_img.tStart = t  # local t and not account for scr refresh
            crdm_trial_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_trial_img.started')
            crdm_trial_img.setAutoDraw(True)
        if crdm_trial_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_img.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_img.tStop = t  # not accounting for scr refresh
                crdm_trial_img.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_trial_img.stopped')
                crdm_trial_img.setAutoDraw(False)
        
        # *crdm_trial_lott_top* updates
        if crdm_trial_lott_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_lott_top.frameNStart = frameN  # exact frame index
            crdm_trial_lott_top.tStart = t  # local t and not account for scr refresh
            crdm_trial_lott_top.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_lott_top, 'tStartRefresh')  # time at next scr refresh
            crdm_trial_lott_top.setAutoDraw(True)
        if crdm_trial_lott_top.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_lott_top.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_lott_top.tStop = t  # not accounting for scr refresh
                crdm_trial_lott_top.frameNStop = frameN  # exact frame index
                crdm_trial_lott_top.setAutoDraw(False)
        
        # *crdm_trial_lott_bot* updates
        if crdm_trial_lott_bot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_lott_bot.frameNStart = frameN  # exact frame index
            crdm_trial_lott_bot.tStart = t  # local t and not account for scr refresh
            crdm_trial_lott_bot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_lott_bot, 'tStartRefresh')  # time at next scr refresh
            crdm_trial_lott_bot.setAutoDraw(True)
        if crdm_trial_lott_bot.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_lott_bot.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_lott_bot.tStop = t  # not accounting for scr refresh
                crdm_trial_lott_bot.frameNStop = frameN  # exact frame index
                crdm_trial_lott_bot.setAutoDraw(False)
        
        # *crdm_trial_sure_amt* updates
        if crdm_trial_sure_amt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_sure_amt.frameNStart = frameN  # exact frame index
            crdm_trial_sure_amt.tStart = t  # local t and not account for scr refresh
            crdm_trial_sure_amt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_sure_amt, 'tStartRefresh')  # time at next scr refresh
            crdm_trial_sure_amt.setAutoDraw(True)
        if crdm_trial_sure_amt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_sure_amt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_sure_amt.tStop = t  # not accounting for scr refresh
                crdm_trial_sure_amt.frameNStop = frameN  # exact frame index
                crdm_trial_sure_amt.setAutoDraw(False)
        
        # *GRFX_fix* updates
        if GRFX_fix.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            GRFX_fix.frameNStart = frameN  # exact frame index
            GRFX_fix.tStart = t  # local t and not account for scr refresh
            GRFX_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GRFX_fix, 'tStartRefresh')  # time at next scr refresh
            GRFX_fix.setAutoDraw(True)
        if GRFX_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GRFX_fix.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                GRFX_fix.tStop = t  # not accounting for scr refresh
                GRFX_fix.frameNStop = frameN  # exact frame index
                GRFX_fix.setAutoDraw(False)
        
        # *crdm_trial_cue* updates
        if crdm_trial_cue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_cue.frameNStart = frameN  # exact frame index
            crdm_trial_cue.tStart = t  # local t and not account for scr refresh
            crdm_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_cue, 'tStartRefresh')  # time at next scr refresh
            crdm_trial_cue.setAutoDraw(True)
        if crdm_trial_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_cue.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_cue.tStop = t  # not accounting for scr refresh
                crdm_trial_cue.frameNStop = frameN  # exact frame index
                crdm_trial_cue.setAutoDraw(False)
        
        # *crdm_trial_resp* updates
        waitOnFlip = False
        if crdm_trial_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_resp.frameNStart = frameN  # exact frame index
            crdm_trial_resp.tStart = t  # local t and not account for scr refresh
            crdm_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_resp, 'tStartRefresh')  # time at next scr refresh
            crdm_trial_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_trial_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_trial_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trial_resp.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trial_resp.tStop = t  # not accounting for scr refresh
                crdm_trial_resp.frameNStop = frameN  # exact frame index
                crdm_trial_resp.status = FINISHED
        if crdm_trial_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_trial_resp.getKeys(keyList=["4", "5"], waitRelease=False)
            _crdm_trial_resp_allKeys.extend(theseKeys)
            if len(_crdm_trial_resp_allKeys):
                crdm_trial_resp.keys = _crdm_trial_resp_allKeys[0].name  # just the first key pressed
                crdm_trial_resp.rt = _crdm_trial_resp_allKeys[0].rt
                # was this correct?
                if (crdm_trial_resp.keys == str(sure_resp)) or (crdm_trial_resp.keys == sure_resp):
                    crdm_trial_resp.corr = 1
                else:
                    crdm_trial_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_trial" ---
    for thisComponent in crdm_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from crdm_trial_py
    utc_resp = int((datetime.utcnow() - epoch).total_seconds()*1000) #output log variable for Ss response time
    
    key = crdm_trial_resp.keys #variable for feedback routine
    sure_key = crdm_trial_resp.corr #1 if certain $ selected
    my_loop.addData("crdm_trial_type", "task")
    
    
    #delta time is remaining time excluding rt
    if type(crdm_trial_resp.rt) is list or crdm_trial_resp.rt >= 2 - 0.5: 
        delta_time = 0
    else:
        delta_time = max(0, 2 - (crdm_trial_resp.rt + stopped_time))
    
    if len(key) == 1: #response received from Ss
        if sure_key == 1: #certain option
            #-1 is placeholder for lott_outcome
            log_out(subid, utc_resp, 1, "Task_Resp-Sure", 1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
            earnings.append(("sure", crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, -1, crdm_win_side, crdm_domain))
            my_loop.addData("crdm_choice", 0)
            my_loop.addData("crdm_choice2", "sure")
            my_loop.addData("crdm_lott", "")
            my_loop.addData("crdm_lott2", "")
        else: #lottery option
            log_out(subid, utc_resp, 1, "Task_Resp-Lott", 2, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
            #probability from bag parameters
            lott_outcome = random.choices([0,1], weights=[100-int(crdm_lott_p), int(crdm_lott_p)])[0] 
            #record Ss choice
            my_loop.addData("crdm_choice", 1)
            my_loop.addData("crdm_choice2", "lott")
    
            if lott_outcome == 1: #winning lottery
                my_loop.addData("crdm_lott", 1)
                my_loop.addData("crdm_lott2", "win")
                if crdm_domain == "gain": #gain domain trial
                    if int(crdm_lott_top) != 0: #top side is winner (non-0 means some money was gained)
                        earnings.append(("lott", crdm_lott_top, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain)) 
                    else: #bottom side is winner
                        earnings.append(("lott", crdm_lott_bot, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain))
                else: #loss domain trial
                    if int(crdm_lott_top) == 0: #top side is winner (0 means no money is lost)
                        earnings.append(("lott", crdm_lott_top, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain)) 
                    else: #bottom side is winner
                        earnings.append(("lott", crdm_lott_bot, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain))
            else: #losing lottery
                my_loop.addData("crdm_lott", 0)
                my_loop.addData("crdm_lott2", "lose") 
                earnings.append(("lott", 0, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain)) 
    else: #no response received from Ss
        log_out(subid, utc_resp, 1, "Task_NonResp", 0, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    # check responses
    if crdm_trial_resp.keys in ['', [], None]:  # No response was made
        crdm_trial_resp.keys = None
        # was no response the correct answer?!
        if str(sure_resp).lower() == 'none':
           crdm_trial_resp.corr = 1;  # correct non-response
        else:
           crdm_trial_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for crdm_trials (TrialHandler)
    crdm_trials.addData('crdm_trial_resp.keys',crdm_trial_resp.keys)
    crdm_trials.addData('crdm_trial_resp.corr', crdm_trial_resp.corr)
    if crdm_trial_resp.keys != None:  # we had a response
        crdm_trials.addData('crdm_trial_resp.rt', crdm_trial_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "crdm_feedback" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_feedback_py
    utc_fb = int((datetime.utcnow() - epoch).total_seconds()*1000)
    
    #Ss did not respond
    if len(key) == 0: 
        crdm_msg = "No Response"
        log_out(subid, utc_fb, 1, "Task_FB-NonResp", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    
        #Ss chose sure $5
    elif sure_key: 
        crdm_msg = "You chose: CERTAIN $" + str(crdm_sure_amt)
        log_out(subid, utc_fb, 1, "Task_FB-Sure", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    
        #Ss chose lottery
    else: 
        crdm_msg = "You chose: LOTTERY"
        log_out(subid, utc_fb, 1, "Task_FB-Lott", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    
    crdm_feedback_txt.setText(crdm_msg)
    # keep track of which components have finished
    crdm_feedbackComponents = [crdm_feedback_txt]
    for thisComponent in crdm_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_feedback" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_feedback_txt* updates
        if crdm_feedback_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_feedback_txt.frameNStart = frameN  # exact frame index
            crdm_feedback_txt.tStart = t  # local t and not account for scr refresh
            crdm_feedback_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_feedback_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_feedback_txt.setAutoDraw(True)
        if crdm_feedback_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_feedback_txt.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                crdm_feedback_txt.tStop = t  # not accounting for scr refresh
                crdm_feedback_txt.frameNStop = frameN  # exact frame index
                crdm_feedback_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_feedback" ---
    for thisComponent in crdm_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "crdm_conf" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_conf_py
    utc_conf = int((datetime.utcnow() - epoch).total_seconds()*1000)
    conf_key = []
    
    if len(key) == 0: #Ss did not respond
        continueRoutine = False
        log_out(subid, utc_conf, 1, "Conf-NoStim", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    else:
        log_out(subid, utc_conf, 1, "Conf_Stim", -1, -1, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    
    #set default gray for all four response boxes
    conf1_color = [0, 0, 0] 
    conf2_color = [0, 0, 0]
    conf3_color = [0, 0, 0]
    conf4_color = [0, 0, 0]
    crdm_conf_resp.keys = []
    crdm_conf_resp.rt = []
    _crdm_conf_resp_allKeys = []
    # keep track of which components have finished
    crdm_confComponents = [crdm_conf_txt, crdm_conf1, crdm_conf1_txt, crdm_conf2, crdm_conf2_txt, crdm_conf3, crdm_conf3_txt, crdm_conf4, crdm_conf4_txt, crdm_conf_resp]
    for thisComponent in crdm_confComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_conf" ---
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from crdm_conf_py
        conf_key = crdm_conf_resp.keys
        if len(conf_key) == 1: #Ss responded
            conf_key = confkey_map[conf_key[-1]]
            utc_confresp = int((datetime.utcnow() - epoch).total_seconds()*1000)
            if conf_key == "1": #not at all confident
                #change box color to indicate selection
                conf1_color = "darkgray" 
                conf2_color = [0,0,0]
                conf3_color = [0,0,0]
                conf4_color = [0,0,0]
            elif conf_key == "2": #less confident
                conf1_color = [0,0,0]
                conf2_color = "darkgray"
                conf3_color = [0,0,0]
                conf4_color = [0,0,0]
            elif conf_key == "3": #somewhat confident
                conf1_color = [0,0,0]
                conf2_color = [0,0,0]
                conf3_color = "darkgray"
                conf4_color = [0,0,0]
            elif conf_key == "4": #very confident
                conf1_color = [0,0,0]
                conf2_color = [0,0,0]
                conf3_color = [0,0,0]
                conf4_color = "darkgray"
        
        # *crdm_conf_txt* updates
        if crdm_conf_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf_txt.frameNStart = frameN  # exact frame index
            crdm_conf_txt.tStart = t  # local t and not account for scr refresh
            crdm_conf_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_conf_txt.setAutoDraw(True)
        if crdm_conf_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf_txt.tStop = t  # not accounting for scr refresh
                crdm_conf_txt.frameNStop = frameN  # exact frame index
                crdm_conf_txt.setAutoDraw(False)
        
        # *crdm_conf1* updates
        if crdm_conf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf1.frameNStart = frameN  # exact frame index
            crdm_conf1.tStart = t  # local t and not account for scr refresh
            crdm_conf1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf1, 'tStartRefresh')  # time at next scr refresh
            crdm_conf1.setAutoDraw(True)
        if crdm_conf1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf1.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf1.tStop = t  # not accounting for scr refresh
                crdm_conf1.frameNStop = frameN  # exact frame index
                crdm_conf1.setAutoDraw(False)
        if crdm_conf1.status == STARTED:  # only update if drawing
            crdm_conf1.setFillColor(conf1_color, log=False)
        
        # *crdm_conf1_txt* updates
        if crdm_conf1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf1_txt.frameNStart = frameN  # exact frame index
            crdm_conf1_txt.tStart = t  # local t and not account for scr refresh
            crdm_conf1_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf1_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_conf1_txt.setAutoDraw(True)
        if crdm_conf1_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf1_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf1_txt.tStop = t  # not accounting for scr refresh
                crdm_conf1_txt.frameNStop = frameN  # exact frame index
                crdm_conf1_txt.setAutoDraw(False)
        
        # *crdm_conf2* updates
        if crdm_conf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf2.frameNStart = frameN  # exact frame index
            crdm_conf2.tStart = t  # local t and not account for scr refresh
            crdm_conf2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf2, 'tStartRefresh')  # time at next scr refresh
            crdm_conf2.setAutoDraw(True)
        if crdm_conf2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf2.tStop = t  # not accounting for scr refresh
                crdm_conf2.frameNStop = frameN  # exact frame index
                crdm_conf2.setAutoDraw(False)
        if crdm_conf2.status == STARTED:  # only update if drawing
            crdm_conf2.setFillColor(conf2_color, log=False)
        
        # *crdm_conf2_txt* updates
        if crdm_conf2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf2_txt.frameNStart = frameN  # exact frame index
            crdm_conf2_txt.tStart = t  # local t and not account for scr refresh
            crdm_conf2_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf2_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_conf2_txt.setAutoDraw(True)
        if crdm_conf2_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf2_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf2_txt.tStop = t  # not accounting for scr refresh
                crdm_conf2_txt.frameNStop = frameN  # exact frame index
                crdm_conf2_txt.setAutoDraw(False)
        
        # *crdm_conf3* updates
        if crdm_conf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf3.frameNStart = frameN  # exact frame index
            crdm_conf3.tStart = t  # local t and not account for scr refresh
            crdm_conf3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf3, 'tStartRefresh')  # time at next scr refresh
            crdm_conf3.setAutoDraw(True)
        if crdm_conf3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf3.tStop = t  # not accounting for scr refresh
                crdm_conf3.frameNStop = frameN  # exact frame index
                crdm_conf3.setAutoDraw(False)
        if crdm_conf3.status == STARTED:  # only update if drawing
            crdm_conf3.setFillColor(conf3_color, log=False)
        
        # *crdm_conf3_txt* updates
        if crdm_conf3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf3_txt.frameNStart = frameN  # exact frame index
            crdm_conf3_txt.tStart = t  # local t and not account for scr refresh
            crdm_conf3_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf3_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_conf3_txt.setAutoDraw(True)
        if crdm_conf3_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf3_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf3_txt.tStop = t  # not accounting for scr refresh
                crdm_conf3_txt.frameNStop = frameN  # exact frame index
                crdm_conf3_txt.setAutoDraw(False)
        
        # *crdm_conf4* updates
        if crdm_conf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf4.frameNStart = frameN  # exact frame index
            crdm_conf4.tStart = t  # local t and not account for scr refresh
            crdm_conf4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf4, 'tStartRefresh')  # time at next scr refresh
            crdm_conf4.setAutoDraw(True)
        if crdm_conf4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf4.tStop = t  # not accounting for scr refresh
                crdm_conf4.frameNStop = frameN  # exact frame index
                crdm_conf4.setAutoDraw(False)
        if crdm_conf4.status == STARTED:  # only update if drawing
            crdm_conf4.setFillColor(conf4_color, log=False)
        
        # *crdm_conf4_txt* updates
        if crdm_conf4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf4_txt.frameNStart = frameN  # exact frame index
            crdm_conf4_txt.tStart = t  # local t and not account for scr refresh
            crdm_conf4_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf4_txt, 'tStartRefresh')  # time at next scr refresh
            crdm_conf4_txt.setAutoDraw(True)
        if crdm_conf4_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf4_txt.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf4_txt.tStop = t  # not accounting for scr refresh
                crdm_conf4_txt.frameNStop = frameN  # exact frame index
                crdm_conf4_txt.setAutoDraw(False)
        
        # *crdm_conf_resp* updates
        waitOnFlip = False
        if crdm_conf_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_conf_resp.frameNStart = frameN  # exact frame index
            crdm_conf_resp.tStart = t  # local t and not account for scr refresh
            crdm_conf_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_conf_resp, 'tStartRefresh')  # time at next scr refresh
            crdm_conf_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_conf_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_conf_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_conf_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_conf_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                crdm_conf_resp.tStop = t  # not accounting for scr refresh
                crdm_conf_resp.frameNStop = frameN  # exact frame index
                crdm_conf_resp.status = FINISHED
        if crdm_conf_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_conf_resp.getKeys(keyList=['2', '3', 'j', 'k'], waitRelease=False)
            _crdm_conf_resp_allKeys.extend(theseKeys)
            if len(_crdm_conf_resp_allKeys):
                crdm_conf_resp.keys = _crdm_conf_resp_allKeys[-1].name  # just the last key pressed
                crdm_conf_resp.rt = _crdm_conf_resp_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_confComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_conf" ---
    for thisComponent in crdm_confComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from crdm_conf_py
    if len(conf_key) == 1:
        if type(conf_key) == list:
            if conf_key[-1] in ["1", "2", "3", "4"]:
                log_out(subid, utc_confresp, 1, "Conf_Resp", -1, "{}".format(conf_key), crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
                conf_resps.append(conf_key)
        else:
            if conf_key in ["1", "2", "3", "4"]:
                log_out(subid, utc_confresp, 1, "Conf_Resp", -1, "{}".format(conf_key), crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
                conf_resps.append(conf_key)
    elif crdm_trial_resp.keys:
        utc_confresp = int((datetime.utcnow() - epoch).total_seconds()*1000)
        log_out(subid, utc_confresp, 1, "Conf_NonResp", -1, 0, crdm_domain, crdm_img.split(".")[0], crdm_lott_top, crdm_lott_bot, crdm_trials.thisTrialN+1)
    # check responses
    if crdm_conf_resp.keys in ['', [], None]:  # No response was made
        crdm_conf_resp.keys = None
    crdm_trials.addData('crdm_conf_resp.keys',crdm_conf_resp.keys)
    if crdm_conf_resp.keys != None:  # we had a response
        crdm_trials.addData('crdm_conf_resp.rt', crdm_conf_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "crdm_trials_iti" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_trials_iti1_py
    utc_iti = int((datetime.utcnow() - epoch).total_seconds()*1000) #output log variable for ITI
    
    iti_time = iti_list[my_loop.thisIndex] + delta_time #variable ITI for non-practice trials
    
    if crdm_trials.thisTrialN == 99: #final trial (number of trials - 1)
        continueRoutine = False #don't present ITI fixation
    else: #not final trial
        log_out(subid, utc_iti, 1, "Rand_ITIFix", -1, -1, "xxxx", "xxxxxxxxx", -1, -1, crdm_trials.thisTrialN+2)
    # keep track of which components have finished
    crdm_trials_itiComponents = [crdm_trials_iti1_poly]
    for thisComponent in crdm_trials_itiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "crdm_trials_iti" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_trials_iti1_poly* updates
        if crdm_trials_iti1_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trials_iti1_poly.frameNStart = frameN  # exact frame index
            crdm_trials_iti1_poly.tStart = t  # local t and not account for scr refresh
            crdm_trials_iti1_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trials_iti1_poly, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_trials_iti1_poly.started')
            crdm_trials_iti1_poly.setAutoDraw(True)
        if crdm_trials_iti1_poly.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_trials_iti1_poly.tStartRefresh + iti_time-frameTolerance:
                # keep track of stop time/frame for later
                crdm_trials_iti1_poly.tStop = t  # not accounting for scr refresh
                crdm_trials_iti1_poly.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_trials_iti1_poly.stopped')
                crdm_trials_iti1_poly.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_trials_itiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_trials_iti" ---
    for thisComponent in crdm_trials_itiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from crdm_trials_iti1_py
    my_loop.addData("crdm_delta_time", delta_time) #record delta time
    my_loop.addData("crdm_iti_time", iti_time) #record iti time
    # the Routine "crdm_trials_iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'crdm_trials'


# --- Prepare to start Routine "crdm_bonus" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from crdm_bonus_py
#indexing examples
#certain chosen - ("sure", 5, crdm_img, crdm_lott_top, crdm_lott_bot, -1, crdm_win_side, crdm_domain)
#lotto chosen, win top - ("lott", crdm_lott_top, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain))
#lotto chosen, win bottom - ("lott", crdm_lott_bot, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain)
#lotto chosen, lose - ("lott", 0, crdm_img, crdm_lott_top, crdm_lott_bot, lott_outcome, crdm_win_side, crdm_domain)

earnings_text = ""
idx = int(random.random() * len(earnings)) #random selection of bonus trial
choice, money, trial_img, top, bottom, outcome, winning_side, domain = earnings[idx]
my_loop.addData("bonus_choice", choice) #record bonus trial choice

red_win = False
if "red" in trial_img: #red wins in non-ambiguous trial
    red_win = True
else: #blue wins or ambiguous red trial
    if "ambig" in trial_img: #ambiguous trial
        if winning_side == "top": #red wins
            red_win = True
            
#text for bonus payment screen
if choice == "cert": ##Ss chose certain $5
    earnings_text = "In the randomly selected trial, you chose: \n \n A CERTAIN $" + str(money)
else: ##Ss chose lottery
    earnings_text = "In the randomly selected trial, you chose: \n \n PLAY THE LOTTERY! \n \n You will now draw a chip from the lottery bag with these possible values. \n \n Good luck!"
crdm_bonus_img.setImage("images/" + trial_img)
crdm_bonus_box.setText(earnings_text)
crdm_bonus_lott_top.setText(str("$"+str(crdm_lott_top)))
crdm_bonus_lott_bot.setText(str("$"+str(crdm_lott_bot)))
crdm_bonus_resp.keys = []
crdm_bonus_resp.rt = []
_crdm_bonus_resp_allKeys = []
# keep track of which components have finished
crdm_bonusComponents = [crdm_bonus_img, crdm_bonus_thanks_txt, crdm_bonus_box, crdm_bonus_lott_top, crdm_bonus_lott_bot, crdm_bonus_space_txt, crdm_bonus_resp]
for thisComponent in crdm_bonusComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "crdm_bonus" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *crdm_bonus_img* updates
    if crdm_bonus_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_img.frameNStart = frameN  # exact frame index
        crdm_bonus_img.tStart = t  # local t and not account for scr refresh
        crdm_bonus_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_img, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_img.setAutoDraw(True)
    
    # *crdm_bonus_thanks_txt* updates
    if crdm_bonus_thanks_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_thanks_txt.frameNStart = frameN  # exact frame index
        crdm_bonus_thanks_txt.tStart = t  # local t and not account for scr refresh
        crdm_bonus_thanks_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_thanks_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_thanks_txt.setAutoDraw(True)
    
    # *crdm_bonus_box* updates
    if crdm_bonus_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_box.frameNStart = frameN  # exact frame index
        crdm_bonus_box.tStart = t  # local t and not account for scr refresh
        crdm_bonus_box.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_box, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_box.setAutoDraw(True)
    
    # *crdm_bonus_lott_top* updates
    if crdm_bonus_lott_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_lott_top.frameNStart = frameN  # exact frame index
        crdm_bonus_lott_top.tStart = t  # local t and not account for scr refresh
        crdm_bonus_lott_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_lott_top, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_lott_top.setAutoDraw(True)
    
    # *crdm_bonus_lott_bot* updates
    if crdm_bonus_lott_bot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_lott_bot.frameNStart = frameN  # exact frame index
        crdm_bonus_lott_bot.tStart = t  # local t and not account for scr refresh
        crdm_bonus_lott_bot.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_lott_bot, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_lott_bot.setAutoDraw(True)
    
    # *crdm_bonus_space_txt* updates
    if crdm_bonus_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_space_txt.frameNStart = frameN  # exact frame index
        crdm_bonus_space_txt.tStart = t  # local t and not account for scr refresh
        crdm_bonus_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_space_txt, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_space_txt.setAutoDraw(True)
    
    # *crdm_bonus_resp* updates
    waitOnFlip = False
    if crdm_bonus_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        crdm_bonus_resp.frameNStart = frameN  # exact frame index
        crdm_bonus_resp.tStart = t  # local t and not account for scr refresh
        crdm_bonus_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(crdm_bonus_resp, 'tStartRefresh')  # time at next scr refresh
        crdm_bonus_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(crdm_bonus_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(crdm_bonus_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if crdm_bonus_resp.status == STARTED and not waitOnFlip:
        theseKeys = crdm_bonus_resp.getKeys(keyList=['space'], waitRelease=False)
        _crdm_bonus_resp_allKeys.extend(theseKeys)
        if len(_crdm_bonus_resp_allKeys):
            crdm_bonus_resp.keys = _crdm_bonus_resp_allKeys[-1].name  # just the last key pressed
            crdm_bonus_resp.rt = _crdm_bonus_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in crdm_bonusComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "crdm_bonus" ---
for thisComponent in crdm_bonusComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "crdm_bonus" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
