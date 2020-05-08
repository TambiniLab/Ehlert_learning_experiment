#import libraries and toolboxes
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
from numpy.random import random, randint, normal, shuffle, sample

# import random  
import random
from random import sample 

#!/usr/bin/env python
import csv

import os, os.path  # handy system and path functions
import sys  # to get file system encoding
import fnmatch #to grab the file we need


from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__))

#where output data is saved
_dataDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/data"
#where stimuli are read in from
_thisDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects"
#save psychopy data out to a seperate directory
os.chdir(_thisDir)

# Store info about the experiment session (saved in psychopy created file)
psychopyVersion = '3.2.4'
expName = 'Memory_Testing_'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

#creates data file
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _dataDir + os.sep + u'data_'+expInfo['participant']+'_'+expName+'_'+expInfo['date']+'/%s' %(expInfo['participant'])
filename = _dataDir + os.sep + u'Subject_'+expInfo['participant']+'/%s_%s_%s' % (expInfo['participant'], expInfo['date'], expName)
 
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=_dataDir,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
#logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation
#change to adjust sizes of grid and stims 
#if after first run grid size etc... seems off check the console log it should output the proper resolution
#change height and width to this resolution and try running again
#unit is pixels
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
    blendMode='avg', useRetina=True, useFBO=True, 
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

#Function Definitions 
#funciton that creates a grid on the screen 
def create_grid(list):
    lineXPos  = -(width/2)
    lineYPos = -(height/2)
                    
    #creates grid
    while lineXPos<(width/2):
        gridList.append(visual.Line(win, start=(lineXPos,(height/2)), end=(lineXPos, -(height/2)), lineColor='white', lineColorSpace='rgb'))
        lineXPos = lineXPos + (width/11)
                        
    while lineYPos<(height/2):
        gridList.append(visual.Line(win, start=((width/2),lineYPos), end=(-(width/2),lineYPos), lineColor='white', lineColorSpace='rgb'))
        lineYPos = lineYPos + (width/11)
                        
    for line in gridList:
        line.lineWidth = 10
        line.setAutoDraw(True)
 

