"""
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, monitors, core, data, event, logging, clock
prefs.hardware['audioLib'] = ['PTB']
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, linalg, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__))
_thisDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects"
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Final_build'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lehlert/.spyder-py3/Psycho-Py/Tambini_Exp/Tambini_Exp.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
#change to adjust sizes of grid and stims 
height=900
width=1440
m = monitors.Monitor("default", width=28.8, distance=200)
m.setSizePix((width, height))
m.save()

# Setup the Window
win = visual.Window(
    size= m.getSizePix(), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor=m, color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
#expInfo['frameRate'] = win.getActualFrameRate()
expInfo['frameRate'] = 60
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

#set random stim locations 
coord_x_list = []
coord_y_list = []
coordFlag=True

# set up handler to look after randomisation of conditions etc
#change nReps here to effect overall rounds of data testing
rounds = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rounds')
#thisExp.addLoop(rounds)  # add the loop to the experiment
thisRound = rounds.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRound.rgb)
if thisRound != None:
    for paramName in thisRound:
        exec('{} = thisRound[paramName]'.format(paramName))

for thisRound in rounds:
    currentLoop = rounds
    # abbreviate parameter names if possible (e.g. rgb = thisRound.rgb)
    if thisRound != None:
        for paramName in thisRound:
            exec('{} = thisRound[paramName]'.format(paramName))

    thisRound = 1
    delay=30
    # Initialize components for Routine "Train_Intro"
    stim_size=((width/11),(width/11))
    outline_size=((width/11)+5,(width/11)+5)
    letter_size=(height/40)
    Train_IntroClock = core.Clock()
    Training_instructions_2 = visual.TextStim(win=win, name='Training_instructions_2',
        text='LEARNING BLOCK\n\n\n\n\nYou will view a series of objects.\n\nEach object will move to a specific location on the grid.cA red frame will appear when each object reaches its location.\n\nYour goal is to learn the specific location of each object on the grid.\n\nAfter the red frame turns black, you should click on the object to end the trial.\n\n\n\nPlease press the space bar to proceed.....\n',
        font='Arial',
        pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    Space_to_continue_2 = keyboard.Keyboard()
    
    # Initialize components for Routine "Training"
    TrainingClock = core.Clock()
    Outline_red_2 = visual.Rect(
        win=win, name='Outline_red_2',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=10, lineColor=[1.0,-1,-1], lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=0.0, interpolate=True)
    Outline_black_2 = visual.Rect(
        win=win, name='Outline_black_2',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=10, lineColor=[-1,-1,-1], lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=-1.0, interpolate=True)
    Stimuli_2 = visual.ImageStim(
        win=win,
        name='Stimuli_2', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=stim_size,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # Initialize components for Routine "Test_Intro"
    Test_IntroClock = core.Clock()
    Training_instructions = visual.TextStim(win=win, name='Training_instructions',
        text='TEST BLOCK\n\n\n\nA object will be presented in the center of the screen on each trial.\n\nClick and drag the object, as accurately as possible, to its specific location on the grid.\n\nYou have the option of changing your initial position by clicking and dragging the object for a second time.\n\nWhen you have selected the final location, a blue frame will appear around the object.\n\nA red frame will then appear around the true location of the object.\n\nIf your selection was approximately correct, the blue frame will turn green.\n\nIf your selection was not accurate, a line will be drawn between your location and the true location.\n\nPlease use this information to learn about the correct location for future trials.\n\n\nPlease press the space bar to proceed.....\n',
        font='Arial',
        pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    Space_to_continue = keyboard.Keyboard()
    
    # Initialize components for Routine "Testing"
    TestingClock = core.Clock()
    Outline_red = visual.Rect(
        win=win, name='Outline_red',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=50, lineColor=[1.0,-1,-1], lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=0.0, interpolate=True)
    Outline_black = visual.Rect(
        win=win, name='Outline_black',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=50, lineColor=[-1,-1,-1], lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=-1.0, interpolate=True)
    Outline_green = visual.Rect(
        win=win, name='Outline_green',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=50, lineColor='Chartreuse', lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=-2.0, interpolate=True)
    Outline_blue = visual.Rect(
        win=win, name='Outline_blue',
        width=outline_size[0], height=outline_size[1],
        ori=0, pos=(0, 0),
        lineWidth=50, lineColor='Blue', lineColorSpace='rgb',
        fillColor=None, fillColorSpace='rgb',
        opacity=0, depth=-3.0, interpolate=True)
    Target = visual.ImageStim(
        win=win,
        name='Target', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=stim_size,
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    Stimuli = visual.ImageStim(
        win=win,
        name='Stimuli', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=stim_size,
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    Mouse = event.Mouse(win=win)
    x, y = [None, None]
    Mouse.mouseClock = core.Clock()
    Mouse1 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse1.mouseClock = core.Clock()
    Mouse2 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse2.mouseClock = core.Clock()
    wrongCounter=0
    looper=0
    #initialize line used to connect target and user location in the testing routine 
    myLine = visual.Line(win, start=(0,0), end=(0,0), lineColor='black', lineColorSpace='rgb')
    myLine.lineWidth = 10
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
            
    # ------Prepare to start Routine "Train_Intro"-------
    # update component parameters for each repeat
    Space_to_continue_2.keys = []
    Space_to_continue_2.rt = []
    #makes mouse invisible 
    win.mouseVisible = 0
    # keep track of which components have finished
    Train_IntroComponents = [Training_instructions_2, Space_to_continue_2]
    for thisComponent in Train_IntroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Train_IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Train_Intro"-------
    while continueRoutine:
        # get current time
        t = Train_IntroClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Train_IntroClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Training_instructions_2* updates
        if Training_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Training_instructions_2.frameNStart = frameN  # exact frame index
            Training_instructions_2.tStart = t  # local t and not account for scr refresh
            Training_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Training_instructions_2, 'tStartRefresh')  # time at next scr refresh
            Training_instructions_2.setAutoDraw(True)
        
        # *Space_to_continue_2* updates
        waitOnFlip = False
        if Space_to_continue_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Space_to_continue_2.frameNStart = frameN  # exact frame index
            Space_to_continue_2.tStart = t  # local t and not account for scr refresh
            Space_to_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Space_to_continue_2, 'tStartRefresh')  # time at next scr refresh
            Space_to_continue_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Space_to_continue_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Space_to_continue_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Space_to_continue_2.status == STARTED and not waitOnFlip:
            theseKeys = Space_to_continue_2.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Space_to_continue_2.keys = theseKeys.name  # just the last key pressed
                Space_to_continue_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            win.close()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Train_IntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Train_Intro"-------
    for thisComponent in Train_IntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #thisExp.addData('Training_instructions_2.started', Training_instructions_2.tStartRefresh)
    #thisExp.addData('Training_instructions_2.stopped', Training_instructions_2.tStopRefresh)
    # check responses
    if Space_to_continue_2.keys in ['', [], None]:  # No response was made
        Space_to_continue_2.keys = None
    #thisExp.addData('Space_to_continue_2.keys',Space_to_continue_2.keys)
    #if Space_to_continue_2.keys != None:  # we had a response
        #thisExp.addData('Space_to_continue_2.rt', Space_to_continue_2.rt)
    #thisExp.addData('Space_to_continue_2.started', Space_to_continue_2.tStartRefresh)
    #thisExp.addData('Space_to_continue_2.stopped', Space_to_continue_2.tStopRefresh)
    #thisExp.nextEntry()
    #returns mouse at the end of the routine
    win.mouseVisible = 1
    # the Routine "Train_Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Trials.xlsx'),
        seed=None, name='training')
    thisExp.addLoop(training)  # add the loop to the experiment
    thisTrial = training.trialList[0]  # so we can initialize stimuli with some values
    runs=len(training.trialList)
    looper=0
    
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    #on first run creates random locations for stims      
    if coordFlag == True:
        for i in training.trialList:
            coord_x_list.append(randint((-(width/2)+(width/11)),((width/2)-(width/11))))
            coord_y_list.append(randint((-(height/2)+(width/11)),((height/2))-(width/11)))
        coordFlag = False
    
    for thisTrial in training:
        currentLoop = training
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Training"-------
        # update component parameters for each repeat
        Stimuli_2.setPos((0,0))
        Stimuli_2.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects_pract/1.jpg')
        #declare necessary variables and flags
        #function that creates grid over screen based upon resolution input
        gridList = [] 
        def create_grid(list):
            
            lineXPos  = -(width/2)
            lineYPos = -(height/2)
            
            #create grid
            while lineXPos<(width/2):
                gridList.append(visual.Line(win, start=(lineXPos,(height/2)), end=(lineXPos, -(height/2)), lineColor='white', lineColorSpace='rgb'))
                lineXPos = lineXPos + (width/11)
                
            while lineYPos<(height/2):
                gridList.append(visual.Line(win, start=((width/2),lineYPos), end=(-(width/2),lineYPos), lineColor='white', lineColorSpace='rgb'))
                lineYPos = lineYPos + (width/11)
                
            for line in gridList:
                line.lineWidth = 10
                line.setAutoDraw(True)
        
        training.addData('order', looper+1)
        training.addData('xCoord', coord_x_list[looper])
        training.addData('yCoord', coord_y_list[looper])
        
        #using the fuction to create the grid
        create_grid(gridList)
        #set the stim image from the directroy each loop
        Stimuli_2.setImage(stim)
    
        #make the mouse invisible
        win.mouseVisible = 0
        xFlag=0
        yFlag=0
        finalFlag= 0
        #set starting position for Stim image (so it starts in the center)
        xPos=0
        yPos=0
        Stimuli_2.setPos((xPos,yPos))
        #set the movement rates for the Stimuli image
        #rate comes from the excel sheet, this is the number of frames it takes for the image to reach its final destination
        xMov=(coord_x_list[looper]/expInfo['frameRate'])
        yMov=(coord_y_list[looper]/expInfo['frameRate'])
        
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        TrainingComponents = [Outline_red_2, Outline_black_2, Stimuli_2, mouse]
        for thisComponent in TrainingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Training"-------
        while continueRoutine:
            # get current time
            t = TrainingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrainingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Outline_red_2* updates
            if Outline_red_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_red_2.frameNStart = frameN  # exact frame index
                Outline_red_2.tStart = t  # local t and not account for scr refresh
                Outline_red_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_red_2, 'tStartRefresh')  # time at next scr refresh
                Outline_red_2.setAutoDraw(True)
            
            # *Outline_black_2* updates
            if Outline_black_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_black_2.frameNStart = frameN  # exact frame index
                Outline_black_2.tStart = t  # local t and not account for scr refresh
                Outline_black_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_black_2, 'tStartRefresh')  # time at next scr refresh
                Outline_black_2.setAutoDraw(True)
            
            # *Stimuli_2* updates
            if Stimuli_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stimuli_2.frameNStart = frameN  # exact frame index
                Stimuli_2.tStart = t  # local t and not account for scr refresh
                Stimuli_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stimuli_2, 'tStartRefresh')  # time at next scr refresh
                Stimuli_2.setAutoDraw(True)
            #delays the start of the movement of the images by delay frames
            if delay >0:
                delay=delay-1
            #after delay starts here
            else:
                #check if xCoord is positive or negative the flags are 1 if positive else remain 0
                if coord_x_list[looper]>0:
                    xFlag=1 
                #checks if yCoord is positive or negative (see above for flag function)
                if coord_y_list[looper]>0:
                    yFlag=1
                    
                    #while the image hasn't reached it's final coordinates keep animating it
                if finalFlag==0:
                    #if final x destination is positive keep moving x while it is less then the final coordinate
                    if xFlag==1: 
                        if xPos<coord_x_list[looper]:
                            xPos=xPos+xMov
                    #otherwise keep moving x while it is greater then the final  =x coordinate
                    else:
                        if xPos>coord_x_list[looper]:
                            xPos=xPos+xMov
                    #do the same as above but for y 
                    if yFlag==1:
                        if yPos<coord_y_list[looper]:
                            yPos=yPos+yMov
                    else:
                        if yPos>coord_y_list[looper]:
                            yPos=yPos+yMov
                    #after changing current x and y coordinates reset the position 
                    Stimuli_2.setPos((xPos,yPos))
                    #check if the final flag should be set AKA both x and y have reached the final coordinate 
                    if xFlag==1 and yFlag==1:
                        if xPos>=coord_x_list[looper] and yPos>=coord_y_list[looper]:
                            finalFlag=1
                    elif xFlag==1 and yFlag==0:
                        if xPos>=coord_x_list[looper] and yPos<=coord_y_list[looper]:
                            finalFlag=1
                    elif xFlag==0 and yFlag==1:
                        if xPos<=coord_x_list[looper] and yPos>=coord_y_list[looper]:
                            finalFlag=1
                    elif xFlag==0 and yFlag==0:
                        if xPos<=coord_x_list[looper] and yPos<=coord_y_list[looper]:
                            finalFlag=1
                #once the final flag is set begin the termination of the routine 
                if finalFlag>=1:
                    #a 30 frame delay built in some things don't happen to quickly
                    if finalFlag >= 30:
                        #move the outlines to the final position and then use opacity to turn them on and off 
                        Outline_black_2.setPos((xPos,yPos))
                        Outline_black_2.opacity = 1
                        Outline_red_2.opacity = 0
                        #make it so the mouse starts over the stimuli 
                        mouse.setPos(Stimuli_2.pos)
                        win.mouseVisible = 1
                    else:
                        Outline_red_2.setPos((xPos,yPos))
                        Outline_red_2.opacity = 1
                        finalFlag = finalFlag+1 
            
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [Stimuli_2]:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
            #skips the training 
            if defaultKeyboard.getKeys(keyList=["s"]):
                break
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Training"-------
        for thisComponent in TrainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #training.addData('Outline_red_2.started', Outline_red_2.tStartRefresh)
        #training.addData('Outline_red_2.stopped', Outline_red_2.tStopRefresh)
        #training.addData('Outline_black_2.started', Outline_black_2.tStartRefresh)
        #training.addData('Outline_black_2.stopped', Outline_black_2.tStopRefresh)
        #training.addData('Stimuli_2.started', Stimuli_2.tStartRefresh)
        #training.addData('Stimuli_2.stopped', Stimuli_2.tStopRefresh)
        #make sure the outlines are invisible again before next loop
        Outline_red_2.opacity = 0
        Outline_black_2.opacity = 0
        
        #removing the grid
        for line in gridList:
            line.setAutoDraw(False)
            
        # store data for training (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [Stimuli_2]:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        #training.addData('mouse.x', x)
        #training.addData('mouse.y', y)
        #training.addData('mouse.leftButton', buttons[0])
        #training.addData('mouse.midButton', buttons[1])
        #training.addData('mouse.rightButton', buttons[2])
       # if len(mouse.clicked_name):
            #training.addData('mouse.clicked_name', mouse.clicked_name[0])
        #training.addData('mouse.started', mouse.tStart)
        #training.addData('mouse.stopped', mouse.tStop)
        # the Routine "Training" was not non-slip safe, so reset the non-slip timer
        looper=looper+1
        routineTimer.reset()
        thisExp.nextEntry()
        
    #save training data
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+ '%_training_'+ str(thisRound)
    training.saveAsExcel(filename, appendFile=False, fileCollisionMethod='rename')
    
    # completed 1 repeats of 'training'
    
    
    # ------Prepare to start Routine "Test_Intro"-------
    # update component parameters for each repeat
    Space_to_continue.keys = []
    Space_to_continue.rt = []
    win.mouseVisible = 0
    # keep track of which components have finished
    Test_IntroComponents = [Training_instructions, Space_to_continue]
    for thisComponent in Test_IntroComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Test_IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Test_Intro"-------
    while continueRoutine:
        # get current time
        t = Test_IntroClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Test_IntroClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Training_instructions* updates
        if Training_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Training_instructions.frameNStart = frameN  # exact frame index
            Training_instructions.tStart = t  # local t and not account for scr refresh
            Training_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Training_instructions, 'tStartRefresh')  # time at next scr refresh
            Training_instructions.setAutoDraw(True)
        
        # *Space_to_continue* updates
        waitOnFlip = False
        if Space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Space_to_continue.frameNStart = frameN  # exact frame index
            Space_to_continue.tStart = t  # local t and not account for scr refresh
            Space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Space_to_continue, 'tStartRefresh')  # time at next scr refresh
            Space_to_continue.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Space_to_continue.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Space_to_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Space_to_continue.status == STARTED and not waitOnFlip:
            theseKeys = Space_to_continue.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                Space_to_continue.keys = theseKeys.name  # just the last key pressed
                Space_to_continue.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            win.close()
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Test_IntroComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Test_Intro"-------
    for thisComponent in Test_IntroComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #thisExp.addData('Training_instructions.started', Training_instructions.tStartRefresh)
    #thisExp.addData('Training_instructions.stopped', Training_instructions.tStopRefresh)
    # check responses
    if Space_to_continue.keys in ['', [], None]:  # No response was made
        Space_to_continue.keys = None
    #thisExp.addData('Space_to_continue.keys',Space_to_continue.keys)
    #if Space_to_continue.keys != None:  # we had a response
        #thisExp.addData('Space_to_continue.rt', Space_to_continue.rt)
    #thisExp.addData('Space_to_continue.started', Space_to_continue.tStartRefresh)
    #thisExp.addData('Space_to_continue.stopped', Space_to_continue.tStopRefresh)
    #thisExp.nextEntry()
    win.mouseVisible = 1
    # the Routine "Test_Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testing = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Trials.xlsx'),
        seed=None, name='testing')
    thisExp.addLoop(testing)  # add the loop to the experiment
    thisTest = testing.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    looper=0
    nextFlag=True
    
    for thisTest in testing:
        currentLoop = testing
        # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
        if thisTest != None:
            for paramName in thisTest:
                exec('{} = thisTest[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Testing"-------
        # update component parameters for each repeat
        Target.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects/1a.jpg')
        Stimuli.setPos((0,0))
        Stimuli.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects/1a.jpg')
        xCoord = []
        yCoord = []
        stimPos = []
        targetPos =[]
        order = []
        delay=30
        doneFlag=0
        # setup some python lists for storing info about the Mouse
        Mouse.x = []
        Mouse.y = []
        Mouse.leftButton = []
        Mouse.midButton = []
        Mouse.rightButton = []
        Mouse.time = []
        Mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # setup some python lists for storing info about the Mouse1
        Mouse1.x = []
        Mouse1.y = []
        Mouse1.leftButton = []
        Mouse1.midButton = []
        Mouse1.rightButton = []
        Mouse1.time = []
        Mouse1.clicked_name = []
        gotValidClick = False  # until a click is received
        # setup some python lists for storing info about the Mouse2
        Mouse2.x = []
        Mouse2.y = []
        Mouse2.leftButton = []
        Mouse2.midButton = []
        Mouse2.rightButton = []
        Mouse2.time = []
        gotValidClick = False  # until a click is received
        #declare necessary variables and flags
        create_grid(gridList)
        Stimuli.opacity = 1
        Stimuli.setImage(stim)
        xPos=0
        yPos=0
        Stimuli.setPos((xPos,yPos))
        if looper<runs:
            Target.setPos((coord_x_list[looper],coord_y_list[looper]))
        mouse_has_been_pressed = False
        startMouse1=0
        
        # keep track of which components have finished
        TestingComponents = [Outline_red, Outline_black, Outline_green, Outline_blue, Target, Stimuli, Mouse, Mouse1, Mouse2]
        for thisComponent in TestingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TestingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Testing"-------
        while continueRoutine:
            # get current time
            t = TestingClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TestingClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Outline_red* updates
            if Outline_red.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_red.frameNStart = frameN  # exact frame index
                Outline_red.tStart = t  # local t and not account for scr refresh
                Outline_red.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_red, 'tStartRefresh')  # time at next scr refresh
                Outline_red.setAutoDraw(True)
            
            # *Outline_black* updates
            if Outline_black.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_black.frameNStart = frameN  # exact frame index
                Outline_black.tStart = t  # local t and not account for scr refresh
                Outline_black.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_black, 'tStartRefresh')  # time at next scr refresh
                Outline_black.setAutoDraw(True)
            
            # *Outline_green* updates
            if Outline_green.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_green.frameNStart = frameN  # exact frame index
                Outline_green.tStart = t  # local t and not account for scr refresh
                Outline_green.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_green, 'tStartRefresh')  # time at next scr refresh
                Outline_green.setAutoDraw(True)
            
            # *Outline_blue* updates
            if Outline_blue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Outline_blue.frameNStart = frameN  # exact frame index
                Outline_blue.tStart = t  # local t and not account for scr refresh
                Outline_blue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outline_blue, 'tStartRefresh')  # time at next scr refresh
                Outline_blue.setAutoDraw(True)
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.setAutoDraw(True)
            if Target.status == STARTED:  # only update if drawing
                Target.setPos((coord_x_list[looper],coord_y_list[looper]), log=False)
            
            # *Stimuli* updates
            if Stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stimuli.frameNStart = frameN  # exact frame index
                Stimuli.tStart = t  # local t and not account for scr refresh
                Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
                Stimuli.setAutoDraw(True)
            # *Mouse* updates
            if Mouse.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                Mouse.frameNStart = frameN  # exact frame index
                Mouse.tStart = t  # local t and not account for scr refresh
                Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mouse, 'tStartRefresh')  # time at next scr refresh
                Mouse.status = STARTED
                Mouse.mouseClock.reset()
                prevButtonState = Mouse.getPressed()  # if button is down already this ISN'T a new click
            if Mouse.status == STARTED:
                if bool(startMouse1==1):
                    # keep track of stop time/frame for later
                    Mouse.tStop = t  # not accounting for scr refresh
                    Mouse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Mouse, 'tStopRefresh')  # time at next scr refresh
                    Mouse.status = FINISHED
            if Mouse.status == STARTED:  # only update if started and not finished!
                x, y = Mouse.getPos()
                Mouse.x.append(x)
                Mouse.y.append(y)
                buttons = Mouse.getPressed()
                Mouse.leftButton.append(buttons[0])
                Mouse.midButton.append(buttons[1])
                Mouse.rightButton.append(buttons[2])
                Mouse.time.append(Mouse.mouseClock.getTime())
            # *Mouse1* updates
            if Mouse1.status == NOT_STARTED and startMouse1==1:
                # keep track of start time/frame for later
                Mouse1.frameNStart = frameN  # exact frame index
                Mouse1.tStart = t  # local t and not account for scr refresh
                Mouse1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mouse1, 'tStartRefresh')  # time at next scr refresh
                Mouse1.status = STARTED
                Mouse1.mouseClock.reset()
                prevButtonState = Mouse1.getPressed()  # if button is down already this ISN'T a new click
            if Mouse1.status == STARTED:
                if bool(startMouse1==0):
                    # keep track of stop time/frame for later
                    Mouse1.tStop = t  # not accounting for scr refresh
                    Mouse1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Mouse1, 'tStopRefresh')  # time at next scr refresh
                    Mouse1.status = FINISHED
            if Mouse1.status == STARTED:  # only update if started and not finished!
                x, y = Mouse1.getPos()
                Mouse1.x.append(x)
                Mouse1.y.append(y)
                buttons = Mouse1.getPressed()
                Mouse1.leftButton.append(buttons[0])
                Mouse1.midButton.append(buttons[1])
                Mouse1.rightButton.append(buttons[2])
                Mouse1.time.append(Mouse1.mouseClock.getTime())
            # *Mouse2* updates
            if Mouse2.status == NOT_STARTED and doneFlag==1:
                # keep track of start time/frame for later
                Mouse2.frameNStart = frameN  # exact frame index
                Mouse2.tStart = t  # local t and not account for scr refresh
                Mouse2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mouse2, 'tStartRefresh')  # time at next scr refresh
                Mouse2.status = STARTED
                Mouse2.mouseClock.reset()
                prevButtonState = Mouse2.getPressed()  # if button is down already this ISN'T a new click
            if Mouse2.status == STARTED:  # only update if started and not finished!
                x, y = Mouse2.getPos()
                Mouse2.x.append(x)
                Mouse2.y.append(y)
                buttons = Mouse2.getPressed()
                Mouse2.leftButton.append(buttons[0])
                Mouse2.midButton.append(buttons[1])
                Mouse2.rightButton.append(buttons[2])
                Mouse2.time.append(Mouse2.mouseClock.getTime())
                buttons = Mouse2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        continueRoutine = False
            
            if Mouse.isPressedIn(Stimuli, buttons=[0]) and startMouse1==0:
                Stimuli.pos = Mouse.getPos()
                Outline_blue.pos = Mouse.getPos()
                mouse_has_been_pressed = True
                
            if not Mouse.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True and startMouse1==0:
                mouse_has_been_pressed = False
                startMouse1=1
                
            else:
                if Mouse1.isPressedIn(Stimuli, buttons=[0]):
                    Stimuli.pos = Mouse.getPos()
                    Outline_blue.pos = Mouse.getPos()
                    mouse_has_been_pressed = True    
                    
                if not Mouse1.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True:
                    mouse_has_been_pressed = False
                    Outline_blue.opacity = 1
                    dist=[]
                    dist=np.linalg.norm(Stimuli.pos-Target.pos)
                    testing.addData('stimPos', Stimuli.pos)
                    testing.addData('targetPos', Target.pos)
                    if Stimuli.overlaps(Target):
                        Outline_green.pos = Stimuli.pos
                        Outline_green.opacity = 1
                        Stimuli.pos=Target.pos
                        Outline_blue.pos = Target.pos
                        if looper==runs-1:
                            textWrong = visual.TextStim(win, text='You performed well on '+str(100*((runs-wrongCounter)/runs))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
                            textRight = visual.TextStim(win, text='Congrats, you performed well on '+str(100*((runs-wrongCounter)/runs))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.', font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
                            Stimuli.opacity = 0
                            Outline_red.opacity = 0
                            Outline_blue.opacity = 0
                            Outline_green.opacity = 0
                            myLine.setAutoDraw(False)
                            for line in gridList:
                                line.setAutoDraw(False)
                            if wrongCounter>=(runs/2):
                                textWrong.setAutoDraw(True)
                                doneFlag=1
                            else:
                                textRight.setAutoDraw(True)
                                doneFlag=1
                        else:
                            doneFlag=1
                    else:
                        Outline_red.pos = Stimuli.pos
                        Outline_red.opacity = 1
                        Outline_green.pos=Stimuli.pos
                        Stimuli.pos=Target.pos
                        Outline_blue.pos = Target.pos
                        wrongCounter=wrongCounter+1
                        myLine.start=Target.pos
                        myLine.end=Outline_green.pos
                        myLine.setAutoDraw(True)
                        if looper==runs-1:
                            textWrong = visual.TextStim(win, text='You performed well on '+str(100*((runs-wrongCounter)/runs))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
                            textRight = visual.TextStim(win, text='Congrats, you performed well on '+str(100*((runs-wrongCounter)/runs))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.', font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
                            Stimuli.opacity = 0
                            Outline_red.opacity = 0
                            Outline_blue.opacity = 0
                            Outline_green.opacity = 0
                            myLine.setAutoDraw(False)
                            for line in gridList:
                                line.setAutoDraw(False)
                            if wrongCounter>=2:
                                textWrong.setAutoDraw(True)
                                doneFlag=1
                            else:
                                textRight.setAutoDraw(True)
                                doneFlag=1
                        else:
                            doneFlag=1
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        # -------Ending Routine "Testing"-------
        for thisComponent in TestingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        testing.addData('xCoord', coord_x_list[looper])
        testing.addData('yCoord', coord_y_list[looper])
        testing.addData('Error', dist)
        #testing.addData('Outline_red.started', Outline_red.tStartRefresh)
        #testing.addData('Outline_red.stopped', Outline_red.tStopRefresh)
        #testing.addData('Outline_black.started', Outline_black.tStartRefresh)
        #testing.addData('Outline_black.stopped', Outline_black.tStopRefresh)
        #testing.addData('Outline_green.started', Outline_green.tStartRefresh)
        #testing.addData('Outline_green.stopped', Outline_green.tStopRefresh)
        #testing.addData('Outline_blue.started', Outline_blue.tStartRefresh)
        #testing.addData('Outline_blue.stopped', Outline_blue.tStopRefresh)
        #testing.addData('Target.started', Target.tStartRefresh)
        #testing.addData('Target.stopped', Target.tStopRefresh)
        #testing.addData('Stimuli.started', Stimuli.tStartRefresh)
        #testing.addData('Stimuli.stopped', Stimuli.tStopRefresh)
        # store data for testing (TrialHandler)
        #testing.addData('Mouse.x', Mouse.x)
        #testing.addData('Mouse.y', Mouse.y)
        #testing.addData('Mouse.leftButton', Mouse.leftButton)
        #testing.addData('Mouse.midButton', Mouse.midButton)
        #testing.addData('Mouse.rightButton', Mouse.rightButton)
        #testing.addData('Mouse.time', Mouse.time)
        #testing.addData('Mouse.clicked_name', Mouse.clicked_name)
        #testing.addData('Mouse.started', Mouse.tStart)
        #testing.addData('Mouse.stopped', Mouse.tStop)
        # store data for testing (TrialHandler)
        #testing.addData('Mouse1.x', Mouse1.x)
        #testing.addData('Mouse1.y', Mouse1.y)
        #testing.addData('Mouse1.leftButton', Mouse1.leftButton)
        #testing.addData('Mouse1.midButton', Mouse1.midButton)
        #testing.addData('Mouse1.rightButton', Mouse1.rightButton)
        #testing.addData('Mouse1.time', Mouse1.time)
        #testing.addData('Mouse1.clicked_name', Mouse1.clicked_name)
        #testing.addData('Mouse1.started', Mouse1.tStart)
        #testing.addData('Mouse1.stopped', Mouse1.tStop)
        # store data for testing (TrialHandler)
        #testing.addData('Mouse2.x', Mouse2.x)
        #testing.addData('Mouse2.y', Mouse2.y)
        #testing.addData('Mouse2.leftButton', Mouse2.leftButton)
        #testing.addData('Mouse2.midButton', Mouse2.midButton)
        #testing.addData('Mouse2.rightButton', Mouse2.rightButton)
        #testing.addData('Mouse2.time', Mouse2.time)
        #testing.addData('Mouse2.started', Mouse2.tStart)
        #testing.addData('Mouse2.stopped', Mouse2.tStop)
        Outline_red.opacity = 0
        Outline_blue.opacity = 0
        Outline_green.opacity = 0
        if looper==runs-1:
            textRight.setAutoDraw(False)
            textWrong.setAutoDraw(False)
        myLine.setAutoDraw(False)
        
    
        # the Routine "Testing" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        #if looper==runs-1:
        #    nextFlag=False
        #if nextFlag==True:
        thisExp.nextEntry()
        
        looper=looper+1
        
    #saving testing data
    filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+'_testing_'+ str(thisRound)
    testing.saveAsExcel(filename,appendFile=False, fileCollisionMethod='rename')
    
    # completed 1 repeats of 'testing'
    thisRound = thisRound+1
            
# completed 2 repeats of 'rounds'
        
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)

thisExp.saveAsWideText(filename)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()


