#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on August 19, 2024, at 11:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.2.2')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from crdm_instr1_PY
###code written by Mandy Renfro (2024)###
import random
earnings = []

##Current Designs Boxes
confkey_map = {"7": "1", 
               "6": "2", 
               "1": "3", 
               "2": "4", 
               None: None}
painkey_map = {"9": "1", 
               "8": "2", 
               "7": "3", 
               "6": "4", 
               "1": "5", 
               "2": "6", 
               "3": "7", 
               "4": "8", 
               None: None}

##Cedrus Boxes
#confkey_map = {"2": "1", "3": "2", "j": "3", "k": "4", None: None} #for Cedrus box code mapping
#painkey_map = {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "j": "6", "k": "7", "l": "8", None: None}
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'CCB_crdm'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/sub-%s/sub-%s_ses-crdm_task' % (expInfo['participant'], expInfo['participant'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='Z:\\data\\SDDM\\code\\task\\CCB-CRDM\\CCB_crdm.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1920, 1080], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='event')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='Pyglet')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "crdm_instr1" ---
    crdm_instr1_title_txt = visual.TextStim(win=win, name='crdm_instr1_title_txt',
        text='* Risk & Ambiguity Task *',
        font='Arial Rounded MT Bold',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    crdm_instr1_txt = visual.TextStim(win=win, name='crdm_instr1_txt',
        text='In this decision making task, you will be asked to make economic choices between: \n\n\n- Gaining a certain smaller amount \nOR\n- Playing a lottery for the chance to win a larger amount',
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
        font='Arial Rounded MT Bold',
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
        font='Arial Rounded MT Bold',
        pos=(-0.2, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_instr3_txt = visual.TextStim(win=win, name='crdm_instr3_txt',
        text='Given information about the number of blue and red chips in the bag, you can decide whether you would prefer a certain smaller amount or if you would rather play for a chance to win a larger amount.\n\nIn this example, you have a 75% chance of pulling a blue chip and winning $20. Conversely, you have a 25% chance of pulling a red chip and receiving $0. \n\nThe value for each color will change from bag to bag. Read the $ amounts above the red and below the blue to know the value of each chip color. ',
        font='Arial',
        pos=(-0.2, 0), height=0.035, wrapWidth=None, ori=0.0, 
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
        font='Arial Rounded MT Bold',
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
        text='When the green circle appears in the center of the screen, use the BLUE buttons on the L and R response pads to indicate your choice as shown below:',
        font='Arial',
        pos=(0, 0.35), height=0.04, wrapWidth=1.35, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_instr6_ex1_L_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_ex1_L_img', 
        image='images/rb_left.jpg', mask=None, anchor='center',
        ori=90.0, pos=(-0.555, -0.25), size=(0.1, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    crdm_instr6_ex1_R_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_ex1_R_img', 
        image='images/rb_right.jpg', mask=None, anchor='center',
        ori=270.0, pos=(-0.29, -0.25), size=(0.1, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    crdm_instr6_ex2_L_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_ex2_L_img', 
        image='images/rb_left.jpg', mask=None, anchor='center',
        ori=90.0, pos=(0.29, -0.25), size=(0.1, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    crdm_instr6_ex2_R_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_ex2_R_img', 
        image='images/rb_right.jpg', mask=None, anchor='center',
        ori=270.0, pos=(0.555, -0.25), size=(0.1, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    crdm_instr6_box1 = visual.Rect(
        win=win, name='crdm_instr6_box1',
        width=(0.51, 0.26)[0], height=(0.51, 0.26)[1],
        ori=0.0, pos=(-0.35, 0.05), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-5.0, interpolate=True)
    crdm_instr6_box2 = visual.Rect(
        win=win, name='crdm_instr6_box2',
        width=(0.51, 0.26)[0], height=(0.51, 0.26)[1],
        ori=0.0, pos=(0.35, 0.05), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
        opacity=None, depth=-6.0, interpolate=True)
    crdm_instr6_choice1_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_choice1_img', 
        image='images/choice_example1.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.35, 0.05), size=(0.5, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    crdm_instr6_choice2_img = visual.ImageStim(
        win=win,
        name='crdm_instr6_choice2_img', 
        image='images/choice_example2.png', mask=None, anchor='center',
        ori=0.0, pos=(0.35, 0.05), size=(0.5, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    crdm_instr6_ex1_txt = visual.TextStim(win=win, name='crdm_instr6_ex1_txt',
        text='Example #1',
        font='Arial',
        pos=(-0.35, 0.225), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    crdm_instr6_ex2_txt = visual.TextStim(win=win, name='crdm_instr6_ex2_txt',
        text='Example #2',
        font='Arial',
        pos=(0.35, 0.225), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    crdm_instr6_ex1_arrow1 = visual.ShapeStim(
        win=win, name='crdm_instr6_ex1_arrow1', vertices='arrow',
        size=(0.025, 0.08),
        ori=0.0, pos=(-0.495, -0.15), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    crdm_instr6_ex1_arrow2 = visual.ShapeStim(
        win=win, name='crdm_instr6_ex1_arrow2', vertices='arrow',
        size=(0.025, 0.08),
        ori=0.0, pos=(-0.35, -0.15), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-12.0, interpolate=True)
    crdm_instr6_ex2_arrow1 = visual.ShapeStim(
        win=win, name='crdm_instr6_ex2_arrow1', vertices='arrow',
        size=(0.025, 0.08),
        ori=0.0, pos=(0.35, -0.15), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-13.0, interpolate=True)
    crdm_instr6_ex2_arrow2 = visual.ShapeStim(
        win=win, name='crdm_instr6_ex2_arrow2', vertices='arrow',
        size=(0.025, 0.08),
        ori=0.0, pos=(0.495, -0.15), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-14.0, interpolate=True)
    crdm_instr6_space_txt = visual.TextStim(win=win, name='crdm_instr6_space_txt',
        text='Press SPACE to continue.',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_instr6_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_instr7" ---
    crdm_instr7_txt = visual.TextStim(win=win, name='crdm_instr7_txt',
        text='After each choice, you will be asked to rate your choice confidence. \n"Not at all confident" means you couldn\'t decide which option you preferred and chose at random, while "Very confident" indicates total certainty in your choice. \nPress the buttons on the response pads as shown below to indicate your choice:\n\n\n\n\n\n\n',
        font='Arial',
        pos=(0, 0.1), height=0.04, wrapWidth=1.45, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_instr7_conf1 = visual.Rect(
        win=win, name='crdm_instr7_conf1',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(-0.6, -0.1), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-1.0, interpolate=True)
    crdm_instr7_conf1_txt = visual.TextStim(win=win, name='crdm_instr7_conf1_txt',
        text='Not at all\nconfident\n',
        font='Arial',
        pos=(-0.6, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    crdm_instr7_conf1_but = visual.ShapeStim(
        win=win, name='crdm_instr7_conf1_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(-0.6, -0.2), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-3.0, interpolate=True)
    crdm_instr7_conf1_L3 = visual.TextStim(win=win, name='crdm_instr7_conf1_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.6, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    crdm_instr7_conf2 = visual.Rect(
        win=win, name='crdm_instr7_conf2',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(-0.2, -0.1), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    crdm_instr7_conf2_txt = visual.TextStim(win=win, name='crdm_instr7_conf2_txt',
        text='Less\nconfident\n',
        font='Arial',
        pos=(-0.2, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    crdm_instr7_conf2_but = visual.ShapeStim(
        win=win, name='crdm_instr7_conf2_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(-0.2, -0.2), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-7.0, interpolate=True)
    crdm_instr7_conf2_L4 = visual.TextStim(win=win, name='crdm_instr7_conf2_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.2, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    crdm_instr7_conf3 = visual.Rect(
        win=win, name='crdm_instr7_conf3',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.2, -0.1), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-9.0, interpolate=True)
    crdm_instr7_conf3_txt = visual.TextStim(win=win, name='crdm_instr7_conf3_txt',
        text='Somewhat\nconfident\n',
        font='Arial',
        pos=(0.2, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    crdm_instr7_conf3_but = visual.ShapeStim(
        win=win, name='crdm_instr7_conf3_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(0.2, -0.2), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-11.0, interpolate=True)
    crdm_instr7_conf3_R1 = visual.TextStim(win=win, name='crdm_instr7_conf3_R1',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.2, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    crdm_instr7_conf4 = visual.Rect(
        win=win, name='crdm_instr7_conf4',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.6, -0.1), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    crdm_instr7_conf4_txt = visual.TextStim(win=win, name='crdm_instr7_conf4_txt',
        text='Very\nconfident\n',
        font='Arial',
        pos=(0.6, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    crdm_instr7_conf4_but = visual.ShapeStim(
        win=win, name='crdm_instr7_conf4_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(0.6, -0.2), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-15.0, interpolate=True)
    crdm_instr7_conf4_R2 = visual.TextStim(win=win, name='crdm_instr7_conf4_R2',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.6, -0.2), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    crdm_instr7_space_txt = visual.TextStim(win=win, name='crdm_instr7_space_txt',
        text='Press SPACE to continue.',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_instr7_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_instr8" ---
    crdm_instr8_txt = visual.TextStim(win=win, name='crdm_instr8_txt',
        text='The final part of each trial will ask you to rate the pain you felt during the initial value choice.  1 means you felt warmth, but not pain. 2 means you felt the slightest pain. 8 means you felt the most pain you are willing to tolerate. If you felt nothing at all, do not respond during the pain prompt.\n\nUse the response pads as shown below to indicate your rating:',
        font='Arial',
        pos=(0, 0.25), height=0.04, wrapWidth=1.4, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_instr8_arrow = visual.ShapeStim(
        win=win, name='crdm_instr8_arrow', vertices='arrow',units='norm', 
        size=(0.075, 0.2),
        ori=180.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    crdm_instr8_zero = visual.TextStim(win=win, name='crdm_instr8_zero',
        text='0',
        font='Arial Rounded MT Bold',
        pos=(0, -0.075), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    crdm_instr8_pain_scale = visual.ImageStim(
        win=win,
        name='crdm_instr8_pain_scale', units='norm', 
        image='images/pain_scale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.45), size=(1.22, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    crdm_instr8_but1 = visual.ShapeStim(
        win=win, name='crdm_instr8_but1',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-4.0, interpolate=True)
    crdm_instr8_but2 = visual.ShapeStim(
        win=win, name='crdm_instr8_but2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-5.0, interpolate=True)
    crdm_instr_but3 = visual.ShapeStim(
        win=win, name='crdm_instr_but3',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-6.0, interpolate=True)
    crdm_instr8_but4 = visual.ShapeStim(
        win=win, name='crdm_instr8_but4',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-7.0, interpolate=True)
    crdm_instr8_but5 = visual.ShapeStim(
        win=win, name='crdm_instr8_but5',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-8.0, interpolate=True)
    crdm_instr8_but6 = visual.ShapeStim(
        win=win, name='crdm_instr8_but6',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-9.0, interpolate=True)
    crdm_instr8_but7 = visual.ShapeStim(
        win=win, name='crdm_instr8_but7',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-10.0, interpolate=True)
    crdm_instr8_but8 = visual.ShapeStim(
        win=win, name='crdm_instr8_but8',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-11.0, interpolate=True)
    crdm_instr8_L1 = visual.TextStim(win=win, name='crdm_instr8_L1',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    crdm_instr8_L2 = visual.TextStim(win=win, name='crdm_instr8_L2',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    crdm_instr8_L3 = visual.TextStim(win=win, name='crdm_instr8_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    crdm_instr8_L4 = visual.TextStim(win=win, name='crdm_instr8_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_instr8_R5 = visual.TextStim(win=win, name='crdm_instr8_R5',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    crdm_instr8_R6 = visual.TextStim(win=win, name='crdm_instr8_R6',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_instr8_R7 = visual.TextStim(win=win, name='crdm_instr8_R7',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    crdm_instr8_R8 = visual.TextStim(win=win, name='crdm_instr8_R8',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-19.0);
    crdm_instr8_no = visual.TextStim(win=win, name='crdm_instr8_no',
        text='\nNo \nPain',
        font='Arial',
        pos=(-0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-20.0);
    crdm_instr8_low = visual.TextStim(win=win, name='crdm_instr8_low',
        text='\nLow \nPain',
        font='Arial',
        pos=(-0.38, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-21.0);
    crdm_instr8_high = visual.TextStim(win=win, name='crdm_instr8_high',
        text='\nHigh \nPain',
        font='Arial',
        pos=(0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-22.0);
    crdm_instr8_space_txt = visual.TextStim(win=win, name='crdm_instr8_space_txt',
        text='Press SPACE to begin.',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-23.0);
    crdm_instr8_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pract_instr" ---
    crdm_pract_instr_name_txt = visual.TextStim(win=win, name='crdm_pract_instr_name_txt',
        text='* Risk & Ambiguity Task *',
        font='Arial Rounded MT Bold',
        pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_pract_instr_txt = visual.TextStim(win=win, name='crdm_pract_instr_txt',
        text="Let's practice!\n\nWhen the green circle appears, indicate your decision between the certain and lottery options. Next, you will be asked to rate your confidence. Finally, please rate the level of pain you received during your monterary choice. During these practice trials, you will receive no heat stimulation. \n\nPlease be sure to answer all prompts or the trial will be considered incomplete. ",
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
    crdm_pract_instr_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pract_init_fix" ---
    crdm_pract_init_fix_poly = visual.ShapeStim(
        win=win, name='crdm_pract_init_fix_poly', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "crdm_pract_trial" ---
    # Run 'Begin Experiment' code from crdm_pract_trial_PY
    #position of certain amount option
    sure_pos = [] 
    sure_resp = []
    crdm_msg = ""
    
    #stimuli positions and respective responses
    #left/right screen locations
    pos = [[-0.5, 0], [0.5, 0]] 
    #6 = left, 1 = right
    resp = ["6", "1"] 
    crdm_pract_trial_img = visual.ImageStim(
        win=win,
        name='crdm_pract_trial_img', 
        image='default.png', mask=None, anchor='center',
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
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.5294, 0.4039, -0.1137], fillColor=[-0.5294, 0.4039, -0.1137],
        opacity=None, depth=-6.0, interpolate=True)
    crdm_pract_trial_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pract_feedback" ---
    crdm_pract_fb_txt = visual.TextStim(win=win, name='crdm_pract_fb_txt',
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
        text='Not at all\nconfident\n',
        font='Arial',
        pos=(-0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    crdm_pract_conf1_but = visual.ShapeStim(
        win=win, name='crdm_pract_conf1_but',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.6, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-4.0, interpolate=True)
    crdm_pract_conf1_L3 = visual.TextStim(win=win, name='crdm_pract_conf1_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.6, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    crdm_pract_conf2 = visual.Rect(
        win=win, name='crdm_pract_conf2',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(-0.2, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    crdm_pract_conf2_txt = visual.TextStim(win=win, name='crdm_pract_conf2_txt',
        text='Less\nconfident\n',
        font='Arial',
        pos=(-0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    crdm_pract_conf2_but = visual.ShapeStim(
        win=win, name='crdm_pract_conf2_but',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.2, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-8.0, interpolate=True)
    crdm_pract_conf2_L4 = visual.TextStim(win=win, name='crdm_pract_conf2_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.2, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    crdm_pract_conf3 = visual.Rect(
        win=win, name='crdm_pract_conf3',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.2, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-10.0, interpolate=True)
    crdm_pract_conf3_txt = visual.TextStim(win=win, name='crdm_pract_conf3_txt',
        text='Somewhat\nconfident\n',
        font='Arial',
        pos=(0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    crdm_pract_conf3_but = visual.ShapeStim(
        win=win, name='crdm_pract_conf3_but',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.2, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-12.0, interpolate=True)
    crdm_pract_conf3_R1 = visual.TextStim(win=win, name='crdm_pract_conf3_R1',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.2, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    crdm_pract_conf4 = visual.Rect(
        win=win, name='crdm_pract_conf4',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.6, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-14.0, interpolate=True)
    crdm_pract_conf4_txt = visual.TextStim(win=win, name='crdm_pract_conf4_txt',
        text='Very\nconfident\n',
        font='Arial',
        pos=(0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_pract_conf4_but = visual.ShapeStim(
        win=win, name='crdm_pract_conf4_but',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.6, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-16.0, interpolate=True)
    crdm_pract_conf4_R2 = visual.TextStim(win=win, name='crdm_pract_conf4_R2',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.6, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_pract_conf_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pract_pain_rating" ---
    # Run 'Begin Experiment' code from crdm_pract_pain_PY
    arrow_choice = [0, 0] 
    crdm_pract_pain_prompt = visual.TextStim(win=win, name='crdm_pract_pain_prompt',
        text='How intense was the pain you felt?',
        font='Arial',
        units='norm', pos=(0, 0.2), height=0.125, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    crdm_pract_pain_rating_arrow = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_arrow', vertices='arrow',units='norm', 
        size=(0.075, 0.2),
        ori=180.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    crdm_pract_pain_rating_zero = visual.TextStim(win=win, name='crdm_pract_pain_rating_zero',
        text='0',
        font='Arial Rounded MT Bold',
        pos=(0, -0.075), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    crdm_pract_pain_scale = visual.ImageStim(
        win=win,
        name='crdm_pract_pain_scale', units='norm', 
        image='images/pain_scale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.45), size=(1.22, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    crdm_pract_pain_rating_but1 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but1',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-5.0, interpolate=True)
    crdm_pract_pain_rating_but2 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-6.0, interpolate=True)
    crdm_pract_pain_rating_but3 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but3',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-7.0, interpolate=True)
    crdm_pract_pain_rating_but4 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but4',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-8.0, interpolate=True)
    crdm_pract_pain_rating_but5 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but5',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-9.0, interpolate=True)
    crdm_pract_pain_rating_but6 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but6',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-10.0, interpolate=True)
    crdm_pract_pain_rating_but7 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but7',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-11.0, interpolate=True)
    crdm_pract_pain_rating_but8 = visual.ShapeStim(
        win=win, name='crdm_pract_pain_rating_but8',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-12.0, interpolate=True)
    crdm_pract_pain_rating_L1 = visual.TextStim(win=win, name='crdm_pract_pain_rating_L1',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    crdm_pract_pain_rating_L2 = visual.TextStim(win=win, name='crdm_pract_pain_rating_L2',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    crdm_pract_pain_rating_L3 = visual.TextStim(win=win, name='crdm_pract_pain_rating_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_pract_pain_rating_L4 = visual.TextStim(win=win, name='crdm_pract_pain_rating_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    crdm_pract_pain_rating_R5 = visual.TextStim(win=win, name='crdm_pract_pain_rating_R5',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_pract_pain_rating_R6 = visual.TextStim(win=win, name='crdm_pract_pain_rating_R6',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    crdm_pract_pain_rating_R7 = visual.TextStim(win=win, name='crdm_pract_pain_rating_R7',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-19.0);
    crdm_pract_pain_rating_R8 = visual.TextStim(win=win, name='crdm_pract_pain_rating_R8',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-20.0);
    crdm_pract_pain_rating_no = visual.TextStim(win=win, name='crdm_pract_pain_rating_no',
        text='\nNo \nPain',
        font='Arial',
        pos=(-0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-21.0);
    crdm_pract_pain_rating_low = visual.TextStim(win=win, name='crdm_pract_pain_rating_low',
        text='\nLow \nPain',
        font='Arial',
        pos=(-0.38, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-22.0);
    crdm_pract_pain_rating_high = visual.TextStim(win=win, name='crdm_pract_pain_rating_high',
        text='\nHigh \nPain',
        font='Arial',
        pos=(0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-23.0);
    crdm_pract_pain_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pract_iti" ---
    crdm_pract_iti1_poly = visual.ShapeStim(
        win=win, name='crdm_pract_iti1_poly', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "crdm_trial_instr" ---
    crdm_trial_instr_title_txt = visual.TextStim(win=win, name='crdm_trial_instr_title_txt',
        text='* Risk & Ambiguity Task *',
        font='Arial',
        pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
        color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    crdm_trial_instr_txt = visual.TextStim(win=win, name='crdm_trial_instr_txt',
        text='Now that you have practiced, the actual task will begin. For all remaining trials, there is the chance you may receive some level of heat stimulation.\n\nMake your choice between the certain outcome and lottery as soon as you see the green circle. You will have 4 seconds to consider and 3 seconds to respond. You will then have an additional 6 seconds to rate your choice confidence. And finally, 6 seconds to rate the level of pain you felt during your monetary choice.\n\nBetween trials, when you see a white cross appears, please focus your attention on the center of the screen. The next trial will begin soon.',
        font='Arial',
        pos=(0, -0.05), height=0.04, wrapWidth=1.25, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    crdm_trial_instr_space_txt = visual.TextStim(win=win, name='crdm_trial_instr_space_txt',
        text='Press SPACE to begin.',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    crdm_trial_instr_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_run_setter" ---
    
    # --- Initialize components for Routine "crdm_init_fix" ---
    crdm_init_fix_poly = visual.ShapeStim(
        win=win, name='crdm_init_fix_poly', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "crdm_trial" ---
    # Run 'Begin Experiment' code from crdm_trial_PY
    delta_time = 0 ##used in variable ITI
    sure_pos = [] ##position of certain amount option
    sure_resp = []
    crdm_msg = ""
    
    ##stimuli positions and respective responses
    pos = [[-0.5, 0], [0.5, 0]] ##left/right screen locations
    resp = ["6", "1"] ##6 = left, 1 = right
    crdm_trial_img = visual.ImageStim(
        win=win,
        name='crdm_trial_img', 
        image='default.png', mask=None, anchor='center',
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
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.5294, 0.4039, -0.1137], fillColor=[-0.5294, 0.4039, -0.1137],
        opacity=None, depth=-6.0, interpolate=True)
    crdm_trial_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_feedback" ---
    crdm_fb_img = visual.ImageStim(
        win=win,
        name='crdm_fb_img', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(2, 1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
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
        text='Not at all\nconfident\n\nLEFT\n',
        font='Arial',
        pos=(-0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    crdm_conf1_but = visual.ShapeStim(
        win=win, name='crdm_conf1_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(-0.6, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-4.0, interpolate=True)
    crdm_conf1_L3 = visual.TextStim(win=win, name='crdm_conf1_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.6, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    crdm_conf2 = visual.Rect(
        win=win, name='crdm_conf2',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(-0.2, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    crdm_conf2_txt = visual.TextStim(win=win, name='crdm_conf2_txt',
        text='Less\nconfident\n\nLEFT\n',
        font='Arial',
        pos=(-0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    crdm_conf2_but = visual.ShapeStim(
        win=win, name='crdm_conf2_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(-0.2, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-8.0, interpolate=True)
    crdm_conf2_L4 = visual.TextStim(win=win, name='crdm_conf2_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.2, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    crdm_conf3 = visual.Rect(
        win=win, name='crdm_conf3',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.2, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-10.0, interpolate=True)
    crdm_conf3_txt = visual.TextStim(win=win, name='crdm_conf3_txt',
        text='Somewhat\nconfident\n\nRIGHT\n',
        font='Arial',
        pos=(0.2, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    crdm_conf3_but = visual.ShapeStim(
        win=win, name='crdm_conf3_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(0.2, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-12.0, interpolate=True)
    crdm_conf3_R1 = visual.TextStim(win=win, name='crdm_conf3_R1',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.2, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    crdm_conf4 = visual.Rect(
        win=win, name='crdm_conf4',
        width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
        ori=0.0, pos=(0.6, -0.3), anchor='center',
        lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-14.0, interpolate=True)
    crdm_conf4_txt = visual.TextStim(win=win, name='crdm_conf4_txt',
        text='Very\nconfident\n\nRIGHT\n',
        font='Arial',
        pos=(0.6, -0.3), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_conf4_but = visual.ShapeStim(
        win=win, name='crdm_conf4_but',
        size=(0.04, 0.04), vertices='circle',
        ori=0.0, pos=(0.6, -0.4), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-16.0, interpolate=True)
    crdm_conf4_R2 = visual.TextStim(win=win, name='crdm_conf4_R2',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.6, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_conf_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_pain_rating" ---
    crdm_pain_prompt = visual.TextStim(win=win, name='crdm_pain_prompt',
        text='How intense was the pain you felt?',
        font='Arial',
        units='norm', pos=(0, 0.2), height=0.125, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    crdm_pain_rating_arrow = visual.ShapeStim(
        win=win, name='crdm_pain_rating_arrow', vertices='arrow',units='norm', 
        size=(0.075, 0.2),
        ori=180.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    crdm_pain_rating_zero = visual.TextStim(win=win, name='crdm_pain_rating_zero',
        text='0',
        font='Arial Rounded MT Bold',
        pos=(0, -0.075), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    crdm_pain_rating_scale = visual.ImageStim(
        win=win,
        name='crdm_pain_rating_scale', units='norm', 
        image='images/pain_scale.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.45), size=(1.22, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    crdm_pain_rating_but1 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but1',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-5.0, interpolate=True)
    crdm_pain_rating_but2 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but2',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-6.0, interpolate=True)
    crdm_pain_rating_but3 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but3',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-7.0, interpolate=True)
    crdm_pain_rating_but4 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but4',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(-0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-8.0, interpolate=True)
    crdm_pain_rating_but5 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but5',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.0775, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 0.0902],
        opacity=None, depth=-9.0, interpolate=True)
    crdm_pain_rating_but6 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but6',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.23, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7098, 0.2941, -0.7490], fillColor=[0.7098, 0.2941, -0.7490],
        opacity=None, depth=-10.0, interpolate=True)
    crdm_pain_rating_but7 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but7',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.3825, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-0.7333, 0.0902, -0.7333], fillColor=[-0.7333, 0.0902, -0.7333],
        opacity=None, depth=-11.0, interpolate=True)
    crdm_pain_rating_but8 = visual.ShapeStim(
        win=win, name='crdm_pain_rating_but8',
        size=(0.05, 0.05), vertices='circle',
        ori=0.0, pos=(0.535, -0.32), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[0.7255, -0.8431, -0.5294], fillColor=[0.7255, -0.8431, -0.5294],
        opacity=None, depth=-12.0, interpolate=True)
    crdm_pain_rating_L1 = visual.TextStim(win=win, name='crdm_pain_rating_L1',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-13.0);
    crdm_pain_rating_L2 = visual.TextStim(win=win, name='crdm_pain_rating_L2',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    crdm_pain_rating_L3 = visual.TextStim(win=win, name='crdm_pain_rating_L3',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    crdm_pain_rating_L4 = visual.TextStim(win=win, name='crdm_pain_rating_L4',
        text='L',
        font='Arial Rounded MT Bold',
        pos=(-0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    crdm_pain_rating_R5 = visual.TextStim(win=win, name='crdm_pain_rating_R5',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.0775, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-17.0);
    crdm_pain_rating_R6 = visual.TextStim(win=win, name='crdm_pain_rating_R6',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.23, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    crdm_pain_rating_R7 = visual.TextStim(win=win, name='crdm_pain_rating_R7',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.3825, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-19.0);
    crdm_pain_rating_R8 = visual.TextStim(win=win, name='crdm_pain_rating_R8',
        text='R',
        font='Arial Rounded MT Bold',
        pos=(0.535, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-20.0);
    crdm_pain_rating_no = visual.TextStim(win=win, name='crdm_pain_rating_no',
        text='\nNo \nPain',
        font='Arial',
        pos=(-0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-21.0);
    crdm_pain_rating_low = visual.TextStim(win=win, name='crdm_pain_rating_low',
        text='\nLow \nPain',
        font='Arial',
        pos=(-0.38, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-22.0);
    crdm_pain_rating_high = visual.TextStim(win=win, name='crdm_pain_rating_high',
        text='\nHigh \nPain',
        font='Arial',
        pos=(0.535, -0.37), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-23.0);
    crdm_pain_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "crdm_trial_iti" ---
    crdm_trial_iti1_poly = visual.ShapeStim(
        win=win, name='crdm_trial_iti1_poly', vertices='cross',
        size=(0.05, 0.05),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "crdm_run_break" ---
    cpdm_run_break_txt = visual.TextStim(win=win, name='cpdm_run_break_txt',
        text='',
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=1.25, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    cpdm_run_break_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "ETTSA_end" ---
    
    # --- Initialize components for Routine "crdm_bonus" ---
    crdm_bonus_img_2 = visual.ImageStim(
        win=win,
        name='crdm_bonus_img_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.6, -0.1), size=(0.3, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    crdm_bonus_thanks_txt_2 = visual.TextStim(win=win, name='crdm_bonus_thanks_txt_2',
        text='Thank you for participating in the Risk & Ambiguity Task!',
        font='Arial',
        pos=(0, 0.35), height=0.05, wrapWidth=1.5, ori=0.0, 
        color=[0.7098, 0.2941, -0.7490], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    crdm_bonus_sure_txt = visual.TextStim(win=win, name='crdm_bonus_sure_txt',
        text='',
        font='Ariel',
        pos=(0.4, -0.075), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    crdm_bonus_box = visual.TextStim(win=win, name='crdm_bonus_box',
        text='',
        font='Arial',
        pos=(-0.20, -0.05), height=0.04, wrapWidth=1.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    crdm_bonus_lott_top_2 = visual.TextStim(win=win, name='crdm_bonus_lott_top_2',
        text='',
        font='Arial',
        pos=(0.6, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    crdm_bonus_lott_bot_2 = visual.TextStim(win=win, name='crdm_bonus_lott_bot_2',
        text='',
        font='Arial',
        pos=(0.6, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    crdm_bonus_space_txt_2 = visual.TextStim(win=win, name='crdm_bonus_space_txt_2',
        text='Press SPACE to end',
        font='Arial',
        pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    crdm_bonus_resp_2 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "crdm_instr1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from crdm_instr1_PY
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr1_title_txt* updates
        
        # if crdm_instr1_title_txt is starting this frame...
        if crdm_instr1_title_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr1_title_txt.frameNStart = frameN  # exact frame index
            crdm_instr1_title_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr1_title_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr1_title_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr1_title_txt.status = STARTED
            crdm_instr1_title_txt.setAutoDraw(True)
        
        # if crdm_instr1_title_txt is active this frame...
        if crdm_instr1_title_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr1_txt* updates
        
        # if crdm_instr1_txt is starting this frame...
        if crdm_instr1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr1_txt.frameNStart = frameN  # exact frame index
            crdm_instr1_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr1_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr1_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr1_txt.status = STARTED
            crdm_instr1_txt.setAutoDraw(True)
        
        # if crdm_instr1_txt is active this frame...
        if crdm_instr1_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr1_space_txt* updates
        
        # if crdm_instr1_space_txt is starting this frame...
        if crdm_instr1_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr1_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr1_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr1_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr1_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr1_space_txt.status = STARTED
            crdm_instr1_space_txt.setAutoDraw(True)
        
        # if crdm_instr1_space_txt is active this frame...
        if crdm_instr1_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr1_resp* updates
        waitOnFlip = False
        
        # if crdm_instr1_resp is starting this frame...
        if crdm_instr1_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr1_resp.frameNStart = frameN  # exact frame index
            crdm_instr1_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr1_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr1_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr1_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr1_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr1_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr1_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr1_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr1_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr1_resp_allKeys):
                crdm_instr1_resp.keys = _crdm_instr1_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr1_resp.rt = _crdm_instr1_resp_allKeys[-1].rt
                crdm_instr1_resp.duration = _crdm_instr1_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr2_lottname_txt* updates
        
        # if crdm_instr2_lottname_txt is starting this frame...
        if crdm_instr2_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_lottname_txt.frameNStart = frameN  # exact frame index
            crdm_instr2_lottname_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr2_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_lottname_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_lottname_txt.status = STARTED
            crdm_instr2_lottname_txt.setAutoDraw(True)
        
        # if crdm_instr2_lottname_txt is active this frame...
        if crdm_instr2_lottname_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_txt* updates
        
        # if crdm_instr2_txt is starting this frame...
        if crdm_instr2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_txt.frameNStart = frameN  # exact frame index
            crdm_instr2_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr2_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_txt.status = STARTED
            crdm_instr2_txt.setAutoDraw(True)
        
        # if crdm_instr2_txt is active this frame...
        if crdm_instr2_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_img* updates
        
        # if crdm_instr2_img is starting this frame...
        if crdm_instr2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_img.frameNStart = frameN  # exact frame index
            crdm_instr2_img.tStart = t  # local t and not account for scr refresh
            crdm_instr2_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_img.status = STARTED
            crdm_instr2_img.setAutoDraw(True)
        
        # if crdm_instr2_img is active this frame...
        if crdm_instr2_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_lott0_txt* updates
        
        # if crdm_instr2_lott0_txt is starting this frame...
        if crdm_instr2_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_lott0_txt.frameNStart = frameN  # exact frame index
            crdm_instr2_lott0_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr2_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_lott0_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_lott0_txt.status = STARTED
            crdm_instr2_lott0_txt.setAutoDraw(True)
        
        # if crdm_instr2_lott0_txt is active this frame...
        if crdm_instr2_lott0_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_lott20_txt* updates
        
        # if crdm_instr2_lott20_txt is starting this frame...
        if crdm_instr2_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_lott20_txt.frameNStart = frameN  # exact frame index
            crdm_instr2_lott20_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr2_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_lott20_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_lott20_txt.status = STARTED
            crdm_instr2_lott20_txt.setAutoDraw(True)
        
        # if crdm_instr2_lott20_txt is active this frame...
        if crdm_instr2_lott20_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_space_txt* updates
        
        # if crdm_instr2_space_txt is starting this frame...
        if crdm_instr2_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr2_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr2_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_space_txt.status = STARTED
            crdm_instr2_space_txt.setAutoDraw(True)
        
        # if crdm_instr2_space_txt is active this frame...
        if crdm_instr2_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr2_resp* updates
        waitOnFlip = False
        
        # if crdm_instr2_resp is starting this frame...
        if crdm_instr2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr2_resp.frameNStart = frameN  # exact frame index
            crdm_instr2_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr2_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr2_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr2_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr2_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr2_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr2_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr2_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr2_resp_allKeys):
                crdm_instr2_resp.keys = _crdm_instr2_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr2_resp.rt = _crdm_instr2_resp_allKeys[-1].rt
                crdm_instr2_resp.duration = _crdm_instr2_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr3_lottname_txt* updates
        
        # if crdm_instr3_lottname_txt is starting this frame...
        if crdm_instr3_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_lottname_txt.frameNStart = frameN  # exact frame index
            crdm_instr3_lottname_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr3_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_lottname_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_lottname_txt.status = STARTED
            crdm_instr3_lottname_txt.setAutoDraw(True)
        
        # if crdm_instr3_lottname_txt is active this frame...
        if crdm_instr3_lottname_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_txt* updates
        
        # if crdm_instr3_txt is starting this frame...
        if crdm_instr3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_txt.frameNStart = frameN  # exact frame index
            crdm_instr3_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr3_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_txt.status = STARTED
            crdm_instr3_txt.setAutoDraw(True)
        
        # if crdm_instr3_txt is active this frame...
        if crdm_instr3_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_img* updates
        
        # if crdm_instr3_img is starting this frame...
        if crdm_instr3_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_img.frameNStart = frameN  # exact frame index
            crdm_instr3_img.tStart = t  # local t and not account for scr refresh
            crdm_instr3_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_img.status = STARTED
            crdm_instr3_img.setAutoDraw(True)
        
        # if crdm_instr3_img is active this frame...
        if crdm_instr3_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_lott0_txt* updates
        
        # if crdm_instr3_lott0_txt is starting this frame...
        if crdm_instr3_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_lott0_txt.frameNStart = frameN  # exact frame index
            crdm_instr3_lott0_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr3_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_lott0_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_lott0_txt.status = STARTED
            crdm_instr3_lott0_txt.setAutoDraw(True)
        
        # if crdm_instr3_lott0_txt is active this frame...
        if crdm_instr3_lott0_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_lott20_txt* updates
        
        # if crdm_instr3_lott20_txt is starting this frame...
        if crdm_instr3_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_lott20_txt.frameNStart = frameN  # exact frame index
            crdm_instr3_lott20_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr3_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_lott20_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_lott20_txt.status = STARTED
            crdm_instr3_lott20_txt.setAutoDraw(True)
        
        # if crdm_instr3_lott20_txt is active this frame...
        if crdm_instr3_lott20_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_space_txt* updates
        
        # if crdm_instr3_space_txt is starting this frame...
        if crdm_instr3_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr3_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr3_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_space_txt.status = STARTED
            crdm_instr3_space_txt.setAutoDraw(True)
        
        # if crdm_instr3_space_txt is active this frame...
        if crdm_instr3_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr3_resp* updates
        waitOnFlip = False
        
        # if crdm_instr3_resp is starting this frame...
        if crdm_instr3_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr3_resp.frameNStart = frameN  # exact frame index
            crdm_instr3_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr3_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr3_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr3_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr3_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr3_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr3_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr3_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr3_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr3_resp_allKeys):
                crdm_instr3_resp.keys = _crdm_instr3_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr3_resp.rt = _crdm_instr3_resp_allKeys[-1].rt
                crdm_instr3_resp.duration = _crdm_instr3_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr4_lottname_txt* updates
        
        # if crdm_instr4_lottname_txt is starting this frame...
        if crdm_instr4_lottname_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_lottname_txt.frameNStart = frameN  # exact frame index
            crdm_instr4_lottname_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr4_lottname_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_lottname_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_lottname_txt.status = STARTED
            crdm_instr4_lottname_txt.setAutoDraw(True)
        
        # if crdm_instr4_lottname_txt is active this frame...
        if crdm_instr4_lottname_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_txt* updates
        
        # if crdm_instr4_txt is starting this frame...
        if crdm_instr4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_txt.frameNStart = frameN  # exact frame index
            crdm_instr4_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr4_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_txt.status = STARTED
            crdm_instr4_txt.setAutoDraw(True)
        
        # if crdm_instr4_txt is active this frame...
        if crdm_instr4_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_img* updates
        
        # if crdm_instr4_img is starting this frame...
        if crdm_instr4_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_img.frameNStart = frameN  # exact frame index
            crdm_instr4_img.tStart = t  # local t and not account for scr refresh
            crdm_instr4_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_img.status = STARTED
            crdm_instr4_img.setAutoDraw(True)
        
        # if crdm_instr4_img is active this frame...
        if crdm_instr4_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_lott0_txt* updates
        
        # if crdm_instr4_lott0_txt is starting this frame...
        if crdm_instr4_lott0_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_lott0_txt.frameNStart = frameN  # exact frame index
            crdm_instr4_lott0_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr4_lott0_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_lott0_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_lott0_txt.status = STARTED
            crdm_instr4_lott0_txt.setAutoDraw(True)
        
        # if crdm_instr4_lott0_txt is active this frame...
        if crdm_instr4_lott0_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_lott20_txt* updates
        
        # if crdm_instr4_lott20_txt is starting this frame...
        if crdm_instr4_lott20_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_lott20_txt.frameNStart = frameN  # exact frame index
            crdm_instr4_lott20_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr4_lott20_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_lott20_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_lott20_txt.status = STARTED
            crdm_instr4_lott20_txt.setAutoDraw(True)
        
        # if crdm_instr4_lott20_txt is active this frame...
        if crdm_instr4_lott20_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_space_txt* updates
        
        # if crdm_instr4_space_txt is starting this frame...
        if crdm_instr4_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr4_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr4_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_space_txt.status = STARTED
            crdm_instr4_space_txt.setAutoDraw(True)
        
        # if crdm_instr4_space_txt is active this frame...
        if crdm_instr4_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr4_resp* updates
        waitOnFlip = False
        
        # if crdm_instr4_resp is starting this frame...
        if crdm_instr4_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr4_resp.frameNStart = frameN  # exact frame index
            crdm_instr4_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr4_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr4_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr4_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr4_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr4_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr4_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr4_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr4_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr4_resp_allKeys):
                crdm_instr4_resp.keys = _crdm_instr4_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr4_resp.rt = _crdm_instr4_resp_allKeys[-1].rt
                crdm_instr4_resp.duration = _crdm_instr4_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr5_txt* updates
        
        # if crdm_instr5_txt is starting this frame...
        if crdm_instr5_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_txt.frameNStart = frameN  # exact frame index
            crdm_instr5_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr5_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_txt.status = STARTED
            crdm_instr5_txt.setAutoDraw(True)
        
        # if crdm_instr5_txt is active this frame...
        if crdm_instr5_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_img* updates
        
        # if crdm_instr5_img is starting this frame...
        if crdm_instr5_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_img.frameNStart = frameN  # exact frame index
            crdm_instr5_img.tStart = t  # local t and not account for scr refresh
            crdm_instr5_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_img.status = STARTED
            crdm_instr5_img.setAutoDraw(True)
        
        # if crdm_instr5_img is active this frame...
        if crdm_instr5_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_lott_top_txt* updates
        
        # if crdm_instr5_lott_top_txt is starting this frame...
        if crdm_instr5_lott_top_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_lott_top_txt.frameNStart = frameN  # exact frame index
            crdm_instr5_lott_top_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr5_lott_top_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_lott_top_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_lott_top_txt.status = STARTED
            crdm_instr5_lott_top_txt.setAutoDraw(True)
        
        # if crdm_instr5_lott_top_txt is active this frame...
        if crdm_instr5_lott_top_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_lott_bot_txt* updates
        
        # if crdm_instr5_lott_bot_txt is starting this frame...
        if crdm_instr5_lott_bot_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_lott_bot_txt.frameNStart = frameN  # exact frame index
            crdm_instr5_lott_bot_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr5_lott_bot_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_lott_bot_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_lott_bot_txt.status = STARTED
            crdm_instr5_lott_bot_txt.setAutoDraw(True)
        
        # if crdm_instr5_lott_bot_txt is active this frame...
        if crdm_instr5_lott_bot_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_sure_txt* updates
        
        # if crdm_instr5_sure_txt is starting this frame...
        if crdm_instr5_sure_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_sure_txt.frameNStart = frameN  # exact frame index
            crdm_instr5_sure_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr5_sure_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_sure_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_sure_txt.status = STARTED
            crdm_instr5_sure_txt.setAutoDraw(True)
        
        # if crdm_instr5_sure_txt is active this frame...
        if crdm_instr5_sure_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_space_txt* updates
        
        # if crdm_instr5_space_txt is starting this frame...
        if crdm_instr5_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr5_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr5_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_space_txt.status = STARTED
            crdm_instr5_space_txt.setAutoDraw(True)
        
        # if crdm_instr5_space_txt is active this frame...
        if crdm_instr5_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr5_resp* updates
        waitOnFlip = False
        
        # if crdm_instr5_resp is starting this frame...
        if crdm_instr5_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr5_resp.frameNStart = frameN  # exact frame index
            crdm_instr5_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr5_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr5_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr5_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr5_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr5_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr5_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr5_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr5_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr5_resp_allKeys):
                crdm_instr5_resp.keys = _crdm_instr5_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr5_resp.rt = _crdm_instr5_resp_allKeys[-1].rt
                crdm_instr5_resp.duration = _crdm_instr5_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    # update component parameters for each repeat
    crdm_instr6_resp.keys = []
    crdm_instr6_resp.rt = []
    _crdm_instr6_resp_allKeys = []
    # keep track of which components have finished
    crdm_instr6Components = [crdm_instr6_txt, crdm_instr6_ex1_L_img, crdm_instr6_ex1_R_img, crdm_instr6_ex2_L_img, crdm_instr6_ex2_R_img, crdm_instr6_box1, crdm_instr6_box2, crdm_instr6_choice1_img, crdm_instr6_choice2_img, crdm_instr6_ex1_txt, crdm_instr6_ex2_txt, crdm_instr6_ex1_arrow1, crdm_instr6_ex1_arrow2, crdm_instr6_ex2_arrow1, crdm_instr6_ex2_arrow2, crdm_instr6_space_txt, crdm_instr6_resp]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr6_txt* updates
        
        # if crdm_instr6_txt is starting this frame...
        if crdm_instr6_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_txt.frameNStart = frameN  # exact frame index
            crdm_instr6_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr6_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_txt.status = STARTED
            crdm_instr6_txt.setAutoDraw(True)
        
        # if crdm_instr6_txt is active this frame...
        if crdm_instr6_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex1_L_img* updates
        
        # if crdm_instr6_ex1_L_img is starting this frame...
        if crdm_instr6_ex1_L_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex1_L_img.frameNStart = frameN  # exact frame index
            crdm_instr6_ex1_L_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex1_L_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex1_L_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex1_L_img.status = STARTED
            crdm_instr6_ex1_L_img.setAutoDraw(True)
        
        # if crdm_instr6_ex1_L_img is active this frame...
        if crdm_instr6_ex1_L_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex1_R_img* updates
        
        # if crdm_instr6_ex1_R_img is starting this frame...
        if crdm_instr6_ex1_R_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex1_R_img.frameNStart = frameN  # exact frame index
            crdm_instr6_ex1_R_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex1_R_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex1_R_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex1_R_img.status = STARTED
            crdm_instr6_ex1_R_img.setAutoDraw(True)
        
        # if crdm_instr6_ex1_R_img is active this frame...
        if crdm_instr6_ex1_R_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex2_L_img* updates
        
        # if crdm_instr6_ex2_L_img is starting this frame...
        if crdm_instr6_ex2_L_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex2_L_img.frameNStart = frameN  # exact frame index
            crdm_instr6_ex2_L_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex2_L_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex2_L_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex2_L_img.status = STARTED
            crdm_instr6_ex2_L_img.setAutoDraw(True)
        
        # if crdm_instr6_ex2_L_img is active this frame...
        if crdm_instr6_ex2_L_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex2_R_img* updates
        
        # if crdm_instr6_ex2_R_img is starting this frame...
        if crdm_instr6_ex2_R_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex2_R_img.frameNStart = frameN  # exact frame index
            crdm_instr6_ex2_R_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex2_R_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex2_R_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex2_R_img.status = STARTED
            crdm_instr6_ex2_R_img.setAutoDraw(True)
        
        # if crdm_instr6_ex2_R_img is active this frame...
        if crdm_instr6_ex2_R_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_box1* updates
        
        # if crdm_instr6_box1 is starting this frame...
        if crdm_instr6_box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_box1.frameNStart = frameN  # exact frame index
            crdm_instr6_box1.tStart = t  # local t and not account for scr refresh
            crdm_instr6_box1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_box1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_box1.status = STARTED
            crdm_instr6_box1.setAutoDraw(True)
        
        # if crdm_instr6_box1 is active this frame...
        if crdm_instr6_box1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_box2* updates
        
        # if crdm_instr6_box2 is starting this frame...
        if crdm_instr6_box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_box2.frameNStart = frameN  # exact frame index
            crdm_instr6_box2.tStart = t  # local t and not account for scr refresh
            crdm_instr6_box2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_box2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_box2.status = STARTED
            crdm_instr6_box2.setAutoDraw(True)
        
        # if crdm_instr6_box2 is active this frame...
        if crdm_instr6_box2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_choice1_img* updates
        
        # if crdm_instr6_choice1_img is starting this frame...
        if crdm_instr6_choice1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_choice1_img.frameNStart = frameN  # exact frame index
            crdm_instr6_choice1_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_choice1_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_choice1_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_choice1_img.status = STARTED
            crdm_instr6_choice1_img.setAutoDraw(True)
        
        # if crdm_instr6_choice1_img is active this frame...
        if crdm_instr6_choice1_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_choice2_img* updates
        
        # if crdm_instr6_choice2_img is starting this frame...
        if crdm_instr6_choice2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_choice2_img.frameNStart = frameN  # exact frame index
            crdm_instr6_choice2_img.tStart = t  # local t and not account for scr refresh
            crdm_instr6_choice2_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_choice2_img, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_choice2_img.status = STARTED
            crdm_instr6_choice2_img.setAutoDraw(True)
        
        # if crdm_instr6_choice2_img is active this frame...
        if crdm_instr6_choice2_img.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex1_txt* updates
        
        # if crdm_instr6_ex1_txt is starting this frame...
        if crdm_instr6_ex1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex1_txt.frameNStart = frameN  # exact frame index
            crdm_instr6_ex1_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex1_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex1_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex1_txt.status = STARTED
            crdm_instr6_ex1_txt.setAutoDraw(True)
        
        # if crdm_instr6_ex1_txt is active this frame...
        if crdm_instr6_ex1_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex2_txt* updates
        
        # if crdm_instr6_ex2_txt is starting this frame...
        if crdm_instr6_ex2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex2_txt.frameNStart = frameN  # exact frame index
            crdm_instr6_ex2_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex2_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex2_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex2_txt.status = STARTED
            crdm_instr6_ex2_txt.setAutoDraw(True)
        
        # if crdm_instr6_ex2_txt is active this frame...
        if crdm_instr6_ex2_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex1_arrow1* updates
        
        # if crdm_instr6_ex1_arrow1 is starting this frame...
        if crdm_instr6_ex1_arrow1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex1_arrow1.frameNStart = frameN  # exact frame index
            crdm_instr6_ex1_arrow1.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex1_arrow1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex1_arrow1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex1_arrow1.status = STARTED
            crdm_instr6_ex1_arrow1.setAutoDraw(True)
        
        # if crdm_instr6_ex1_arrow1 is active this frame...
        if crdm_instr6_ex1_arrow1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex1_arrow2* updates
        
        # if crdm_instr6_ex1_arrow2 is starting this frame...
        if crdm_instr6_ex1_arrow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex1_arrow2.frameNStart = frameN  # exact frame index
            crdm_instr6_ex1_arrow2.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex1_arrow2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex1_arrow2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex1_arrow2.status = STARTED
            crdm_instr6_ex1_arrow2.setAutoDraw(True)
        
        # if crdm_instr6_ex1_arrow2 is active this frame...
        if crdm_instr6_ex1_arrow2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex2_arrow1* updates
        
        # if crdm_instr6_ex2_arrow1 is starting this frame...
        if crdm_instr6_ex2_arrow1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex2_arrow1.frameNStart = frameN  # exact frame index
            crdm_instr6_ex2_arrow1.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex2_arrow1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex2_arrow1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex2_arrow1.status = STARTED
            crdm_instr6_ex2_arrow1.setAutoDraw(True)
        
        # if crdm_instr6_ex2_arrow1 is active this frame...
        if crdm_instr6_ex2_arrow1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_ex2_arrow2* updates
        
        # if crdm_instr6_ex2_arrow2 is starting this frame...
        if crdm_instr6_ex2_arrow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_ex2_arrow2.frameNStart = frameN  # exact frame index
            crdm_instr6_ex2_arrow2.tStart = t  # local t and not account for scr refresh
            crdm_instr6_ex2_arrow2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_ex2_arrow2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_ex2_arrow2.status = STARTED
            crdm_instr6_ex2_arrow2.setAutoDraw(True)
        
        # if crdm_instr6_ex2_arrow2 is active this frame...
        if crdm_instr6_ex2_arrow2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_space_txt* updates
        
        # if crdm_instr6_space_txt is starting this frame...
        if crdm_instr6_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr6_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr6_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_space_txt.status = STARTED
            crdm_instr6_space_txt.setAutoDraw(True)
        
        # if crdm_instr6_space_txt is active this frame...
        if crdm_instr6_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr6_resp* updates
        waitOnFlip = False
        
        # if crdm_instr6_resp is starting this frame...
        if crdm_instr6_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr6_resp.frameNStart = frameN  # exact frame index
            crdm_instr6_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr6_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr6_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr6_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr6_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr6_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr6_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr6_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr6_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr6_resp_allKeys):
                crdm_instr6_resp.keys = _crdm_instr6_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr6_resp.rt = _crdm_instr6_resp_allKeys[-1].rt
                crdm_instr6_resp.duration = _crdm_instr6_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    # update component parameters for each repeat
    crdm_instr7_resp.keys = []
    crdm_instr7_resp.rt = []
    _crdm_instr7_resp_allKeys = []
    # keep track of which components have finished
    crdm_instr7Components = [crdm_instr7_txt, crdm_instr7_conf1, crdm_instr7_conf1_txt, crdm_instr7_conf1_but, crdm_instr7_conf1_L3, crdm_instr7_conf2, crdm_instr7_conf2_txt, crdm_instr7_conf2_but, crdm_instr7_conf2_L4, crdm_instr7_conf3, crdm_instr7_conf3_txt, crdm_instr7_conf3_but, crdm_instr7_conf3_R1, crdm_instr7_conf4, crdm_instr7_conf4_txt, crdm_instr7_conf4_but, crdm_instr7_conf4_R2, crdm_instr7_space_txt, crdm_instr7_resp]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr7_txt* updates
        
        # if crdm_instr7_txt is starting this frame...
        if crdm_instr7_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_txt.status = STARTED
            crdm_instr7_txt.setAutoDraw(True)
        
        # if crdm_instr7_txt is active this frame...
        if crdm_instr7_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf1* updates
        
        # if crdm_instr7_conf1 is starting this frame...
        if crdm_instr7_conf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf1.frameNStart = frameN  # exact frame index
            crdm_instr7_conf1.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf1.status = STARTED
            crdm_instr7_conf1.setAutoDraw(True)
        
        # if crdm_instr7_conf1 is active this frame...
        if crdm_instr7_conf1.status == STARTED:
            # update params
            crdm_instr7_conf1.setFillColor('', log=False)
        
        # *crdm_instr7_conf1_txt* updates
        
        # if crdm_instr7_conf1_txt is starting this frame...
        if crdm_instr7_conf1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf1_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_conf1_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf1_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf1_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf1_txt.status = STARTED
            crdm_instr7_conf1_txt.setAutoDraw(True)
        
        # if crdm_instr7_conf1_txt is active this frame...
        if crdm_instr7_conf1_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf1_but* updates
        
        # if crdm_instr7_conf1_but is starting this frame...
        if crdm_instr7_conf1_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf1_but.frameNStart = frameN  # exact frame index
            crdm_instr7_conf1_but.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf1_but.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf1_but, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf1_but.status = STARTED
            crdm_instr7_conf1_but.setAutoDraw(True)
        
        # if crdm_instr7_conf1_but is active this frame...
        if crdm_instr7_conf1_but.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf1_L3* updates
        
        # if crdm_instr7_conf1_L3 is starting this frame...
        if crdm_instr7_conf1_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf1_L3.frameNStart = frameN  # exact frame index
            crdm_instr7_conf1_L3.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf1_L3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf1_L3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_instr7_conf1_L3.started')
            # update status
            crdm_instr7_conf1_L3.status = STARTED
            crdm_instr7_conf1_L3.setAutoDraw(True)
        
        # if crdm_instr7_conf1_L3 is active this frame...
        if crdm_instr7_conf1_L3.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf2* updates
        
        # if crdm_instr7_conf2 is starting this frame...
        if crdm_instr7_conf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf2.frameNStart = frameN  # exact frame index
            crdm_instr7_conf2.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf2.status = STARTED
            crdm_instr7_conf2.setAutoDraw(True)
        
        # if crdm_instr7_conf2 is active this frame...
        if crdm_instr7_conf2.status == STARTED:
            # update params
            crdm_instr7_conf2.setFillColor('', log=False)
        
        # *crdm_instr7_conf2_txt* updates
        
        # if crdm_instr7_conf2_txt is starting this frame...
        if crdm_instr7_conf2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf2_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_conf2_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf2_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf2_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf2_txt.status = STARTED
            crdm_instr7_conf2_txt.setAutoDraw(True)
        
        # if crdm_instr7_conf2_txt is active this frame...
        if crdm_instr7_conf2_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf2_but* updates
        
        # if crdm_instr7_conf2_but is starting this frame...
        if crdm_instr7_conf2_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf2_but.frameNStart = frameN  # exact frame index
            crdm_instr7_conf2_but.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf2_but.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf2_but, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf2_but.status = STARTED
            crdm_instr7_conf2_but.setAutoDraw(True)
        
        # if crdm_instr7_conf2_but is active this frame...
        if crdm_instr7_conf2_but.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf2_L4* updates
        
        # if crdm_instr7_conf2_L4 is starting this frame...
        if crdm_instr7_conf2_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf2_L4.frameNStart = frameN  # exact frame index
            crdm_instr7_conf2_L4.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf2_L4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf2_L4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_instr7_conf2_L4.started')
            # update status
            crdm_instr7_conf2_L4.status = STARTED
            crdm_instr7_conf2_L4.setAutoDraw(True)
        
        # if crdm_instr7_conf2_L4 is active this frame...
        if crdm_instr7_conf2_L4.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf3* updates
        
        # if crdm_instr7_conf3 is starting this frame...
        if crdm_instr7_conf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf3.frameNStart = frameN  # exact frame index
            crdm_instr7_conf3.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf3, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf3.status = STARTED
            crdm_instr7_conf3.setAutoDraw(True)
        
        # if crdm_instr7_conf3 is active this frame...
        if crdm_instr7_conf3.status == STARTED:
            # update params
            crdm_instr7_conf3.setFillColor('', log=False)
        
        # *crdm_instr7_conf3_txt* updates
        
        # if crdm_instr7_conf3_txt is starting this frame...
        if crdm_instr7_conf3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf3_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_conf3_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf3_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf3_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf3_txt.status = STARTED
            crdm_instr7_conf3_txt.setAutoDraw(True)
        
        # if crdm_instr7_conf3_txt is active this frame...
        if crdm_instr7_conf3_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf3_but* updates
        
        # if crdm_instr7_conf3_but is starting this frame...
        if crdm_instr7_conf3_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf3_but.frameNStart = frameN  # exact frame index
            crdm_instr7_conf3_but.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf3_but.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf3_but, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf3_but.status = STARTED
            crdm_instr7_conf3_but.setAutoDraw(True)
        
        # if crdm_instr7_conf3_but is active this frame...
        if crdm_instr7_conf3_but.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf3_R1* updates
        
        # if crdm_instr7_conf3_R1 is starting this frame...
        if crdm_instr7_conf3_R1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf3_R1.frameNStart = frameN  # exact frame index
            crdm_instr7_conf3_R1.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf3_R1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf3_R1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_instr7_conf3_R1.started')
            # update status
            crdm_instr7_conf3_R1.status = STARTED
            crdm_instr7_conf3_R1.setAutoDraw(True)
        
        # if crdm_instr7_conf3_R1 is active this frame...
        if crdm_instr7_conf3_R1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf4* updates
        
        # if crdm_instr7_conf4 is starting this frame...
        if crdm_instr7_conf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf4.frameNStart = frameN  # exact frame index
            crdm_instr7_conf4.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf4, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf4.status = STARTED
            crdm_instr7_conf4.setAutoDraw(True)
        
        # if crdm_instr7_conf4 is active this frame...
        if crdm_instr7_conf4.status == STARTED:
            # update params
            crdm_instr7_conf4.setFillColor('', log=False)
        
        # *crdm_instr7_conf4_txt* updates
        
        # if crdm_instr7_conf4_txt is starting this frame...
        if crdm_instr7_conf4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf4_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_conf4_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf4_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf4_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf4_txt.status = STARTED
            crdm_instr7_conf4_txt.setAutoDraw(True)
        
        # if crdm_instr7_conf4_txt is active this frame...
        if crdm_instr7_conf4_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf4_but* updates
        
        # if crdm_instr7_conf4_but is starting this frame...
        if crdm_instr7_conf4_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf4_but.frameNStart = frameN  # exact frame index
            crdm_instr7_conf4_but.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf4_but.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf4_but, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_conf4_but.status = STARTED
            crdm_instr7_conf4_but.setAutoDraw(True)
        
        # if crdm_instr7_conf4_but is active this frame...
        if crdm_instr7_conf4_but.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_conf4_R2* updates
        
        # if crdm_instr7_conf4_R2 is starting this frame...
        if crdm_instr7_conf4_R2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_conf4_R2.frameNStart = frameN  # exact frame index
            crdm_instr7_conf4_R2.tStart = t  # local t and not account for scr refresh
            crdm_instr7_conf4_R2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_conf4_R2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'crdm_instr7_conf4_R2.started')
            # update status
            crdm_instr7_conf4_R2.status = STARTED
            crdm_instr7_conf4_R2.setAutoDraw(True)
        
        # if crdm_instr7_conf4_R2 is active this frame...
        if crdm_instr7_conf4_R2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_space_txt* updates
        
        # if crdm_instr7_space_txt is starting this frame...
        if crdm_instr7_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr7_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr7_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_space_txt.status = STARTED
            crdm_instr7_space_txt.setAutoDraw(True)
        
        # if crdm_instr7_space_txt is active this frame...
        if crdm_instr7_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr7_resp* updates
        waitOnFlip = False
        
        # if crdm_instr7_resp is starting this frame...
        if crdm_instr7_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr7_resp.frameNStart = frameN  # exact frame index
            crdm_instr7_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr7_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr7_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr7_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr7_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr7_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr7_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr7_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr7_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr7_resp_allKeys):
                crdm_instr7_resp.keys = _crdm_instr7_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr7_resp.rt = _crdm_instr7_resp_allKeys[-1].rt
                crdm_instr7_resp.duration = _crdm_instr7_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    
    # --- Prepare to start Routine "crdm_instr8" ---
    continueRoutine = True
    # update component parameters for each repeat
    crdm_instr8_resp.keys = []
    crdm_instr8_resp.rt = []
    _crdm_instr8_resp_allKeys = []
    # keep track of which components have finished
    crdm_instr8Components = [crdm_instr8_txt, crdm_instr8_arrow, crdm_instr8_zero, crdm_instr8_pain_scale, crdm_instr8_but1, crdm_instr8_but2, crdm_instr_but3, crdm_instr8_but4, crdm_instr8_but5, crdm_instr8_but6, crdm_instr8_but7, crdm_instr8_but8, crdm_instr8_L1, crdm_instr8_L2, crdm_instr8_L3, crdm_instr8_L4, crdm_instr8_R5, crdm_instr8_R6, crdm_instr8_R7, crdm_instr8_R8, crdm_instr8_no, crdm_instr8_low, crdm_instr8_high, crdm_instr8_space_txt, crdm_instr8_resp]
    for thisComponent in crdm_instr8Components:
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
    
    # --- Run Routine "crdm_instr8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_instr8_txt* updates
        
        # if crdm_instr8_txt is starting this frame...
        if crdm_instr8_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_txt.frameNStart = frameN  # exact frame index
            crdm_instr8_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr8_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_txt.status = STARTED
            crdm_instr8_txt.setAutoDraw(True)
        
        # if crdm_instr8_txt is active this frame...
        if crdm_instr8_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_arrow* updates
        
        # if crdm_instr8_arrow is starting this frame...
        if crdm_instr8_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_arrow.frameNStart = frameN  # exact frame index
            crdm_instr8_arrow.tStart = t  # local t and not account for scr refresh
            crdm_instr8_arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_arrow, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_arrow.status = STARTED
            crdm_instr8_arrow.setAutoDraw(True)
        
        # if crdm_instr8_arrow is active this frame...
        if crdm_instr8_arrow.status == STARTED:
            # update params
            crdm_instr8_arrow.setPos(arrow_choice, log=False)
        
        # *crdm_instr8_zero* updates
        
        # if crdm_instr8_zero is starting this frame...
        if crdm_instr8_zero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_zero.frameNStart = frameN  # exact frame index
            crdm_instr8_zero.tStart = t  # local t and not account for scr refresh
            crdm_instr8_zero.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_zero, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_zero.status = STARTED
            crdm_instr8_zero.setAutoDraw(True)
        
        # if crdm_instr8_zero is active this frame...
        if crdm_instr8_zero.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_pain_scale* updates
        
        # if crdm_instr8_pain_scale is starting this frame...
        if crdm_instr8_pain_scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_pain_scale.frameNStart = frameN  # exact frame index
            crdm_instr8_pain_scale.tStart = t  # local t and not account for scr refresh
            crdm_instr8_pain_scale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_pain_scale, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_pain_scale.status = STARTED
            crdm_instr8_pain_scale.setAutoDraw(True)
        
        # if crdm_instr8_pain_scale is active this frame...
        if crdm_instr8_pain_scale.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but1* updates
        
        # if crdm_instr8_but1 is starting this frame...
        if crdm_instr8_but1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but1.frameNStart = frameN  # exact frame index
            crdm_instr8_but1.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but1.status = STARTED
            crdm_instr8_but1.setAutoDraw(True)
        
        # if crdm_instr8_but1 is active this frame...
        if crdm_instr8_but1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but2* updates
        
        # if crdm_instr8_but2 is starting this frame...
        if crdm_instr8_but2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but2.frameNStart = frameN  # exact frame index
            crdm_instr8_but2.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but2.status = STARTED
            crdm_instr8_but2.setAutoDraw(True)
        
        # if crdm_instr8_but2 is active this frame...
        if crdm_instr8_but2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr_but3* updates
        
        # if crdm_instr_but3 is starting this frame...
        if crdm_instr_but3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr_but3.frameNStart = frameN  # exact frame index
            crdm_instr_but3.tStart = t  # local t and not account for scr refresh
            crdm_instr_but3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr_but3, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr_but3.status = STARTED
            crdm_instr_but3.setAutoDraw(True)
        
        # if crdm_instr_but3 is active this frame...
        if crdm_instr_but3.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but4* updates
        
        # if crdm_instr8_but4 is starting this frame...
        if crdm_instr8_but4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but4.frameNStart = frameN  # exact frame index
            crdm_instr8_but4.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but4, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but4.status = STARTED
            crdm_instr8_but4.setAutoDraw(True)
        
        # if crdm_instr8_but4 is active this frame...
        if crdm_instr8_but4.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but5* updates
        
        # if crdm_instr8_but5 is starting this frame...
        if crdm_instr8_but5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but5.frameNStart = frameN  # exact frame index
            crdm_instr8_but5.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but5, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but5.status = STARTED
            crdm_instr8_but5.setAutoDraw(True)
        
        # if crdm_instr8_but5 is active this frame...
        if crdm_instr8_but5.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but6* updates
        
        # if crdm_instr8_but6 is starting this frame...
        if crdm_instr8_but6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but6.frameNStart = frameN  # exact frame index
            crdm_instr8_but6.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but6, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but6.status = STARTED
            crdm_instr8_but6.setAutoDraw(True)
        
        # if crdm_instr8_but6 is active this frame...
        if crdm_instr8_but6.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but7* updates
        
        # if crdm_instr8_but7 is starting this frame...
        if crdm_instr8_but7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but7.frameNStart = frameN  # exact frame index
            crdm_instr8_but7.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but7, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but7.status = STARTED
            crdm_instr8_but7.setAutoDraw(True)
        
        # if crdm_instr8_but7 is active this frame...
        if crdm_instr8_but7.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_but8* updates
        
        # if crdm_instr8_but8 is starting this frame...
        if crdm_instr8_but8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_but8.frameNStart = frameN  # exact frame index
            crdm_instr8_but8.tStart = t  # local t and not account for scr refresh
            crdm_instr8_but8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_but8, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_but8.status = STARTED
            crdm_instr8_but8.setAutoDraw(True)
        
        # if crdm_instr8_but8 is active this frame...
        if crdm_instr8_but8.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_L1* updates
        
        # if crdm_instr8_L1 is starting this frame...
        if crdm_instr8_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_L1.frameNStart = frameN  # exact frame index
            crdm_instr8_L1.tStart = t  # local t and not account for scr refresh
            crdm_instr8_L1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_L1, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_L1.status = STARTED
            crdm_instr8_L1.setAutoDraw(True)
        
        # if crdm_instr8_L1 is active this frame...
        if crdm_instr8_L1.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_L2* updates
        
        # if crdm_instr8_L2 is starting this frame...
        if crdm_instr8_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_L2.frameNStart = frameN  # exact frame index
            crdm_instr8_L2.tStart = t  # local t and not account for scr refresh
            crdm_instr8_L2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_L2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_L2.status = STARTED
            crdm_instr8_L2.setAutoDraw(True)
        
        # if crdm_instr8_L2 is active this frame...
        if crdm_instr8_L2.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_L3* updates
        
        # if crdm_instr8_L3 is starting this frame...
        if crdm_instr8_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_L3.frameNStart = frameN  # exact frame index
            crdm_instr8_L3.tStart = t  # local t and not account for scr refresh
            crdm_instr8_L3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_L3, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_L3.status = STARTED
            crdm_instr8_L3.setAutoDraw(True)
        
        # if crdm_instr8_L3 is active this frame...
        if crdm_instr8_L3.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_L4* updates
        
        # if crdm_instr8_L4 is starting this frame...
        if crdm_instr8_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_L4.frameNStart = frameN  # exact frame index
            crdm_instr8_L4.tStart = t  # local t and not account for scr refresh
            crdm_instr8_L4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_L4, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_L4.status = STARTED
            crdm_instr8_L4.setAutoDraw(True)
        
        # if crdm_instr8_L4 is active this frame...
        if crdm_instr8_L4.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_R5* updates
        
        # if crdm_instr8_R5 is starting this frame...
        if crdm_instr8_R5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_R5.frameNStart = frameN  # exact frame index
            crdm_instr8_R5.tStart = t  # local t and not account for scr refresh
            crdm_instr8_R5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_R5, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_R5.status = STARTED
            crdm_instr8_R5.setAutoDraw(True)
        
        # if crdm_instr8_R5 is active this frame...
        if crdm_instr8_R5.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_R6* updates
        
        # if crdm_instr8_R6 is starting this frame...
        if crdm_instr8_R6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_R6.frameNStart = frameN  # exact frame index
            crdm_instr8_R6.tStart = t  # local t and not account for scr refresh
            crdm_instr8_R6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_R6, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_R6.status = STARTED
            crdm_instr8_R6.setAutoDraw(True)
        
        # if crdm_instr8_R6 is active this frame...
        if crdm_instr8_R6.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_R7* updates
        
        # if crdm_instr8_R7 is starting this frame...
        if crdm_instr8_R7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_R7.frameNStart = frameN  # exact frame index
            crdm_instr8_R7.tStart = t  # local t and not account for scr refresh
            crdm_instr8_R7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_R7, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_R7.status = STARTED
            crdm_instr8_R7.setAutoDraw(True)
        
        # if crdm_instr8_R7 is active this frame...
        if crdm_instr8_R7.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_R8* updates
        
        # if crdm_instr8_R8 is starting this frame...
        if crdm_instr8_R8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_R8.frameNStart = frameN  # exact frame index
            crdm_instr8_R8.tStart = t  # local t and not account for scr refresh
            crdm_instr8_R8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_R8, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_R8.status = STARTED
            crdm_instr8_R8.setAutoDraw(True)
        
        # if crdm_instr8_R8 is active this frame...
        if crdm_instr8_R8.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_no* updates
        
        # if crdm_instr8_no is starting this frame...
        if crdm_instr8_no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_no.frameNStart = frameN  # exact frame index
            crdm_instr8_no.tStart = t  # local t and not account for scr refresh
            crdm_instr8_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_no, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_no.status = STARTED
            crdm_instr8_no.setAutoDraw(True)
        
        # if crdm_instr8_no is active this frame...
        if crdm_instr8_no.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_low* updates
        
        # if crdm_instr8_low is starting this frame...
        if crdm_instr8_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_low.frameNStart = frameN  # exact frame index
            crdm_instr8_low.tStart = t  # local t and not account for scr refresh
            crdm_instr8_low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_low, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_low.status = STARTED
            crdm_instr8_low.setAutoDraw(True)
        
        # if crdm_instr8_low is active this frame...
        if crdm_instr8_low.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_high* updates
        
        # if crdm_instr8_high is starting this frame...
        if crdm_instr8_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_high.frameNStart = frameN  # exact frame index
            crdm_instr8_high.tStart = t  # local t and not account for scr refresh
            crdm_instr8_high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_high, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_high.status = STARTED
            crdm_instr8_high.setAutoDraw(True)
        
        # if crdm_instr8_high is active this frame...
        if crdm_instr8_high.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_space_txt* updates
        
        # if crdm_instr8_space_txt is starting this frame...
        if crdm_instr8_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_space_txt.frameNStart = frameN  # exact frame index
            crdm_instr8_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_instr8_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_space_txt.status = STARTED
            crdm_instr8_space_txt.setAutoDraw(True)
        
        # if crdm_instr8_space_txt is active this frame...
        if crdm_instr8_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_instr8_resp* updates
        waitOnFlip = False
        
        # if crdm_instr8_resp is starting this frame...
        if crdm_instr8_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_instr8_resp.frameNStart = frameN  # exact frame index
            crdm_instr8_resp.tStart = t  # local t and not account for scr refresh
            crdm_instr8_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_instr8_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_instr8_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_instr8_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_instr8_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_instr8_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_instr8_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_instr8_resp_allKeys.extend(theseKeys)
            if len(_crdm_instr8_resp_allKeys):
                crdm_instr8_resp.keys = _crdm_instr8_resp_allKeys[-1].name  # just the last key pressed
                crdm_instr8_resp.rt = _crdm_instr8_resp_allKeys[-1].rt
                crdm_instr8_resp.duration = _crdm_instr8_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in crdm_instr8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "crdm_instr8" ---
    for thisComponent in crdm_instr8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "crdm_instr8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "crdm_pract_instr" ---
    continueRoutine = True
    # update component parameters for each repeat
    crdm_pract_instr_resp.keys = []
    crdm_pract_instr_resp.rt = []
    _crdm_pract_instr_resp_allKeys = []
    # keep track of which components have finished
    crdm_pract_instrComponents = [crdm_pract_instr_name_txt, crdm_pract_instr_txt, crdm_pract_instr_space_txt, crdm_pract_instr_resp]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_pract_instr_name_txt* updates
        
        # if crdm_pract_instr_name_txt is starting this frame...
        if crdm_pract_instr_name_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_instr_name_txt.frameNStart = frameN  # exact frame index
            crdm_pract_instr_name_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_instr_name_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_instr_name_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_pract_instr_name_txt.status = STARTED
            crdm_pract_instr_name_txt.setAutoDraw(True)
        
        # if crdm_pract_instr_name_txt is active this frame...
        if crdm_pract_instr_name_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_pract_instr_txt* updates
        
        # if crdm_pract_instr_txt is starting this frame...
        if crdm_pract_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_instr_txt.frameNStart = frameN  # exact frame index
            crdm_pract_instr_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_instr_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_pract_instr_txt.status = STARTED
            crdm_pract_instr_txt.setAutoDraw(True)
        
        # if crdm_pract_instr_txt is active this frame...
        if crdm_pract_instr_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_pract_instr_space_txt* updates
        
        # if crdm_pract_instr_space_txt is starting this frame...
        if crdm_pract_instr_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_instr_space_txt.frameNStart = frameN  # exact frame index
            crdm_pract_instr_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_pract_instr_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_instr_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_pract_instr_space_txt.status = STARTED
            crdm_pract_instr_space_txt.setAutoDraw(True)
        
        # if crdm_pract_instr_space_txt is active this frame...
        if crdm_pract_instr_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_pract_instr_resp* updates
        waitOnFlip = False
        
        # if crdm_pract_instr_resp is starting this frame...
        if crdm_pract_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_instr_resp.frameNStart = frameN  # exact frame index
            crdm_pract_instr_resp.tStart = t  # local t and not account for scr refresh
            crdm_pract_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_instr_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_pract_instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_pract_instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_pract_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_pract_instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_pract_instr_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_pract_instr_resp_allKeys.extend(theseKeys)
            if len(_crdm_pract_instr_resp_allKeys):
                crdm_pract_instr_resp.keys = _crdm_pract_instr_resp_allKeys[-1].name  # just the last key pressed
                crdm_pract_instr_resp.rt = _crdm_pract_instr_resp_allKeys[-1].rt
                crdm_pract_instr_resp.duration = _crdm_pract_instr_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    # update component parameters for each repeat
    # keep track of which components have finished
    crdm_pract_init_fixComponents = [crdm_pract_init_fix_poly]
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
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_pract_init_fix_poly* updates
        
        # if crdm_pract_init_fix_poly is starting this frame...
        if crdm_pract_init_fix_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_pract_init_fix_poly.frameNStart = frameN  # exact frame index
            crdm_pract_init_fix_poly.tStart = t  # local t and not account for scr refresh
            crdm_pract_init_fix_poly.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_pract_init_fix_poly, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_pract_init_fix_poly.status = STARTED
            crdm_pract_init_fix_poly.setAutoDraw(True)
        
        # if crdm_pract_init_fix_poly is active this frame...
        if crdm_pract_init_fix_poly.status == STARTED:
            # update params
            pass
        
        # if crdm_pract_init_fix_poly is stopping this frame...
        if crdm_pract_init_fix_poly.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > crdm_pract_init_fix_poly.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                crdm_pract_init_fix_poly.tStop = t  # not accounting for scr refresh
                crdm_pract_init_fix_poly.frameNStop = frameN  # exact frame index
                # update status
                crdm_pract_init_fix_poly.status = FINISHED
                crdm_pract_init_fix_poly.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
        trialList=data.importConditions('crdm_practice.csv'),
        seed=None, name='crdm_pract_trials')
    thisExp.addLoop(crdm_pract_trials)  # add the loop to the experiment
    thisCrdm_pract_trial = crdm_pract_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCrdm_pract_trial.rgb)
    if thisCrdm_pract_trial != None:
        for paramName in thisCrdm_pract_trial:
            globals()[paramName] = thisCrdm_pract_trial[paramName]
    
    for thisCrdm_pract_trial in crdm_pract_trials:
        currentLoop = crdm_pract_trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisCrdm_pract_trial.rgb)
        if thisCrdm_pract_trial != None:
            for paramName in thisCrdm_pract_trial:
                globals()[paramName] = thisCrdm_pract_trial[paramName]
        
        # --- Prepare to start Routine "crdm_pract_trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_pract_trial_PY
        my_loop = eval(practice_loop_name)
        
        #random index for certain outcome position and response
        idx = random.randint(0,1) 
        sure_pos = pos[idx] 
        sure_resp = resp[idx]
        #sure_amt = 5
        
        #certain outcome screen position is left/right, lottery is opposite
        if idx == 0: 
            lott_pos = pos[1]
        else:
            lott_pos = pos[0]
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crdm_pract_trial_img* updates
            
            # if crdm_pract_trial_img is starting this frame...
            if crdm_pract_trial_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_img.frameNStart = frameN  # exact frame index
                crdm_pract_trial_img.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_img, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_img.status = STARTED
                crdm_pract_trial_img.setAutoDraw(True)
            
            # if crdm_pract_trial_img is active this frame...
            if crdm_pract_trial_img.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_trial_img is stopping this frame...
            if crdm_pract_trial_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_img.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_img.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_img.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_img.status = FINISHED
                    crdm_pract_trial_img.setAutoDraw(False)
            
            # *crdm_pract_trial_lott_top_txt* updates
            
            # if crdm_pract_trial_lott_top_txt is starting this frame...
            if crdm_pract_trial_lott_top_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_lott_top_txt.frameNStart = frameN  # exact frame index
                crdm_pract_trial_lott_top_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_lott_top_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_lott_top_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_lott_top_txt.status = STARTED
                crdm_pract_trial_lott_top_txt.setAutoDraw(True)
            
            # if crdm_pract_trial_lott_top_txt is active this frame...
            if crdm_pract_trial_lott_top_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_trial_lott_top_txt is stopping this frame...
            if crdm_pract_trial_lott_top_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_lott_top_txt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_lott_top_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_lott_top_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_lott_top_txt.status = FINISHED
                    crdm_pract_trial_lott_top_txt.setAutoDraw(False)
            
            # *crdm_pract_trial_lott_bot_txt* updates
            
            # if crdm_pract_trial_lott_bot_txt is starting this frame...
            if crdm_pract_trial_lott_bot_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_lott_bot_txt.frameNStart = frameN  # exact frame index
                crdm_pract_trial_lott_bot_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_lott_bot_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_lott_bot_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_lott_bot_txt.status = STARTED
                crdm_pract_trial_lott_bot_txt.setAutoDraw(True)
            
            # if crdm_pract_trial_lott_bot_txt is active this frame...
            if crdm_pract_trial_lott_bot_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_trial_lott_bot_txt is stopping this frame...
            if crdm_pract_trial_lott_bot_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_lott_bot_txt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_lott_bot_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_lott_bot_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_lott_bot_txt.status = FINISHED
                    crdm_pract_trial_lott_bot_txt.setAutoDraw(False)
            
            # *crdm_pract_trial_sure_amt_txt* updates
            
            # if crdm_pract_trial_sure_amt_txt is starting this frame...
            if crdm_pract_trial_sure_amt_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_sure_amt_txt.frameNStart = frameN  # exact frame index
                crdm_pract_trial_sure_amt_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_sure_amt_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_sure_amt_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_sure_amt_txt.status = STARTED
                crdm_pract_trial_sure_amt_txt.setAutoDraw(True)
            
            # if crdm_pract_trial_sure_amt_txt is active this frame...
            if crdm_pract_trial_sure_amt_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_trial_sure_amt_txt is stopping this frame...
            if crdm_pract_trial_sure_amt_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_sure_amt_txt.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_sure_amt_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_sure_amt_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_sure_amt_txt.status = FINISHED
                    crdm_pract_trial_sure_amt_txt.setAutoDraw(False)
            
            # *GRFX_fix2* updates
            
            # if GRFX_fix2 is starting this frame...
            if GRFX_fix2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                GRFX_fix2.frameNStart = frameN  # exact frame index
                GRFX_fix2.tStart = t  # local t and not account for scr refresh
                GRFX_fix2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(GRFX_fix2, 'tStartRefresh')  # time at next scr refresh
                # update status
                GRFX_fix2.status = STARTED
                GRFX_fix2.setAutoDraw(True)
            
            # if GRFX_fix2 is active this frame...
            if GRFX_fix2.status == STARTED:
                # update params
                pass
            
            # if GRFX_fix2 is stopping this frame...
            if GRFX_fix2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > GRFX_fix2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    GRFX_fix2.tStop = t  # not accounting for scr refresh
                    GRFX_fix2.frameNStop = frameN  # exact frame index
                    # update status
                    GRFX_fix2.status = FINISHED
                    GRFX_fix2.setAutoDraw(False)
            
            # *crdm_pract_trial_cue* updates
            
            # if crdm_pract_trial_cue is starting this frame...
            if crdm_pract_trial_cue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_cue.frameNStart = frameN  # exact frame index
                crdm_pract_trial_cue.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_cue, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_cue.status = STARTED
                crdm_pract_trial_cue.setAutoDraw(True)
            
            # if crdm_pract_trial_cue is active this frame...
            if crdm_pract_trial_cue.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_trial_cue is stopping this frame...
            if crdm_pract_trial_cue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_cue.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_cue.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_cue.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_cue.status = FINISHED
                    crdm_pract_trial_cue.setAutoDraw(False)
            
            # *crdm_pract_trial_resp* updates
            waitOnFlip = False
            
            # if crdm_pract_trial_resp is starting this frame...
            if crdm_pract_trial_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_trial_resp.frameNStart = frameN  # exact frame index
                crdm_pract_trial_resp.tStart = t  # local t and not account for scr refresh
                crdm_pract_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_trial_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_trial_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(crdm_pract_trial_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(crdm_pract_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if crdm_pract_trial_resp is stopping this frame...
            if crdm_pract_trial_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_trial_resp.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_trial_resp.tStop = t  # not accounting for scr refresh
                    crdm_pract_trial_resp.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_trial_resp.status = FINISHED
                    crdm_pract_trial_resp.status = FINISHED
            if crdm_pract_trial_resp.status == STARTED and not waitOnFlip:
                theseKeys = crdm_pract_trial_resp.getKeys(keyList=["6", "1"], ignoreKeys=["escape"], waitRelease=False)
                _crdm_pract_trial_resp_allKeys.extend(theseKeys)
                if len(_crdm_pract_trial_resp_allKeys):
                    crdm_pract_trial_resp.keys = _crdm_pract_trial_resp_allKeys[-1].name  # just the last key pressed
                    crdm_pract_trial_resp.rt = _crdm_pract_trial_resp_allKeys[-1].rt
                    crdm_pract_trial_resp.duration = _crdm_pract_trial_resp_allKeys[-1].duration
                    # was this correct?
                    if (crdm_pract_trial_resp.keys == str(sure_resp)) or (crdm_pract_trial_resp.keys == sure_resp):
                        crdm_pract_trial_resp.corr = 1
                    else:
                        crdm_pract_trial_resp.corr = 0
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
        # Run 'End Routine' code from crdm_pract_trial_PY
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
            crdm_pract_trials.addData('crdm_pract_trial_resp.duration', crdm_pract_trial_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        
        # --- Prepare to start Routine "crdm_pract_feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_pract_fb_PY
        #Ss did not respond
        if len(pract_key) == 0: 
            crdm_msg = "NO RESPONSE"
            #Ss chose sure $5
        elif pract_sure_key: 
            crdm_msg = "CERTAIN $" + str(crdm_sure_amt)
            #Ss chose lottery
        else: 
            crdm_msg = "PLAY THE LOTTERY"
        crdm_pract_fb_txt.setText(crdm_msg)
        # keep track of which components have finished
        crdm_pract_feedbackComponents = [crdm_pract_fb_txt]
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crdm_pract_fb_txt* updates
            
            # if crdm_pract_fb_txt is starting this frame...
            if crdm_pract_fb_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_fb_txt.frameNStart = frameN  # exact frame index
                crdm_pract_fb_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_fb_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_fb_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_fb_txt.status = STARTED
                crdm_pract_fb_txt.setAutoDraw(True)
            
            # if crdm_pract_fb_txt is active this frame...
            if crdm_pract_fb_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_fb_txt is stopping this frame...
            if crdm_pract_fb_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_fb_txt.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_fb_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_fb_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_fb_txt.status = FINISHED
                    crdm_pract_fb_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "crdm_pract_conf" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_pract_conf_PY
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
        crdm_pract_confComponents = [crdm_pract_conf_txt, crdm_pract_conf1, crdm_pract_conf1_txt, crdm_pract_conf1_but, crdm_pract_conf1_L3, crdm_pract_conf2, crdm_pract_conf2_txt, crdm_pract_conf2_but, crdm_pract_conf2_L4, crdm_pract_conf3, crdm_pract_conf3_txt, crdm_pract_conf3_but, crdm_pract_conf3_R1, crdm_pract_conf4, crdm_pract_conf4_txt, crdm_pract_conf4_but, crdm_pract_conf4_R2, crdm_pract_conf_resp]
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from crdm_pract_conf_PY
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
            
            # if crdm_pract_conf_txt is starting this frame...
            if crdm_pract_conf_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf_txt.frameNStart = frameN  # exact frame index
                crdm_pract_conf_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf_txt.status = STARTED
                crdm_pract_conf_txt.setAutoDraw(True)
            
            # if crdm_pract_conf_txt is active this frame...
            if crdm_pract_conf_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf_txt is stopping this frame...
            if crdm_pract_conf_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf_txt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf_txt.status = FINISHED
                    crdm_pract_conf_txt.setAutoDraw(False)
            
            # *crdm_pract_conf1* updates
            
            # if crdm_pract_conf1 is starting this frame...
            if crdm_pract_conf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf1.frameNStart = frameN  # exact frame index
                crdm_pract_conf1.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf1, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf1.status = STARTED
                crdm_pract_conf1.setAutoDraw(True)
            
            # if crdm_pract_conf1 is active this frame...
            if crdm_pract_conf1.status == STARTED:
                # update params
                crdm_pract_conf1.setFillColor(conf1_color, log=False)
            
            # if crdm_pract_conf1 is stopping this frame...
            if crdm_pract_conf1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf1.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf1.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf1.status = FINISHED
                    crdm_pract_conf1.setAutoDraw(False)
            
            # *crdm_pract_conf1_txt* updates
            
            # if crdm_pract_conf1_txt is starting this frame...
            if crdm_pract_conf1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf1_txt.frameNStart = frameN  # exact frame index
                crdm_pract_conf1_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf1_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf1_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf1_txt.status = STARTED
                crdm_pract_conf1_txt.setAutoDraw(True)
            
            # if crdm_pract_conf1_txt is active this frame...
            if crdm_pract_conf1_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf1_txt is stopping this frame...
            if crdm_pract_conf1_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf1_txt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf1_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf1_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf1_txt.status = FINISHED
                    crdm_pract_conf1_txt.setAutoDraw(False)
            
            # *crdm_pract_conf1_but* updates
            
            # if crdm_pract_conf1_but is starting this frame...
            if crdm_pract_conf1_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf1_but.frameNStart = frameN  # exact frame index
                crdm_pract_conf1_but.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf1_but.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf1_but, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf1_but.status = STARTED
                crdm_pract_conf1_but.setAutoDraw(True)
            
            # if crdm_pract_conf1_but is active this frame...
            if crdm_pract_conf1_but.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf1_but is stopping this frame...
            if crdm_pract_conf1_but.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf1_but.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf1_but.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf1_but.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf1_but.status = FINISHED
                    crdm_pract_conf1_but.setAutoDraw(False)
            
            # *crdm_pract_conf1_L3* updates
            
            # if crdm_pract_conf1_L3 is starting this frame...
            if crdm_pract_conf1_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf1_L3.frameNStart = frameN  # exact frame index
                crdm_pract_conf1_L3.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf1_L3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf1_L3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_pract_conf1_L3.started')
                # update status
                crdm_pract_conf1_L3.status = STARTED
                crdm_pract_conf1_L3.setAutoDraw(True)
            
            # if crdm_pract_conf1_L3 is active this frame...
            if crdm_pract_conf1_L3.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf1_L3 is stopping this frame...
            if crdm_pract_conf1_L3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf1_L3.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf1_L3.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf1_L3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_pract_conf1_L3.stopped')
                    # update status
                    crdm_pract_conf1_L3.status = FINISHED
                    crdm_pract_conf1_L3.setAutoDraw(False)
            
            # *crdm_pract_conf2* updates
            
            # if crdm_pract_conf2 is starting this frame...
            if crdm_pract_conf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf2.frameNStart = frameN  # exact frame index
                crdm_pract_conf2.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf2, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf2.status = STARTED
                crdm_pract_conf2.setAutoDraw(True)
            
            # if crdm_pract_conf2 is active this frame...
            if crdm_pract_conf2.status == STARTED:
                # update params
                crdm_pract_conf2.setFillColor(conf2_color, log=False)
            
            # if crdm_pract_conf2 is stopping this frame...
            if crdm_pract_conf2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf2.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf2.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf2.status = FINISHED
                    crdm_pract_conf2.setAutoDraw(False)
            
            # *crdm_pract_conf2_txt* updates
            
            # if crdm_pract_conf2_txt is starting this frame...
            if crdm_pract_conf2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf2_txt.frameNStart = frameN  # exact frame index
                crdm_pract_conf2_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf2_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf2_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf2_txt.status = STARTED
                crdm_pract_conf2_txt.setAutoDraw(True)
            
            # if crdm_pract_conf2_txt is active this frame...
            if crdm_pract_conf2_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf2_txt is stopping this frame...
            if crdm_pract_conf2_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf2_txt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf2_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf2_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf2_txt.status = FINISHED
                    crdm_pract_conf2_txt.setAutoDraw(False)
            
            # *crdm_pract_conf2_but* updates
            
            # if crdm_pract_conf2_but is starting this frame...
            if crdm_pract_conf2_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf2_but.frameNStart = frameN  # exact frame index
                crdm_pract_conf2_but.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf2_but.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf2_but, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf2_but.status = STARTED
                crdm_pract_conf2_but.setAutoDraw(True)
            
            # if crdm_pract_conf2_but is active this frame...
            if crdm_pract_conf2_but.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf2_but is stopping this frame...
            if crdm_pract_conf2_but.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf2_but.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf2_but.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf2_but.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf2_but.status = FINISHED
                    crdm_pract_conf2_but.setAutoDraw(False)
            
            # *crdm_pract_conf2_L4* updates
            
            # if crdm_pract_conf2_L4 is starting this frame...
            if crdm_pract_conf2_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf2_L4.frameNStart = frameN  # exact frame index
                crdm_pract_conf2_L4.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf2_L4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf2_L4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_pract_conf2_L4.started')
                # update status
                crdm_pract_conf2_L4.status = STARTED
                crdm_pract_conf2_L4.setAutoDraw(True)
            
            # if crdm_pract_conf2_L4 is active this frame...
            if crdm_pract_conf2_L4.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf2_L4 is stopping this frame...
            if crdm_pract_conf2_L4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf2_L4.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf2_L4.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf2_L4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_pract_conf2_L4.stopped')
                    # update status
                    crdm_pract_conf2_L4.status = FINISHED
                    crdm_pract_conf2_L4.setAutoDraw(False)
            
            # *crdm_pract_conf3* updates
            
            # if crdm_pract_conf3 is starting this frame...
            if crdm_pract_conf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf3.frameNStart = frameN  # exact frame index
                crdm_pract_conf3.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf3, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf3.status = STARTED
                crdm_pract_conf3.setAutoDraw(True)
            
            # if crdm_pract_conf3 is active this frame...
            if crdm_pract_conf3.status == STARTED:
                # update params
                crdm_pract_conf3.setFillColor(conf3_color, log=False)
            
            # if crdm_pract_conf3 is stopping this frame...
            if crdm_pract_conf3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf3.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf3.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf3.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf3.status = FINISHED
                    crdm_pract_conf3.setAutoDraw(False)
            
            # *crdm_pract_conf3_txt* updates
            
            # if crdm_pract_conf3_txt is starting this frame...
            if crdm_pract_conf3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf3_txt.frameNStart = frameN  # exact frame index
                crdm_pract_conf3_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf3_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf3_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf3_txt.status = STARTED
                crdm_pract_conf3_txt.setAutoDraw(True)
            
            # if crdm_pract_conf3_txt is active this frame...
            if crdm_pract_conf3_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf3_txt is stopping this frame...
            if crdm_pract_conf3_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf3_txt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf3_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf3_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf3_txt.status = FINISHED
                    crdm_pract_conf3_txt.setAutoDraw(False)
            
            # *crdm_pract_conf3_but* updates
            
            # if crdm_pract_conf3_but is starting this frame...
            if crdm_pract_conf3_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf3_but.frameNStart = frameN  # exact frame index
                crdm_pract_conf3_but.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf3_but.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf3_but, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf3_but.status = STARTED
                crdm_pract_conf3_but.setAutoDraw(True)
            
            # if crdm_pract_conf3_but is active this frame...
            if crdm_pract_conf3_but.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf3_but is stopping this frame...
            if crdm_pract_conf3_but.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf3_but.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf3_but.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf3_but.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf3_but.status = FINISHED
                    crdm_pract_conf3_but.setAutoDraw(False)
            
            # *crdm_pract_conf3_R1* updates
            
            # if crdm_pract_conf3_R1 is starting this frame...
            if crdm_pract_conf3_R1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf3_R1.frameNStart = frameN  # exact frame index
                crdm_pract_conf3_R1.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf3_R1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf3_R1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_pract_conf3_R1.started')
                # update status
                crdm_pract_conf3_R1.status = STARTED
                crdm_pract_conf3_R1.setAutoDraw(True)
            
            # if crdm_pract_conf3_R1 is active this frame...
            if crdm_pract_conf3_R1.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf3_R1 is stopping this frame...
            if crdm_pract_conf3_R1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf3_R1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf3_R1.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf3_R1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_pract_conf3_R1.stopped')
                    # update status
                    crdm_pract_conf3_R1.status = FINISHED
                    crdm_pract_conf3_R1.setAutoDraw(False)
            
            # *crdm_pract_conf4* updates
            
            # if crdm_pract_conf4 is starting this frame...
            if crdm_pract_conf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf4.frameNStart = frameN  # exact frame index
                crdm_pract_conf4.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf4, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf4.status = STARTED
                crdm_pract_conf4.setAutoDraw(True)
            
            # if crdm_pract_conf4 is active this frame...
            if crdm_pract_conf4.status == STARTED:
                # update params
                crdm_pract_conf4.setFillColor(conf4_color, log=False)
            
            # if crdm_pract_conf4 is stopping this frame...
            if crdm_pract_conf4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf4.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf4.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf4.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf4.status = FINISHED
                    crdm_pract_conf4.setAutoDraw(False)
            
            # *crdm_pract_conf4_txt* updates
            
            # if crdm_pract_conf4_txt is starting this frame...
            if crdm_pract_conf4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf4_txt.frameNStart = frameN  # exact frame index
                crdm_pract_conf4_txt.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf4_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf4_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf4_txt.status = STARTED
                crdm_pract_conf4_txt.setAutoDraw(True)
            
            # if crdm_pract_conf4_txt is active this frame...
            if crdm_pract_conf4_txt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf4_txt is stopping this frame...
            if crdm_pract_conf4_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf4_txt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf4_txt.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf4_txt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf4_txt.status = FINISHED
                    crdm_pract_conf4_txt.setAutoDraw(False)
            
            # *crdm_pract_conf4_but* updates
            
            # if crdm_pract_conf4_but is starting this frame...
            if crdm_pract_conf4_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf4_but.frameNStart = frameN  # exact frame index
                crdm_pract_conf4_but.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf4_but.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf4_but, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf4_but.status = STARTED
                crdm_pract_conf4_but.setAutoDraw(True)
            
            # if crdm_pract_conf4_but is active this frame...
            if crdm_pract_conf4_but.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf4_but is stopping this frame...
            if crdm_pract_conf4_but.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf4_but.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf4_but.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf4_but.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf4_but.status = FINISHED
                    crdm_pract_conf4_but.setAutoDraw(False)
            
            # *crdm_pract_conf4_R2* updates
            
            # if crdm_pract_conf4_R2 is starting this frame...
            if crdm_pract_conf4_R2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf4_R2.frameNStart = frameN  # exact frame index
                crdm_pract_conf4_R2.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf4_R2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf4_R2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'crdm_pract_conf4_R2.started')
                # update status
                crdm_pract_conf4_R2.status = STARTED
                crdm_pract_conf4_R2.setAutoDraw(True)
            
            # if crdm_pract_conf4_R2 is active this frame...
            if crdm_pract_conf4_R2.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_conf4_R2 is stopping this frame...
            if crdm_pract_conf4_R2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf4_R2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf4_R2.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf4_R2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_pract_conf4_R2.stopped')
                    # update status
                    crdm_pract_conf4_R2.status = FINISHED
                    crdm_pract_conf4_R2.setAutoDraw(False)
            
            # *crdm_pract_conf_resp* updates
            waitOnFlip = False
            
            # if crdm_pract_conf_resp is starting this frame...
            if crdm_pract_conf_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_conf_resp.frameNStart = frameN  # exact frame index
                crdm_pract_conf_resp.tStart = t  # local t and not account for scr refresh
                crdm_pract_conf_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_conf_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_conf_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(crdm_pract_conf_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(crdm_pract_conf_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if crdm_pract_conf_resp is stopping this frame...
            if crdm_pract_conf_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_conf_resp.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_conf_resp.tStop = t  # not accounting for scr refresh
                    crdm_pract_conf_resp.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_conf_resp.status = FINISHED
                    crdm_pract_conf_resp.status = FINISHED
            if crdm_pract_conf_resp.status == STARTED and not waitOnFlip:
                theseKeys = crdm_pract_conf_resp.getKeys(keyList=["7", "6", "1", "2"], ignoreKeys=["escape"], waitRelease=False)
                _crdm_pract_conf_resp_allKeys.extend(theseKeys)
                if len(_crdm_pract_conf_resp_allKeys):
                    crdm_pract_conf_resp.keys = _crdm_pract_conf_resp_allKeys[-1].name  # just the last key pressed
                    crdm_pract_conf_resp.rt = _crdm_pract_conf_resp_allKeys[-1].rt
                    crdm_pract_conf_resp.duration = _crdm_pract_conf_resp_allKeys[-1].duration
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
            crdm_pract_trials.addData('crdm_pract_conf_resp.duration', crdm_pract_conf_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # --- Prepare to start Routine "crdm_pract_pain_rating" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_pract_pain_PY
        arrow_choice = [0, 0] 
        crdm_pract_pain_resp.keys = []
        crdm_pract_pain_resp.rt = []
        _crdm_pract_pain_resp_allKeys = []
        # keep track of which components have finished
        crdm_pract_pain_ratingComponents = [crdm_pract_pain_prompt, crdm_pract_pain_rating_arrow, crdm_pract_pain_rating_zero, crdm_pract_pain_scale, crdm_pract_pain_rating_but1, crdm_pract_pain_rating_but2, crdm_pract_pain_rating_but3, crdm_pract_pain_rating_but4, crdm_pract_pain_rating_but5, crdm_pract_pain_rating_but6, crdm_pract_pain_rating_but7, crdm_pract_pain_rating_but8, crdm_pract_pain_rating_L1, crdm_pract_pain_rating_L2, crdm_pract_pain_rating_L3, crdm_pract_pain_rating_L4, crdm_pract_pain_rating_R5, crdm_pract_pain_rating_R6, crdm_pract_pain_rating_R7, crdm_pract_pain_rating_R8, crdm_pract_pain_rating_no, crdm_pract_pain_rating_low, crdm_pract_pain_rating_high, crdm_pract_pain_resp]
        for thisComponent in crdm_pract_pain_ratingComponents:
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
        
        # --- Run Routine "crdm_pract_pain_rating" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 6.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from crdm_pract_pain_PY
            #resp is received
            pract_pain_key = crdm_pract_pain_resp.keys
            if len(pract_pain_key) == 1:
                pract_pain_key = painkey_map[pract_pain_key[-1]]
                #arrow moves to indicate selection
                if pract_pain_key == "1": #Pain rating of 1 (lowest)
                    arrow_choice = [-0.6, -0.2] 
                elif pract_pain_key == "2": #Pain rating of 2
                    arrow_choice = [-0.43, -0.2] 
                elif pract_pain_key == "3": #Pain rating of 3
                    arrow_choice = [-0.26, -0.2] 
                elif pract_pain_key == "4": #Pain rating of 4
                    arrow_choice = [-0.085, -0.2] 
                elif pract_pain_key == "5": #Pain rating of 5
                    arrow_choice = [0.085, -0.2] 
                elif pract_pain_key == "6": #Pain rating of 6
                    arrow_choice = [0.26, -0.2] 
                elif pract_pain_key == "7": #Pain rating of 7
                    arrow_choice = [0.43, -0.2] 
                elif pract_pain_key == "8": #Pain rating of 8 (highest)
                    arrow_choice = [0.6, -0.2] 
            
            # *crdm_pract_pain_prompt* updates
            
            # if crdm_pract_pain_prompt is starting this frame...
            if crdm_pract_pain_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_prompt.frameNStart = frameN  # exact frame index
                crdm_pract_pain_prompt.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_prompt, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_prompt.status = STARTED
                crdm_pract_pain_prompt.setAutoDraw(True)
            
            # if crdm_pract_pain_prompt is active this frame...
            if crdm_pract_pain_prompt.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_prompt is stopping this frame...
            if crdm_pract_pain_prompt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_prompt.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_prompt.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_prompt.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_prompt.status = FINISHED
                    crdm_pract_pain_prompt.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_arrow* updates
            
            # if crdm_pract_pain_rating_arrow is starting this frame...
            if crdm_pract_pain_rating_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_arrow.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_arrow.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_arrow, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_arrow.status = STARTED
                crdm_pract_pain_rating_arrow.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_arrow is active this frame...
            if crdm_pract_pain_rating_arrow.status == STARTED:
                # update params
                crdm_pract_pain_rating_arrow.setPos(arrow_choice, log=False)
            
            # if crdm_pract_pain_rating_arrow is stopping this frame...
            if crdm_pract_pain_rating_arrow.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_arrow.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_arrow.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_arrow.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_arrow.status = FINISHED
                    crdm_pract_pain_rating_arrow.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_zero* updates
            
            # if crdm_pract_pain_rating_zero is starting this frame...
            if crdm_pract_pain_rating_zero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_zero.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_zero.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_zero.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_zero, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_zero.status = STARTED
                crdm_pract_pain_rating_zero.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_zero is active this frame...
            if crdm_pract_pain_rating_zero.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_zero is stopping this frame...
            if crdm_pract_pain_rating_zero.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_zero.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_zero.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_zero.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_zero.status = FINISHED
                    crdm_pract_pain_rating_zero.setAutoDraw(False)
            
            # *crdm_pract_pain_scale* updates
            
            # if crdm_pract_pain_scale is starting this frame...
            if crdm_pract_pain_scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_scale.frameNStart = frameN  # exact frame index
                crdm_pract_pain_scale.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_scale.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_scale, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_scale.status = STARTED
                crdm_pract_pain_scale.setAutoDraw(True)
            
            # if crdm_pract_pain_scale is active this frame...
            if crdm_pract_pain_scale.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_scale is stopping this frame...
            if crdm_pract_pain_scale.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_scale.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_scale.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_scale.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_scale.status = FINISHED
                    crdm_pract_pain_scale.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but1* updates
            
            # if crdm_pract_pain_rating_but1 is starting this frame...
            if crdm_pract_pain_rating_but1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but1.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but1.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but1, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but1.status = STARTED
                crdm_pract_pain_rating_but1.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but1 is active this frame...
            if crdm_pract_pain_rating_but1.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but1 is stopping this frame...
            if crdm_pract_pain_rating_but1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but1.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but1.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but1.status = FINISHED
                    crdm_pract_pain_rating_but1.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but2* updates
            
            # if crdm_pract_pain_rating_but2 is starting this frame...
            if crdm_pract_pain_rating_but2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but2.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but2.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but2, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but2.status = STARTED
                crdm_pract_pain_rating_but2.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but2 is active this frame...
            if crdm_pract_pain_rating_but2.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but2 is stopping this frame...
            if crdm_pract_pain_rating_but2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but2.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but2.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but2.status = FINISHED
                    crdm_pract_pain_rating_but2.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but3* updates
            
            # if crdm_pract_pain_rating_but3 is starting this frame...
            if crdm_pract_pain_rating_but3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but3.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but3.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but3, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but3.status = STARTED
                crdm_pract_pain_rating_but3.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but3 is active this frame...
            if crdm_pract_pain_rating_but3.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but3 is stopping this frame...
            if crdm_pract_pain_rating_but3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but3.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but3.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but3.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but3.status = FINISHED
                    crdm_pract_pain_rating_but3.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but4* updates
            
            # if crdm_pract_pain_rating_but4 is starting this frame...
            if crdm_pract_pain_rating_but4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but4.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but4.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but4, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but4.status = STARTED
                crdm_pract_pain_rating_but4.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but4 is active this frame...
            if crdm_pract_pain_rating_but4.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but4 is stopping this frame...
            if crdm_pract_pain_rating_but4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but4.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but4.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but4.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but4.status = FINISHED
                    crdm_pract_pain_rating_but4.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but5* updates
            
            # if crdm_pract_pain_rating_but5 is starting this frame...
            if crdm_pract_pain_rating_but5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but5.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but5.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but5, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but5.status = STARTED
                crdm_pract_pain_rating_but5.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but5 is active this frame...
            if crdm_pract_pain_rating_but5.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but5 is stopping this frame...
            if crdm_pract_pain_rating_but5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but5.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but5.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but5.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but5.status = FINISHED
                    crdm_pract_pain_rating_but5.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but6* updates
            
            # if crdm_pract_pain_rating_but6 is starting this frame...
            if crdm_pract_pain_rating_but6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but6.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but6.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but6, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but6.status = STARTED
                crdm_pract_pain_rating_but6.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but6 is active this frame...
            if crdm_pract_pain_rating_but6.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but6 is stopping this frame...
            if crdm_pract_pain_rating_but6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but6.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but6.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but6.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but6.status = FINISHED
                    crdm_pract_pain_rating_but6.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but7* updates
            
            # if crdm_pract_pain_rating_but7 is starting this frame...
            if crdm_pract_pain_rating_but7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but7.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but7.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but7, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but7.status = STARTED
                crdm_pract_pain_rating_but7.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but7 is active this frame...
            if crdm_pract_pain_rating_but7.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but7 is stopping this frame...
            if crdm_pract_pain_rating_but7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but7.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but7.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but7.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but7.status = FINISHED
                    crdm_pract_pain_rating_but7.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_but8* updates
            
            # if crdm_pract_pain_rating_but8 is starting this frame...
            if crdm_pract_pain_rating_but8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_but8.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_but8.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_but8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_but8, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_but8.status = STARTED
                crdm_pract_pain_rating_but8.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_but8 is active this frame...
            if crdm_pract_pain_rating_but8.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_but8 is stopping this frame...
            if crdm_pract_pain_rating_but8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_but8.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_but8.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_but8.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_but8.status = FINISHED
                    crdm_pract_pain_rating_but8.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_L1* updates
            
            # if crdm_pract_pain_rating_L1 is starting this frame...
            if crdm_pract_pain_rating_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_L1.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_L1.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_L1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_L1, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_L1.status = STARTED
                crdm_pract_pain_rating_L1.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_L1 is active this frame...
            if crdm_pract_pain_rating_L1.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_L1 is stopping this frame...
            if crdm_pract_pain_rating_L1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_L1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_L1.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_L1.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_L1.status = FINISHED
                    crdm_pract_pain_rating_L1.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_L2* updates
            
            # if crdm_pract_pain_rating_L2 is starting this frame...
            if crdm_pract_pain_rating_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_L2.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_L2.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_L2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_L2, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_L2.status = STARTED
                crdm_pract_pain_rating_L2.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_L2 is active this frame...
            if crdm_pract_pain_rating_L2.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_L2 is stopping this frame...
            if crdm_pract_pain_rating_L2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_L2.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_L2.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_L2.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_L2.status = FINISHED
                    crdm_pract_pain_rating_L2.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_L3* updates
            
            # if crdm_pract_pain_rating_L3 is starting this frame...
            if crdm_pract_pain_rating_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_L3.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_L3.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_L3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_L3, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_L3.status = STARTED
                crdm_pract_pain_rating_L3.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_L3 is active this frame...
            if crdm_pract_pain_rating_L3.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_L3 is stopping this frame...
            if crdm_pract_pain_rating_L3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_L3.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_L3.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_L3.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_L3.status = FINISHED
                    crdm_pract_pain_rating_L3.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_L4* updates
            
            # if crdm_pract_pain_rating_L4 is starting this frame...
            if crdm_pract_pain_rating_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_L4.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_L4.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_L4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_L4, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_L4.status = STARTED
                crdm_pract_pain_rating_L4.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_L4 is active this frame...
            if crdm_pract_pain_rating_L4.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_L4 is stopping this frame...
            if crdm_pract_pain_rating_L4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_L4.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_L4.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_L4.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_L4.status = FINISHED
                    crdm_pract_pain_rating_L4.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_R5* updates
            
            # if crdm_pract_pain_rating_R5 is starting this frame...
            if crdm_pract_pain_rating_R5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_R5.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_R5.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_R5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_R5, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_R5.status = STARTED
                crdm_pract_pain_rating_R5.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_R5 is active this frame...
            if crdm_pract_pain_rating_R5.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_R5 is stopping this frame...
            if crdm_pract_pain_rating_R5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_R5.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_R5.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_R5.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_R5.status = FINISHED
                    crdm_pract_pain_rating_R5.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_R6* updates
            
            # if crdm_pract_pain_rating_R6 is starting this frame...
            if crdm_pract_pain_rating_R6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_R6.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_R6.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_R6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_R6, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_R6.status = STARTED
                crdm_pract_pain_rating_R6.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_R6 is active this frame...
            if crdm_pract_pain_rating_R6.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_R6 is stopping this frame...
            if crdm_pract_pain_rating_R6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_R6.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_R6.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_R6.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_R6.status = FINISHED
                    crdm_pract_pain_rating_R6.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_R7* updates
            
            # if crdm_pract_pain_rating_R7 is starting this frame...
            if crdm_pract_pain_rating_R7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_R7.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_R7.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_R7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_R7, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_R7.status = STARTED
                crdm_pract_pain_rating_R7.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_R7 is active this frame...
            if crdm_pract_pain_rating_R7.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_R7 is stopping this frame...
            if crdm_pract_pain_rating_R7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_R7.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_R7.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_R7.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_R7.status = FINISHED
                    crdm_pract_pain_rating_R7.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_R8* updates
            
            # if crdm_pract_pain_rating_R8 is starting this frame...
            if crdm_pract_pain_rating_R8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_R8.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_R8.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_R8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_R8, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_R8.status = STARTED
                crdm_pract_pain_rating_R8.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_R8 is active this frame...
            if crdm_pract_pain_rating_R8.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_R8 is stopping this frame...
            if crdm_pract_pain_rating_R8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_R8.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_R8.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_R8.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_R8.status = FINISHED
                    crdm_pract_pain_rating_R8.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_no* updates
            
            # if crdm_pract_pain_rating_no is starting this frame...
            if crdm_pract_pain_rating_no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_no.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_no.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_no.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_no, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_no.status = STARTED
                crdm_pract_pain_rating_no.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_no is active this frame...
            if crdm_pract_pain_rating_no.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_no is stopping this frame...
            if crdm_pract_pain_rating_no.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_no.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_no.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_no.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_no.status = FINISHED
                    crdm_pract_pain_rating_no.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_low* updates
            
            # if crdm_pract_pain_rating_low is starting this frame...
            if crdm_pract_pain_rating_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_low.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_low.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_low.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_low, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_low.status = STARTED
                crdm_pract_pain_rating_low.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_low is active this frame...
            if crdm_pract_pain_rating_low.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_low is stopping this frame...
            if crdm_pract_pain_rating_low.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_low.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_low.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_low.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_low.status = FINISHED
                    crdm_pract_pain_rating_low.setAutoDraw(False)
            
            # *crdm_pract_pain_rating_high* updates
            
            # if crdm_pract_pain_rating_high is starting this frame...
            if crdm_pract_pain_rating_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_rating_high.frameNStart = frameN  # exact frame index
                crdm_pract_pain_rating_high.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_rating_high.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_rating_high, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_rating_high.status = STARTED
                crdm_pract_pain_rating_high.setAutoDraw(True)
            
            # if crdm_pract_pain_rating_high is active this frame...
            if crdm_pract_pain_rating_high.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_pain_rating_high is stopping this frame...
            if crdm_pract_pain_rating_high.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_rating_high.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_rating_high.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_rating_high.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_rating_high.status = FINISHED
                    crdm_pract_pain_rating_high.setAutoDraw(False)
            
            # *crdm_pract_pain_resp* updates
            waitOnFlip = False
            
            # if crdm_pract_pain_resp is starting this frame...
            if crdm_pract_pain_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_pain_resp.frameNStart = frameN  # exact frame index
                crdm_pract_pain_resp.tStart = t  # local t and not account for scr refresh
                crdm_pract_pain_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_pain_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_pain_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(crdm_pract_pain_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(crdm_pract_pain_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if crdm_pract_pain_resp is stopping this frame...
            if crdm_pract_pain_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_pain_resp.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_pain_resp.tStop = t  # not accounting for scr refresh
                    crdm_pract_pain_resp.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_pain_resp.status = FINISHED
                    crdm_pract_pain_resp.status = FINISHED
            if crdm_pract_pain_resp.status == STARTED and not waitOnFlip:
                theseKeys = crdm_pract_pain_resp.getKeys(keyList=["9", "8", "7", "6", "1", "2", "3", "4"], ignoreKeys=["escape"], waitRelease=False)
                _crdm_pract_pain_resp_allKeys.extend(theseKeys)
                if len(_crdm_pract_pain_resp_allKeys):
                    crdm_pract_pain_resp.keys = _crdm_pract_pain_resp_allKeys[-1].name  # just the last key pressed
                    crdm_pract_pain_resp.rt = _crdm_pract_pain_resp_allKeys[-1].rt
                    crdm_pract_pain_resp.duration = _crdm_pract_pain_resp_allKeys[-1].duration
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crdm_pract_pain_ratingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crdm_pract_pain_rating" ---
        for thisComponent in crdm_pract_pain_ratingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from crdm_pract_pain_PY
        my_loop.addData("crdm_pract_pain_rating", pract_pain_key)
        # check responses
        if crdm_pract_pain_resp.keys in ['', [], None]:  # No response was made
            crdm_pract_pain_resp.keys = None
        crdm_pract_trials.addData('crdm_pract_pain_resp.keys',crdm_pract_pain_resp.keys)
        if crdm_pract_pain_resp.keys != None:  # we had a response
            crdm_pract_trials.addData('crdm_pract_pain_resp.rt', crdm_pract_pain_resp.rt)
            crdm_pract_trials.addData('crdm_pract_pain_resp.duration', crdm_pract_pain_resp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-6.000000)
        
        # --- Prepare to start Routine "crdm_pract_iti" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_pract_iti1_PY
        #3 CRDM practice trials
        if crdm_pract_trials.thisTrialN == 2:
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 12.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crdm_pract_iti1_poly* updates
            
            # if crdm_pract_iti1_poly is starting this frame...
            if crdm_pract_iti1_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_pract_iti1_poly.frameNStart = frameN  # exact frame index
                crdm_pract_iti1_poly.tStart = t  # local t and not account for scr refresh
                crdm_pract_iti1_poly.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_pract_iti1_poly, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_pract_iti1_poly.status = STARTED
                crdm_pract_iti1_poly.setAutoDraw(True)
            
            # if crdm_pract_iti1_poly is active this frame...
            if crdm_pract_iti1_poly.status == STARTED:
                # update params
                pass
            
            # if crdm_pract_iti1_poly is stopping this frame...
            if crdm_pract_iti1_poly.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_pract_iti1_poly.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_pract_iti1_poly.tStop = t  # not accounting for scr refresh
                    crdm_pract_iti1_poly.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_pract_iti1_poly.status = FINISHED
                    crdm_pract_iti1_poly.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
            routineTimer.addTime(-12.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'crdm_pract_trials'
    
    # get names of stimulus parameters
    if crdm_pract_trials.trialList in ([], [None], None):
        params = []
    else:
        params = crdm_pract_trials.trialList[0].keys()
    # save data for this loop
    crdm_pract_trials.saveAsText(filename + 'crdm_pract_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "crdm_trial_instr" ---
    continueRoutine = True
    # update component parameters for each repeat
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_trial_instr_title_txt* updates
        
        # if crdm_trial_instr_title_txt is starting this frame...
        if crdm_trial_instr_title_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_instr_title_txt.frameNStart = frameN  # exact frame index
            crdm_trial_instr_title_txt.tStart = t  # local t and not account for scr refresh
            crdm_trial_instr_title_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_instr_title_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_trial_instr_title_txt.status = STARTED
            crdm_trial_instr_title_txt.setAutoDraw(True)
        
        # if crdm_trial_instr_title_txt is active this frame...
        if crdm_trial_instr_title_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_trial_instr_txt* updates
        
        # if crdm_trial_instr_txt is starting this frame...
        if crdm_trial_instr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_instr_txt.frameNStart = frameN  # exact frame index
            crdm_trial_instr_txt.tStart = t  # local t and not account for scr refresh
            crdm_trial_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_instr_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_trial_instr_txt.status = STARTED
            crdm_trial_instr_txt.setAutoDraw(True)
        
        # if crdm_trial_instr_txt is active this frame...
        if crdm_trial_instr_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_trial_instr_space_txt* updates
        
        # if crdm_trial_instr_space_txt is starting this frame...
        if crdm_trial_instr_space_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_instr_space_txt.frameNStart = frameN  # exact frame index
            crdm_trial_instr_space_txt.tStart = t  # local t and not account for scr refresh
            crdm_trial_instr_space_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_instr_space_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_trial_instr_space_txt.status = STARTED
            crdm_trial_instr_space_txt.setAutoDraw(True)
        
        # if crdm_trial_instr_space_txt is active this frame...
        if crdm_trial_instr_space_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_trial_instr_resp* updates
        waitOnFlip = False
        
        # if crdm_trial_instr_resp is starting this frame...
        if crdm_trial_instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_trial_instr_resp.frameNStart = frameN  # exact frame index
            crdm_trial_instr_resp.tStart = t  # local t and not account for scr refresh
            crdm_trial_instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_trial_instr_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_trial_instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_trial_instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_trial_instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_trial_instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = crdm_trial_instr_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_trial_instr_resp_allKeys.extend(theseKeys)
            if len(_crdm_trial_instr_resp_allKeys):
                crdm_trial_instr_resp.keys = _crdm_trial_instr_resp_allKeys[-1].name  # just the last key pressed
                crdm_trial_instr_resp.rt = _crdm_trial_instr_resp_allKeys[-1].rt
                crdm_trial_instr_resp.duration = _crdm_trial_instr_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    
    # set up handler to look after randomisation of conditions etc
    task_runs = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions("run_temps/sub-" + expInfo['participant'] + "_ses-crdm_runs-temps.csv"),
        seed=None, name='task_runs')
    thisExp.addLoop(task_runs)  # add the loop to the experiment
    thisTask_run = task_runs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTask_run.rgb)
    if thisTask_run != None:
        for paramName in thisTask_run:
            globals()[paramName] = thisTask_run[paramName]
    
    for thisTask_run in task_runs:
        currentLoop = task_runs
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTask_run.rgb)
        if thisTask_run != None:
            for paramName in thisTask_run:
                globals()[paramName] = thisTask_run[paramName]
        
        # --- Prepare to start Routine "crdm_run_setter" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_run_setter_PY
        ##Setting up which trial csv will be imported for each run (16 trials each)
        
        if run_set == 1:
            run_file = "crdm_trials1.csv"
        elif run_set == 2:
            run_file = "crdm_trials2.csv"
        elif run_set == 3:
            run_file = "crdm_trials3.csv"
        else:
            run_file = "crdm_trials4.csv"
        # keep track of which components have finished
        crdm_run_setterComponents = []
        for thisComponent in crdm_run_setterComponents:
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
        
        # --- Run Routine "crdm_run_setter" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crdm_run_setterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crdm_run_setter" ---
        for thisComponent in crdm_run_setterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "crdm_run_setter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "crdm_init_fix" ---
        continueRoutine = True
        # update component parameters for each repeat
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
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *crdm_init_fix_poly* updates
            
            # if crdm_init_fix_poly is starting this frame...
            if crdm_init_fix_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                crdm_init_fix_poly.frameNStart = frameN  # exact frame index
                crdm_init_fix_poly.tStart = t  # local t and not account for scr refresh
                crdm_init_fix_poly.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(crdm_init_fix_poly, 'tStartRefresh')  # time at next scr refresh
                # update status
                crdm_init_fix_poly.status = STARTED
                crdm_init_fix_poly.setAutoDraw(True)
            
            # if crdm_init_fix_poly is active this frame...
            if crdm_init_fix_poly.status == STARTED:
                # update params
                pass
            
            # if crdm_init_fix_poly is stopping this frame...
            if crdm_init_fix_poly.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > crdm_init_fix_poly.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    crdm_init_fix_poly.tStop = t  # not accounting for scr refresh
                    crdm_init_fix_poly.frameNStop = frameN  # exact frame index
                    # update status
                    crdm_init_fix_poly.status = FINISHED
                    crdm_init_fix_poly.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
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
            trialList=data.importConditions(run_file),
            seed=None, name='crdm_trials')
        thisExp.addLoop(crdm_trials)  # add the loop to the experiment
        thisCrdm_trial = crdm_trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisCrdm_trial.rgb)
        if thisCrdm_trial != None:
            for paramName in thisCrdm_trial:
                globals()[paramName] = thisCrdm_trial[paramName]
        
        for thisCrdm_trial in crdm_trials:
            currentLoop = crdm_trials
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisCrdm_trial.rgb)
            if thisCrdm_trial != None:
                for paramName in thisCrdm_trial:
                    globals()[paramName] = thisCrdm_trial[paramName]
            
            # --- Prepare to start Routine "crdm_trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('crdm_trial.started', globalClock.getTime())
            # Run 'Begin Routine' code from crdm_trial_PY
            my_loop = eval(loop_name) ##variable for saving data
            stop_timer = None 
            stopped_time = 0
            lott_outcome = 0
            
            ##random index for certain outcome position and response
            idx = random.randint(0,1) 
            sure_pos = pos[idx] 
            sure_resp = resp[idx]
            
            ##certain outcome screen position is left/right, lottery is opposite
            if idx == 0: 
                lott_pos = pos[1]
            else:
                lott_pos = pos[0]
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
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 7.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *crdm_trial_img* updates
                
                # if crdm_trial_img is starting this frame...
                if crdm_trial_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_img.frameNStart = frameN  # exact frame index
                    crdm_trial_img.tStart = t  # local t and not account for scr refresh
                    crdm_trial_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_trial_img.started')
                    # update status
                    crdm_trial_img.status = STARTED
                    crdm_trial_img.setAutoDraw(True)
                
                # if crdm_trial_img is active this frame...
                if crdm_trial_img.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_img is stopping this frame...
                if crdm_trial_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_img.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_img.tStop = t  # not accounting for scr refresh
                        crdm_trial_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_trial_img.stopped')
                        # update status
                        crdm_trial_img.status = FINISHED
                        crdm_trial_img.setAutoDraw(False)
                
                # *crdm_trial_lott_top* updates
                
                # if crdm_trial_lott_top is starting this frame...
                if crdm_trial_lott_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_lott_top.frameNStart = frameN  # exact frame index
                    crdm_trial_lott_top.tStart = t  # local t and not account for scr refresh
                    crdm_trial_lott_top.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_lott_top, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_trial_lott_top.status = STARTED
                    crdm_trial_lott_top.setAutoDraw(True)
                
                # if crdm_trial_lott_top is active this frame...
                if crdm_trial_lott_top.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_lott_top is stopping this frame...
                if crdm_trial_lott_top.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_lott_top.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_lott_top.tStop = t  # not accounting for scr refresh
                        crdm_trial_lott_top.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_trial_lott_top.status = FINISHED
                        crdm_trial_lott_top.setAutoDraw(False)
                
                # *crdm_trial_lott_bot* updates
                
                # if crdm_trial_lott_bot is starting this frame...
                if crdm_trial_lott_bot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_lott_bot.frameNStart = frameN  # exact frame index
                    crdm_trial_lott_bot.tStart = t  # local t and not account for scr refresh
                    crdm_trial_lott_bot.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_lott_bot, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_trial_lott_bot.status = STARTED
                    crdm_trial_lott_bot.setAutoDraw(True)
                
                # if crdm_trial_lott_bot is active this frame...
                if crdm_trial_lott_bot.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_lott_bot is stopping this frame...
                if crdm_trial_lott_bot.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_lott_bot.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_lott_bot.tStop = t  # not accounting for scr refresh
                        crdm_trial_lott_bot.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_trial_lott_bot.status = FINISHED
                        crdm_trial_lott_bot.setAutoDraw(False)
                
                # *crdm_trial_sure_amt* updates
                
                # if crdm_trial_sure_amt is starting this frame...
                if crdm_trial_sure_amt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_sure_amt.frameNStart = frameN  # exact frame index
                    crdm_trial_sure_amt.tStart = t  # local t and not account for scr refresh
                    crdm_trial_sure_amt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_sure_amt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_trial_sure_amt.status = STARTED
                    crdm_trial_sure_amt.setAutoDraw(True)
                
                # if crdm_trial_sure_amt is active this frame...
                if crdm_trial_sure_amt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_sure_amt is stopping this frame...
                if crdm_trial_sure_amt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_sure_amt.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_sure_amt.tStop = t  # not accounting for scr refresh
                        crdm_trial_sure_amt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_trial_sure_amt.status = FINISHED
                        crdm_trial_sure_amt.setAutoDraw(False)
                
                # *GRFX_fix* updates
                
                # if GRFX_fix is starting this frame...
                if GRFX_fix.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                    # keep track of start time/frame for later
                    GRFX_fix.frameNStart = frameN  # exact frame index
                    GRFX_fix.tStart = t  # local t and not account for scr refresh
                    GRFX_fix.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(GRFX_fix, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    GRFX_fix.status = STARTED
                    GRFX_fix.setAutoDraw(True)
                
                # if GRFX_fix is active this frame...
                if GRFX_fix.status == STARTED:
                    # update params
                    pass
                
                # if GRFX_fix is stopping this frame...
                if GRFX_fix.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > GRFX_fix.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        GRFX_fix.tStop = t  # not accounting for scr refresh
                        GRFX_fix.frameNStop = frameN  # exact frame index
                        # update status
                        GRFX_fix.status = FINISHED
                        GRFX_fix.setAutoDraw(False)
                
                # *crdm_trial_cue* updates
                
                # if crdm_trial_cue is starting this frame...
                if crdm_trial_cue.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_cue.frameNStart = frameN  # exact frame index
                    crdm_trial_cue.tStart = t  # local t and not account for scr refresh
                    crdm_trial_cue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_cue, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_trial_cue.status = STARTED
                    crdm_trial_cue.setAutoDraw(True)
                
                # if crdm_trial_cue is active this frame...
                if crdm_trial_cue.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_cue is stopping this frame...
                if crdm_trial_cue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_cue.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_cue.tStop = t  # not accounting for scr refresh
                        crdm_trial_cue.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_trial_cue.status = FINISHED
                        crdm_trial_cue.setAutoDraw(False)
                
                # *crdm_trial_resp* updates
                waitOnFlip = False
                
                # if crdm_trial_resp is starting this frame...
                if crdm_trial_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_resp.frameNStart = frameN  # exact frame index
                    crdm_trial_resp.tStart = t  # local t and not account for scr refresh
                    crdm_trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_resp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_trial_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(crdm_trial_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(crdm_trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if crdm_trial_resp is stopping this frame...
                if crdm_trial_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_resp.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_resp.tStop = t  # not accounting for scr refresh
                        crdm_trial_resp.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_trial_resp.status = FINISHED
                        crdm_trial_resp.status = FINISHED
                if crdm_trial_resp.status == STARTED and not waitOnFlip:
                    theseKeys = crdm_trial_resp.getKeys(keyList=["6", "1"], ignoreKeys=["escape"], waitRelease=False)
                    _crdm_trial_resp_allKeys.extend(theseKeys)
                    if len(_crdm_trial_resp_allKeys):
                        crdm_trial_resp.keys = _crdm_trial_resp_allKeys[-1].name  # just the last key pressed
                        crdm_trial_resp.rt = _crdm_trial_resp_allKeys[-1].rt
                        crdm_trial_resp.duration = _crdm_trial_resp_allKeys[-1].duration
                        # was this correct?
                        if (crdm_trial_resp.keys == str(sure_resp)) or (crdm_trial_resp.keys == sure_resp):
                            crdm_trial_resp.corr = 1
                        else:
                            crdm_trial_resp.corr = 0
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
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
            thisExp.addData('crdm_trial.stopped', globalClock.getTime())
            # Run 'End Routine' code from crdm_trial_PY
            key = crdm_trial_resp.keys ##variable for feedback routine
            sure_key = crdm_trial_resp.corr ##1 if certain $ selected
            my_loop.addData("crdm_trial_type", "task") ##mark current trial as "task"
            
            ##pseudo-random chip draw using bag probabilities and store/record outcome
            if len(key) == 1: ##response received
                if sure_key == 1: ##sure option
                    earnings.append(("sure", crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, crdm_nonzero_side, crdm_domain))
                    my_loop.addData("crdm_choice", 0) ##record Ss choice as binary
                    my_loop.addData("crdm_choice2", "sure") ##record Ss choice as str
                else: ##lottery option
                    earnings.append(("lott", "?", crdm_img, crdm_lott_top, crdm_lott_bot, crdm_nonzero_side, crdm_domain))
                    my_loop.addData("crdm_choice", 1) ##record Ss choice as binary
                    my_loop.addData("crdm_choice2", "lott") ##record Ss choice as str
                     
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
                crdm_trials.addData('crdm_trial_resp.duration', crdm_trial_resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-7.000000)
            
            # --- Prepare to start Routine "crdm_feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('crdm_feedback.started', globalClock.getTime())
            # Run 'Begin Routine' code from crdm_fb_PY
            if len(key) == 0: ##Ss did not respond
                feedback_img = "images/FB_nonresp.png"
                #crdm_msg = "NO RESPONSE"
            elif sure_key: ##Ss chose sure $5
                feedback_img = "images/FB_cert.png"
                #crdm_msg = "CERTAIN $" + str(crdm_sure_amt)
            else: ##Ss chose lottery
                feedback_img = "images/FB_lott.png"
                #crdm_msg = "PLAY THE LOTTERY" 
            crdm_fb_img.setImage(feedback_img)
            # keep track of which components have finished
            crdm_feedbackComponents = [crdm_fb_img]
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
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *crdm_fb_img* updates
                
                # if crdm_fb_img is starting this frame...
                if crdm_fb_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_fb_img.frameNStart = frameN  # exact frame index
                    crdm_fb_img.tStart = t  # local t and not account for scr refresh
                    crdm_fb_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_fb_img, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_fb_img.status = STARTED
                    crdm_fb_img.setAutoDraw(True)
                
                # if crdm_fb_img is active this frame...
                if crdm_fb_img.status == STARTED:
                    # update params
                    pass
                
                # if crdm_fb_img is stopping this frame...
                if crdm_fb_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_fb_img.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_fb_img.tStop = t  # not accounting for scr refresh
                        crdm_fb_img.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_fb_img.status = FINISHED
                        crdm_fb_img.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
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
            thisExp.addData('crdm_feedback.stopped', globalClock.getTime())
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "crdm_conf" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('crdm_conf.started', globalClock.getTime())
            # Run 'Begin Routine' code from crdm_conf_PY
            if len(key) == 0: ##Ss did not respond
                continueRoutine = False
            
            ##set default gray for all four response boxes
            conf1_color = [0, 0, 0] 
            conf2_color = [0, 0, 0]
            conf3_color = [0, 0, 0]
            conf4_color = [0, 0, 0]
            
            conf_key = []
            crdm_conf_resp.keys = []
            crdm_conf_resp.rt = []
            _crdm_conf_resp_allKeys = []
            # keep track of which components have finished
            crdm_confComponents = [crdm_conf_txt, crdm_conf1, crdm_conf1_txt, crdm_conf1_but, crdm_conf1_L3, crdm_conf2, crdm_conf2_txt, crdm_conf2_but, crdm_conf2_L4, crdm_conf3, crdm_conf3_txt, crdm_conf3_but, crdm_conf3_R1, crdm_conf4, crdm_conf4_txt, crdm_conf4_but, crdm_conf4_R2, crdm_conf_resp]
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
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 6.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from crdm_conf_PY
                ##resp is received
                conf_key = crdm_conf_resp.keys
                
                if len(conf_key) == 1:
                    conf_key = confkey_map[conf_key[-1]]
                    if conf_key == "1": ##not at all confident
                        ##change box color to indicate selection
                        conf1_color = "darkgray" 
                        conf2_color = [0,0,0]
                        conf3_color = [0,0,0]
                        conf4_color = [0,0,0]
                    elif conf_key == "2": ##less confident
                        conf1_color = [0,0,0]
                        conf2_color = "darkgray"
                        conf3_color = [0,0,0]
                        conf4_color = [0,0,0]
                    elif conf_key == "3": ##somewhat confident
                        conf1_color = [0,0,0]
                        conf2_color = [0,0,0]
                        conf3_color = "darkgray"
                        conf4_color = [0,0,0]
                    elif conf_key == "4": ##very confident
                        conf1_color = [0,0,0]
                        conf2_color = [0,0,0]
                        conf3_color = [0,0,0]
                        conf4_color = "darkgray"
                
                # *crdm_conf_txt* updates
                
                # if crdm_conf_txt is starting this frame...
                if crdm_conf_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf_txt.frameNStart = frameN  # exact frame index
                    crdm_conf_txt.tStart = t  # local t and not account for scr refresh
                    crdm_conf_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf_txt.status = STARTED
                    crdm_conf_txt.setAutoDraw(True)
                
                # if crdm_conf_txt is active this frame...
                if crdm_conf_txt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf_txt is stopping this frame...
                if crdm_conf_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf_txt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf_txt.tStop = t  # not accounting for scr refresh
                        crdm_conf_txt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf_txt.status = FINISHED
                        crdm_conf_txt.setAutoDraw(False)
                
                # *crdm_conf1* updates
                
                # if crdm_conf1 is starting this frame...
                if crdm_conf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf1.frameNStart = frameN  # exact frame index
                    crdm_conf1.tStart = t  # local t and not account for scr refresh
                    crdm_conf1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf1.status = STARTED
                    crdm_conf1.setAutoDraw(True)
                
                # if crdm_conf1 is active this frame...
                if crdm_conf1.status == STARTED:
                    # update params
                    crdm_conf1.setFillColor(conf1_color, log=False)
                
                # if crdm_conf1 is stopping this frame...
                if crdm_conf1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf1.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf1.tStop = t  # not accounting for scr refresh
                        crdm_conf1.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf1.status = FINISHED
                        crdm_conf1.setAutoDraw(False)
                
                # *crdm_conf1_txt* updates
                
                # if crdm_conf1_txt is starting this frame...
                if crdm_conf1_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf1_txt.frameNStart = frameN  # exact frame index
                    crdm_conf1_txt.tStart = t  # local t and not account for scr refresh
                    crdm_conf1_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf1_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf1_txt.status = STARTED
                    crdm_conf1_txt.setAutoDraw(True)
                
                # if crdm_conf1_txt is active this frame...
                if crdm_conf1_txt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf1_txt is stopping this frame...
                if crdm_conf1_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf1_txt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf1_txt.tStop = t  # not accounting for scr refresh
                        crdm_conf1_txt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf1_txt.status = FINISHED
                        crdm_conf1_txt.setAutoDraw(False)
                
                # *crdm_conf1_but* updates
                
                # if crdm_conf1_but is starting this frame...
                if crdm_conf1_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf1_but.frameNStart = frameN  # exact frame index
                    crdm_conf1_but.tStart = t  # local t and not account for scr refresh
                    crdm_conf1_but.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf1_but, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf1_but.status = STARTED
                    crdm_conf1_but.setAutoDraw(True)
                
                # if crdm_conf1_but is active this frame...
                if crdm_conf1_but.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf1_but is stopping this frame...
                if crdm_conf1_but.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf1_but.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf1_but.tStop = t  # not accounting for scr refresh
                        crdm_conf1_but.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf1_but.status = FINISHED
                        crdm_conf1_but.setAutoDraw(False)
                
                # *crdm_conf1_L3* updates
                
                # if crdm_conf1_L3 is starting this frame...
                if crdm_conf1_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf1_L3.frameNStart = frameN  # exact frame index
                    crdm_conf1_L3.tStart = t  # local t and not account for scr refresh
                    crdm_conf1_L3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf1_L3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_conf1_L3.started')
                    # update status
                    crdm_conf1_L3.status = STARTED
                    crdm_conf1_L3.setAutoDraw(True)
                
                # if crdm_conf1_L3 is active this frame...
                if crdm_conf1_L3.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf1_L3 is stopping this frame...
                if crdm_conf1_L3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf1_L3.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf1_L3.tStop = t  # not accounting for scr refresh
                        crdm_conf1_L3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_conf1_L3.stopped')
                        # update status
                        crdm_conf1_L3.status = FINISHED
                        crdm_conf1_L3.setAutoDraw(False)
                
                # *crdm_conf2* updates
                
                # if crdm_conf2 is starting this frame...
                if crdm_conf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf2.frameNStart = frameN  # exact frame index
                    crdm_conf2.tStart = t  # local t and not account for scr refresh
                    crdm_conf2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf2.status = STARTED
                    crdm_conf2.setAutoDraw(True)
                
                # if crdm_conf2 is active this frame...
                if crdm_conf2.status == STARTED:
                    # update params
                    crdm_conf2.setFillColor(conf2_color, log=False)
                
                # if crdm_conf2 is stopping this frame...
                if crdm_conf2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf2.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf2.tStop = t  # not accounting for scr refresh
                        crdm_conf2.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf2.status = FINISHED
                        crdm_conf2.setAutoDraw(False)
                
                # *crdm_conf2_txt* updates
                
                # if crdm_conf2_txt is starting this frame...
                if crdm_conf2_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf2_txt.frameNStart = frameN  # exact frame index
                    crdm_conf2_txt.tStart = t  # local t and not account for scr refresh
                    crdm_conf2_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf2_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf2_txt.status = STARTED
                    crdm_conf2_txt.setAutoDraw(True)
                
                # if crdm_conf2_txt is active this frame...
                if crdm_conf2_txt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf2_txt is stopping this frame...
                if crdm_conf2_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf2_txt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf2_txt.tStop = t  # not accounting for scr refresh
                        crdm_conf2_txt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf2_txt.status = FINISHED
                        crdm_conf2_txt.setAutoDraw(False)
                
                # *crdm_conf2_but* updates
                
                # if crdm_conf2_but is starting this frame...
                if crdm_conf2_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf2_but.frameNStart = frameN  # exact frame index
                    crdm_conf2_but.tStart = t  # local t and not account for scr refresh
                    crdm_conf2_but.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf2_but, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf2_but.status = STARTED
                    crdm_conf2_but.setAutoDraw(True)
                
                # if crdm_conf2_but is active this frame...
                if crdm_conf2_but.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf2_but is stopping this frame...
                if crdm_conf2_but.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf2_but.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf2_but.tStop = t  # not accounting for scr refresh
                        crdm_conf2_but.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf2_but.status = FINISHED
                        crdm_conf2_but.setAutoDraw(False)
                
                # *crdm_conf2_L4* updates
                
                # if crdm_conf2_L4 is starting this frame...
                if crdm_conf2_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf2_L4.frameNStart = frameN  # exact frame index
                    crdm_conf2_L4.tStart = t  # local t and not account for scr refresh
                    crdm_conf2_L4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf2_L4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_conf2_L4.started')
                    # update status
                    crdm_conf2_L4.status = STARTED
                    crdm_conf2_L4.setAutoDraw(True)
                
                # if crdm_conf2_L4 is active this frame...
                if crdm_conf2_L4.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf2_L4 is stopping this frame...
                if crdm_conf2_L4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf2_L4.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf2_L4.tStop = t  # not accounting for scr refresh
                        crdm_conf2_L4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_conf2_L4.stopped')
                        # update status
                        crdm_conf2_L4.status = FINISHED
                        crdm_conf2_L4.setAutoDraw(False)
                
                # *crdm_conf3* updates
                
                # if crdm_conf3 is starting this frame...
                if crdm_conf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf3.frameNStart = frameN  # exact frame index
                    crdm_conf3.tStart = t  # local t and not account for scr refresh
                    crdm_conf3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf3.status = STARTED
                    crdm_conf3.setAutoDraw(True)
                
                # if crdm_conf3 is active this frame...
                if crdm_conf3.status == STARTED:
                    # update params
                    crdm_conf3.setFillColor(conf3_color, log=False)
                
                # if crdm_conf3 is stopping this frame...
                if crdm_conf3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf3.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf3.tStop = t  # not accounting for scr refresh
                        crdm_conf3.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf3.status = FINISHED
                        crdm_conf3.setAutoDraw(False)
                
                # *crdm_conf3_txt* updates
                
                # if crdm_conf3_txt is starting this frame...
                if crdm_conf3_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf3_txt.frameNStart = frameN  # exact frame index
                    crdm_conf3_txt.tStart = t  # local t and not account for scr refresh
                    crdm_conf3_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf3_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf3_txt.status = STARTED
                    crdm_conf3_txt.setAutoDraw(True)
                
                # if crdm_conf3_txt is active this frame...
                if crdm_conf3_txt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf3_txt is stopping this frame...
                if crdm_conf3_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf3_txt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf3_txt.tStop = t  # not accounting for scr refresh
                        crdm_conf3_txt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf3_txt.status = FINISHED
                        crdm_conf3_txt.setAutoDraw(False)
                
                # *crdm_conf3_but* updates
                
                # if crdm_conf3_but is starting this frame...
                if crdm_conf3_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf3_but.frameNStart = frameN  # exact frame index
                    crdm_conf3_but.tStart = t  # local t and not account for scr refresh
                    crdm_conf3_but.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf3_but, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf3_but.status = STARTED
                    crdm_conf3_but.setAutoDraw(True)
                
                # if crdm_conf3_but is active this frame...
                if crdm_conf3_but.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf3_but is stopping this frame...
                if crdm_conf3_but.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf3_but.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf3_but.tStop = t  # not accounting for scr refresh
                        crdm_conf3_but.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf3_but.status = FINISHED
                        crdm_conf3_but.setAutoDraw(False)
                
                # *crdm_conf3_R1* updates
                
                # if crdm_conf3_R1 is starting this frame...
                if crdm_conf3_R1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf3_R1.frameNStart = frameN  # exact frame index
                    crdm_conf3_R1.tStart = t  # local t and not account for scr refresh
                    crdm_conf3_R1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf3_R1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_conf3_R1.started')
                    # update status
                    crdm_conf3_R1.status = STARTED
                    crdm_conf3_R1.setAutoDraw(True)
                
                # if crdm_conf3_R1 is active this frame...
                if crdm_conf3_R1.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf3_R1 is stopping this frame...
                if crdm_conf3_R1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf3_R1.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf3_R1.tStop = t  # not accounting for scr refresh
                        crdm_conf3_R1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_conf3_R1.stopped')
                        # update status
                        crdm_conf3_R1.status = FINISHED
                        crdm_conf3_R1.setAutoDraw(False)
                
                # *crdm_conf4* updates
                
                # if crdm_conf4 is starting this frame...
                if crdm_conf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf4.frameNStart = frameN  # exact frame index
                    crdm_conf4.tStart = t  # local t and not account for scr refresh
                    crdm_conf4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf4.status = STARTED
                    crdm_conf4.setAutoDraw(True)
                
                # if crdm_conf4 is active this frame...
                if crdm_conf4.status == STARTED:
                    # update params
                    crdm_conf4.setFillColor(conf4_color, log=False)
                
                # if crdm_conf4 is stopping this frame...
                if crdm_conf4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf4.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf4.tStop = t  # not accounting for scr refresh
                        crdm_conf4.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf4.status = FINISHED
                        crdm_conf4.setAutoDraw(False)
                
                # *crdm_conf4_txt* updates
                
                # if crdm_conf4_txt is starting this frame...
                if crdm_conf4_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf4_txt.frameNStart = frameN  # exact frame index
                    crdm_conf4_txt.tStart = t  # local t and not account for scr refresh
                    crdm_conf4_txt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf4_txt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf4_txt.status = STARTED
                    crdm_conf4_txt.setAutoDraw(True)
                
                # if crdm_conf4_txt is active this frame...
                if crdm_conf4_txt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf4_txt is stopping this frame...
                if crdm_conf4_txt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf4_txt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf4_txt.tStop = t  # not accounting for scr refresh
                        crdm_conf4_txt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf4_txt.status = FINISHED
                        crdm_conf4_txt.setAutoDraw(False)
                
                # *crdm_conf4_but* updates
                
                # if crdm_conf4_but is starting this frame...
                if crdm_conf4_but.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf4_but.frameNStart = frameN  # exact frame index
                    crdm_conf4_but.tStart = t  # local t and not account for scr refresh
                    crdm_conf4_but.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf4_but, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf4_but.status = STARTED
                    crdm_conf4_but.setAutoDraw(True)
                
                # if crdm_conf4_but is active this frame...
                if crdm_conf4_but.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf4_but is stopping this frame...
                if crdm_conf4_but.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf4_but.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf4_but.tStop = t  # not accounting for scr refresh
                        crdm_conf4_but.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf4_but.status = FINISHED
                        crdm_conf4_but.setAutoDraw(False)
                
                # *crdm_conf4_R2* updates
                
                # if crdm_conf4_R2 is starting this frame...
                if crdm_conf4_R2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf4_R2.frameNStart = frameN  # exact frame index
                    crdm_conf4_R2.tStart = t  # local t and not account for scr refresh
                    crdm_conf4_R2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf4_R2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_conf4_R2.started')
                    # update status
                    crdm_conf4_R2.status = STARTED
                    crdm_conf4_R2.setAutoDraw(True)
                
                # if crdm_conf4_R2 is active this frame...
                if crdm_conf4_R2.status == STARTED:
                    # update params
                    pass
                
                # if crdm_conf4_R2 is stopping this frame...
                if crdm_conf4_R2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf4_R2.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf4_R2.tStop = t  # not accounting for scr refresh
                        crdm_conf4_R2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_conf4_R2.stopped')
                        # update status
                        crdm_conf4_R2.status = FINISHED
                        crdm_conf4_R2.setAutoDraw(False)
                
                # *crdm_conf_resp* updates
                waitOnFlip = False
                
                # if crdm_conf_resp is starting this frame...
                if crdm_conf_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_conf_resp.frameNStart = frameN  # exact frame index
                    crdm_conf_resp.tStart = t  # local t and not account for scr refresh
                    crdm_conf_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_conf_resp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_conf_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(crdm_conf_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(crdm_conf_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if crdm_conf_resp is stopping this frame...
                if crdm_conf_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_conf_resp.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_conf_resp.tStop = t  # not accounting for scr refresh
                        crdm_conf_resp.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_conf_resp.status = FINISHED
                        crdm_conf_resp.status = FINISHED
                if crdm_conf_resp.status == STARTED and not waitOnFlip:
                    theseKeys = crdm_conf_resp.getKeys(keyList=["7", "6", "1", "2"], ignoreKeys=["escape"], waitRelease=False)
                    _crdm_conf_resp_allKeys.extend(theseKeys)
                    if len(_crdm_conf_resp_allKeys):
                        crdm_conf_resp.keys = _crdm_conf_resp_allKeys[-1].name  # just the last key pressed
                        crdm_conf_resp.rt = _crdm_conf_resp_allKeys[-1].rt
                        crdm_conf_resp.duration = _crdm_conf_resp_allKeys[-1].duration
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
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
            thisExp.addData('crdm_conf.stopped', globalClock.getTime())
            # Run 'End Routine' code from crdm_conf_PY
            my_loop.addData("crdm_conf", conf_key) ##record confident rating
            # check responses
            if crdm_conf_resp.keys in ['', [], None]:  # No response was made
                crdm_conf_resp.keys = None
            crdm_trials.addData('crdm_conf_resp.keys',crdm_conf_resp.keys)
            if crdm_conf_resp.keys != None:  # we had a response
                crdm_trials.addData('crdm_conf_resp.rt', crdm_conf_resp.rt)
                crdm_trials.addData('crdm_conf_resp.duration', crdm_conf_resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-6.000000)
            
            # --- Prepare to start Routine "crdm_pain_rating" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('crdm_pain_rating.started', globalClock.getTime())
            # Run 'Begin Routine' code from crdm_pain_PY
            arrow_choice = [0, -0.2] 
            crdm_pain_resp.keys = []
            crdm_pain_resp.rt = []
            _crdm_pain_resp_allKeys = []
            # keep track of which components have finished
            crdm_pain_ratingComponents = [crdm_pain_prompt, crdm_pain_rating_arrow, crdm_pain_rating_zero, crdm_pain_rating_scale, crdm_pain_rating_but1, crdm_pain_rating_but2, crdm_pain_rating_but3, crdm_pain_rating_but4, crdm_pain_rating_but5, crdm_pain_rating_but6, crdm_pain_rating_but7, crdm_pain_rating_but8, crdm_pain_rating_L1, crdm_pain_rating_L2, crdm_pain_rating_L3, crdm_pain_rating_L4, crdm_pain_rating_R5, crdm_pain_rating_R6, crdm_pain_rating_R7, crdm_pain_rating_R8, crdm_pain_rating_no, crdm_pain_rating_low, crdm_pain_rating_high, crdm_pain_resp]
            for thisComponent in crdm_pain_ratingComponents:
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
            
            # --- Run Routine "crdm_pain_rating" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 6.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from crdm_pain_PY
                pain_key = crdm_pain_resp.keys ##resp is received
                if len(pain_key) == 1:
                    pain_key = painkey_map[pain_key[-1]]
                    ##arrow moves to indicate selection
                    if pain_key == "1": ##Pain rating of 1 (lowest)
                        arrow_choice = [-0.6, -0.2] 
                    elif pain_key == "2": ##Pain rating of 2
                        arrow_choice = [-0.43, -0.2] 
                    elif pain_key == "3": ##Pain rating of 3
                        arrow_choice = [-0.26, -0.2] 
                    elif pain_key == "4": ##Pain rating of 4
                        arrow_choice = [-0.085, -0.2] 
                    elif pain_key == "5": ##Pain rating of 5
                        arrow_choice = [0.085, -0.2] 
                    elif pain_key == "6": ##Pain rating of 6
                        arrow_choice = [0.26, -0.2] 
                    elif pain_key == "7": ##Pain rating of 7
                        arrow_choice = [0.43, -0.2] 
                    elif pain_key == "8": ##Pain rating of 8 (highest)
                        arrow_choice = [0.6, -0.2] 
                
                # *crdm_pain_prompt* updates
                
                # if crdm_pain_prompt is starting this frame...
                if crdm_pain_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_prompt.frameNStart = frameN  # exact frame index
                    crdm_pain_prompt.tStart = t  # local t and not account for scr refresh
                    crdm_pain_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_prompt, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_prompt.status = STARTED
                    crdm_pain_prompt.setAutoDraw(True)
                
                # if crdm_pain_prompt is active this frame...
                if crdm_pain_prompt.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_prompt is stopping this frame...
                if crdm_pain_prompt.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_prompt.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_prompt.tStop = t  # not accounting for scr refresh
                        crdm_pain_prompt.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_prompt.status = FINISHED
                        crdm_pain_prompt.setAutoDraw(False)
                
                # *crdm_pain_rating_arrow* updates
                
                # if crdm_pain_rating_arrow is starting this frame...
                if crdm_pain_rating_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_arrow.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_arrow.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_arrow.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_arrow, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_arrow.status = STARTED
                    crdm_pain_rating_arrow.setAutoDraw(True)
                
                # if crdm_pain_rating_arrow is active this frame...
                if crdm_pain_rating_arrow.status == STARTED:
                    # update params
                    crdm_pain_rating_arrow.setPos(arrow_choice, log=False)
                
                # if crdm_pain_rating_arrow is stopping this frame...
                if crdm_pain_rating_arrow.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_arrow.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_arrow.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_arrow.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_arrow.status = FINISHED
                        crdm_pain_rating_arrow.setAutoDraw(False)
                
                # *crdm_pain_rating_zero* updates
                
                # if crdm_pain_rating_zero is starting this frame...
                if crdm_pain_rating_zero.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_zero.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_zero.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_zero.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_zero, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_zero.status = STARTED
                    crdm_pain_rating_zero.setAutoDraw(True)
                
                # if crdm_pain_rating_zero is active this frame...
                if crdm_pain_rating_zero.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_zero is stopping this frame...
                if crdm_pain_rating_zero.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_zero.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_zero.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_zero.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_zero.status = FINISHED
                        crdm_pain_rating_zero.setAutoDraw(False)
                
                # *crdm_pain_rating_scale* updates
                
                # if crdm_pain_rating_scale is starting this frame...
                if crdm_pain_rating_scale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_scale.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_scale.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_scale.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_scale, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_scale.status = STARTED
                    crdm_pain_rating_scale.setAutoDraw(True)
                
                # if crdm_pain_rating_scale is active this frame...
                if crdm_pain_rating_scale.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_scale is stopping this frame...
                if crdm_pain_rating_scale.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_scale.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_scale.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_scale.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_scale.status = FINISHED
                        crdm_pain_rating_scale.setAutoDraw(False)
                
                # *crdm_pain_rating_but1* updates
                
                # if crdm_pain_rating_but1 is starting this frame...
                if crdm_pain_rating_but1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but1.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but1.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but1.status = STARTED
                    crdm_pain_rating_but1.setAutoDraw(True)
                
                # if crdm_pain_rating_but1 is active this frame...
                if crdm_pain_rating_but1.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but1 is stopping this frame...
                if crdm_pain_rating_but1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but1.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but1.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but1.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but1.status = FINISHED
                        crdm_pain_rating_but1.setAutoDraw(False)
                
                # *crdm_pain_rating_but2* updates
                
                # if crdm_pain_rating_but2 is starting this frame...
                if crdm_pain_rating_but2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but2.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but2.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but2.status = STARTED
                    crdm_pain_rating_but2.setAutoDraw(True)
                
                # if crdm_pain_rating_but2 is active this frame...
                if crdm_pain_rating_but2.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but2 is stopping this frame...
                if crdm_pain_rating_but2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but2.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but2.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but2.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but2.status = FINISHED
                        crdm_pain_rating_but2.setAutoDraw(False)
                
                # *crdm_pain_rating_but3* updates
                
                # if crdm_pain_rating_but3 is starting this frame...
                if crdm_pain_rating_but3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but3.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but3.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but3.status = STARTED
                    crdm_pain_rating_but3.setAutoDraw(True)
                
                # if crdm_pain_rating_but3 is active this frame...
                if crdm_pain_rating_but3.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but3 is stopping this frame...
                if crdm_pain_rating_but3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but3.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but3.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but3.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but3.status = FINISHED
                        crdm_pain_rating_but3.setAutoDraw(False)
                
                # *crdm_pain_rating_but4* updates
                
                # if crdm_pain_rating_but4 is starting this frame...
                if crdm_pain_rating_but4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but4.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but4.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but4.status = STARTED
                    crdm_pain_rating_but4.setAutoDraw(True)
                
                # if crdm_pain_rating_but4 is active this frame...
                if crdm_pain_rating_but4.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but4 is stopping this frame...
                if crdm_pain_rating_but4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but4.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but4.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but4.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but4.status = FINISHED
                        crdm_pain_rating_but4.setAutoDraw(False)
                
                # *crdm_pain_rating_but5* updates
                
                # if crdm_pain_rating_but5 is starting this frame...
                if crdm_pain_rating_but5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but5.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but5.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but5.status = STARTED
                    crdm_pain_rating_but5.setAutoDraw(True)
                
                # if crdm_pain_rating_but5 is active this frame...
                if crdm_pain_rating_but5.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but5 is stopping this frame...
                if crdm_pain_rating_but5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but5.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but5.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but5.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but5.status = FINISHED
                        crdm_pain_rating_but5.setAutoDraw(False)
                
                # *crdm_pain_rating_but6* updates
                
                # if crdm_pain_rating_but6 is starting this frame...
                if crdm_pain_rating_but6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but6.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but6.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but6.status = STARTED
                    crdm_pain_rating_but6.setAutoDraw(True)
                
                # if crdm_pain_rating_but6 is active this frame...
                if crdm_pain_rating_but6.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but6 is stopping this frame...
                if crdm_pain_rating_but6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but6.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but6.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but6.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but6.status = FINISHED
                        crdm_pain_rating_but6.setAutoDraw(False)
                
                # *crdm_pain_rating_but7* updates
                
                # if crdm_pain_rating_but7 is starting this frame...
                if crdm_pain_rating_but7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but7.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but7.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but7, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but7.status = STARTED
                    crdm_pain_rating_but7.setAutoDraw(True)
                
                # if crdm_pain_rating_but7 is active this frame...
                if crdm_pain_rating_but7.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but7 is stopping this frame...
                if crdm_pain_rating_but7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but7.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but7.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but7.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but7.status = FINISHED
                        crdm_pain_rating_but7.setAutoDraw(False)
                
                # *crdm_pain_rating_but8* updates
                
                # if crdm_pain_rating_but8 is starting this frame...
                if crdm_pain_rating_but8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_but8.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_but8.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_but8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_but8, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_but8.status = STARTED
                    crdm_pain_rating_but8.setAutoDraw(True)
                
                # if crdm_pain_rating_but8 is active this frame...
                if crdm_pain_rating_but8.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_but8 is stopping this frame...
                if crdm_pain_rating_but8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_but8.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_but8.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_but8.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_but8.status = FINISHED
                        crdm_pain_rating_but8.setAutoDraw(False)
                
                # *crdm_pain_rating_L1* updates
                
                # if crdm_pain_rating_L1 is starting this frame...
                if crdm_pain_rating_L1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_L1.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_L1.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_L1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_L1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_L1.status = STARTED
                    crdm_pain_rating_L1.setAutoDraw(True)
                
                # if crdm_pain_rating_L1 is active this frame...
                if crdm_pain_rating_L1.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_L1 is stopping this frame...
                if crdm_pain_rating_L1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_L1.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_L1.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_L1.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_L1.status = FINISHED
                        crdm_pain_rating_L1.setAutoDraw(False)
                
                # *crdm_pain_rating_L2* updates
                
                # if crdm_pain_rating_L2 is starting this frame...
                if crdm_pain_rating_L2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_L2.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_L2.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_L2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_L2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_L2.status = STARTED
                    crdm_pain_rating_L2.setAutoDraw(True)
                
                # if crdm_pain_rating_L2 is active this frame...
                if crdm_pain_rating_L2.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_L2 is stopping this frame...
                if crdm_pain_rating_L2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_L2.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_L2.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_L2.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_L2.status = FINISHED
                        crdm_pain_rating_L2.setAutoDraw(False)
                
                # *crdm_pain_rating_L3* updates
                
                # if crdm_pain_rating_L3 is starting this frame...
                if crdm_pain_rating_L3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_L3.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_L3.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_L3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_L3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_L3.status = STARTED
                    crdm_pain_rating_L3.setAutoDraw(True)
                
                # if crdm_pain_rating_L3 is active this frame...
                if crdm_pain_rating_L3.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_L3 is stopping this frame...
                if crdm_pain_rating_L3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_L3.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_L3.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_L3.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_L3.status = FINISHED
                        crdm_pain_rating_L3.setAutoDraw(False)
                
                # *crdm_pain_rating_L4* updates
                
                # if crdm_pain_rating_L4 is starting this frame...
                if crdm_pain_rating_L4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_L4.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_L4.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_L4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_L4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_L4.status = STARTED
                    crdm_pain_rating_L4.setAutoDraw(True)
                
                # if crdm_pain_rating_L4 is active this frame...
                if crdm_pain_rating_L4.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_L4 is stopping this frame...
                if crdm_pain_rating_L4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_L4.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_L4.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_L4.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_L4.status = FINISHED
                        crdm_pain_rating_L4.setAutoDraw(False)
                
                # *crdm_pain_rating_R5* updates
                
                # if crdm_pain_rating_R5 is starting this frame...
                if crdm_pain_rating_R5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_R5.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_R5.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_R5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_R5, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_R5.status = STARTED
                    crdm_pain_rating_R5.setAutoDraw(True)
                
                # if crdm_pain_rating_R5 is active this frame...
                if crdm_pain_rating_R5.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_R5 is stopping this frame...
                if crdm_pain_rating_R5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_R5.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_R5.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_R5.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_R5.status = FINISHED
                        crdm_pain_rating_R5.setAutoDraw(False)
                
                # *crdm_pain_rating_R6* updates
                
                # if crdm_pain_rating_R6 is starting this frame...
                if crdm_pain_rating_R6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_R6.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_R6.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_R6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_R6, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_R6.status = STARTED
                    crdm_pain_rating_R6.setAutoDraw(True)
                
                # if crdm_pain_rating_R6 is active this frame...
                if crdm_pain_rating_R6.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_R6 is stopping this frame...
                if crdm_pain_rating_R6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_R6.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_R6.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_R6.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_R6.status = FINISHED
                        crdm_pain_rating_R6.setAutoDraw(False)
                
                # *crdm_pain_rating_R7* updates
                
                # if crdm_pain_rating_R7 is starting this frame...
                if crdm_pain_rating_R7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_R7.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_R7.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_R7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_R7, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_R7.status = STARTED
                    crdm_pain_rating_R7.setAutoDraw(True)
                
                # if crdm_pain_rating_R7 is active this frame...
                if crdm_pain_rating_R7.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_R7 is stopping this frame...
                if crdm_pain_rating_R7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_R7.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_R7.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_R7.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_R7.status = FINISHED
                        crdm_pain_rating_R7.setAutoDraw(False)
                
                # *crdm_pain_rating_R8* updates
                
                # if crdm_pain_rating_R8 is starting this frame...
                if crdm_pain_rating_R8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_R8.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_R8.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_R8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_R8, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_R8.status = STARTED
                    crdm_pain_rating_R8.setAutoDraw(True)
                
                # if crdm_pain_rating_R8 is active this frame...
                if crdm_pain_rating_R8.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_R8 is stopping this frame...
                if crdm_pain_rating_R8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_R8.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_R8.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_R8.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_R8.status = FINISHED
                        crdm_pain_rating_R8.setAutoDraw(False)
                
                # *crdm_pain_rating_no* updates
                
                # if crdm_pain_rating_no is starting this frame...
                if crdm_pain_rating_no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_no.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_no.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_no.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_no, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_no.status = STARTED
                    crdm_pain_rating_no.setAutoDraw(True)
                
                # if crdm_pain_rating_no is active this frame...
                if crdm_pain_rating_no.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_no is stopping this frame...
                if crdm_pain_rating_no.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_no.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_no.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_no.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_no.status = FINISHED
                        crdm_pain_rating_no.setAutoDraw(False)
                
                # *crdm_pain_rating_low* updates
                
                # if crdm_pain_rating_low is starting this frame...
                if crdm_pain_rating_low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_low.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_low.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_low.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_low, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_low.status = STARTED
                    crdm_pain_rating_low.setAutoDraw(True)
                
                # if crdm_pain_rating_low is active this frame...
                if crdm_pain_rating_low.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_low is stopping this frame...
                if crdm_pain_rating_low.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_low.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_low.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_low.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_low.status = FINISHED
                        crdm_pain_rating_low.setAutoDraw(False)
                
                # *crdm_pain_rating_high* updates
                
                # if crdm_pain_rating_high is starting this frame...
                if crdm_pain_rating_high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_rating_high.frameNStart = frameN  # exact frame index
                    crdm_pain_rating_high.tStart = t  # local t and not account for scr refresh
                    crdm_pain_rating_high.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_rating_high, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_rating_high.status = STARTED
                    crdm_pain_rating_high.setAutoDraw(True)
                
                # if crdm_pain_rating_high is active this frame...
                if crdm_pain_rating_high.status == STARTED:
                    # update params
                    pass
                
                # if crdm_pain_rating_high is stopping this frame...
                if crdm_pain_rating_high.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_rating_high.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_rating_high.tStop = t  # not accounting for scr refresh
                        crdm_pain_rating_high.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_rating_high.status = FINISHED
                        crdm_pain_rating_high.setAutoDraw(False)
                
                # *crdm_pain_resp* updates
                waitOnFlip = False
                
                # if crdm_pain_resp is starting this frame...
                if crdm_pain_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_pain_resp.frameNStart = frameN  # exact frame index
                    crdm_pain_resp.tStart = t  # local t and not account for scr refresh
                    crdm_pain_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_pain_resp, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    crdm_pain_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(crdm_pain_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(crdm_pain_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if crdm_pain_resp is stopping this frame...
                if crdm_pain_resp.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_pain_resp.tStartRefresh + 6-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_pain_resp.tStop = t  # not accounting for scr refresh
                        crdm_pain_resp.frameNStop = frameN  # exact frame index
                        # update status
                        crdm_pain_resp.status = FINISHED
                        crdm_pain_resp.status = FINISHED
                if crdm_pain_resp.status == STARTED and not waitOnFlip:
                    theseKeys = crdm_pain_resp.getKeys(keyList=["9", "8", "7", "6", "1", "2", "3", "4"], ignoreKeys=["escape"], waitRelease=False)
                    _crdm_pain_resp_allKeys.extend(theseKeys)
                    if len(_crdm_pain_resp_allKeys):
                        crdm_pain_resp.keys = _crdm_pain_resp_allKeys[-1].name  # just the last key pressed
                        crdm_pain_resp.rt = _crdm_pain_resp_allKeys[-1].rt
                        crdm_pain_resp.duration = _crdm_pain_resp_allKeys[-1].duration
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in crdm_pain_ratingComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "crdm_pain_rating" ---
            for thisComponent in crdm_pain_ratingComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('crdm_pain_rating.stopped', globalClock.getTime())
            # Run 'End Routine' code from crdm_pain_PY
            my_loop.addData("crdm_pain_rating", pain_key) ##record pain rating
            # check responses
            if crdm_pain_resp.keys in ['', [], None]:  # No response was made
                crdm_pain_resp.keys = None
            crdm_trials.addData('crdm_pain_resp.keys',crdm_pain_resp.keys)
            if crdm_pain_resp.keys != None:  # we had a response
                crdm_trials.addData('crdm_pain_resp.rt', crdm_pain_resp.rt)
                crdm_trials.addData('crdm_pain_resp.duration', crdm_pain_resp.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-6.000000)
            
            # --- Prepare to start Routine "crdm_trial_iti" ---
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from crdm_trial_iti1_PY
            iti_dur = 12
            #16 trials per run
            if crdm_trials.thisTrialN == 15: ##checks if final trial
                continueRoutine = False ##does not run ITI on final trial
            # keep track of which components have finished
            crdm_trial_itiComponents = [crdm_trial_iti1_poly]
            for thisComponent in crdm_trial_itiComponents:
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
            
            # --- Run Routine "crdm_trial_iti" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *crdm_trial_iti1_poly* updates
                
                # if crdm_trial_iti1_poly is starting this frame...
                if crdm_trial_iti1_poly.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    crdm_trial_iti1_poly.frameNStart = frameN  # exact frame index
                    crdm_trial_iti1_poly.tStart = t  # local t and not account for scr refresh
                    crdm_trial_iti1_poly.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(crdm_trial_iti1_poly, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'crdm_trial_iti1_poly.started')
                    # update status
                    crdm_trial_iti1_poly.status = STARTED
                    crdm_trial_iti1_poly.setAutoDraw(True)
                
                # if crdm_trial_iti1_poly is active this frame...
                if crdm_trial_iti1_poly.status == STARTED:
                    # update params
                    pass
                
                # if crdm_trial_iti1_poly is stopping this frame...
                if crdm_trial_iti1_poly.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > crdm_trial_iti1_poly.tStartRefresh + iti_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        crdm_trial_iti1_poly.tStop = t  # not accounting for scr refresh
                        crdm_trial_iti1_poly.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'crdm_trial_iti1_poly.stopped')
                        # update status
                        crdm_trial_iti1_poly.status = FINISHED
                        crdm_trial_iti1_poly.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, inputs=inputs, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in crdm_trial_itiComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "crdm_trial_iti" ---
            for thisComponent in crdm_trial_itiComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "crdm_trial_iti" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'crdm_trials'
        
        # get names of stimulus parameters
        if crdm_trials.trialList in ([], [None], None):
            params = []
        else:
            params = crdm_trials.trialList[0].keys()
        # save data for this loop
        crdm_trials.saveAsText(filename + 'crdm_trials.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "crdm_run_break" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from crdm_run_break_PY
        if task_runs.thisN == 0: 
            run_break_txt = "You have completed Task Block #1. \n \n Task Block #2 will begin shortly."
        elif task_runs.thisN == 1:
            run_break_txt = "You have completed Task Block #2. \n \n Task Block #3 will begin shortly."
        elif task_runs.thisN == 2:
            run_break_txt = "You have completed Task Block #3. \n \n Task Block #4 will begin shortly."
        elif task_runs.thisN == 3:
            run_break_txt = "You have completed Task Block #4. \n \n Task Block #5 will begin shortly."
        elif task_runs.thisN == 4:
            run_break_txt = "You have completed Task Block #5. \n \n Task Block #6 will begin shortly."
        elif task_runs.thisN == 5:
            run_break_txt = "You have completed Task Block #6. \n \n Task Block #7 will begin shortly."
        elif task_runs.thisN == 6:
            run_break_txt = "You have completed Task Block #7. \n \n Task Block #8 will begin shortly."
        elif task_runs.thisN == 7:
            run_break_txt = "You have completed Task Block #8. \n \n Task Block #9 will begin shortly."
        elif task_runs.thisN == 8:
            run_break_txt = "You have completed Task Block #9. \n \n Task Block #10 will begin shortly."
        elif task_runs.thisN == 9:
            run_break_txt = "You have completed Task Block #10. \n \n Task Block #11 will begin shortly."
        elif task_runs.thisN == 10:
            run_break_txt = "You have completed Task Block #11. \n \n Task Block #12 will begin shortly."
        else: #11
            run_break_txt = "You have completed the final Task Block. Thank you for your all hard work!"
        cpdm_run_break_txt.setText(run_break_txt)
        cpdm_run_break_resp.keys = []
        cpdm_run_break_resp.rt = []
        _cpdm_run_break_resp_allKeys = []
        # keep track of which components have finished
        crdm_run_breakComponents = [cpdm_run_break_txt, cpdm_run_break_resp]
        for thisComponent in crdm_run_breakComponents:
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
        
        # --- Run Routine "crdm_run_break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cpdm_run_break_txt* updates
            
            # if cpdm_run_break_txt is starting this frame...
            if cpdm_run_break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cpdm_run_break_txt.frameNStart = frameN  # exact frame index
                cpdm_run_break_txt.tStart = t  # local t and not account for scr refresh
                cpdm_run_break_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cpdm_run_break_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                cpdm_run_break_txt.status = STARTED
                cpdm_run_break_txt.setAutoDraw(True)
            
            # if cpdm_run_break_txt is active this frame...
            if cpdm_run_break_txt.status == STARTED:
                # update params
                pass
            
            # *cpdm_run_break_resp* updates
            waitOnFlip = False
            
            # if cpdm_run_break_resp is starting this frame...
            if cpdm_run_break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cpdm_run_break_resp.frameNStart = frameN  # exact frame index
                cpdm_run_break_resp.tStart = t  # local t and not account for scr refresh
                cpdm_run_break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cpdm_run_break_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                cpdm_run_break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(cpdm_run_break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(cpdm_run_break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if cpdm_run_break_resp.status == STARTED and not waitOnFlip:
                theseKeys = cpdm_run_break_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _cpdm_run_break_resp_allKeys.extend(theseKeys)
                if len(_cpdm_run_break_resp_allKeys):
                    cpdm_run_break_resp.keys = _cpdm_run_break_resp_allKeys[-1].name  # just the last key pressed
                    cpdm_run_break_resp.rt = _cpdm_run_break_resp_allKeys[-1].rt
                    cpdm_run_break_resp.duration = _cpdm_run_break_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crdm_run_breakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crdm_run_break" ---
        for thisComponent in crdm_run_breakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "crdm_run_break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'task_runs'
    
    # get names of stimulus parameters
    if task_runs.trialList in ([], [None], None):
        params = []
    else:
        params = task_runs.trialList[0].keys()
    # save data for this loop
    task_runs.saveAsText(filename + 'task_runs.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "ETTSA_end" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from TSA_close_PY
    #device.tsa2_close()
    # keep track of which components have finished
    ETTSA_endComponents = []
    for thisComponent in ETTSA_endComponents:
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
    
    # --- Run Routine "ETTSA_end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ETTSA_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ETTSA_end" ---
    for thisComponent in ETTSA_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ETTSA_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "crdm_bonus" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('crdm_bonus.started', globalClock.getTime())
    # Run 'Begin Routine' code from crdm_bonus_py
    ##indexing examples
    ##certain chosen - ("sure", crdm_sure_amt, crdm_img, crdm_lott_top, crdm_lott_bot, crdm_nonzero_side, crdm_domain)
    ##lotto chosen - ("lott", "?", crdm_img, crdm_lott_top, crdm_lott_bot, crdm_nonzero_side, crdm_domain))
    
    earnings_text = ""
    idx = int(random.random() * len(earnings)) ##random selection of bonus trial
    choice, money, trial_img, top, bottom, winning_side, domain = earnings[idx]
    my_loop.addData("bonus_choice", choice) ##record bonus trial choice
    
    ##text for bonus payment screen
    if choice == "sure": ##Ss chose certain $5
        earnings_text = "In the randomly selected trial, you chose: \n \n A CERTAIN $" + str(money)
    else: ##Ss chose lottery
        earnings_text = "In the randomly selected trial, you chose: \n \n PLAY THE LOTTERY! \n \n You will now draw a chip from the lottery bag with these odds. \n \n Good luck!"
    crdm_bonus_img_2.setImage("images/" + trial_img)
    crdm_bonus_sure_txt.setText(str("$"+str(money)))
    crdm_bonus_box.setText(earnings_text)
    crdm_bonus_lott_top_2.setText(str("$"+str(top)))
    crdm_bonus_lott_bot_2.setText(str("$"+str(bottom)))
    crdm_bonus_resp_2.keys = []
    crdm_bonus_resp_2.rt = []
    _crdm_bonus_resp_2_allKeys = []
    # keep track of which components have finished
    crdm_bonusComponents = [crdm_bonus_img_2, crdm_bonus_thanks_txt_2, crdm_bonus_sure_txt, crdm_bonus_box, crdm_bonus_lott_top_2, crdm_bonus_lott_bot_2, crdm_bonus_space_txt_2, crdm_bonus_resp_2]
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
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *crdm_bonus_img_2* updates
        
        # if crdm_bonus_img_2 is starting this frame...
        if crdm_bonus_img_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_img_2.frameNStart = frameN  # exact frame index
            crdm_bonus_img_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_img_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_img_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_img_2.status = STARTED
            crdm_bonus_img_2.setAutoDraw(True)
        
        # if crdm_bonus_img_2 is active this frame...
        if crdm_bonus_img_2.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_thanks_txt_2* updates
        
        # if crdm_bonus_thanks_txt_2 is starting this frame...
        if crdm_bonus_thanks_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_thanks_txt_2.frameNStart = frameN  # exact frame index
            crdm_bonus_thanks_txt_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_thanks_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_thanks_txt_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_thanks_txt_2.status = STARTED
            crdm_bonus_thanks_txt_2.setAutoDraw(True)
        
        # if crdm_bonus_thanks_txt_2 is active this frame...
        if crdm_bonus_thanks_txt_2.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_sure_txt* updates
        
        # if crdm_bonus_sure_txt is starting this frame...
        if crdm_bonus_sure_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_sure_txt.frameNStart = frameN  # exact frame index
            crdm_bonus_sure_txt.tStart = t  # local t and not account for scr refresh
            crdm_bonus_sure_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_sure_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_sure_txt.status = STARTED
            crdm_bonus_sure_txt.setAutoDraw(True)
        
        # if crdm_bonus_sure_txt is active this frame...
        if crdm_bonus_sure_txt.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_box* updates
        
        # if crdm_bonus_box is starting this frame...
        if crdm_bonus_box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_box.frameNStart = frameN  # exact frame index
            crdm_bonus_box.tStart = t  # local t and not account for scr refresh
            crdm_bonus_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_box, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_box.status = STARTED
            crdm_bonus_box.setAutoDraw(True)
        
        # if crdm_bonus_box is active this frame...
        if crdm_bonus_box.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_lott_top_2* updates
        
        # if crdm_bonus_lott_top_2 is starting this frame...
        if crdm_bonus_lott_top_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_lott_top_2.frameNStart = frameN  # exact frame index
            crdm_bonus_lott_top_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_lott_top_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_lott_top_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_lott_top_2.status = STARTED
            crdm_bonus_lott_top_2.setAutoDraw(True)
        
        # if crdm_bonus_lott_top_2 is active this frame...
        if crdm_bonus_lott_top_2.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_lott_bot_2* updates
        
        # if crdm_bonus_lott_bot_2 is starting this frame...
        if crdm_bonus_lott_bot_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_lott_bot_2.frameNStart = frameN  # exact frame index
            crdm_bonus_lott_bot_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_lott_bot_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_lott_bot_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_lott_bot_2.status = STARTED
            crdm_bonus_lott_bot_2.setAutoDraw(True)
        
        # if crdm_bonus_lott_bot_2 is active this frame...
        if crdm_bonus_lott_bot_2.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_space_txt_2* updates
        
        # if crdm_bonus_space_txt_2 is starting this frame...
        if crdm_bonus_space_txt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_space_txt_2.frameNStart = frameN  # exact frame index
            crdm_bonus_space_txt_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_space_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_space_txt_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_space_txt_2.status = STARTED
            crdm_bonus_space_txt_2.setAutoDraw(True)
        
        # if crdm_bonus_space_txt_2 is active this frame...
        if crdm_bonus_space_txt_2.status == STARTED:
            # update params
            pass
        
        # *crdm_bonus_resp_2* updates
        waitOnFlip = False
        
        # if crdm_bonus_resp_2 is starting this frame...
        if crdm_bonus_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            crdm_bonus_resp_2.frameNStart = frameN  # exact frame index
            crdm_bonus_resp_2.tStart = t  # local t and not account for scr refresh
            crdm_bonus_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(crdm_bonus_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            crdm_bonus_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(crdm_bonus_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(crdm_bonus_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if crdm_bonus_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = crdm_bonus_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _crdm_bonus_resp_2_allKeys.extend(theseKeys)
            if len(_crdm_bonus_resp_2_allKeys):
                crdm_bonus_resp_2.keys = _crdm_bonus_resp_2_allKeys[-1].name  # just the last key pressed
                crdm_bonus_resp_2.rt = _crdm_bonus_resp_2_allKeys[-1].rt
                crdm_bonus_resp_2.duration = _crdm_bonus_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
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
    thisExp.addData('crdm_bonus.stopped', globalClock.getTime())
    # the Routine "crdm_bonus" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