#this function takes the file name you are looking for an number you want and if it finds it it returns the number of rows in the file       
def count_rows(looking_for,this):
    counter=0
    for file_name in os.listdir(_dataDir+"/Subject_"+expInfo['participant']):
         if fnmatch.fnmatch(file_name, '*'+looking_for+str(this)+'.csv'):
            with open(_dataDir+"/Subject_"+expInfo['participant']+"/"+file_name, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for lines in csv_reader:
                    counter += 1
    return counter
    
#this function takes the file name and number you are looking for and the rows and collums of a matrix makes the matrix, and fills it with imported data then returns it   
def import_data(looking_for,this,rows,cols): 
    looper=0
    row=0
    matrix = np.zeros( (rows, cols) )
    #find the appropriate data fileopen the data file and save the data to a new matrix
    for file_name in os.listdir(_dataDir+"/Subject_"+expInfo['participant']):
         if fnmatch.fnmatch(file_name, '*'+looking_for+str(this)+'.csv'):
            with open(_dataDir+"/Subject_"+expInfo['participant']+"/"+file_name, "r") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for lines in csv_reader:
                    while looper<cols:
                        matrix[row][looper]=float(lines[looper])
                        looper=looper+1
                    coord_x_list.append(float(lines[1]))
                    coord_y_list.append(float(lines[2]))
                    row=row+1
                    looper=0
    return matrix


#wait time variables 
nReps=1
#should be 2
wait_time1=2
#should be 3
wait_time2=3
#number of stimuli to be used per run of experiment 
rows=0
files=0
final_files=0 
num_files=0

final_files = len(fnmatch.filter(os.listdir(_dataDir+"/Subject_"+expInfo['participant']), '*final_test_*'))
    
if final_files>0:
    #change file name to last testing file of testing to criterion session.   
    files = len(fnmatch.filter(os.listdir(_dataDir+"/Subject_"+expInfo['participant']), '*testing_*'))
    #determine number of stims used in previous training to criterion or testing
    rows=count_rows('final_test_', final_files-1)
    nRound=final_files
else:
    #change file name to last testing file of testing to criterion session.   
    files = len(fnmatch.filter(os.listdir(_dataDir+"/Subject_"+expInfo['participant']), '*testing_*'))
    #determine number of stims used in previous training to criterion or testing
    rows=count_rows('testing_', files)
    nRound=0
    
coord_x_list=[]
coord_y_list=[]

#Create a new data matrix the same size as the past data matrix 
n_stims=rows

if final_files >0:
    cols=3+(files*3)+(final_files*(2*nReps))
    currentCol=cols
    data_matrix = import_data('final_test_', final_files-1, rows, cols) 
else:
    cols=3+(files*3)
    currentCol=cols
    data_matrix = import_data('testing_', files , rows, cols) 
    
#datafile.close()
#used to make sure coords are only generated on first run through
gridList = []

looper=0
#while looper<n_stims:
    #data_matrix[looper][0]=int(stim_list[looper])
    #data_matrix[looper][1]=int(coord_x_list[looper])
    #data_matrix[looper][2]=int(coord_y_list[looper])
    #looper=looper+1
#looper=0    

# set up handler to look after randomisation of conditions etc
#change nReps here to effect overall rounds of data testing
rounds = data.TrialHandler(nReps=nReps, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='rounds')
thisExp.addLoop(rounds)  # add the loop to the experiment
#create matrix to save data

thisRound = rounds.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisRound.rgb)
if thisRound != None:
    for paramName in thisRound:
        exec('{} = thisRound[paramName]'.format(paramName))
   

