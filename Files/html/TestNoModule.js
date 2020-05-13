/************* 
 * Test Test *
 *************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Test';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(IntroRoutineBegin);
flowScheduler.add(IntroRoutineEachFrame);
flowScheduler.add(IntroRoutineEnd);
flowScheduler.add(TrainingRoutineBegin);
flowScheduler.add(TrainingRoutineEachFrame);
flowScheduler.add(TrainingRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var IntroClock;
var Training_instructions;
var Space_to_continue;
var TrainingClock;
var Background;
var Hort_neg_375;
var Hort_neg_225;
var Hort_neg_075;
var Hort_pos_075;
var Hort_pos_225;
var Hort_pos_375;
var Vert_neg_675;
var Vert_neg_525;
var Vert_neg_375;
var Vert_neg_225;
var Vert_neg_075;
var Ver_pos_075;
var Vert_pos_225;
var Vert_pos_375;
var Vert_pos_525;
var Vert_pos_675;
var Outline_red;
var Outline_black;
var Stimuli;
var mouse;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Intro"
  IntroClock = new util.Clock();
  Training_instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'Training_instructions',
    text: 'PRACTICE LEARNING BLOCK\n\n\n\n\nYou will view a series of objects.\n\nEach object will move to a specific location on the grid.\n\nA red frame will appear when each object reaches its location.\n\nYour goal is to learn the specific location of each object on the grid.\n\nAfter the red frame turns black, you should click on the object to end the trial.\n\n\n\nPlease press the space bar to proceed.....\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Space_to_continue = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Training"
  TrainingClock = new util.Clock();
  Background = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Background', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Hort_neg_375 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_neg_375', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, (- 0.375)],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Hort_neg_225 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_neg_225', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, (- 0.225)],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  Hort_neg_075 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_neg_075', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, (- 0.075)],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  Hort_pos_075 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_pos_075', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, 0.075],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  Hort_pos_225 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_pos_225', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, 0.225],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  Hort_pos_375 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Hort_pos_375', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 0, pos: [0, 0.375],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -6, interpolate: true,
  });
  
  Vert_neg_675 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_neg_675', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [(- 0.675), 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -7, interpolate: true,
  });
  
  Vert_neg_525 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_neg_525', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [(- 0.525), 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -8, interpolate: true,
  });
  
  Vert_neg_375 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_neg_375', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [(- 0.375), 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  Vert_neg_225 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_neg_225', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [(- 0.225), 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -10, interpolate: true,
  });
  
  Vert_neg_075 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_neg_075', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [(- 0.075), 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -11, interpolate: true,
  });
  
  Ver_pos_075 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Ver_pos_075', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [0.075, 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -12, interpolate: true,
  });
  
  Vert_pos_225 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_pos_225', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [0.225, 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -13, interpolate: true,
  });
  
  Vert_pos_375 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_pos_375', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [0.375, 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -14, interpolate: true,
  });
  
  Vert_pos_525 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_pos_525', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [0.525, 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -15, interpolate: true,
  });
  
  Vert_pos_675 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'Vert_pos_675', 
    vertices: [[-[2, 2][0]/2.0, 0], [+[2, 2][0]/2.0, 0]],
    ori: 90, pos: [0.675, 0],
    lineWidth: 10, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -16, interpolate: true,
  });
  
  Outline_red = new visual.Rect ({
    win: psychoJS.window, name: 'Outline_red', 
    width: [0.31, 0.31][0], height: [0.31, 0.31][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1.0, (- 1), (- 1)]),
    fillColor: new util.Color([1.0, (- 1), (- 1)]),
    opacity: 0, depth: -17, interpolate: true,
  });
  
  Outline_black = new visual.Rect ({
    win: psychoJS.window, name: 'Outline_black', 
    width: [0.31, 0.31][0], height: [0.31, 0.31][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1), (- 1), (- 1)]),
    fillColor: new util.Color([(- 1), (- 1), (- 1)]),
    opacity: 0, depth: -18, interpolate: true,
  });
  
  Stimuli = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Stimuli', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -19.0 
  });
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var IntroComponents;
function IntroRoutineBegin() {
  //------Prepare to start Routine 'Intro'-------
  t = 0;
  IntroClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Space_to_continue.keys = undefined;
  Space_to_continue.rt = undefined;
  // keep track of which components have finished
  IntroComponents = [];
  IntroComponents.push(Training_instructions);
  IntroComponents.push(Space_to_continue);
  
  IntroComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function IntroRoutineEachFrame() {
  //------Loop for each frame of Routine 'Intro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = IntroClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Training_instructions* updates
  if (t >= 0.0 && Training_instructions.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Training_instructions.tStart = t;  // (not accounting for frame time here)
    Training_instructions.frameNStart = frameN;  // exact frame index
    Training_instructions.setAutoDraw(true);
  }

  
  // *Space_to_continue* updates
  if (t >= 0.0 && Space_to_continue.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Space_to_continue.tStart = t;  // (not accounting for frame time here)
    Space_to_continue.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { Space_to_continue.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { Space_to_continue.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { Space_to_continue.clearEvents(); });
  }

  if (Space_to_continue.status === PsychoJS.Status.STARTED) {
    let theseKeys = Space_to_continue.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      Space_to_continue.keys = theseKeys[0].name;  // just the last key pressed
      Space_to_continue.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  IntroComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function IntroRoutineEnd() {
  //------Ending Routine 'Intro'-------
  IntroComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  psychoJS.experiment.addData('Space_to_continue.keys', Space_to_continue.keys);
  if (typeof Space_to_continue.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('Space_to_continue.rt', Space_to_continue.rt);
      routineTimer.reset();
      }
  
  Space_to_continue.stop();
  // the Routine "Intro" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var gotValidClick;
var TrainingComponents;
function TrainingRoutineBegin() {
  //------Prepare to start Routine 'Training'-------
  t = 0;
  TrainingClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // setup some python lists for storing info about the mouse
  mouse.clicked_name = [];
  gotValidClick = false; // until a click is received
  // keep track of which components have finished
  TrainingComponents = [];
  TrainingComponents.push(Background);
  TrainingComponents.push(Hort_neg_375);
  TrainingComponents.push(Hort_neg_225);
  TrainingComponents.push(Hort_neg_075);
  TrainingComponents.push(Hort_pos_075);
  TrainingComponents.push(Hort_pos_225);
  TrainingComponents.push(Hort_pos_375);
  TrainingComponents.push(Vert_neg_675);
  TrainingComponents.push(Vert_neg_525);
  TrainingComponents.push(Vert_neg_375);
  TrainingComponents.push(Vert_neg_225);
  TrainingComponents.push(Vert_neg_075);
  TrainingComponents.push(Ver_pos_075);
  TrainingComponents.push(Vert_pos_225);
  TrainingComponents.push(Vert_pos_375);
  TrainingComponents.push(Vert_pos_525);
  TrainingComponents.push(Vert_pos_675);
  TrainingComponents.push(Outline_red);
  TrainingComponents.push(Outline_black);
  TrainingComponents.push(Stimuli);
  TrainingComponents.push(mouse);
  
  TrainingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
     });
  
  return Scheduler.Event.NEXT;
}

var prevButtonState;
function TrainingRoutineEachFrame() {
  //------Loop for each frame of Routine 'Training'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = TrainingClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Background* updates
  if (t >= 0.0 && Background.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Background.tStart = t;  // (not accounting for frame time here)
    Background.frameNStart = frameN;  // exact frame index
    Background.setAutoDraw(true);
  }

  
  // *Hort_neg_375* updates
  if (t >= 0.0 && Hort_neg_375.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_neg_375.tStart = t;  // (not accounting for frame time here)
    Hort_neg_375.frameNStart = frameN;  // exact frame index
    Hort_neg_375.setAutoDraw(true);
  }

  
  // *Hort_neg_225* updates
  if (t >= 0.0 && Hort_neg_225.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_neg_225.tStart = t;  // (not accounting for frame time here)
    Hort_neg_225.frameNStart = frameN;  // exact frame index
    Hort_neg_225.setAutoDraw(true);
  }

  
  // *Hort_neg_075* updates
  if (t >= 0 && Hort_neg_075.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_neg_075.tStart = t;  // (not accounting for frame time here)
    Hort_neg_075.frameNStart = frameN;  // exact frame index
    Hort_neg_075.setAutoDraw(true);
  }

  
  // *Hort_pos_075* updates
  if (t >= 0.0 && Hort_pos_075.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_pos_075.tStart = t;  // (not accounting for frame time here)
    Hort_pos_075.frameNStart = frameN;  // exact frame index
    Hort_pos_075.setAutoDraw(true);
  }

  
  // *Hort_pos_225* updates
  if (t >= 0.0 && Hort_pos_225.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_pos_225.tStart = t;  // (not accounting for frame time here)
    Hort_pos_225.frameNStart = frameN;  // exact frame index
    Hort_pos_225.setAutoDraw(true);
  }

  
  // *Hort_pos_375* updates
  if (t >= 0.0 && Hort_pos_375.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Hort_pos_375.tStart = t;  // (not accounting for frame time here)
    Hort_pos_375.frameNStart = frameN;  // exact frame index
    Hort_pos_375.setAutoDraw(true);
  }

  
  // *Vert_neg_675* updates
  if (t >= 0.0 && Vert_neg_675.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_neg_675.tStart = t;  // (not accounting for frame time here)
    Vert_neg_675.frameNStart = frameN;  // exact frame index
    Vert_neg_675.setAutoDraw(true);
  }

  
  // *Vert_neg_525* updates
  if (t >= 0.0 && Vert_neg_525.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_neg_525.tStart = t;  // (not accounting for frame time here)
    Vert_neg_525.frameNStart = frameN;  // exact frame index
    Vert_neg_525.setAutoDraw(true);
  }

  if (Vert_neg_525.status === PsychoJS.Status.STARTED && Boolean(0)) {
    Vert_neg_525.setAutoDraw(false);
  }
  
  // *Vert_neg_375* updates
  if (t >= 0.0 && Vert_neg_375.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_neg_375.tStart = t;  // (not accounting for frame time here)
    Vert_neg_375.frameNStart = frameN;  // exact frame index
    Vert_neg_375.setAutoDraw(true);
  }

  if (Vert_neg_375.status === PsychoJS.Status.STARTED && Boolean(0)) {
    Vert_neg_375.setAutoDraw(false);
  }
  
  // *Vert_neg_225* updates
  if (t >= 0.0 && Vert_neg_225.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_neg_225.tStart = t;  // (not accounting for frame time here)
    Vert_neg_225.frameNStart = frameN;  // exact frame index
    Vert_neg_225.setAutoDraw(true);
  }

  if (Vert_neg_225.status === PsychoJS.Status.STARTED && Boolean(0)) {
    Vert_neg_225.setAutoDraw(false);
  }
  
  // *Vert_neg_075* updates
  if (t >= 0.0 && Vert_neg_075.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_neg_075.tStart = t;  // (not accounting for frame time here)
    Vert_neg_075.frameNStart = frameN;  // exact frame index
    Vert_neg_075.setAutoDraw(true);
  }

  
  // *Ver_pos_075* updates
  if (t >= 0.0 && Ver_pos_075.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Ver_pos_075.tStart = t;  // (not accounting for frame time here)
    Ver_pos_075.frameNStart = frameN;  // exact frame index
    Ver_pos_075.setAutoDraw(true);
  }

  
  // *Vert_pos_225* updates
  if (t >= 0.0 && Vert_pos_225.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_pos_225.tStart = t;  // (not accounting for frame time here)
    Vert_pos_225.frameNStart = frameN;  // exact frame index
    Vert_pos_225.setAutoDraw(true);
  }

  
  // *Vert_pos_375* updates
  if (t >= 0.0 && Vert_pos_375.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_pos_375.tStart = t;  // (not accounting for frame time here)
    Vert_pos_375.frameNStart = frameN;  // exact frame index
    Vert_pos_375.setAutoDraw(true);
  }

  
  // *Vert_pos_525* updates
  if (t >= 0.0 && Vert_pos_525.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_pos_525.tStart = t;  // (not accounting for frame time here)
    Vert_pos_525.frameNStart = frameN;  // exact frame index
    Vert_pos_525.setAutoDraw(true);
  }

  
  // *Vert_pos_675* updates
  if (t >= 0.0 && Vert_pos_675.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Vert_pos_675.tStart = t;  // (not accounting for frame time here)
    Vert_pos_675.frameNStart = frameN;  // exact frame index
    Vert_pos_675.setAutoDraw(true);
  }

  if (Vert_pos_675.status === PsychoJS.Status.STARTED && Boolean(0)) {
    Vert_pos_675.setAutoDraw(false);
  }
  
  // *Outline_red* updates
  if (t >= 0.0 && Outline_red.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Outline_red.tStart = t;  // (not accounting for frame time here)
    Outline_red.frameNStart = frameN;  // exact frame index
    Outline_red.setAutoDraw(true);
  }

  
  // *Outline_black* updates
  if (t >= 0.0 && Outline_black.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Outline_black.tStart = t;  // (not accounting for frame time here)
    Outline_black.frameNStart = frameN;  // exact frame index
    Outline_black.setAutoDraw(true);
  }

  
  // *Stimuli* updates
  if (t >= 0.0 && Stimuli.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Stimuli.tStart = t;  // (not accounting for frame time here)
    Stimuli.frameNStart = frameN;  // exact frame index
    Stimuli.setAutoDraw(true);
  }

  
  if (Stimuli.status === PsychoJS.Status.STARTED){ // only update if being drawn
    Stimuli.setPos([0, 0]);
    Stimuli.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects_pract/1.jpg');
  }
  // *mouse* updates
  if ((0.0) && mouse.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mouse.tStart = t;  // (not accounting for frame time here)
    mouse.frameNStart = frameN;  // exact frame index
    mouse.status = PsychoJS.Status.STARTED;
    mouse.mouseClock.reset();
    prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
    }
  if (mouse.status === PsychoJS.Status.STARTED && Boolean(1.0)) {
    mouse.status = PsychoJS.Status.FINISHED;
  }
  if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
    let buttons = mouse.getPressed();
    if (!buttons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
      prevButtonState = buttons;
      if (buttons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
        // check if the mouse was inside our 'clickable' objects
        gotValidClick = false;
        for (const obj of [Stimuli]) {
          if (obj.contains(mouse)) {
            gotValidClick = true;
            mouse.clicked_name.push(obj.name)
          }
        }
        if (gotValidClick === true) { // abort routine on response
          continueRoutine = false;
        }
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  TrainingComponents.forEach( function(thisComponent) {
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
    }});
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function TrainingRoutineEnd() {
  //------Ending Routine 'Training'-------
  TrainingComponents.forEach( function(thisComponent) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }});
  // store data for thisExp (ExperimentHandler)
  const xys = mouse.getPos();
  const buttons = mouse.getPressed();
  psychoJS.experiment.addData('mouse.x', xys[0]);
  psychoJS.experiment.addData('mouse.y', xys[1]);
  psychoJS.experiment.addData('mouse.leftButton', buttons[0]);
  psychoJS.experiment.addData('mouse.midButton', buttons[1]);
  psychoJS.experiment.addData('mouse.rightButton', buttons[2]);
  if (mouse.clicked_name.length > 0) {
    psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0]);}
  // the Routine "Training" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
