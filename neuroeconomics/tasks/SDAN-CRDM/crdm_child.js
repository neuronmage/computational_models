/******************* 
 * Crdm_Child *
 *******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.2.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'crdm_child';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from crdm_instr1_py
/* Syntax Error: Fix Python code */
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
flowScheduler.add(crdm_instrV_2RoutineBegin());
flowScheduler.add(crdm_instrV_2RoutineEachFrame());
flowScheduler.add(crdm_instrV_2RoutineEnd());
flowScheduler.add(crdm_pract_instrRoutineBegin());
flowScheduler.add(crdm_pract_instrRoutineEachFrame());
flowScheduler.add(crdm_pract_instrRoutineEnd());
const crdm_pract_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crdm_pract_trialsLoopBegin(crdm_pract_trialsLoopScheduler));
flowScheduler.add(crdm_pract_trialsLoopScheduler);
flowScheduler.add(crdm_pract_trialsLoopEnd);





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
    {'name': 'crdm_child_practice.csv', 'path': 'crdm_child_practice.csv'},
    {'name': 'crdm_child_trials.csv', 'path': 'crdm_child_trials.csv'},
    {'name': 'images/crdm_instrV5.mp4', 'path': 'images/crdm_instrV5.mp4'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'images/machine_sure1.png', 'path': 'images/machine_sure1.png'},
    {'name': 'crdm_child_trials_TEST.csv', 'path': 'crdm_child_trials_TEST.csv'},
    {'name': 'crdm_child_practice.csv', 'path': 'crdm_child_practice.csv'},
    {'name': 'crdm_child_trials.csv', 'path': 'crdm_child_trials.csv'},
    {'name': 'images/crdm_instrV5.mp4', 'path': 'images/crdm_instrV5.mp4'},
    {'name': 'images/machine_b2_r6.png', 'path': 'images/machine_b2_r6.png'},
    {'name': 'images/machine_b4_r4.png', 'path': 'images/machine_b4_r4.png'},
    {'name': 'images/machine_b6_r2.png', 'path': 'images/machine_b6_r2.png'},
    {'name': 'images/machine_sure1.png', 'path': 'images/machine_sure1.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/sub-${expInfo["participant"]}/sub-${expInfo["participant"]}_ses${expInfo["session"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var crdm_instr1Clock;
var random;
var earnings;
var crdm_instr1_title_txt;
var crdm_instr1_txt;
var crdm_instr1_space_txt;
var crdm_instr1_resp;
var crdm_instrV_2Clock;
var crdm_instrV_movClock;
var crdm_instrV_mov;
var crdm_pract_instrClock;
var crdm_pract_instr_name_txt;
var crdm_pract_instr_txt;
var crdm_pract_instr_space_txt;
var crdm_pract_instr_key;
var crdm_pract_trialClock;
var sure_pos;
var sure_resp;
var crdm_msg;
var pos;
var txt;
var left;
var right;
var resp;
var crdm_pract_trial_lott_img;
var crdm_pract_trial_lott_left_txt;
var crdm_pract_trial_lott_right_txt;
var crdm_pract_trial_OR_txt;
var crdm_pract_trial_sure_img;
var crdm_pract_trial_sure_txt;
var GRFX_fix2;
var crdm_pract_trial_cue;
var crdm_pract_trial_resp;
var crdm_pract_feedbackClock;
var crdm_pract_feedback_txt;
var crdm_pract_confClock;
var crdm_pract_conf_txt;
var crdm_pract_conf1;
var crdm_pract_conf1_txt;
var crdm_pract_conf2;
var crdm_pract_conf2_txt;
var crdm_pract_conf3;
var crdm_pract_conf3_txt;
var crdm_pract_conf4;
var crdm_pract_conf4_txt;
var crdm_pract_conf_resp;
var crdm_pract_itiClock;
var crdm_pract_iti1_poly;
var crdm_trial_instrClock;
var crdm_trial_instr_title_txt;
var crdm_trial_instr_txt;
var crdm_trial_instr_space_txt;
var crdm_trial_instr_resp;
var crdm_init_fixClock;
var crdm_init_fix_poly;
var crdm_trialClock;
var crdm_trial_lott_img;
var crdm_trial_sure_img;
var crdm_trial_lott_left_txt;
var crdm_trial_lott_right_txt;
var crdm_trial_OR_txt;
var crdm_trial_sure_txt;
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
var crdm_trial_itiClock;
var crdm_trial_iti1_poly;
var crdm_bonusClock;
var crdm_bonus_img;
var crdm_bonus_thanks_txt;
var crdm_bonus_lott_left_txt;
var crdm_bonus_sure_center_txt;
var crdm_bonus_lott_right_txt;
var crdm_bonus_prompt_txt;
var crdm_bonus_choice_text_txt;
var crdm_bonus_choice_outcome_txt;
var crdm_bonus_drawn_txt;
var crdm_bonus_gumball_poly;
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
  
  earnings = []
  // Run 'Begin Experiment' code from crdm_instr1_py
  earnings = [];
  
  crdm_instr1_title_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr1_title_txt',
    text: '* The Lottery Game *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_instr1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_instr1_txt',
    text: 'In this game, you will make choices between: \n\n\n- Gaining/losing a certain amount \nOR\n- Playing a lottery for the chance to win a larger gain or smaller loss ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
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
    depth: -4.0 
  });
  
  crdm_instr1_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_instrV_2"
  crdm_instrV_2Clock = new util.Clock();
  crdm_instrV_movClock = new util.Clock();
  crdm_instrV_mov = new visual.MovieStim({
    win: psychoJS.window,
    name: 'crdm_instrV_mov',
    units: 'pix',
    movie: undefined,
    pos: [0, 0],
    anchor: 'center',
    size: [1920, 1080],
    ori: 0.0,
    opacity: undefined,
    loop: false,
    noAudio: false,
    depth: 0
    });
  // Initialize components for Routine "crdm_pract_instr"
  crdm_pract_instrClock = new util.Clock();
  crdm_pract_instr_name_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_instr_name_txt',
    text: '* The Lottery Game *',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: 0.0 
  });
  
  crdm_pract_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_instr_txt',
    text: "Let's practice how to play! When you see a green circle:\n\nPress 1 ----> LEFT Gumball Machine \nPress 2 ----> RIGHT Gumball Machine\n\nThen we'll ask how sure you are that you picked your favorite.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_pract_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract_instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract_trial"
  crdm_pract_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from crdm_pract_trial_py
  sure_pos = [];
  sure_resp = [];
  crdm_msg = "";
  pos = [[(- 0.5), 0], [0.5, 0]];
  txt = [[(- 0.5), 0.15], [0.5, 0.15]];
  left = [[(- 0.565), 0.15], [0.435, 0.15]];
  right = [[(- 0.435), 0.15], [0.565, 0.15]];
  resp = ["1", "2"];
  
  crdm_pract_trial_lott_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_pract_trial_lott_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_pract_trial_lott_left_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_trial_lott_left_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 0.2157), 0.1686, 0.8588]),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_pract_trial_lott_right_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_trial_lott_right_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7255, (- 0.8431), (- 0.5294)]),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_pract_trial_OR_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_trial_OR_txt',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_pract_trial_sure_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_pract_trial_sure_img', units : undefined, 
    image : 'images/machine_sure1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  crdm_pract_trial_sure_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_trial_sure_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -6.0 
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
    opacity: undefined, depth: -7, interpolate: true,
  });
  
  crdm_pract_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_pract_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  crdm_pract_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract_feedback"
  crdm_pract_feedbackClock = new util.Clock();
  crdm_pract_feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "crdm_pract_conf"
  crdm_pract_confClock = new util.Clock();
  crdm_pract_conf_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_conf_txt',
    text: 'Are you sure you picked your favorite?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  crdm_pract_conf1 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract_conf1', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.6), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  crdm_pract_conf1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_conf1_txt',
    text: "Don't know if \nI picked my \nfavorite\n\n1",
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.6), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_pract_conf2 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract_conf2', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [(- 0.2), (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  crdm_pract_conf2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_conf2_txt',
    text: 'Maybe I picked \nmy favorite\n\n\n2',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_pract_conf3 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract_conf3', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.2, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  crdm_pract_conf3_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_conf3_txt',
    text: 'Pretty sure I \npicked my \nfavorite\n\n3',
    font: 'Arial',
    units: undefined, 
    pos: [0.2, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  crdm_pract_conf4 = new visual.Rect ({
    win: psychoJS.window, name: 'crdm_pract_conf4', 
    width: [0.3, 0.3][0], height: [0.3, 0.3][1],
    ori: 0.0, pos: [0.6, (- 0.3)],
    anchor: 'center',
    lineWidth: 10.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  crdm_pract_conf4_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_pract_conf4_txt',
    text: 'I definitely \npicked my \nfavorite\n\n4',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  crdm_pract_conf_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_pract_iti"
  crdm_pract_itiClock = new util.Clock();
  crdm_pract_iti1_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_pract_iti1_poly', 
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
    text: '* The Lottery Game *',
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
    text: "Now we're about to begin the real game!\n\nPlease focus on the white cross when it appears onscreen. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 1.25, ori: 0.0,
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
  // Run 'Begin Experiment' code from crdm_trial_py
  sure_pos = [];
  sure_resp = [];
  crdm_msg = "";
  pos = [[(- 0.5), 0], [0.5, 0]];
  txt = [[(- 0.5), 0.15], [0.5, 0.15]];
  left = [[(- 0.565), 0.15], [0.435, 0.15]];
  right = [[(- 0.435), 0.15], [0.565, 0.15]];
  resp = ["1", "2"];
  crdm_trial_lott_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_trial_lott_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_trial_sure_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_trial_sure_img', units : undefined, 
    image : 'images/machine_sure1.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.3, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  crdm_trial_lott_left_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_lott_left_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 0.2157), 0.1686, 0.8588]),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_trial_lott_right_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_lott_right_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7255, (- 0.8431), (- 0.5294)]),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_trial_OR_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_OR_txt',
    text: 'OR',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  crdm_trial_sure_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_trial_sure_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -6.0 
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
    opacity: undefined, depth: -7, interpolate: true,
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
    opacity: undefined, depth: -8, interpolate: true,
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
    text: 'Are you sure you picked your favorite?',
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
    text: "Don't know if \nI picked my \nfavorite\n\n1",
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
    text: 'Maybe I picked \nmy favorite\n\n\n2',
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
    text: 'Pretty sure I \npicked my \nfavorite\n\n3',
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
    text: 'I definitely \npicked my \nfavorite\n\n4',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  crdm_conf_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crdm_trial_iti"
  crdm_trial_itiClock = new util.Clock();
  crdm_trial_iti1_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'crdm_trial_iti1_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "crdm_bonus"
  crdm_bonusClock = new util.Clock();
  crdm_bonus_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'crdm_bonus_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0.5, 0], size : [0.3, 0.6],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  crdm_bonus_thanks_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_thanks_txt',
    text: '** The Lottery Game Bonus Trial ** ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], height: 0.06,  wrapWidth: 1.35, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -2.0 
  });
  
  crdm_bonus_lott_left_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_lott_left_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.435, 0.15], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  crdm_bonus_sure_center_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_sure_center_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.5, 0.15], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  crdm_bonus_lott_right_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'crdm_bonus_lott_right_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.565, 0.15], height: 0.04,  wrapWidth: undefined, ori: 0.0,
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
  
  crdm_bonus_gumball_poly = new visual.Polygon({
    win: psychoJS.window, name: 'crdm_bonus_gumball_poly', 
    edges: 100, size:[0.075, 0.075],
    ori: 0.0, pos: [0.05, 0],
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
var practice_loop_name;
var loop_name;
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
    // Run 'Begin Routine' code from crdm_instr1_py
    practice_loop_name = "crdm_pract_trials";
    loop_name = "crdm_trials";
    
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


var crdm_instrV_2Components;
function crdm_instrV_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_instrV_2' ---
    t = 0;
    crdm_instrV_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(613.000000);
    // update component parameters for each repeat
    crdm_instrV_mov.setMovie('images/crdm_instrV5.mp4');
    // keep track of which components have finished
    crdm_instrV_2Components = [];
    crdm_instrV_2Components.push(crdm_instrV_mov);
    
    for (const thisComponent of crdm_instrV_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function crdm_instrV_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_instrV_2' ---
    // get current time
    t = crdm_instrV_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_instrV_mov* updates
    if (t >= 0.0 && crdm_instrV_mov.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_instrV_mov.tStart = t;  // (not accounting for frame time here)
      crdm_instrV_mov.frameNStart = frameN;  // exact frame index
      
      crdm_instrV_mov.setAutoDraw(true);
      crdm_instrV_mov.play();
    }
    
    frameRemains = 0.0 + 613.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_instrV_mov.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_instrV_mov.setAutoDraw(false);
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
    for (const thisComponent of crdm_instrV_2Components)
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


function crdm_instrV_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_instrV_2' ---
    for (const thisComponent of crdm_instrV_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    crdm_instrV_mov.stop();  // ensure movie has stopped at end of Routine
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _crdm_pract_instr_key_allKeys;
var crdm_pract_instrComponents;
function crdm_pract_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_instr' ---
    t = 0;
    crdm_pract_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    crdm_pract_instr_key.keys = undefined;
    crdm_pract_instr_key.rt = undefined;
    _crdm_pract_instr_key_allKeys = [];
    // keep track of which components have finished
    crdm_pract_instrComponents = [];
    crdm_pract_instrComponents.push(crdm_pract_instr_name_txt);
    crdm_pract_instrComponents.push(crdm_pract_instr_txt);
    crdm_pract_instrComponents.push(crdm_pract_instr_space_txt);
    crdm_pract_instrComponents.push(crdm_pract_instr_key);
    
    for (const thisComponent of crdm_pract_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_instr' ---
    // get current time
    t = crdm_pract_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract_instr_name_txt* updates
    if (t >= 0.0 && crdm_pract_instr_name_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_instr_name_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_instr_name_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_instr_name_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract_instr_txt* updates
    if (t >= 0.0 && crdm_pract_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_instr_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_instr_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_instr_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract_instr_space_txt* updates
    if (t >= 0.0 && crdm_pract_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *crdm_pract_instr_key* updates
    if (t >= 0.0 && crdm_pract_instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_instr_key.tStart = t;  // (not accounting for frame time here)
      crdm_pract_instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract_instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_instr_key.clearEvents(); });
    }
    
    if (crdm_pract_instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract_instr_key.getKeys({keyList: ['space'], waitRelease: false});
      _crdm_pract_instr_key_allKeys = _crdm_pract_instr_key_allKeys.concat(theseKeys);
      if (_crdm_pract_instr_key_allKeys.length > 0) {
        crdm_pract_instr_key.keys = _crdm_pract_instr_key_allKeys[_crdm_pract_instr_key_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract_instr_key.rt = _crdm_pract_instr_key_allKeys[_crdm_pract_instr_key_allKeys.length - 1].rt;
        crdm_pract_instr_key.duration = _crdm_pract_instr_key_allKeys[_crdm_pract_instr_key_allKeys.length - 1].duration;
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
    for (const thisComponent of crdm_pract_instrComponents)
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


function crdm_pract_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_instr' ---
    for (const thisComponent of crdm_pract_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    crdm_pract_instr_key.stop();
    // the Routine "crdm_pract_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract_trials;
function crdm_pract_trialsLoopBegin(crdm_pract_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crdm_pract_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crdm_child_practice.csv',
      seed: undefined, name: 'crdm_pract_trials'
    });
    psychoJS.experiment.addLoop(crdm_pract_trials); // add the loop to the experiment
    currentLoop = crdm_pract_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrdm_pract_trial of crdm_pract_trials) {
      snapshot = crdm_pract_trials.getSnapshot();
      crdm_pract_trialsLoopScheduler.add(importConditions(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_trialRoutineBegin(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_trialRoutineEachFrame());
      crdm_pract_trialsLoopScheduler.add(crdm_pract_trialRoutineEnd(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_feedbackRoutineBegin(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_feedbackRoutineEachFrame());
      crdm_pract_trialsLoopScheduler.add(crdm_pract_feedbackRoutineEnd(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_confRoutineBegin(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_confRoutineEachFrame());
      crdm_pract_trialsLoopScheduler.add(crdm_pract_confRoutineEnd(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_itiRoutineBegin(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_itiRoutineEachFrame());
      crdm_pract_trialsLoopScheduler.add(crdm_pract_itiRoutineEnd(snapshot));
      crdm_pract_trialsLoopScheduler.add(crdm_pract_trialsLoopEndIteration(crdm_pract_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crdm_pract_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crdm_pract_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crdm_pract_trialsLoopEndIteration(scheduler, snapshot) {
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
      trialList: 'crdm_child_trials.csv',
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
      crdm_trialsLoopScheduler.add(crdm_trial_itiRoutineBegin(snapshot));
      crdm_trialsLoopScheduler.add(crdm_trial_itiRoutineEachFrame());
      crdm_trialsLoopScheduler.add(crdm_trial_itiRoutineEnd(snapshot));
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
var idx;
var lott_pos;
var left_pos;
var right_pos;
var sure_txt;
var _crdm_pract_trial_resp_allKeys;
var crdm_pract_trialComponents;
function crdm_pract_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_trial' ---
    t = 0;
    crdm_pract_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_pract_trial_py
    my_loop = eval(practice_loop_name);
    idx = random.randint(0,1);
    sure_resp = resp[idx];
    if ((idx === 0)) {
        lott_pos = pos[1];
        left_pos = left[1];
        right_pos = right[1];
        sure_pos = pos[0];
        sure_txt = txt[0];
    } else {
        lott_pos = pos[0];
        left_pos = left[0];
        right_pos = right[0];
        sure_pos = pos[1];
        sure_txt = txt[1];
    }
    
    crdm_pract_trial_lott_img.setPos(lott_pos);
    crdm_pract_trial_lott_img.setImage(("images/" + crdm_img));
    crdm_pract_trial_lott_left_txt.setPos(left_pos);
    crdm_pract_trial_lott_left_txt.setText(("$" + crdm_lott_left.toString()).toString());
    crdm_pract_trial_lott_right_txt.setPos(right_pos);
    crdm_pract_trial_lott_right_txt.setText(("$" + crdm_lott_right.toString()).toString());
    crdm_pract_trial_sure_img.setPos(sure_pos);
    crdm_pract_trial_sure_txt.setPos(sure_txt);
    crdm_pract_trial_sure_txt.setText(("$" + crdm_sure_amt.toString()).toString());
    crdm_pract_trial_resp.keys = undefined;
    crdm_pract_trial_resp.rt = undefined;
    _crdm_pract_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_pract_trialComponents = [];
    crdm_pract_trialComponents.push(crdm_pract_trial_lott_img);
    crdm_pract_trialComponents.push(crdm_pract_trial_lott_left_txt);
    crdm_pract_trialComponents.push(crdm_pract_trial_lott_right_txt);
    crdm_pract_trialComponents.push(crdm_pract_trial_OR_txt);
    crdm_pract_trialComponents.push(crdm_pract_trial_sure_img);
    crdm_pract_trialComponents.push(crdm_pract_trial_sure_txt);
    crdm_pract_trialComponents.push(GRFX_fix2);
    crdm_pract_trialComponents.push(crdm_pract_trial_cue);
    crdm_pract_trialComponents.push(crdm_pract_trial_resp);
    
    for (const thisComponent of crdm_pract_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_trial' ---
    // get current time
    t = crdm_pract_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract_trial_lott_img* updates
    if (t >= 0.0 && crdm_pract_trial_lott_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_lott_img.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_lott_img.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_lott_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_lott_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_lott_img.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_lott_left_txt* updates
    if (t >= 0.0 && crdm_pract_trial_lott_left_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_lott_left_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_lott_left_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_lott_left_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_lott_left_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_lott_left_txt.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_lott_right_txt* updates
    if (t >= 0.0 && crdm_pract_trial_lott_right_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_lott_right_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_lott_right_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_lott_right_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_lott_right_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_lott_right_txt.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_OR_txt* updates
    if (t >= 0.0 && crdm_pract_trial_OR_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_OR_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_OR_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_OR_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_OR_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_OR_txt.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_sure_img* updates
    if (t >= 0.0 && crdm_pract_trial_sure_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_sure_img.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_sure_img.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_sure_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_sure_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_sure_img.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_sure_txt* updates
    if (t >= 0.0 && crdm_pract_trial_sure_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_sure_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_sure_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_sure_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_sure_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_sure_txt.setAutoDraw(false);
    }
    
    // *GRFX_fix2* updates
    if (t >= 4 && GRFX_fix2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix2.tStart = t;  // (not accounting for frame time here)
      GRFX_fix2.frameNStart = frameN;  // exact frame index
      
      GRFX_fix2.setAutoDraw(true);
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix2.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_cue* updates
    if (t >= 4 && crdm_pract_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_pract_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_pract_trial_resp* updates
    if (t >= 4 && crdm_pract_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_pract_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_trial_resp.clearEvents(); });
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_pract_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_pract_trial_resp_allKeys = _crdm_pract_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_pract_trial_resp_allKeys.length > 0) {
        crdm_pract_trial_resp.keys = _crdm_pract_trial_resp_allKeys[_crdm_pract_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract_trial_resp.rt = _crdm_pract_trial_resp_allKeys[_crdm_pract_trial_resp_allKeys.length - 1].rt;
        crdm_pract_trial_resp.duration = _crdm_pract_trial_resp_allKeys[_crdm_pract_trial_resp_allKeys.length - 1].duration;
        // was this correct?
        if (crdm_pract_trial_resp.keys == sure_resp) {
            crdm_pract_trial_resp.corr = 1;
        } else {
            crdm_pract_trial_resp.corr = 0;
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
    for (const thisComponent of crdm_pract_trialComponents)
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


var pract_key;
var pract_sure_key;
function crdm_pract_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_trial' ---
    for (const thisComponent of crdm_pract_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from crdm_pract_trial_py
    pract_key = crdm_pract_trial_resp.keys;
    pract_sure_key = crdm_pract_trial_resp.corr;
    my_loop.addData("crdm_trial_type", "practice");
    
    // was no response the correct answer?!
    if (crdm_pract_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(sure_resp)) {
         crdm_pract_trial_resp.corr = 1;  // correct non-response
      } else {
         crdm_pract_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_pract_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_pract_trial_resp.keys', crdm_pract_trial_resp.keys);
    psychoJS.experiment.addData('crdm_pract_trial_resp.corr', crdm_pract_trial_resp.corr);
    if (typeof crdm_pract_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_pract_trial_resp.rt', crdm_pract_trial_resp.rt);
        psychoJS.experiment.addData('crdm_pract_trial_resp.duration', crdm_pract_trial_resp.duration);
        routineTimer.reset();
        }
    
    crdm_pract_trial_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract_feedbackComponents;
function crdm_pract_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_feedback' ---
    t = 0;
    crdm_pract_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_pract_feedback_py
    if ((pract_key === undefined)) {
        crdm_msg = "NO RESPONSE";
    } else {
        if (pract_sure_key) {
            crdm_msg = ("CERTAIN $" + crdm_sure_amt.toString());
        } else {
            crdm_msg = "PLAY THE LOTTERY";
        }
    }
    
    crdm_pract_feedback_txt.setText(crdm_msg);
    // keep track of which components have finished
    crdm_pract_feedbackComponents = [];
    crdm_pract_feedbackComponents.push(crdm_pract_feedback_txt);
    
    for (const thisComponent of crdm_pract_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_feedback' ---
    // get current time
    t = crdm_pract_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract_feedback_txt* updates
    if (t >= 0.0 && crdm_pract_feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_feedback_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_feedback_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_feedback_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_feedback_txt.setAutoDraw(false);
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
    for (const thisComponent of crdm_pract_feedbackComponents)
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


function crdm_pract_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_feedback' ---
    for (const thisComponent of crdm_pract_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
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
var _crdm_pract_conf_resp_allKeys;
var crdm_pract_confComponents;
function crdm_pract_confRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_conf' ---
    t = 0;
    crdm_pract_confClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_pract_conf_py
    if ((pract_key === undefined)) {
        continueRoutine = false;
    }
    conf1_color = [0, 0, 0];
    conf2_color = [0, 0, 0];
    conf3_color = [0, 0, 0];
    conf4_color = [0, 0, 0];
    
    crdm_pract_conf_resp.keys = undefined;
    crdm_pract_conf_resp.rt = undefined;
    _crdm_pract_conf_resp_allKeys = [];
    // keep track of which components have finished
    crdm_pract_confComponents = [];
    crdm_pract_confComponents.push(crdm_pract_conf_txt);
    crdm_pract_confComponents.push(crdm_pract_conf1);
    crdm_pract_confComponents.push(crdm_pract_conf1_txt);
    crdm_pract_confComponents.push(crdm_pract_conf2);
    crdm_pract_confComponents.push(crdm_pract_conf2_txt);
    crdm_pract_confComponents.push(crdm_pract_conf3);
    crdm_pract_confComponents.push(crdm_pract_conf3_txt);
    crdm_pract_confComponents.push(crdm_pract_conf4);
    crdm_pract_confComponents.push(crdm_pract_conf4_txt);
    crdm_pract_confComponents.push(crdm_pract_conf_resp);
    
    for (const thisComponent of crdm_pract_confComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var pract_conf_key;
function crdm_pract_confRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_conf' ---
    // get current time
    t = crdm_pract_confClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from crdm_pract_conf_py
    pract_conf_key = crdm_pract_conf_resp.keys;
    if (!(pract_conf_key === undefined) && (pract_conf_key.length === 1)) {
        if ((pract_conf_key === "1")) {
            conf1_color = "darkgray";
            conf2_color = [0, 0, 0];
            conf3_color = [0, 0, 0];
            conf4_color = [0, 0, 0];
        } else {
            if ((pract_conf_key === "2")) {
                conf1_color = [0, 0, 0];
                conf2_color = "darkgray";
                conf3_color = [0, 0, 0];
                conf4_color = [0, 0, 0];
            } else {
                if ((pract_conf_key === "3")) {
                    conf1_color = [0, 0, 0];
                    conf2_color = [0, 0, 0];
                    conf3_color = "darkgray";
                    conf4_color = [0, 0, 0];
                } else {
                    if ((pract_conf_key === "4")) {
                        conf1_color = [0, 0, 0];
                        conf2_color = [0, 0, 0];
                        conf3_color = [0, 0, 0];
                        conf4_color = "darkgray";
                    }
                }
            }
        }
    }
    
    
    // *crdm_pract_conf_txt* updates
    if (t >= 0.0 && crdm_pract_conf_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf_txt.setAutoDraw(false);
    }
    
    if (crdm_pract_conf1.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract_conf1.setFillColor(new util.Color(conf1_color), false);
    }
    
    // *crdm_pract_conf1* updates
    if (t >= 0.0 && crdm_pract_conf1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf1.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf1.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf1.setAutoDraw(false);
    }
    
    // *crdm_pract_conf1_txt* updates
    if (t >= 0.0 && crdm_pract_conf1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf1_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf1_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf1_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf1_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf1_txt.setAutoDraw(false);
    }
    
    if (crdm_pract_conf2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract_conf2.setFillColor(new util.Color(conf2_color), false);
    }
    
    // *crdm_pract_conf2* updates
    if (t >= 0.0 && crdm_pract_conf2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf2.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf2.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf2.setAutoDraw(false);
    }
    
    // *crdm_pract_conf2_txt* updates
    if (t >= 0.0 && crdm_pract_conf2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf2_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf2_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf2_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf2_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf2_txt.setAutoDraw(false);
    }
    
    if (crdm_pract_conf3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract_conf3.setFillColor(new util.Color(conf3_color), false);
    }
    
    // *crdm_pract_conf3* updates
    if (t >= 0.0 && crdm_pract_conf3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf3.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf3.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf3.setAutoDraw(false);
    }
    
    // *crdm_pract_conf3_txt* updates
    if (t >= 0.0 && crdm_pract_conf3_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf3_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf3_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf3_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf3_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf3_txt.setAutoDraw(false);
    }
    
    if (crdm_pract_conf4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      crdm_pract_conf4.setFillColor(new util.Color(conf4_color), false);
    }
    
    // *crdm_pract_conf4* updates
    if (t >= 0.0 && crdm_pract_conf4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf4.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf4.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf4.setAutoDraw(false);
    }
    
    // *crdm_pract_conf4_txt* updates
    if (t >= 0.0 && crdm_pract_conf4_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf4_txt.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf4_txt.frameNStart = frameN;  // exact frame index
      
      crdm_pract_conf4_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf4_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf4_txt.setAutoDraw(false);
    }
    
    // *crdm_pract_conf_resp* updates
    if (t >= 0.0 && crdm_pract_conf_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_conf_resp.tStart = t;  // (not accounting for frame time here)
      crdm_pract_conf_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_pract_conf_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_conf_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_pract_conf_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_conf_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_conf_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_pract_conf_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_pract_conf_resp.getKeys({keyList: ['1', '2', '3', '4'], waitRelease: false});
      _crdm_pract_conf_resp_allKeys = _crdm_pract_conf_resp_allKeys.concat(theseKeys);
      if (_crdm_pract_conf_resp_allKeys.length > 0) {
        crdm_pract_conf_resp.keys = _crdm_pract_conf_resp_allKeys[_crdm_pract_conf_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_pract_conf_resp.rt = _crdm_pract_conf_resp_allKeys[_crdm_pract_conf_resp_allKeys.length - 1].rt;
        crdm_pract_conf_resp.duration = _crdm_pract_conf_resp_allKeys[_crdm_pract_conf_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of crdm_pract_confComponents)
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


function crdm_pract_confRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_conf' ---
    for (const thisComponent of crdm_pract_confComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    conf1_color = [0, 0, 0];
    conf2_color = [0, 0, 0];
    conf3_color = [0, 0, 0];
    conf4_color = [0, 0, 0];
    
    crdm_pract_conf1.setFillColor(new util.Color(conf1_color), false);
    crdm_pract_conf2.setFillColor(new util.Color(conf2_color), false);
    crdm_pract_conf3.setFillColor(new util.Color(conf3_color), false);
    crdm_pract_conf4.setFillColor(new util.Color(conf4_color), false);
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(crdm_pract_conf_resp.corr, level);
    }
    psychoJS.experiment.addData('crdm_pract_conf_resp.keys', crdm_pract_conf_resp.keys);
    if (typeof crdm_pract_conf_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('crdm_pract_conf_resp.rt', crdm_pract_conf_resp.rt);
        psychoJS.experiment.addData('crdm_pract_conf_resp.duration', crdm_pract_conf_resp.duration);
        }
    
    crdm_pract_conf_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crdm_pract_itiComponents;
function crdm_pract_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_pract_iti' ---
    t = 0;
    crdm_pract_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_pract_iti1_py
    if (!(crdm_pract_trials.thisTrialN === undefined) && (crdm_pract_trials.thisTrialN === 5)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    crdm_pract_itiComponents = [];
    crdm_pract_itiComponents.push(crdm_pract_iti1_poly);
    
    for (const thisComponent of crdm_pract_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_pract_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_pract_iti' ---
    // get current time
    t = crdm_pract_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_pract_iti1_poly* updates
    if (t >= 0.0 && crdm_pract_iti1_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_pract_iti1_poly.tStart = t;  // (not accounting for frame time here)
      crdm_pract_iti1_poly.frameNStart = frameN;  // exact frame index
      
      crdm_pract_iti1_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_pract_iti1_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_pract_iti1_poly.setAutoDraw(false);
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
    for (const thisComponent of crdm_pract_itiComponents)
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


function crdm_pract_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_pract_iti' ---
    for (const thisComponent of crdm_pract_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var task_resps;
var conf_resps;
var catch_trials;
var iti_list;
var s;
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
    // Run 'Begin Routine' code from crdm_trial_instr_py
    task_resps = [];
    conf_resps = [];
    catch_trials = [];
    iti_list = function () {
        var _pj_a = [], _pj_b = util.range(180);
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(random.random());
        }
        return _pj_a;
    }
    .call(this);
    s = util.sum(iti_list);
    iti_list = function () {
        var _pj_a = [], _pj_b = iti_list;
        for (var _pj_c = 0, _pj_d = _pj_b.length; (_pj_c < _pj_d); _pj_c += 1) {
            var i = _pj_b[_pj_c];
            _pj_a.push(((i * 180) / s));
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
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stop_timer;
var stopped_time;
var lott_outcome;
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
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_trial_py
    my_loop = eval(loop_name);
    stop_timer = null;
    stopped_time = 0;
    lott_outcome = 0;
    
    idx = random.randint(0,1)
    sure_resp = resp[idx];
    if ((idx === 0)) {
        lott_pos = pos[1];
        left_pos = left[1];
        right_pos = right[1];
        sure_pos = pos[0];
        sure_txt = txt[0];
    } else {
        lott_pos = pos[0];
        left_pos = left[0];
        right_pos = right[0];
        sure_pos = pos[1];
        sure_txt = txt[1];
    }
    crdm_trial_lott_img.setPos(lott_pos);
    crdm_trial_lott_img.setImage(("images/" + crdm_img));
    crdm_trial_sure_img.setPos(sure_pos);
    crdm_trial_lott_left_txt.setPos(left_pos);
    crdm_trial_lott_left_txt.setText(("$" + crdm_lott_left.toString()).toString());
    crdm_trial_lott_right_txt.setPos(right_pos);
    crdm_trial_lott_right_txt.setText(("$" + crdm_lott_right.toString()).toString());
    crdm_trial_sure_txt.setPos(sure_txt);
    crdm_trial_sure_txt.setText(("$" + crdm_sure_amt.toString()).toString());
    crdm_trial_resp.keys = undefined;
    crdm_trial_resp.rt = undefined;
    _crdm_trial_resp_allKeys = [];
    // keep track of which components have finished
    crdm_trialComponents = [];
    crdm_trialComponents.push(crdm_trial_lott_img);
    crdm_trialComponents.push(crdm_trial_sure_img);
    crdm_trialComponents.push(crdm_trial_lott_left_txt);
    crdm_trialComponents.push(crdm_trial_lott_right_txt);
    crdm_trialComponents.push(crdm_trial_OR_txt);
    crdm_trialComponents.push(crdm_trial_sure_txt);
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
    // Run 'Each Frame' code from crdm_trial_py
    if (!(crdm_trial_resp.keys == undefined) && (crdm_trial_resp.keys.length === 1)) {
        if ((stop_timer === null)) {
            stop_timer = new util.Clock();
        } else {
            if ((stop_timer.getTime() >= 0.5)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *crdm_trial_lott_img* updates
    if (t >= 0.0 && crdm_trial_lott_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_lott_img.tStart = t;  // (not accounting for frame time here)
      crdm_trial_lott_img.frameNStart = frameN;  // exact frame index
      
      crdm_trial_lott_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_lott_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_lott_img.setAutoDraw(false);
    }
    
    // *crdm_trial_sure_img* updates
    if (t >= 0.0 && crdm_trial_sure_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_sure_img.tStart = t;  // (not accounting for frame time here)
      crdm_trial_sure_img.frameNStart = frameN;  // exact frame index
      
      crdm_trial_sure_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_sure_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_sure_img.setAutoDraw(false);
    }
    
    // *crdm_trial_lott_left_txt* updates
    if (t >= 0.0 && crdm_trial_lott_left_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_lott_left_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_lott_left_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_lott_left_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_lott_left_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_lott_left_txt.setAutoDraw(false);
    }
    
    // *crdm_trial_lott_right_txt* updates
    if (t >= 0.0 && crdm_trial_lott_right_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_lott_right_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_lott_right_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_lott_right_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_lott_right_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_lott_right_txt.setAutoDraw(false);
    }
    
    // *crdm_trial_OR_txt* updates
    if (t >= 0.0 && crdm_trial_OR_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_OR_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_OR_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_OR_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_OR_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_OR_txt.setAutoDraw(false);
    }
    
    // *crdm_trial_sure_txt* updates
    if (t >= 0.0 && crdm_trial_sure_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_sure_txt.tStart = t;  // (not accounting for frame time here)
      crdm_trial_sure_txt.frameNStart = frameN;  // exact frame index
      
      crdm_trial_sure_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_sure_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_sure_txt.setAutoDraw(false);
    }
    
    // *GRFX_fix* updates
    if (t >= 4 && GRFX_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      GRFX_fix.tStart = t;  // (not accounting for frame time here)
      GRFX_fix.frameNStart = frameN;  // exact frame index
      
      GRFX_fix.setAutoDraw(true);
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (GRFX_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      GRFX_fix.setAutoDraw(false);
    }
    
    // *crdm_trial_cue* updates
    if (t >= 4 && crdm_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_cue.tStart = t;  // (not accounting for frame time here)
      crdm_trial_cue.frameNStart = frameN;  // exact frame index
      
      crdm_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_cue.setAutoDraw(false);
    }
    
    // *crdm_trial_resp* updates
    if (t >= 4 && crdm_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_resp.tStart = t;  // (not accounting for frame time here)
      crdm_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { crdm_trial_resp.clearEvents(); });
    }
    
    frameRemains = 4 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (crdm_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = crdm_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _crdm_trial_resp_allKeys = _crdm_trial_resp_allKeys.concat(theseKeys);
      if (_crdm_trial_resp_allKeys.length > 0) {
        crdm_trial_resp.keys = _crdm_trial_resp_allKeys[_crdm_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        crdm_trial_resp.rt = _crdm_trial_resp_allKeys[_crdm_trial_resp_allKeys.length - 1].rt;
        crdm_trial_resp.duration = _crdm_trial_resp_allKeys[_crdm_trial_resp_allKeys.length - 1].duration;
        // was this correct?
        if (crdm_trial_resp.keys == sure_resp) {
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


var key;
var sure_key;
var delta_time;
function crdm_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_trial' ---
    for (const thisComponent of crdm_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from crdm_trial_py
    key = crdm_trial_resp.keys;
    sure_key = crdm_trial_resp.corr;
    my_loop.addData("crdm_trial_type", "task");
    if ((((crdm_trial_resp.rt) === undefined) || (crdm_trial_resp.rt >= (2 - 0.5)))) {
        delta_time = 0;
    } else {
        delta_time = Math.max(0, (2 - (crdm_trial_resp.rt + stopped_time)));
    }
    if (!(key === undefined) && (key.length === 1)) {
        if ((sure_key === 1)) {
            earnings.push(["sure", crdm_sure_amt, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, (- 1), crdm_nonzero_side, crdm_domain]);
            my_loop.addData("crdm_choice", 0);
            my_loop.addData("crdm_choice2", "sure");
            my_loop.addData("crdm_lott", "");
            my_loop.addData("crdm_lott2", "");
        } else {
            lott_outcome = random.choices([0, 1], [100 - Number.parseInt(crdm_lott_p), Number.parseInt(crdm_lott_p)]);
            my_loop.addData("crdm_choice", 1);
            my_loop.addData("crdm_choice2", "lott");
            my_loop.addData("crdm_lott", lott_outcome);
            if ((lott_outcome === 1)) {
                my_loop.addData("crdm_lott2", "win");
                if ((crdm_domain === "gain")) {
                    if ((Number.parseInt(crdm_lott_left) !== 0)) {
                        earnings.push(["lott", crdm_lott_left, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    } else {
                        earnings.push(["lott", crdm_lott_right, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    }
                } else {
                    if ((crdm_domain === "loss")) {
                        if ((Number.parseInt(crdm_lott_left) === 0)) {
                            earnings.push(["lott", crdm_lott_left, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        } else {
                            earnings.push(["lott", crdm_lott_right, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        }
                    }
                }
            } else {
                my_loop.addData("crdm_lott2", "lose");
                if ((crdm_domain === "gain")) {
                    if ((Number.parseInt(crdm_lott_left) === 0)) {
                        earnings.push(["lott", crdm_lott_left, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    } else {
                        earnings.push(["lott", crdm_lott_right, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                    }
                } else {
                    if ((crdm_domain === "loss")) {
                        if ((Number.parseInt(crdm_lott_left) < 0)) {
                            earnings.push(["lott", crdm_lott_left, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        } else {
                            earnings.push(["lott", crdm_lott_right, crdm_sure_amt, crdm_img, crdm_lott_left, crdm_lott_right, lott_outcome, crdm_nonzero_side, crdm_domain]);
                        }
                    }
                }
            }
        }
    }
    
    // was no response the correct answer?!
    if (crdm_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(sure_resp)) {
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
    // Run 'Begin Routine' code from crdm_feedback_py
    if ((key === undefined)) {
        crdm_msg = "NO RESPONSE";
    } else {
        if (sure_key) {
            crdm_msg = ("CERTAIN $" + crdm_sure_amt.toString());
        } else {
            crdm_msg = "PLAY THE LOTTERY";
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
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_conf_py
    if ((key === undefined)) {
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


var conf_key;
function crdm_confRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_conf' ---
    // get current time
    t = crdm_confClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from crdm_conf_py
    conf_key = crdm_conf_resp.keys;
    if (!(conf_key === undefined) && (conf_key.length === 1)) {
        if ((conf_key === "1")) {
            conf1_color = "darkgray";
            conf2_color = [0, 0, 0];
            conf3_color = [0, 0, 0];
            conf4_color = [0, 0, 0];
        } else {
            if ((conf_key === "2")) {
                conf1_color = [0, 0, 0];
                conf2_color = "darkgray";
                conf3_color = [0, 0, 0];
                conf4_color = [0, 0, 0];
            } else {
                if ((conf_key === "3")) {
                    conf1_color = [0, 0, 0];
                    conf2_color = [0, 0, 0];
                    conf3_color = "darkgray";
                    conf4_color = [0, 0, 0];
                } else {
                    if ((conf_key === "4")) {
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    
    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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


var iti_time;
var crdm_trial_itiComponents;
function crdm_trial_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crdm_trial_iti' ---
    t = 0;
    crdm_trial_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from crdm_trial_iti1_py
    iti_time = (iti_list[my_loop.thisIndex] + delta_time);
    if (!(crdm_trials.thisTrialN === undefined) && (crdm_trials.thisTrialN === 179)) {
        continueRoutine = false;
    }
    // keep track of which components have finished
    crdm_trial_itiComponents = [];
    crdm_trial_itiComponents.push(crdm_trial_iti1_poly);
    
    for (const thisComponent of crdm_trial_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crdm_trial_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crdm_trial_iti' ---
    // get current time
    t = crdm_trial_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *crdm_trial_iti1_poly* updates
    if (t >= 0.0 && crdm_trial_iti1_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_trial_iti1_poly.tStart = t;  // (not accounting for frame time here)
      crdm_trial_iti1_poly.frameNStart = frameN;  // exact frame index
      
      crdm_trial_iti1_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + iti_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (crdm_trial_iti1_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      crdm_trial_iti1_poly.setAutoDraw(false);
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
    for (const thisComponent of crdm_trial_itiComponents)
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


function crdm_trial_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crdm_trial_iti' ---
    for (const thisComponent of crdm_trial_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from crdm_trial_iti1_py
    my_loop.addData("crdm_delta_time", delta_time);
    my_loop.addData("crdm_iti_time", iti_time);
    
    // the Routine "crdm_trial_iti" was not non-slip safe, so reset the non-slip timer
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
var outcome;
var nonzero_side;
var domain;
var sure_amt;
var earnings_text;
var choice_text;
var outcome_color;
var gumball_color;
var gumball_text;
var choice_outcome;
var money_outcome;
var choice_img;
var sure_color;
var left_color;
var right_color;
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
    // Run 'Begin Routine' code from crdm_bonus_code
    exp = [];
    choice = [];
    money = [];
    trial_img = [];
    left = [];
    right = [];
    outcome = [];
    nonzero_side = [];
    domain = [];
    sure_amt = "";
    earnings_text = "";
    choice_text = "";
    outcome_color = [0, 0, 0];
    gumball_color = [0, 0, 0];
    gumball_text = "";
    choice_outcome = "";
    money_outcome = "";
    choice_img = "";
    sure_color = [0, 0, 0];
    left_color = [0, 0, 0];
    right_color = [0, 0, 0];
    idx = Number.parseInt((random.random() * earnings.length));
    console.log(earnings[idx]);
    [choice, money, sure_amt, trial_img, left, right, outcome, nonzero_side, domain] = earnings[idx];
    my_loop.addData("crdm_bonus_choice", choice);
    my_loop.addData("crdm_bonus_amt", money);
    red_nonzero = false;
    if ((nonzero_side === "right")) {
        red_nonzero = true;
    }
    if ((choice === "sure")) {
        choice_text = "*CERTAIN*";
        outcome_color = [0.7098, 0.2941, (- 0.749)];
        gumball_color = [(- 1), (- 1), (- 1)];
        gumball_text = "";
        choice_outcome = ("$" + money.toString());
        money_outcome = "";
        choice_img = "images/machine_sure1.png";
        sure_color = [(- 1), (- 1), (- 1)];
        left_color = [1, 1, 1];
        right_color = [1, 1, 1];
    } else {
        choice_text = "*PLAY THE LOTTERY*";
        choice_img = ("images/" + trial_img);
        sure_color = [1, 1, 1];
        left_color = [(- 0.2157), 0.1686, 0.8588];
        right_color = [0.9608, 0.0039, (- 0.1059)];
        if ((red_nonzero === true)) {
            if (((outcome === 1) && (domain === "gain"))) {
                outcome_color = [0.9608, 0.0039, (- 0.1059)];
                gumball_color = [0.9608, 0.0039, (- 0.1059)];
                choice_outcome = "A red gumball";
                gumball_text = "was drawn and the outcome was";
                money_outcome = ("$" + money.toString());
            } else {
                if (((outcome === 1) && (domain === "loss"))) {
                    outcome_color = [(- 0.2157), 0.1686, 0.8588];
                    gumball_color = [(- 0.2157), 0.1686, 0.8588];
                    choice_outcome = "A blue gumball";
                    gumball_text = "was drawn and the outcome was";
                    money_outcome = ("$" + money.toString());
                } else {
                    if (((outcome === 0) && (domain === "gain"))) {
                        outcome_color = [(- 0.2157), 0.1686, 0.8588];
                        gumball_color = [(- 0.2157), 0.1686, 0.8588];
                        choice_outcome = "A blue gumball";
                        gumball_text = "was drawn and the outcome was";
                        money_outcome = ("$" + money.toString());
                    } else {
                        if (((outcome === 0) && (domain === "loss"))) {
                            outcome_color = [0.9608, 0.0039, (- 0.1059)];
                            gumball_color = [0.9608, 0.0039, (- 0.1059)];
                            choice_outcome = "A red gumball";
                            gumball_text = "was drawn and the outcome was";
                            money_outcome = ("$" + money.toString());
                        }
                    }
                }
            }
        } else {
            if (((outcome === 1) && (domain === "gain"))) {
                outcome_color = [(- 0.2157), 0.1686, 0.8588];
                gumball_color = [(- 0.2157), 0.1686, 0.8588];
                choice_outcome = "A blue gumball";
                gumball_text = "was drawn and the outcome was";
                money_outcome = ("$" + money.toString());
            } else {
                if (((outcome === 1) && (domain === "loss"))) {
                    outcome_color = [0.9608, 0.0039, (- 0.1059)];
                    gumball_color = [0.9608, 0.0039, (- 0.1059)];
                    choice_outcome = "A red gumball";
                    gumball_text = "was drawn and the outcome was";
                    money_outcome = ("$" + money.toString());
                } else {
                    if (((outcome === 0) && (domain === "gain"))) {
                        outcome_color = [0.9608, 0.0039, (- 0.1059)];
                        gumball_color = [0.9608, 0.0039, (- 0.1059)];
                        choice_outcome = "A red gumball";
                        gumball_text = "was drawn and the outcome was";
                        money_outcome = ("$" + money.toString());
                    } else {
                        if (((outcome === 0) && (domain === "loss"))) {
                            outcome_color = [(- 0.2157), 0.1686, 0.8588];
                            gumball_color = [(- 0.2157), 0.1686, 0.8588];
                            choice_outcome = "A blue gumball";
                            gumball_text = "was drawn and the outcome was";
                            money_outcome = ("$" + money.toString());
                        }
                    }
                }
            }
        }
    }
    
    crdm_bonus_img.setImage(choice_img);
    crdm_bonus_lott_left_txt.setColor(new util.Color(left_color));
    crdm_bonus_lott_left_txt.setText(("$" + left.toString()).toString());
    crdm_bonus_sure_center_txt.setColor(new util.Color(sure_color));
    crdm_bonus_sure_center_txt.setText(("$" + sure_amt.toString()).toString());
    crdm_bonus_lott_right_txt.setColor(new util.Color(right_color));
    crdm_bonus_lott_right_txt.setText(("$" + right.toString()).toString());
    crdm_bonus_choice_text_txt.setText(choice_text);
    crdm_bonus_choice_outcome_txt.setColor(new util.Color(outcome_color));
    crdm_bonus_choice_outcome_txt.setText(choice_outcome);
    crdm_bonus_drawn_txt.setText(gumball_text);
    crdm_bonus_gumball_poly.setFillColor(new util.Color(gumball_color));
    crdm_bonus_gumball_poly.setLineColor(new util.Color(gumball_color));
    crdm_bonus_winnings_txt.setText(money_outcome);
    crdm_bonus_resp.keys = undefined;
    crdm_bonus_resp.rt = undefined;
    _crdm_bonus_resp_allKeys = [];
    // keep track of which components have finished
    crdm_bonusComponents = [];
    crdm_bonusComponents.push(crdm_bonus_img);
    crdm_bonusComponents.push(crdm_bonus_thanks_txt);
    crdm_bonusComponents.push(crdm_bonus_lott_left_txt);
    crdm_bonusComponents.push(crdm_bonus_sure_center_txt);
    crdm_bonusComponents.push(crdm_bonus_lott_right_txt);
    crdm_bonusComponents.push(crdm_bonus_prompt_txt);
    crdm_bonusComponents.push(crdm_bonus_choice_text_txt);
    crdm_bonusComponents.push(crdm_bonus_choice_outcome_txt);
    crdm_bonusComponents.push(crdm_bonus_drawn_txt);
    crdm_bonusComponents.push(crdm_bonus_gumball_poly);
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
    
    // *crdm_bonus_img* updates
    if (t >= 0.0 && crdm_bonus_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_img.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_img.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_img.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_thanks_txt* updates
    if (t >= 0.0 && crdm_bonus_thanks_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_thanks_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_thanks_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_thanks_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_lott_left_txt* updates
    if (t >= 0.0 && crdm_bonus_lott_left_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_lott_left_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_lott_left_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_lott_left_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_sure_center_txt* updates
    if (t >= 0.0 && crdm_bonus_sure_center_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_sure_center_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_sure_center_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_sure_center_txt.setAutoDraw(true);
    }
    
    
    // *crdm_bonus_lott_right_txt* updates
    if (t >= 0.0 && crdm_bonus_lott_right_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_lott_right_txt.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_lott_right_txt.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_lott_right_txt.setAutoDraw(true);
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
    
    
    // *crdm_bonus_gumball_poly* updates
    if (t >= 0.0 && crdm_bonus_gumball_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      crdm_bonus_gumball_poly.tStart = t;  // (not accounting for frame time here)
      crdm_bonus_gumball_poly.frameNStart = frameN;  // exact frame index
      
      crdm_bonus_gumball_poly.setAutoDraw(true);
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