for thisRound in rounds:
    currentLoop = rounds
    #set flags to False 

    # abbreviate parameter names if possible (e.g. rgb = thisRound.rgb)
    if thisRound != None:
        for paramName in thisRound:
            exec('{} = thisRound[paramName]'.format(paramName))
    #use core.wait() to have more control over wait times
    #delay=30   
    stim_size=250
    letter_size=(height/40)
    
    
    # Initialize components for Routine "Test_Intro"
    Test_IntroClock = core.Clock()
    Training_instructions = visual.TextStim(win=win, name='Training_instructions',
        text='TEST BLOCK\n\n\n\nA object will be presented in the center of the screen on each trial.\n\nClick and drag the object, as accurately as possible, to its specific location on the grid.\n\nYou have the option of changing your initial position by clicking and dragging the object for a second time.\n\n\nPlease press the space bar to proceed.....\n',
        font='Arial',
        pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    Space_to_continue = keyboard.Keyboard()
    
    # Initialize components for Routine "Testing"
    TestingClock = core.Clock()
    Target = visual.ImageStim(
        win=win,
        name='Target', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=(stim_size, stim_size),
        color=[1,1,1], colorSpace='rgb', opacity=0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    Stimuli = visual.ImageStim(
        win=win,
        name='Stimuli', 
        image='sin', mask=None,
        ori=0, pos=[0,0], size=(stim_size, stim_size),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    
    #define mice objects for testing 
    Mouse4 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse4.mouseClock = core.Clock()
    
    Mouse1 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse1.mouseClock = core.Clock()
    
    Mouse2 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse2.mouseClock = core.Clock()
    
    #initialize variables for loops and array manipulation and keeping track of users incorrect inputs
    wrongCounter=0
    looper=0
    
    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
   
    #used as index for arrays and matrixes while keeping track of how many stimuli have been displayed for training and testing
    looper=0
    
    #generate random order for each run through of training 
    random.seed()
    order_list=random.sample(range(0, n_stims), n_stims)
    
    #resize matrix 
    new_col = data_matrix.sum(1)[...,None] 
    new_col.shape
    all_data = np.append(data_matrix, new_col, 1)
    all_data.shape
    data_matrix=all_data
    #resize matrix 
    new_col = data_matrix.sum(1)[...,None] 
    new_col.shape
    all_data = np.append(data_matrix, new_col, 1)
    all_data.shape
    data_matrix=all_data
    #resize matrix 
    #new_col = data_matrix.sum(1)[...,None] 
    #new_col.shape
    #all_data = np.append(data_matrix, new_col, 1)
    #all_data.shape
    #data_matrix=all_data
    
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
    testing = data.TrialHandler(nReps=n_stims, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='testing')
    thisExp.addLoop(testing)  # add the loop to the experiment
    thisTest = testing.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    #generate random order on each runthrough of testing
    random.seed()
    order_list=random.sample(range(0, n_stims), n_stims)
    #flag used later to end test
    nextFlag=True
    looper=0
    order_var=0
    
    for thisTest in testing:
        currentLoop = testing
        # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
        if thisTest != None:
            for paramName in thisTest:
                exec('{} = thisTest[paramName]'.format(paramName))
        # ------Prepare to start Routine "Testing"-------
        #update component parameters for each repeat
        #hide the mouse
        win.mouseVisible=0
        #Target.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects/1a.jpg')
        Stimuli.setPos((0,0))
        #Stimuli.setImage('/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects/1a.jpg')
        xCoord = []
        yCoord = []
        #stimPos = []
        #targetPos =[]
        order = []
        #delay=15
        doneFlag=0
        # setup some python lists for storing info about the Mouse
        Mouse4.x = []
        Mouse4.y = []
        Mouse4.leftButton = []
        Mouse4.midButton = []
        Mouse4.rightButton = []
        Mouse4.time = []
        Mouse4.clicked_name = []
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
        Stimuli.setImage(str(int(data_matrix[order_list[looper]][0]))+'a.jpg')
        xPos=0
        yPos=0
        Stimuli.setPos((xPos,yPos))
        core.wait(wait_time1)
        if looper<n_stims:
            Target.setPos((coord_x_list[order_list[looper]],coord_y_list[order_list[looper]]))
        mouse_has_been_pressed = False
        startMouse1=0
        Mouse4.setPos((0,0))
        
        # keep track of which components have finished
        TestingComponents = [Target, Stimuli, Mouse4, Mouse1, Mouse2]
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
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.setAutoDraw(True)
            if Target.status == STARTED:  # only update if drawing
                Target.setPos((coord_x_list[order_list[looper]],coord_y_list[order_list[looper]]), log=False)
            
            # *Stimuli* updates
            if Stimuli.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Stimuli.frameNStart = frameN  # exact frame index
                Stimuli.tStart = t  # local t and not account for scr refresh
                Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
                Stimuli.setAutoDraw(True)
            # *Mouse* updates
            if Mouse4.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                Mouse4.frameNStart = frameN  # exact frame index
                Mouse4.tStart = t  # local t and not account for scr refresh
                Mouse4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mouse4, 'tStartRefresh')  # time at next scr refresh
                Mouse4.status = STARTED
                Mouse4.mouseClock.reset()
                prevButtonState = Mouse4.getPressed()  # if button is down already this ISN'T a new click
            if Mouse4.status == STARTED:
                if bool(startMouse1==1):
                    # keep track of stop time/frame for later
                    Mouse4.tStop = t  # not accounting for scr refresh
                    Mouse4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Mouse4, 'tStopRefresh')  # time at next scr refresh
                    Mouse4.status = FINISHED
            if Mouse4.status == STARTED:  # only update if started and not finished!
                x, y = Mouse4.getPos()
                Mouse4.x.append(x)
                Mouse4.y.append(y)
                buttons = Mouse4.getPressed()
                Mouse4.leftButton.append(buttons[0])
                Mouse4.midButton.append(buttons[1])
                Mouse4.rightButton.append(buttons[2])
                Mouse4.time.append(Mouse4.mouseClock.getTime())
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
            #if Mouse2.status == NOT_STARTED and doneFlag==1:
                # keep track of start time/frame for later
                #Mouse2.frameNStart = frameN  # exact frame index
                #Mouse2.tStart = t  # local t and not account for scr refresh
                #Mouse2.tStartRefresh = tThisFlipGlobal  # on global time
                #win.timeOnFlip(Mouse2, 'tStartRefresh')  # time at next scr refresh
                #Mouse2.status = STARTED
                #Mouse2.mouseClock.reset()
                #prevButtonState = Mouse2.getPressed()  # if button is down already this ISN'T a new click
            #if Mouse2.status == STARTED:  # only update if started and not finished!
                #x, y = Mouse2.getPos()
                ##Mouse2.x.append(x)
                #Mouse2.y.append(y)
                #buttons = Mouse2.getPressed()
                #Mouse2.leftButton.append(buttons[0])
                #Mouse2.midButton.append(buttons[1])
                #Mouse2.rightButton.append(buttons[2])
                #Mouse2.time.append(Mouse2.mouseClock.getTime())
                #buttons = Mouse2.getPressed()
                #if buttons != prevButtonState:  # button state changed?
                    #prevButtonState = buttons
                    #if sum(buttons) > 0:  # state changed to a new click
                        # abort routine on response
                        #continueRoutine = False
            #after a short pause allow user to use mouse to change stim position
            #if delay > 0:
            #delay=delay-1
                #move mouse to center of the screen and reveal it
            #set mouse to center and have it appear 
                
            win.mouseVisible=1
                #check if mouse is pressed and move stim with mouse
            if Mouse4.isPressedIn(Stimuli, buttons=[0]) and startMouse1==0:
                Stimuli.pos = Mouse4.getPos()
                mouse_has_been_pressed = True
                    
            if not Mouse4.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True and startMouse1==0:
                mouse_has_been_pressed = False
                startMouse1=1
                    
            else:
                if Mouse1.isPressedIn(Stimuli, buttons=[0]):
                    Stimuli.pos = Mouse4.getPos()
                    mouse_has_been_pressed = True    
                        
                if not Mouse1.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True:
                    mouse_has_been_pressed = False
                    dist=[]
                    dist=np.linalg.norm(Stimuli.pos-Target.pos)
                    #add order and error to data matrix to be output 
                    data_matrix[order_list[looper]][currentCol]=order_var+1
                    data_matrix[order_list[looper]][currentCol+1]=dist  
                    #one the second run on check if error was <= 200, if user got location right twice in a row remove it from runs 
                    
                    if dist<=200:
                        doneFlag=1
                        win.mouseVisible=0
                        startMouse1=0
                        win.flip()
                        
                    else:
                        wrongCounter=wrongCounter+1
                        win.mouseVisible=0
                        doneFlag=1
                        startMouse1=0
                        win.flip()
        
        
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
           
            if doneFlag==1:
                core.wait(wait_time2)
                continueRoutine=False
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        # -------Ending Routine "Testing"-------
        for thisComponent in TestingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #store other data in psychopy "final" file
        testing.addData('xCoord', coord_x_list[order_list[looper]])
        testing.addData('yCoord', coord_y_list[order_list[looper]])
        testing.addData('Error', dist)
        testing.addData('Target.started', Target.tStartRefresh)
        testing.addData('Target.stopped', Target.tStopRefresh)
        testing.addData('Stimuli.started', Stimuli.tStartRefresh)
        testing.addData('Stimuli.stopped', Stimuli.tStopRefresh)
        # store data for testing (TrialHandler)
        testing.addData('Mouse.x', Mouse4.x)
        testing.addData('Mouse.y', Mouse4.y)
        testing.addData('Mouse.leftButton', Mouse4.leftButton)
        testing.addData('Mouse.midButton', Mouse4.midButton)
        testing.addData('Mouse.rightButton', Mouse4.rightButton)
        testing.addData('Mouse.time', Mouse4.time)
        testing.addData('Mouse.clicked_name', Mouse4.clicked_name)
        testing.addData('Mouse.started', Mouse4.tStart)
        testing.addData('Mouse.stopped', Mouse4.tStop)
        # store data for testing (TrialHandler)
        testing.addData('Mouse1.x', Mouse1.x)
        testing.addData('Mouse1.y', Mouse1.y)
        testing.addData('Mouse1.leftButton', Mouse1.leftButton)
        testing.addData('Mouse1.midButton', Mouse1.midButton)
        testing.addData('Mouse1.rightButton', Mouse1.rightButton)
        testing.addData('Mouse1.time', Mouse1.time)
        testing.addData('Mouse1.clicked_name', Mouse1.clicked_name)
        testing.addData('Mouse1.started', Mouse1.tStart)
        testing.addData('Mouse1.stopped', Mouse1.tStop)
        # store data for testing (TrialHandler)
        testing.addData('Mouse2.x', Mouse2.x)
        testing.addData('Mouse2.y', Mouse2.y)
        testing.addData('Mouse2.leftButton', Mouse2.leftButton)
        testing.addData('Mouse2.midButton', Mouse2.midButton)
        testing.addData('Mouse2.rightButton', Mouse2.rightButton)
        testing.addData('Mouse2.time', Mouse2.time)
        testing.addData('Mouse2.started', Mouse2.tStart)
        testing.addData('Mouse2.stopped', Mouse2.tStop)
        order_var=order_var+1
        
        if looper==n_stims-1:
            Stimuli.opacity = 0
            win.flip()
            core.wait(wait_time2)
             #display a final message
            completeText = visual.TextStim(win, text= 'Great job, you have completed the final memory test!!\n\n\nPlease alert the experimenter.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
            #textWrong = visual.TextStim(win, text='You performed well on '+str(int(100*((n_stims-wrongCounter)/n_stims)))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
            #textRight = visual.TextStim(win, text='Congrats, you performed well on '+str(int(100*((n_stims-wrongCounter)/n_stims)))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.', font='Arial',pos=(0, 0), height=letter_size, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
            for line in gridList:
                line.setAutoDraw(False)
            win.flip()
            #if wrongCounter>=2:
               # win.mouseVisible=0
                #textWrong.setAutoDraw(True)
               # win.flip()
               # core.wait(wait_time2)
           # else:
            win.mouseVisible=0
                #textRight.setAutoDraw(True)
            win.flip()
            completeText.setAutoDraw(True)
            win.flip()
            core.wait(wait_time2)
            #textRight.setAutoDraw(False)
            #textWrong.setAutoDraw(False)
        else:
            #make sure everything is off
            for line in gridList:
                line.setAutoDraw(False)

        # the Routine "Testing" was not non-slip safe, so reset the non-slip timer
        thisExp.nextEntry()
        routineTimer.reset()
        #if looper==n_stims-1:
        #    nextFlag=False
        #if nextFlag==True
        looper=looper+1
        
    #save matrix out
    #filename = _dataDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+'_testing_'+ str(nRound)
    #testing.saveAsWideText(filename, appendFile=False, fileCollisionMethod='rename')
    np.savetxt(filename+'final_test_'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
    #filename='pickle'
    #testing.saveAsPickle(filename)
    
    # completed 1 repeats of 'testing'
    #keep track of turrent collums to add more data next run in correct spot
    currentCol=currentCol+2
    #keep track of round for output file names 
    nRound = nRound+1       
    # completed 2 repeats of 'rounds'
        
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()
    thisExp.nextEntry()
    
#saves data out in "final" file
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'_final')
#thisExp.saveAsPickle(filename+'_final')
#logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()


