/*************** 
 * Rdm_V1 *
 ***************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.1post4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'rdm_v1';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from rdm_instructions1_code
var bottom, choice, earnings, money, outcome, top, trial_img, trial_type, winning_side;
earnings = [];
choice = [];
money = [];
trial_img = [];
top = [];
bottom = [];
outcome = [];
winning_side = [];

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
flowScheduler.add(rdm_instructions1RoutineBegin());
flowScheduler.add(rdm_instructions1RoutineEachFrame());
flowScheduler.add(rdm_instructions1RoutineEnd());
flowScheduler.add(rdm_instructions2RoutineBegin());
flowScheduler.add(rdm_instructions2RoutineEachFrame());
flowScheduler.add(rdm_instructions2RoutineEnd());
flowScheduler.add(rdm_instructions3RoutineBegin());
flowScheduler.add(rdm_instructions3RoutineEachFrame());
flowScheduler.add(rdm_instructions3RoutineEnd());
flowScheduler.add(rdm_instructions4RoutineBegin());
flowScheduler.add(rdm_instructions4RoutineEachFrame());
flowScheduler.add(rdm_instructions4RoutineEnd());
flowScheduler.add(rdm_instructions5RoutineBegin());
flowScheduler.add(rdm_instructions5RoutineEachFrame());
flowScheduler.add(rdm_instructions5RoutineEnd());
flowScheduler.add(rdm_instructions6RoutineBegin());
flowScheduler.add(rdm_instructions6RoutineEachFrame());
flowScheduler.add(rdm_instructions6RoutineEnd());
flowScheduler.add(rdm_practice_instrRoutineBegin());
flowScheduler.add(rdm_practice_instrRoutineEachFrame());
flowScheduler.add(rdm_practice_instrRoutineEnd());
flowScheduler.add(rdm_init_itiRoutineBegin());
flowScheduler.add(rdm_init_itiRoutineEachFrame());
flowScheduler.add(rdm_init_itiRoutineEnd());
const rdm_pract_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(rdm_pract_trialsLoopBegin(rdm_pract_trialsLoopScheduler));
flowScheduler.add(rdm_pract_trialsLoopScheduler);
flowScheduler.add(rdm_pract_trialsLoopEnd);




flowScheduler.add(rdm_trial_instrRoutineBegin());
flowScheduler.add(rdm_trial_instrRoutineEachFrame());
flowScheduler.add(rdm_trial_instrRoutineEnd());
flowScheduler.add(rdm_init_itiRoutineBegin());
flowScheduler.add(rdm_init_itiRoutineEachFrame());
flowScheduler.add(rdm_init_itiRoutineEnd());
const rdm_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(rdm_trialsLoopBegin(rdm_trialsLoopScheduler));
flowScheduler.add(rdm_trialsLoopScheduler);
flowScheduler.add(rdm_trialsLoopEnd);




flowScheduler.add(rdm_bonusRoutineBegin());
flowScheduler.add(rdm_bonusRoutineEachFrame());
flowScheduler.add(rdm_bonusRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'rdm_practice.xlsx', 'path': 'rdm_practice.xlsx'},
    {'name': 'risk_red_13.bmp', 'path': 'risk_red_13.bmp'},
    {'name': 'risk_blue_25.bmp', 'path': 'risk_blue_25.bmp'},
    {'name': 'ambig_74.bmp', 'path': 'ambig_74.bmp'},
    {'name': 'rdm_trials.xlsx', 'path': 'rdm_trials.xlsx'},
    {'name': 'risk_red_13.bmp', 'path': 'risk_red_13.bmp'},
    {'name': 'risk_blue_13.bmp', 'path': 'risk_blue_13.bmp'},
    {'name': 'risk_blue_25.bmp', 'path': 'risk_blue_25.bmp'},
    {'name': 'risk_red_25.bmp', 'path': 'risk_red_25.bmp'},
    {'name': 'risk_red_38.bmp', 'path': 'risk_red_38.bmp'},
    {'name': 'risk_blue_38.bmp', 'path': 'risk_blue_38.bmp'},
    {'name': 'risk_blue_50.bmp', 'path': 'risk_blue_50.bmp'},
    {'name': 'risk_red_50.bmp', 'path': 'risk_red_50.bmp'},
    {'name': 'risk_red_75.bmp', 'path': 'risk_red_75.bmp'},
    {'name': 'risk_blue_75.bmp', 'path': 'risk_blue_75.bmp'},
    {'name': 'ambig_24.bmp', 'path': 'ambig_24.bmp'},
    {'name': 'ambig_50.bmp', 'path': 'ambig_50.bmp'},
    {'name': 'ambig_74.bmp', 'path': 'ambig_74.bmp'},
    {'name': 'risk_blue_75.bmp', 'path': 'risk_blue_75.bmp'},
    {'name': 'ambig_50.bmp', 'path': 'ambig_50.bmp'},
    {'name': '2key.png', 'path': '2key.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': '2key.png', 'path': '2key.png'},
    {'name': '4key.png', 'path': '4key.png'},
    {'name': 'ambig_24.bmp', 'path': 'ambig_24.bmp'},
    {'name': 'ambig_50.bmp', 'path': 'ambig_50.bmp'},
    {'name': 'ambig_74.bmp', 'path': 'ambig_74.bmp'},
    {'name': 'circle_green_20.bmp', 'path': 'circle_green_20.bmp'},
    {'name': 'risk_blue_13.bmp', 'path': 'risk_blue_13.bmp'},
    {'name': 'risk_blue_25.bmp', 'path': 'risk_blue_25.bmp'},
    {'name': 'risk_blue_38.bmp', 'path': 'risk_blue_38.bmp'},
    {'name': 'risk_blue_50.bmp', 'path': 'risk_blue_50.bmp'},
    {'name': 'risk_blue_75.bmp', 'path': 'risk_blue_75.bmp'},
    {'name': 'risk_red_13.bmp', 'path': 'risk_red_13.bmp'},
    {'name': 'risk_red_25.bmp', 'path': 'risk_red_25.bmp'},
    {'name': 'risk_red_38.bmp', 'path': 'risk_red_38.bmp'},
    {'name': 'risk_red_50.bmp', 'path': 'risk_red_50.bmp'},
    {'name': 'risk_red_75.bmp', 'path': 'risk_red_75.bmp'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.1post4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var rdm_instructions1Clock;
var random;
var rdm_instructions1_txt;
var rdm_instructions1_space_txt;
var rdm_instructions1_resp;
var rdm_instructions2Clock;
var rdm_instructions2_txt;
var rdm_instructions2_img;
var rdm_instructions2_lott0_txt;
var rdm_instructions2_lott20_txt;
var rdm_instructions2_space_txt;
var rdm_instructions2_resp;
var rdm_instructions3Clock;
var rdm_instructions3_txt;
var rdm_instructions3_img;
var rdm_instructions3_lott0_txt;
var rdm_instructions3_lott20_txt;
var rdm_instructions3_space_txt;
var rdm_instructions3_resp;
var rdm_instructions4Clock;
var rdm_instructions4_txt;
var rdm_instructions4_img;
var rdm_instructions4_lott0_txt;
var rdm_instructions4_lott20_txt;
var rdm_instructions4_space_txt;
var rdm_instructions4_resp;
var rdm_instructions5Clock;
var rdm_instructions5_txt;
var rdm_instruction5_img;
var rdm_instructions5_lott_top_txt;
var rdm_instructions5_lott_bot_txt;
var rdm_instructions5_sure_txt;
var rdm_instructions5_space_txt;
var rdm_instructions5_resp;
var rdm_instructions6Clock;
var rdm_instructions6_txt;
var rdm_instructions6_img;
var rdm_instructions6_space_txt;
var rdm_instructions6_resp;
var rdm_practice_instrClock;
var rdm_practice_instr_txt;
var rdm_practice_instr_space_txt;
var rdm_practice_instr_key;
var rdm_init_itiClock;
var polygon;
var rdm_pract_trialClock;
var sure_pos;
var sure_resp;
var crdm_msg;
var pos;
var resp;
var rdm_pract_trial_img;
var rdm_pract_trial_lott_top_txt;
var rdm_pract_trial_lott_bot_txt;
var rdm_pract_trial_sure_amt_txt;
var rdm_pract_trial_cue;
var rdm_pract_trial_resp;
var rdm_feedbackClock;
var rdm_feedback_txt;
var rdm_pract_itiClock;
var rdm_pract_iti_poly;
var rdm_trial_instrClock;
var rdm_trial_instr_txt;
var rdm_trial_instr_space_txt;
var rdm_trial_instr_resp;
var rdm_trialClock;
var delta_time;
var rdm_trial_img;
var rdm_trial_lott_top;
var rdm_trial_lott_bot;
var rdm_trial_sure_amt;
var rdm_trial_cue;
var rdm_trial_resp;
var rdm_trials_itiClock;
var rdm_trials_ITI_poly;
var rdm_bonusClock;
var choice_text;
var outcome_color;
var chip_color;
var chip_text;
var choice_outcome;
var money_outcome;
var rdm_bonus_img;
var rdm_bonus_thanks_txt;
var rdm_bonus_lott_top;
var rdm_bonus_lott_bot;
var rdm_bonus_sure_amt_txt;
var rdm_bonus_prompt_txt;
var rdm_bonus_choice_text_txt;
var rdm_bonus_choice_outcome_txt;
var rdm_bonus_drawn_txt;
var rdm_bonus_winnings_txt;
var rdm_bonus_space_txt;
var rdm_bonus_resp;
var rdm_bonus_chip_poly;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "rdm_instructions1"
  rdm_instructions1Clock = new util.Clock();
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
  rdm_instructions1_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions1_txt',
    text: 'Welcome to the Risk and Ambiguity Task!\n\nIn this decision making experiment, you will be asked to make several economic choices. For each trial, you will be given an option between (1) receiving a certain amount of money or (2) playing a lottery for the chance to win a larger amount of money. \n\nAt the end of the experiment one trial will be selected at random. The amount you may have gained during this randomly selected trial will be added to your total participation earnings.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions1_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions1_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_instructions1_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_instructions2"
  rdm_instructions2Clock = new util.Clock();
  rdm_instructions2_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions2_txt',
    text: '*Playing the Lottery*\n\nThe lottery consists of an imaginary bag containing 100 poker chips, some red and some blue. To play, you pull a random chip from the bag.  \n\nThe figure on the left represents the proportion of blue and red chips in the imaginary bag. \n\nIn this example, most chips are blue (75 of 100) and fewer are red (25 of 100).',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_instructions2_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_instructions2_img', units : 'height', 
    image : 'risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, 0], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_instructions2_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions2_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions2_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions2_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_instructions2_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions2_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_instructions2_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_instructions3"
  rdm_instructions3Clock = new util.Clock();
  rdm_instructions3_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions3_txt',
    text: '*Playing the Lottery*\n\nGiven information about the number of blue and red chips in the bag, you can decide whether you would prefer a certain monetary outcome or if you would rather play the lottery for a chance to win a different amount.\n\nIn this example, you have a 75% of winning $20 by pulling a blue chip from the bag and a 25% chance of $0 by pulling a red chip.\n\nThe value for each color will change from bag to bag. Read the $ amount above the red and below the blue to know the value of each chip color.',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_instructions3_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_instructions3_img', units : undefined, 
    image : 'risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, 0], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_instructions3_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions3_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions3_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions3_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_instructions3_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions3_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_instructions3_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_instructions4"
  rdm_instructions4Clock = new util.Clock();
  rdm_instructions4_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions4_txt',
    text: '*Playing the Lottery*\n\nFor some lotteries, information about the contents of the bag may be partially hidden. \n\nIn this example, the bag has at least 25 blue chips and 25 red chips. However, the color of the remaining 50 chips is unknown. The remaining 50 chips could be all red, all blue, or any combination of the two. ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_instructions4_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_instructions4_img', units : undefined, 
    image : 'ambig_50.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, 0], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_instructions4_lott0_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions4_lott0_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.3], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions4_lott20_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions4_lott20_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.3)], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_instructions4_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions4_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_instructions4_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_instructions5"
  rdm_instructions5Clock = new util.Clock();
  rdm_instructions5_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions5_txt',
    text: 'The lottery bag will appear in the center of the screen. The certain dollar amount will be presented on either the right or left side of the bag. In this example, the certain $5 would be the left option, and the lottery would be the right option:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.035,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_instruction5_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_instruction5_img', units : undefined, 
    image : 'risk_blue_75.bmp', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.05)], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_instructions5_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions5_lott_top_txt',
    text: '$0',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions5_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions5_lott_bot_txt',
    text: '$20',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.35)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_instructions5_sure_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions5_sure_txt',
    text: '$5\n',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.3), (- 0.05)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_instructions5_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions5_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  rdm_instructions5_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_instructions6"
  rdm_instructions6Clock = new util.Clock();
  rdm_instructions6_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions6_txt',
    text: 'When the green circle appears, use the number keys at the top of your keyboard to indicate your choice:\n\nPress 1 to select the left option\nPress 2 to select the right option \n\n\n\n\n\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_instructions6_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_instructions6_img', units : undefined, 
    image : '2key.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.1)], 
    draggable: false,
    size : [0.6, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_instructions6_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_instructions6_space_txt',
    text: 'Press SPACE to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_instructions6_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_practice_instr"
  rdm_practice_instrClock = new util.Clock();
  rdm_practice_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_practice_instr_txt',
    text: "Now let's practice.\n\nWhen the green circle appears, indicate your decision by pressing 1 for the left option and 2 for the right option. Next, you will rate your confidence. ",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rdm_practice_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_practice_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  rdm_practice_instr_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_init_iti"
  rdm_init_itiClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "rdm_pract_trial"
  rdm_pract_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from rdm_pract_trial_code1
  sure_pos = [];
  sure_resp = [];
  crdm_msg = "";
  pos = [[(- 0.3), 0], [0.3, 0]];
  resp = ["1", "2"];
  
  rdm_pract_trial_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_pract_trial_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_pract_trial_lott_top_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_pract_trial_lott_top_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_pract_trial_lott_bot_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_pract_trial_lott_bot_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_pract_trial_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_pract_trial_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_pract_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'rdm_pract_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: [(- 1.0), 1.0, (- 1.0)],
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  rdm_pract_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_feedback"
  rdm_feedbackClock = new util.Clock();
  rdm_feedback_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_feedback_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "rdm_pract_iti"
  rdm_pract_itiClock = new util.Clock();
  rdm_pract_iti_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'rdm_pract_iti_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "rdm_trial_instr"
  rdm_trial_instrClock = new util.Clock();
  rdm_trial_instr_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_trial_instr_txt',
    text: 'Now that you have practiced a few trials, we will begin the actual task.\n\nRemember to make your choice between the certain outcome and lottery as soon as you see the green circle. You will have 3 seconds to consider the options and 2 seconds to make your choice.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  rdm_trial_instr_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_trial_instr_space_txt',
    text: 'Press SPACE to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_trial_instr_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_trial"
  rdm_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from rdm_trial_code
  delta_time = 0;
  sure_pos = [];
  sure_resp = [];
  crdm_msg = "";
  pos = [[(- 0.3), 0], [0.3, 0]];
  resp = ["1", "2"];
  
  rdm_trial_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_trial_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_trial_lott_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_trial_lott_top',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_trial_lott_bot = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_trial_lott_bot',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_trial_sure_amt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_trial_sure_amt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_trial_cue = new visual.Polygon({
    win: psychoJS.window, name: 'rdm_trial_cue', 
    edges: 100, size:[0.04, 0.04],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 1.0, (- 1.0)]),
    fillColor: [(- 1.0), 1.0, (- 1.0)],
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  rdm_trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rdm_trials_iti"
  rdm_trials_itiClock = new util.Clock();
  rdm_trials_ITI_poly = new visual.ShapeStim ({
    win: psychoJS.window, name: 'rdm_trials_ITI_poly', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "rdm_bonus"
  rdm_bonusClock = new util.Clock();
  // Run 'Begin Experiment' code from rdm_bonus_code
  choice_text = "";
  outcome_color = "";
  chip_color = [0, 0, 0];
  chip_text = "";
  choice_outcome = "";
  money_outcome = "";
  
  rdm_bonus_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'rdm_bonus_img', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0.6, (- 0.1)], 
    draggable: false,
    size : [0.3, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  rdm_bonus_thanks_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_thanks_txt',
    text: 'Thank you for participating in the Risk & Ambiguity Task!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.35], draggable: false, height: 0.05,  wrapWidth: 1.25, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  rdm_bonus_lott_top = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_lott_top',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, 0.2], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  rdm_bonus_lott_bot = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_lott_bot',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.6, (- 0.4)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  rdm_bonus_sure_amt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_sure_amt_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.4, (- 0.1)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  rdm_bonus_prompt_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_prompt_txt',
    text: 'In the randomly selected trial, you chose:',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.2], draggable: false, height: 0.04,  wrapWidth: 1.0, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  rdm_bonus_choice_text_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_choice_text_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0.1], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  rdm_bonus_choice_outcome_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_choice_outcome_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), 0], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  rdm_bonus_drawn_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_drawn_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.1)], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  rdm_bonus_winnings_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_winnings_txt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.2), (- 0.2)], draggable: false, height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([0.7098, 0.2941, (- 0.749)]),  opacity: undefined,
    depth: -10.0 
  });
  
  rdm_bonus_space_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'rdm_bonus_space_txt',
    text: 'Press SPACE to end',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -11.0 
  });
  
  rdm_bonus_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rdm_bonus_chip_poly = new visual.Polygon({
    win: psychoJS.window, name: 'rdm_bonus_chip_poly', 
    edges: 100, size:[0.075, 0.075],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    fillColor: 'white',
    opacity: undefined, depth: -13, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var rdm_instructions1MaxDurationReached;
var practice_loop_name;
var loop_name;
var _rdm_instructions1_resp_allKeys;
var rdm_instructions1MaxDuration;
var rdm_instructions1Components;
function rdm_instructions1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions1' ---
    t = 0;
    rdm_instructions1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions1MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_instructions1_code
    practice_loop_name = "rdm_pract_trials";
    loop_name = "rdm_trials";
    
    rdm_instructions1_resp.keys = undefined;
    rdm_instructions1_resp.rt = undefined;
    _rdm_instructions1_resp_allKeys = [];
    rdm_instructions1MaxDuration = null
    // keep track of which components have finished
    rdm_instructions1Components = [];
    rdm_instructions1Components.push(rdm_instructions1_txt);
    rdm_instructions1Components.push(rdm_instructions1_space_txt);
    rdm_instructions1Components.push(rdm_instructions1_resp);
    
    for (const thisComponent of rdm_instructions1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions1' ---
    // get current time
    t = rdm_instructions1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions1_txt* updates
    if (t >= 0.0 && rdm_instructions1_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions1_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions1_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions1_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions1_space_txt* updates
    if (t >= 0.0 && rdm_instructions1_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions1_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions1_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions1_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions1_resp* updates
    if (t >= 0.0 && rdm_instructions1_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions1_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions1_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions1_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions1_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions1_resp.clearEvents(); });
    }
    
    if (rdm_instructions1_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions1_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions1_resp_allKeys = _rdm_instructions1_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions1_resp_allKeys.length > 0) {
        rdm_instructions1_resp.keys = _rdm_instructions1_resp_allKeys[_rdm_instructions1_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions1_resp.rt = _rdm_instructions1_resp_allKeys[_rdm_instructions1_resp_allKeys.length - 1].rt;
        rdm_instructions1_resp.duration = _rdm_instructions1_resp_allKeys[_rdm_instructions1_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions1Components)
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


function rdm_instructions1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions1' ---
    for (const thisComponent of rdm_instructions1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions1_resp.stop();
    // the Routine "rdm_instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_instructions2MaxDurationReached;
var _rdm_instructions2_resp_allKeys;
var rdm_instructions2MaxDuration;
var rdm_instructions2Components;
function rdm_instructions2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions2' ---
    t = 0;
    rdm_instructions2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions2MaxDurationReached = false;
    // update component parameters for each repeat
    rdm_instructions2_resp.keys = undefined;
    rdm_instructions2_resp.rt = undefined;
    _rdm_instructions2_resp_allKeys = [];
    rdm_instructions2MaxDuration = null
    // keep track of which components have finished
    rdm_instructions2Components = [];
    rdm_instructions2Components.push(rdm_instructions2_txt);
    rdm_instructions2Components.push(rdm_instructions2_img);
    rdm_instructions2Components.push(rdm_instructions2_lott0_txt);
    rdm_instructions2Components.push(rdm_instructions2_lott20_txt);
    rdm_instructions2Components.push(rdm_instructions2_space_txt);
    rdm_instructions2Components.push(rdm_instructions2_resp);
    
    for (const thisComponent of rdm_instructions2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions2' ---
    // get current time
    t = rdm_instructions2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions2_txt* updates
    if (t >= 0.0 && rdm_instructions2_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions2_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions2_img* updates
    if (t >= 0.0 && rdm_instructions2_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_img.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_img.frameNStart = frameN;  // exact frame index
      
      rdm_instructions2_img.setAutoDraw(true);
    }
    
    
    // *rdm_instructions2_lott0_txt* updates
    if (t >= 0.0 && rdm_instructions2_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_lott0_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_lott0_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions2_lott0_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions2_lott20_txt* updates
    if (t >= 0.0 && rdm_instructions2_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_lott20_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_lott20_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions2_lott20_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions2_space_txt* updates
    if (t >= 0.0 && rdm_instructions2_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions2_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions2_resp* updates
    if (t >= 0.0 && rdm_instructions2_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions2_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions2_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions2_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions2_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions2_resp.clearEvents(); });
    }
    
    if (rdm_instructions2_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions2_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions2_resp_allKeys = _rdm_instructions2_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions2_resp_allKeys.length > 0) {
        rdm_instructions2_resp.keys = _rdm_instructions2_resp_allKeys[_rdm_instructions2_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions2_resp.rt = _rdm_instructions2_resp_allKeys[_rdm_instructions2_resp_allKeys.length - 1].rt;
        rdm_instructions2_resp.duration = _rdm_instructions2_resp_allKeys[_rdm_instructions2_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions2Components)
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


function rdm_instructions2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions2' ---
    for (const thisComponent of rdm_instructions2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions2_resp.stop();
    // the Routine "rdm_instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_instructions3MaxDurationReached;
var _rdm_instructions3_resp_allKeys;
var rdm_instructions3MaxDuration;
var rdm_instructions3Components;
function rdm_instructions3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions3' ---
    t = 0;
    rdm_instructions3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions3MaxDurationReached = false;
    // update component parameters for each repeat
    rdm_instructions3_resp.keys = undefined;
    rdm_instructions3_resp.rt = undefined;
    _rdm_instructions3_resp_allKeys = [];
    rdm_instructions3MaxDuration = null
    // keep track of which components have finished
    rdm_instructions3Components = [];
    rdm_instructions3Components.push(rdm_instructions3_txt);
    rdm_instructions3Components.push(rdm_instructions3_img);
    rdm_instructions3Components.push(rdm_instructions3_lott0_txt);
    rdm_instructions3Components.push(rdm_instructions3_lott20_txt);
    rdm_instructions3Components.push(rdm_instructions3_space_txt);
    rdm_instructions3Components.push(rdm_instructions3_resp);
    
    for (const thisComponent of rdm_instructions3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions3' ---
    // get current time
    t = rdm_instructions3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions3_txt* updates
    if (t >= 0.0 && rdm_instructions3_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions3_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions3_img* updates
    if (t >= 0.0 && rdm_instructions3_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_img.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_img.frameNStart = frameN;  // exact frame index
      
      rdm_instructions3_img.setAutoDraw(true);
    }
    
    
    // *rdm_instructions3_lott0_txt* updates
    if (t >= 0.0 && rdm_instructions3_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_lott0_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_lott0_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions3_lott0_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions3_lott20_txt* updates
    if (t >= 0.0 && rdm_instructions3_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_lott20_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_lott20_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions3_lott20_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions3_space_txt* updates
    if (t >= 0.0 && rdm_instructions3_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions3_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions3_resp* updates
    if (t >= 0.0 && rdm_instructions3_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions3_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions3_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions3_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions3_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions3_resp.clearEvents(); });
    }
    
    if (rdm_instructions3_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions3_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions3_resp_allKeys = _rdm_instructions3_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions3_resp_allKeys.length > 0) {
        rdm_instructions3_resp.keys = _rdm_instructions3_resp_allKeys[_rdm_instructions3_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions3_resp.rt = _rdm_instructions3_resp_allKeys[_rdm_instructions3_resp_allKeys.length - 1].rt;
        rdm_instructions3_resp.duration = _rdm_instructions3_resp_allKeys[_rdm_instructions3_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions3Components)
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


function rdm_instructions3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions3' ---
    for (const thisComponent of rdm_instructions3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions3_resp.stop();
    // the Routine "rdm_instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_instructions4MaxDurationReached;
var _rdm_instructions4_resp_allKeys;
var rdm_instructions4MaxDuration;
var rdm_instructions4Components;
function rdm_instructions4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions4' ---
    t = 0;
    rdm_instructions4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions4MaxDurationReached = false;
    // update component parameters for each repeat
    rdm_instructions4_resp.keys = undefined;
    rdm_instructions4_resp.rt = undefined;
    _rdm_instructions4_resp_allKeys = [];
    rdm_instructions4MaxDuration = null
    // keep track of which components have finished
    rdm_instructions4Components = [];
    rdm_instructions4Components.push(rdm_instructions4_txt);
    rdm_instructions4Components.push(rdm_instructions4_img);
    rdm_instructions4Components.push(rdm_instructions4_lott0_txt);
    rdm_instructions4Components.push(rdm_instructions4_lott20_txt);
    rdm_instructions4Components.push(rdm_instructions4_space_txt);
    rdm_instructions4Components.push(rdm_instructions4_resp);
    
    for (const thisComponent of rdm_instructions4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions4' ---
    // get current time
    t = rdm_instructions4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions4_txt* updates
    if (t >= 0.0 && rdm_instructions4_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions4_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions4_img* updates
    if (t >= 0.0 && rdm_instructions4_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_img.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_img.frameNStart = frameN;  // exact frame index
      
      rdm_instructions4_img.setAutoDraw(true);
    }
    
    
    // *rdm_instructions4_lott0_txt* updates
    if (t >= 0.0 && rdm_instructions4_lott0_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_lott0_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_lott0_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions4_lott0_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions4_lott20_txt* updates
    if (t >= 0.0 && rdm_instructions4_lott20_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_lott20_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_lott20_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions4_lott20_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions4_space_txt* updates
    if (t >= 0.0 && rdm_instructions4_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions4_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions4_resp* updates
    if (t >= 0.0 && rdm_instructions4_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions4_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions4_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions4_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions4_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions4_resp.clearEvents(); });
    }
    
    if (rdm_instructions4_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions4_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions4_resp_allKeys = _rdm_instructions4_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions4_resp_allKeys.length > 0) {
        rdm_instructions4_resp.keys = _rdm_instructions4_resp_allKeys[_rdm_instructions4_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions4_resp.rt = _rdm_instructions4_resp_allKeys[_rdm_instructions4_resp_allKeys.length - 1].rt;
        rdm_instructions4_resp.duration = _rdm_instructions4_resp_allKeys[_rdm_instructions4_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions4Components)
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


function rdm_instructions4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions4' ---
    for (const thisComponent of rdm_instructions4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions4_resp.stop();
    // the Routine "rdm_instructions4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_instructions5MaxDurationReached;
var _rdm_instructions5_resp_allKeys;
var rdm_instructions5MaxDuration;
var rdm_instructions5Components;
function rdm_instructions5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions5' ---
    t = 0;
    rdm_instructions5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions5MaxDurationReached = false;
    // update component parameters for each repeat
    rdm_instructions5_resp.keys = undefined;
    rdm_instructions5_resp.rt = undefined;
    _rdm_instructions5_resp_allKeys = [];
    rdm_instructions5MaxDuration = null
    // keep track of which components have finished
    rdm_instructions5Components = [];
    rdm_instructions5Components.push(rdm_instructions5_txt);
    rdm_instructions5Components.push(rdm_instruction5_img);
    rdm_instructions5Components.push(rdm_instructions5_lott_top_txt);
    rdm_instructions5Components.push(rdm_instructions5_lott_bot_txt);
    rdm_instructions5Components.push(rdm_instructions5_sure_txt);
    rdm_instructions5Components.push(rdm_instructions5_space_txt);
    rdm_instructions5Components.push(rdm_instructions5_resp);
    
    for (const thisComponent of rdm_instructions5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions5' ---
    // get current time
    t = rdm_instructions5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions5_txt* updates
    if (t >= 0.0 && rdm_instructions5_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions5_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instruction5_img* updates
    if (t >= 0.0 && rdm_instruction5_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instruction5_img.tStart = t;  // (not accounting for frame time here)
      rdm_instruction5_img.frameNStart = frameN;  // exact frame index
      
      rdm_instruction5_img.setAutoDraw(true);
    }
    
    
    // *rdm_instructions5_lott_top_txt* updates
    if (t >= 0.0 && rdm_instructions5_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions5_lott_top_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions5_lott_bot_txt* updates
    if (t >= 0.0 && rdm_instructions5_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions5_lott_bot_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions5_sure_txt* updates
    if (t >= 0.0 && rdm_instructions5_sure_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_sure_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_sure_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions5_sure_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions5_space_txt* updates
    if (t >= 0.0 && rdm_instructions5_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions5_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions5_resp* updates
    if (t >= 0.0 && rdm_instructions5_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions5_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions5_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions5_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions5_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions5_resp.clearEvents(); });
    }
    
    if (rdm_instructions5_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions5_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions5_resp_allKeys = _rdm_instructions5_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions5_resp_allKeys.length > 0) {
        rdm_instructions5_resp.keys = _rdm_instructions5_resp_allKeys[_rdm_instructions5_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions5_resp.rt = _rdm_instructions5_resp_allKeys[_rdm_instructions5_resp_allKeys.length - 1].rt;
        rdm_instructions5_resp.duration = _rdm_instructions5_resp_allKeys[_rdm_instructions5_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions5Components)
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


function rdm_instructions5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions5' ---
    for (const thisComponent of rdm_instructions5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions5_resp.stop();
    // the Routine "rdm_instructions5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_instructions6MaxDurationReached;
var _rdm_instructions6_resp_allKeys;
var rdm_instructions6MaxDuration;
var rdm_instructions6Components;
function rdm_instructions6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_instructions6' ---
    t = 0;
    rdm_instructions6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_instructions6MaxDurationReached = false;
    // update component parameters for each repeat
    rdm_instructions6_resp.keys = undefined;
    rdm_instructions6_resp.rt = undefined;
    _rdm_instructions6_resp_allKeys = [];
    rdm_instructions6MaxDuration = null
    // keep track of which components have finished
    rdm_instructions6Components = [];
    rdm_instructions6Components.push(rdm_instructions6_txt);
    rdm_instructions6Components.push(rdm_instructions6_img);
    rdm_instructions6Components.push(rdm_instructions6_space_txt);
    rdm_instructions6Components.push(rdm_instructions6_resp);
    
    for (const thisComponent of rdm_instructions6Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_instructions6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_instructions6' ---
    // get current time
    t = rdm_instructions6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_instructions6_txt* updates
    if (t >= 0.0 && rdm_instructions6_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions6_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions6_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions6_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions6_img* updates
    if (t >= 0.0 && rdm_instructions6_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions6_img.tStart = t;  // (not accounting for frame time here)
      rdm_instructions6_img.frameNStart = frameN;  // exact frame index
      
      rdm_instructions6_img.setAutoDraw(true);
    }
    
    
    // *rdm_instructions6_space_txt* updates
    if (t >= 0.0 && rdm_instructions6_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions6_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_instructions6_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_instructions6_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_instructions6_resp* updates
    if (t >= 0.0 && rdm_instructions6_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_instructions6_resp.tStart = t;  // (not accounting for frame time here)
      rdm_instructions6_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_instructions6_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions6_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_instructions6_resp.clearEvents(); });
    }
    
    if (rdm_instructions6_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_instructions6_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_instructions6_resp_allKeys = _rdm_instructions6_resp_allKeys.concat(theseKeys);
      if (_rdm_instructions6_resp_allKeys.length > 0) {
        rdm_instructions6_resp.keys = _rdm_instructions6_resp_allKeys[_rdm_instructions6_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_instructions6_resp.rt = _rdm_instructions6_resp_allKeys[_rdm_instructions6_resp_allKeys.length - 1].rt;
        rdm_instructions6_resp.duration = _rdm_instructions6_resp_allKeys[_rdm_instructions6_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_instructions6Components)
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


function rdm_instructions6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_instructions6' ---
    for (const thisComponent of rdm_instructions6Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_instructions6_resp.stop();
    // the Routine "rdm_instructions6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_practice_instrMaxDurationReached;
var _rdm_practice_instr_key_allKeys;
var rdm_practice_instrMaxDuration;
var rdm_practice_instrComponents;
function rdm_practice_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_practice_instr' ---
    t = 0;
    rdm_practice_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_practice_instrMaxDurationReached = false;
    // update component parameters for each repeat
    rdm_practice_instr_key.keys = undefined;
    rdm_practice_instr_key.rt = undefined;
    _rdm_practice_instr_key_allKeys = [];
    rdm_practice_instrMaxDuration = null
    // keep track of which components have finished
    rdm_practice_instrComponents = [];
    rdm_practice_instrComponents.push(rdm_practice_instr_txt);
    rdm_practice_instrComponents.push(rdm_practice_instr_space_txt);
    rdm_practice_instrComponents.push(rdm_practice_instr_key);
    
    for (const thisComponent of rdm_practice_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_practice_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_practice_instr' ---
    // get current time
    t = rdm_practice_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_practice_instr_txt* updates
    if (t >= 0.0 && rdm_practice_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_practice_instr_txt.tStart = t;  // (not accounting for frame time here)
      rdm_practice_instr_txt.frameNStart = frameN;  // exact frame index
      
      rdm_practice_instr_txt.setAutoDraw(true);
    }
    
    
    // *rdm_practice_instr_space_txt* updates
    if (t >= 0.0 && rdm_practice_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_practice_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_practice_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_practice_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_practice_instr_key* updates
    if (t >= 0.0 && rdm_practice_instr_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_practice_instr_key.tStart = t;  // (not accounting for frame time here)
      rdm_practice_instr_key.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_practice_instr_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_practice_instr_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_practice_instr_key.clearEvents(); });
    }
    
    if (rdm_practice_instr_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_practice_instr_key.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_practice_instr_key_allKeys = _rdm_practice_instr_key_allKeys.concat(theseKeys);
      if (_rdm_practice_instr_key_allKeys.length > 0) {
        rdm_practice_instr_key.keys = _rdm_practice_instr_key_allKeys[_rdm_practice_instr_key_allKeys.length - 1].name;  // just the last key pressed
        rdm_practice_instr_key.rt = _rdm_practice_instr_key_allKeys[_rdm_practice_instr_key_allKeys.length - 1].rt;
        rdm_practice_instr_key.duration = _rdm_practice_instr_key_allKeys[_rdm_practice_instr_key_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_practice_instrComponents)
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


function rdm_practice_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_practice_instr' ---
    for (const thisComponent of rdm_practice_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_practice_instr_key.stop();
    // the Routine "rdm_practice_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_init_itiMaxDurationReached;
var rdm_init_itiMaxDuration;
var rdm_init_itiComponents;
function rdm_init_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_init_iti' ---
    t = 0;
    rdm_init_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    rdm_init_itiMaxDurationReached = false;
    // update component parameters for each repeat
    rdm_init_itiMaxDuration = null
    // keep track of which components have finished
    rdm_init_itiComponents = [];
    rdm_init_itiComponents.push(polygon);
    
    for (const thisComponent of rdm_init_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function rdm_init_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_init_iti' ---
    // get current time
    t = rdm_init_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
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
    for (const thisComponent of rdm_init_itiComponents)
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


function rdm_init_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_init_iti' ---
    for (const thisComponent of rdm_init_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (rdm_init_itiMaxDurationReached) {
        routineTimer.add(rdm_init_itiMaxDuration);
    } else {
        routineTimer.add(-1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_pract_trials;
function rdm_pract_trialsLoopBegin(rdm_pract_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rdm_pract_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'rdm_practice.xlsx',
      seed: undefined, name: 'rdm_pract_trials'
    });
    psychoJS.experiment.addLoop(rdm_pract_trials); // add the loop to the experiment
    currentLoop = rdm_pract_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRdm_pract_trial of rdm_pract_trials) {
      snapshot = rdm_pract_trials.getSnapshot();
      rdm_pract_trialsLoopScheduler.add(importConditions(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_pract_trialRoutineBegin(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_pract_trialRoutineEachFrame());
      rdm_pract_trialsLoopScheduler.add(rdm_pract_trialRoutineEnd(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_feedbackRoutineBegin(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_feedbackRoutineEachFrame());
      rdm_pract_trialsLoopScheduler.add(rdm_feedbackRoutineEnd(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_pract_itiRoutineBegin(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_pract_itiRoutineEachFrame());
      rdm_pract_trialsLoopScheduler.add(rdm_pract_itiRoutineEnd(snapshot));
      rdm_pract_trialsLoopScheduler.add(rdm_pract_trialsLoopEndIteration(rdm_pract_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function rdm_pract_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rdm_pract_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function rdm_pract_trialsLoopEndIteration(scheduler, snapshot) {
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


var rdm_trials;
function rdm_trialsLoopBegin(rdm_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    rdm_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'rdm_trials.xlsx',
      seed: undefined, name: 'rdm_trials'
    });
    psychoJS.experiment.addLoop(rdm_trials); // add the loop to the experiment
    currentLoop = rdm_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRdm_trial of rdm_trials) {
      snapshot = rdm_trials.getSnapshot();
      rdm_trialsLoopScheduler.add(importConditions(snapshot));
      rdm_trialsLoopScheduler.add(rdm_trialRoutineBegin(snapshot));
      rdm_trialsLoopScheduler.add(rdm_trialRoutineEachFrame());
      rdm_trialsLoopScheduler.add(rdm_trialRoutineEnd(snapshot));
      rdm_trialsLoopScheduler.add(rdm_feedbackRoutineBegin(snapshot));
      rdm_trialsLoopScheduler.add(rdm_feedbackRoutineEachFrame());
      rdm_trialsLoopScheduler.add(rdm_feedbackRoutineEnd(snapshot));
      rdm_trialsLoopScheduler.add(rdm_trials_itiRoutineBegin(snapshot));
      rdm_trialsLoopScheduler.add(rdm_trials_itiRoutineEachFrame());
      rdm_trialsLoopScheduler.add(rdm_trials_itiRoutineEnd(snapshot));
      rdm_trialsLoopScheduler.add(rdm_trialsLoopEndIteration(rdm_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function rdm_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(rdm_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function rdm_trialsLoopEndIteration(scheduler, snapshot) {
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


var rdm_pract_trialMaxDurationReached;
var my_loop;
var idx;
var sure_amt;
var lott_pos;
var _rdm_pract_trial_resp_allKeys;
var rdm_pract_trialMaxDuration;
var rdm_pract_trialComponents;
function rdm_pract_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_pract_trial' ---
    t = 0;
    rdm_pract_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    rdm_pract_trialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_pract_trial_code1
    my_loop = eval(practice_loop_name);
    idx = random.randint(0, 1);
    sure_pos = pos[idx];
    sure_resp = resp[idx];
    sure_amt = 5;
    if ((idx === 0)) {
        lott_pos = pos[1];
    } else {
        lott_pos = pos[0];
    }
    
    rdm_pract_trial_img.setImage(img);
    rdm_pract_trial_lott_top_txt.setText(("$" + lott_top.toString()).toString());
    rdm_pract_trial_lott_bot_txt.setText(("$" + lott_bot.toString()).toString());
    rdm_pract_trial_sure_amt_txt.setPos(sure_pos);
    rdm_pract_trial_sure_amt_txt.setText(("$" + sure_amt.toString()).toString());
    rdm_pract_trial_resp.keys = undefined;
    rdm_pract_trial_resp.rt = undefined;
    _rdm_pract_trial_resp_allKeys = [];
    rdm_pract_trialMaxDuration = null
    // keep track of which components have finished
    rdm_pract_trialComponents = [];
    rdm_pract_trialComponents.push(rdm_pract_trial_img);
    rdm_pract_trialComponents.push(rdm_pract_trial_lott_top_txt);
    rdm_pract_trialComponents.push(rdm_pract_trial_lott_bot_txt);
    rdm_pract_trialComponents.push(rdm_pract_trial_sure_amt_txt);
    rdm_pract_trialComponents.push(rdm_pract_trial_cue);
    rdm_pract_trialComponents.push(rdm_pract_trial_resp);
    
    for (const thisComponent of rdm_pract_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_pract_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_pract_trial' ---
    // get current time
    t = rdm_pract_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_pract_trial_img* updates
    if (t >= 0.0 && rdm_pract_trial_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_img.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_img.frameNStart = frameN;  // exact frame index
      
      rdm_pract_trial_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_img.setAutoDraw(false);
    }
    
    
    // *rdm_pract_trial_lott_top_txt* updates
    if (t >= 0.0 && rdm_pract_trial_lott_top_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_lott_top_txt.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_lott_top_txt.frameNStart = frameN;  // exact frame index
      
      rdm_pract_trial_lott_top_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_lott_top_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_lott_top_txt.setAutoDraw(false);
    }
    
    
    // *rdm_pract_trial_lott_bot_txt* updates
    if (t >= 0.0 && rdm_pract_trial_lott_bot_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_lott_bot_txt.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_lott_bot_txt.frameNStart = frameN;  // exact frame index
      
      rdm_pract_trial_lott_bot_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_lott_bot_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_lott_bot_txt.setAutoDraw(false);
    }
    
    
    // *rdm_pract_trial_sure_amt_txt* updates
    if (t >= 0.0 && rdm_pract_trial_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      rdm_pract_trial_sure_amt_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_sure_amt_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_sure_amt_txt.setAutoDraw(false);
    }
    
    
    // *rdm_pract_trial_cue* updates
    if (t >= 3 && rdm_pract_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_cue.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_cue.frameNStart = frameN;  // exact frame index
      
      rdm_pract_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_cue.setAutoDraw(false);
    }
    
    
    // *rdm_pract_trial_resp* updates
    if (t >= 3 && rdm_pract_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_trial_resp.tStart = t;  // (not accounting for frame time here)
      rdm_pract_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_pract_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_pract_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_pract_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (rdm_pract_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_pract_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _rdm_pract_trial_resp_allKeys = _rdm_pract_trial_resp_allKeys.concat(theseKeys);
      if (_rdm_pract_trial_resp_allKeys.length > 0) {
        rdm_pract_trial_resp.keys = _rdm_pract_trial_resp_allKeys[_rdm_pract_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_pract_trial_resp.rt = _rdm_pract_trial_resp_allKeys[_rdm_pract_trial_resp_allKeys.length - 1].rt;
        rdm_pract_trial_resp.duration = _rdm_pract_trial_resp_allKeys[_rdm_pract_trial_resp_allKeys.length - 1].duration;
        // was this correct?
        if (rdm_pract_trial_resp.keys == sure_resp) {
            rdm_pract_trial_resp.corr = 1;
        } else {
            rdm_pract_trial_resp.corr = 0;
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
    for (const thisComponent of rdm_pract_trialComponents)
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
function rdm_pract_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_pract_trial' ---
    for (const thisComponent of rdm_pract_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from rdm_pract_trial_code1
    key = rdm_pract_trial_resp.keys;
    sure_key = rdm_pract_trial_resp.corr;
    
    // was no response the correct answer?!
    if (rdm_pract_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(sure_resp)) {
         rdm_pract_trial_resp.corr = 1;  // correct non-response
      } else {
         rdm_pract_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rdm_pract_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('rdm_pract_trial_resp.keys', rdm_pract_trial_resp.keys);
    psychoJS.experiment.addData('rdm_pract_trial_resp.corr', rdm_pract_trial_resp.corr);
    if (typeof rdm_pract_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rdm_pract_trial_resp.rt', rdm_pract_trial_resp.rt);
        psychoJS.experiment.addData('rdm_pract_trial_resp.duration', rdm_pract_trial_resp.duration);
        routineTimer.reset();
        }
    
    rdm_pract_trial_resp.stop();
    if (rdm_pract_trialMaxDurationReached) {
        routineTimer.add(rdm_pract_trialMaxDuration);
    } else {
        routineTimer.add(-5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_feedbackMaxDurationReached;
var rdm_msg;
var rdm_feedbackMaxDuration;
var rdm_feedbackComponents;
function rdm_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_feedback' ---
    t = 0;
    rdm_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    rdm_feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_feedback_code
    if ((key === undefined)) {
        rdm_msg = "No response";
    } else {
        if (sure_key) {
            rdm_msg = ("You chose: Certain $" + sure_amt.toString());
        } else {
            rdm_msg = "You chose: Lottery";
        }
    }
    
    rdm_feedback_txt.setText(rdm_msg);
    rdm_feedbackMaxDuration = null
    // keep track of which components have finished
    rdm_feedbackComponents = [];
    rdm_feedbackComponents.push(rdm_feedback_txt);
    
    for (const thisComponent of rdm_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_feedback' ---
    // get current time
    t = rdm_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_feedback_txt* updates
    if (t >= 0.0 && rdm_feedback_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_feedback_txt.tStart = t;  // (not accounting for frame time here)
      rdm_feedback_txt.frameNStart = frameN;  // exact frame index
      
      rdm_feedback_txt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_feedback_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_feedback_txt.setAutoDraw(false);
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
    for (const thisComponent of rdm_feedbackComponents)
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


function rdm_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_feedback' ---
    for (const thisComponent of rdm_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (rdm_feedbackMaxDurationReached) {
        routineTimer.add(rdm_feedbackMaxDuration);
    } else {
        routineTimer.add(-0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_pract_itiMaxDurationReached;
var rdm_pract_itiMaxDuration;
var rdm_pract_itiComponents;
function rdm_pract_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_pract_iti' ---
    t = 0;
    rdm_pract_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    rdm_pract_itiMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_pract_iti_code
    if (!(rdm_pract_trials.thisTrialN == undefined) && (rdm_pract_trials.thisTrialN === 4)) {
        continueRoutine = false;
    }
    rdm_pract_itiMaxDuration = null
    // keep track of which components have finished
    rdm_pract_itiComponents = [];
    rdm_pract_itiComponents.push(rdm_pract_iti_poly);
    
    for (const thisComponent of rdm_pract_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_pract_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_pract_iti' ---
    // get current time
    t = rdm_pract_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_pract_iti_poly* updates
    if (t >= 0.0 && rdm_pract_iti_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_pract_iti_poly.tStart = t;  // (not accounting for frame time here)
      rdm_pract_iti_poly.frameNStart = frameN;  // exact frame index
      
      rdm_pract_iti_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_pract_iti_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_pract_iti_poly.setAutoDraw(false);
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
    for (const thisComponent of rdm_pract_itiComponents)
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


function rdm_pract_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_pract_iti' ---
    for (const thisComponent of rdm_pract_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (rdm_pract_itiMaxDurationReached) {
        routineTimer.add(rdm_pract_itiMaxDuration);
    } else {
        routineTimer.add(-2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_trial_instrMaxDurationReached;
var iti_list;
var s;
var _rdm_trial_instr_resp_allKeys;
var rdm_trial_instrMaxDuration;
var rdm_trial_instrComponents;
function rdm_trial_instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_trial_instr' ---
    t = 0;
    rdm_trial_instrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_trial_instrMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_trial_instr_code
    iti_list = function () {
        var _pj_a = [], _pj_b = util.range(80);
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
            _pj_a.push(((i * 80) / s));
        }
        return _pj_a;
    }
    .call(this);
    
    rdm_trial_instr_resp.keys = undefined;
    rdm_trial_instr_resp.rt = undefined;
    _rdm_trial_instr_resp_allKeys = [];
    rdm_trial_instrMaxDuration = null
    // keep track of which components have finished
    rdm_trial_instrComponents = [];
    rdm_trial_instrComponents.push(rdm_trial_instr_txt);
    rdm_trial_instrComponents.push(rdm_trial_instr_space_txt);
    rdm_trial_instrComponents.push(rdm_trial_instr_resp);
    
    for (const thisComponent of rdm_trial_instrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_trial_instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_trial_instr' ---
    // get current time
    t = rdm_trial_instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_trial_instr_txt* updates
    if (t >= 0.0 && rdm_trial_instr_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_instr_txt.tStart = t;  // (not accounting for frame time here)
      rdm_trial_instr_txt.frameNStart = frameN;  // exact frame index
      
      rdm_trial_instr_txt.setAutoDraw(true);
    }
    
    
    // *rdm_trial_instr_space_txt* updates
    if (t >= 0.0 && rdm_trial_instr_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_instr_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_trial_instr_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_trial_instr_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_trial_instr_resp* updates
    if (t >= 0.0 && rdm_trial_instr_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_instr_resp.tStart = t;  // (not accounting for frame time here)
      rdm_trial_instr_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_trial_instr_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_trial_instr_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_trial_instr_resp.clearEvents(); });
    }
    
    if (rdm_trial_instr_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_trial_instr_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_trial_instr_resp_allKeys = _rdm_trial_instr_resp_allKeys.concat(theseKeys);
      if (_rdm_trial_instr_resp_allKeys.length > 0) {
        rdm_trial_instr_resp.keys = _rdm_trial_instr_resp_allKeys[_rdm_trial_instr_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_trial_instr_resp.rt = _rdm_trial_instr_resp_allKeys[_rdm_trial_instr_resp_allKeys.length - 1].rt;
        rdm_trial_instr_resp.duration = _rdm_trial_instr_resp_allKeys[_rdm_trial_instr_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of rdm_trial_instrComponents)
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


function rdm_trial_instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_trial_instr' ---
    for (const thisComponent of rdm_trial_instrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_trial_instr_resp.stop();
    // the Routine "rdm_trial_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_trialMaxDurationReached;
var stop_timer;
var stopped_time;
var lott_outcome;
var _rdm_trial_resp_allKeys;
var rdm_trialMaxDuration;
var rdm_trialComponents;
function rdm_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_trial' ---
    t = 0;
    rdm_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    rdm_trialMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_trial_code
    my_loop = eval(loop_name);
    stop_timer = null;
    stopped_time = 0;
    lott_outcome = 0;
    idx = random.randint(0, 1);
    sure_pos = pos[idx];
    sure_resp = resp[idx];
    sure_amt = 5;
    if ((idx === 0)) {
        lott_pos = pos[1];
    } else {
        lott_pos = pos[0];
    }
    
    rdm_trial_img.setImage(img);
    rdm_trial_lott_top.setText(("$" + lott_top.toString()).toString());
    rdm_trial_lott_bot.setText(("$" + lott_bot.toString()).toString());
    rdm_trial_sure_amt.setPos(sure_pos);
    rdm_trial_sure_amt.setText(("$" + sure_amt.toString()).toString());
    rdm_trial_resp.keys = undefined;
    rdm_trial_resp.rt = undefined;
    _rdm_trial_resp_allKeys = [];
    rdm_trialMaxDuration = null
    // keep track of which components have finished
    rdm_trialComponents = [];
    rdm_trialComponents.push(rdm_trial_img);
    rdm_trialComponents.push(rdm_trial_lott_top);
    rdm_trialComponents.push(rdm_trial_lott_bot);
    rdm_trialComponents.push(rdm_trial_sure_amt);
    rdm_trialComponents.push(rdm_trial_cue);
    rdm_trialComponents.push(rdm_trial_resp);
    
    for (const thisComponent of rdm_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_trial' ---
    // get current time
    t = rdm_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from rdm_trial_code
    if (!(rdm_trial_resp.keys === undefined) && (rdm_trial_resp.keys.length === 1)) {
        if ((stop_timer === null)) {
            stop_timer = new core.Clock();
        } else {
            if ((stop_timer.getTime() >= 0.5)) {
                continueRoutine = false;
            }
        }
    }
    
    
    // *rdm_trial_img* updates
    if (t >= 0.0 && rdm_trial_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_img.tStart = t;  // (not accounting for frame time here)
      rdm_trial_img.frameNStart = frameN;  // exact frame index
      
      rdm_trial_img.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_img.setAutoDraw(false);
    }
    
    
    // *rdm_trial_lott_top* updates
    if (t >= 0.0 && rdm_trial_lott_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_lott_top.tStart = t;  // (not accounting for frame time here)
      rdm_trial_lott_top.frameNStart = frameN;  // exact frame index
      
      rdm_trial_lott_top.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_lott_top.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_lott_top.setAutoDraw(false);
    }
    
    
    // *rdm_trial_lott_bot* updates
    if (t >= 0.0 && rdm_trial_lott_bot.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_lott_bot.tStart = t;  // (not accounting for frame time here)
      rdm_trial_lott_bot.frameNStart = frameN;  // exact frame index
      
      rdm_trial_lott_bot.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_lott_bot.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_lott_bot.setAutoDraw(false);
    }
    
    
    // *rdm_trial_sure_amt* updates
    if (t >= 0.0 && rdm_trial_sure_amt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_sure_amt.tStart = t;  // (not accounting for frame time here)
      rdm_trial_sure_amt.frameNStart = frameN;  // exact frame index
      
      rdm_trial_sure_amt.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_sure_amt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_sure_amt.setAutoDraw(false);
    }
    
    
    // *rdm_trial_cue* updates
    if (t >= 3 && rdm_trial_cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_cue.tStart = t;  // (not accounting for frame time here)
      rdm_trial_cue.frameNStart = frameN;  // exact frame index
      
      rdm_trial_cue.setAutoDraw(true);
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_cue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_cue.setAutoDraw(false);
    }
    
    
    // *rdm_trial_resp* updates
    if (t >= 3 && rdm_trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trial_resp.tStart = t;  // (not accounting for frame time here)
      rdm_trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_trial_resp.clearEvents(); });
    }
    
    frameRemains = 3 + 2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (rdm_trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_trial_resp.getKeys({keyList: ['1', '2'], waitRelease: false});
      _rdm_trial_resp_allKeys = _rdm_trial_resp_allKeys.concat(theseKeys);
      if (_rdm_trial_resp_allKeys.length > 0) {
        rdm_trial_resp.keys = _rdm_trial_resp_allKeys[_rdm_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_trial_resp.rt = _rdm_trial_resp_allKeys[_rdm_trial_resp_allKeys.length - 1].rt;
        rdm_trial_resp.duration = _rdm_trial_resp_allKeys[_rdm_trial_resp_allKeys.length - 1].duration;
        // was this correct?
        if (rdm_trial_resp.keys == sure_resp) {
            rdm_trial_resp.corr = 1;
        } else {
            rdm_trial_resp.corr = 0;
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
    for (const thisComponent of rdm_trialComponents)
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


function rdm_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_trial' ---
    for (const thisComponent of rdm_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from rdm_trial_code
    key = rdm_trial_resp.keys; 
    sure_key = rdm_trial_resp.corr; 
    
    if ((((rdm_trial_resp.rt) === undefined) || (rdm_trial_resp.rt >= (2.2 - 0.5)))) {
        delta_time = 0;
    } else {
        delta_time = Math.max(0, (2.2 - (rdm_trial_resp.rt + stopped_time)));
    }
    if (!(rdm_trial_resp.keys === undefined) && (rdm_trial_resp.keys.length === 1)) {
        if ((sure_key === 1)) {
            earnings.push(["sure", 5, img, lott_top, lott_bot, (-1), win_side, domain]);
            my_loop.addData("crdm_choice", "sure");
        } else {
            lott_outcome = random.choices([0, 1], [100 - Number.parseInt(lott_p), Number.parseInt(lott_p)]);
            my_loop.addData("crdm_choice", "lott");
            my_loop.addData("lott_outcome", lott_outcome);
            if ((lott_outcome === 1)) {
                if ((Number.parseInt(lott_top) !== 0)) {
                    earnings.push(["lott", lott_top, img, lott_top, lott_bot, lott_outcome, win_side, domain]);
                } else {
                    earnings.push(["lott", lott_bot, img, lott_top, lott_bot, lott_outcome, win_side, domain]);
                }
            } else {
                earnings.push(["lott", 0, img, lott_top, lott_bot, lott_outcome, win_side, domain]);
            }
        }
    }
    
    // was no response the correct answer?!
    if (rdm_trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(sure_resp)) {
         rdm_trial_resp.corr = 1;  // correct non-response
      } else {
         rdm_trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rdm_trial_resp.corr, level);
    }
    psychoJS.experiment.addData('rdm_trial_resp.keys', rdm_trial_resp.keys);
    psychoJS.experiment.addData('rdm_trial_resp.corr', rdm_trial_resp.corr);
    if (typeof rdm_trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rdm_trial_resp.rt', rdm_trial_resp.rt);
        psychoJS.experiment.addData('rdm_trial_resp.duration', rdm_trial_resp.duration);
        routineTimer.reset();
        }
    
    rdm_trial_resp.stop();
    if (rdm_trialMaxDurationReached) {
        routineTimer.add(rdm_trialMaxDuration);
    } else {
        routineTimer.add(-5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_trials_itiMaxDurationReached;
var iti_time;
var rdm_trials_itiMaxDuration;
var rdm_trials_itiComponents;
function rdm_trials_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_trials_iti' ---
    t = 0;
    rdm_trials_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_trials_itiMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_trials_ITI_code
    iti_time = (iti_list[my_loop.thisIndex] + delta_time);
    if (!(rdm_pract_trials.thisTrialN == undefined) && (rdm_pract_trials.thisTrialN === 79)) {
        continueRoutine = false;
    }
    rdm_trials_itiMaxDuration = null
    // keep track of which components have finished
    rdm_trials_itiComponents = [];
    rdm_trials_itiComponents.push(rdm_trials_ITI_poly);
    
    for (const thisComponent of rdm_trials_itiComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_trials_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_trials_iti' ---
    // get current time
    t = rdm_trials_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_trials_ITI_poly* updates
    if (t >= 0.0 && rdm_trials_ITI_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_trials_ITI_poly.tStart = t;  // (not accounting for frame time here)
      rdm_trials_ITI_poly.frameNStart = frameN;  // exact frame index
      
      rdm_trials_ITI_poly.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + iti_time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (rdm_trials_ITI_poly.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rdm_trials_ITI_poly.setAutoDraw(false);
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
    for (const thisComponent of rdm_trials_itiComponents)
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


function rdm_trials_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_trials_iti' ---
    for (const thisComponent of rdm_trials_itiComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from rdm_trials_ITI_code
    my_loop.addData("delta_time", delta_time);
    my_loop.addData("iti_time", iti_time);
    
    // the Routine "rdm_trials_iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var rdm_bonusMaxDurationReached;
var _pj;
var red_win;
var _rdm_bonus_resp_allKeys;
var rdm_bonusMaxDuration;
var rdm_bonusComponents;
function rdm_bonusRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rdm_bonus' ---
    t = 0;
    rdm_bonusClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    rdm_bonusMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from rdm_bonus_code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    idx = Number.parseInt((random.random() * earnings.length));
    console.log(earnings[idx]);
    [choice, money, trial_img, top, bottom, outcome, winning_side, domain] = earnings[idx];
    sure_amt = 5;
    my_loop.addData("bonus_choice", choice);
    my_loop.addData("bonus_amount", money);
    red_win = false;
    if (_pj.in_es6("red", trial_img)) {
        red_win = true;
    } else {
        if (_pj.in_es6("ambig", trial_img)) {
            if ((winning_side === "top")) {
                red_win = true;
            }
        }
    }
    if ((choice === "sure")) {
        choice_text = "*CERTAIN*";
        outcome_color = "goldenrod";
        chip_color = [0, 0, 0];
        chip_text = "";
        choice_outcome = ("$" + money.toString());
        money_outcome = "";
    } else {
        choice_text = "*PLAY THE LOTTERY*";
        if ((outcome === 1)) {
            if ((red_win === true)) {
                outcome_color = "salmon";
                chip_color = "salmon";
                choice_outcome = "A red chip";
                chip_text = "was drawn and you received";
                money_outcome = ("$" + money.toString());
            } else {
                outcome_color = "cornflowerblue";
                chip_color = "cornflowerblue";
                choice_outcome = "A blue chip";
                chip_text = "was drawn and you received";
                money_outcome = ("$" + money.toString());
            }
        }
        if ((outcome === 0)) {
            if ((red_win === true)) {
                outcome_color = "cornflowerblue";
                chip_color = "cornflowerblue";
                choice_outcome = "A blue chip";
                chip_text = "was drawn and you received";
                money_outcome = ("$" + money.toString());
            } else {
                outcome_color = "salmon";
                chip_color = "salmon";
                choice_outcome = "A red chip";
                chip_text = "was drawn and you received";
                money_outcome = ("$" + money.toString());
            }
        }
    }
    
    rdm_bonus_img.setImage(trial_img);
    rdm_bonus_lott_top.setText(("$" + top.toString()).toString());
    rdm_bonus_lott_bot.setText(("$" + bottom.toString()).toString());
    rdm_bonus_sure_amt_txt.setText(("$" + sure_amt.toString()).toString());
    rdm_bonus_choice_text_txt.setText(choice_text);
    rdm_bonus_choice_outcome_txt.setColor(new util.Color(outcome_color));
    rdm_bonus_choice_outcome_txt.setText(choice_outcome);
    rdm_bonus_drawn_txt.setText(chip_text);
    rdm_bonus_winnings_txt.setText(money_outcome);
    rdm_bonus_resp.keys = undefined;
    rdm_bonus_resp.rt = undefined;
    _rdm_bonus_resp_allKeys = [];
    rdm_bonus_chip_poly.setFillColor(new util.Color(chip_color));
    rdm_bonus_chip_poly.setLineColor(new util.Color(chip_color));
    rdm_bonusMaxDuration = null
    // keep track of which components have finished
    rdm_bonusComponents = [];
    rdm_bonusComponents.push(rdm_bonus_img);
    rdm_bonusComponents.push(rdm_bonus_thanks_txt);
    rdm_bonusComponents.push(rdm_bonus_lott_top);
    rdm_bonusComponents.push(rdm_bonus_lott_bot);
    rdm_bonusComponents.push(rdm_bonus_sure_amt_txt);
    rdm_bonusComponents.push(rdm_bonus_prompt_txt);
    rdm_bonusComponents.push(rdm_bonus_choice_text_txt);
    rdm_bonusComponents.push(rdm_bonus_choice_outcome_txt);
    rdm_bonusComponents.push(rdm_bonus_drawn_txt);
    rdm_bonusComponents.push(rdm_bonus_winnings_txt);
    rdm_bonusComponents.push(rdm_bonus_space_txt);
    rdm_bonusComponents.push(rdm_bonus_resp);
    rdm_bonusComponents.push(rdm_bonus_chip_poly);
    
    for (const thisComponent of rdm_bonusComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function rdm_bonusRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rdm_bonus' ---
    // get current time
    t = rdm_bonusClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rdm_bonus_img* updates
    if (t >= 0.0 && rdm_bonus_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_img.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_img.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_img.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_thanks_txt* updates
    if (t >= 0.0 && rdm_bonus_thanks_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_thanks_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_thanks_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_thanks_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_lott_top* updates
    if (t >= 0.0 && rdm_bonus_lott_top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_lott_top.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_lott_top.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_lott_top.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_lott_bot* updates
    if (t >= 0.0 && rdm_bonus_lott_bot.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_lott_bot.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_lott_bot.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_lott_bot.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_sure_amt_txt* updates
    if (t >= 0.0 && rdm_bonus_sure_amt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_sure_amt_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_sure_amt_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_sure_amt_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_prompt_txt* updates
    if (t >= 0.0 && rdm_bonus_prompt_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_prompt_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_prompt_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_prompt_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_choice_text_txt* updates
    if (t >= 0.0 && rdm_bonus_choice_text_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_choice_text_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_choice_text_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_choice_text_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_choice_outcome_txt* updates
    if (t >= 0.0 && rdm_bonus_choice_outcome_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_choice_outcome_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_choice_outcome_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_choice_outcome_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_drawn_txt* updates
    if (t >= 0.0 && rdm_bonus_drawn_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_drawn_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_drawn_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_drawn_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_winnings_txt* updates
    if (t >= 0.0 && rdm_bonus_winnings_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_winnings_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_winnings_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_winnings_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_space_txt* updates
    if (t >= 0.0 && rdm_bonus_space_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_space_txt.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_space_txt.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_space_txt.setAutoDraw(true);
    }
    
    
    // *rdm_bonus_resp* updates
    if (t >= 0.0 && rdm_bonus_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_resp.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rdm_bonus_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rdm_bonus_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rdm_bonus_resp.clearEvents(); });
    }
    
    if (rdm_bonus_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rdm_bonus_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rdm_bonus_resp_allKeys = _rdm_bonus_resp_allKeys.concat(theseKeys);
      if (_rdm_bonus_resp_allKeys.length > 0) {
        rdm_bonus_resp.keys = _rdm_bonus_resp_allKeys[_rdm_bonus_resp_allKeys.length - 1].name;  // just the last key pressed
        rdm_bonus_resp.rt = _rdm_bonus_resp_allKeys[_rdm_bonus_resp_allKeys.length - 1].rt;
        rdm_bonus_resp.duration = _rdm_bonus_resp_allKeys[_rdm_bonus_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rdm_bonus_chip_poly* updates
    if (t >= 0.0 && rdm_bonus_chip_poly.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rdm_bonus_chip_poly.tStart = t;  // (not accounting for frame time here)
      rdm_bonus_chip_poly.frameNStart = frameN;  // exact frame index
      
      rdm_bonus_chip_poly.setAutoDraw(true);
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
    for (const thisComponent of rdm_bonusComponents)
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


function rdm_bonusRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rdm_bonus' ---
    for (const thisComponent of rdm_bonusComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    rdm_bonus_resp.stop();
    // the Routine "rdm_bonus" was not non-slip safe, so reset the non-slip timer
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
