##import libraries and toolboxes
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

import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
#_thisDir = os.path.dirname(os.path.abspath(__file__))

#where output data is saved
_dataDir = "Files/data" 
#where stimuli are read in from
_thisDir = "Files/stimuli/objects"
os.chdir(_thisDir)

# Store info about the experiment session (saved in psychopy created file)
psychopyVersion = '3.2.4'
expName = 'Training_To_Criterion'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

#creates data file
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
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

#wait time variables 
#should be 2
wait_time1=2
#should be 3
wait_time2=3
#number of stimuli to be used per run of experiment 
n_stims=18

#create matrix three collumns, and one row per stimuli used
rows=n_stims
cols=3
currentCol=3
data_matrix = np.zeros( (rows, cols) )
#create lists to hold stim locations
coord_x_list = []
coord_y_list = []

#used to make sure coords are only generated on first run through
coordFlag=False

#list used for testing to criterion 
#0 = not met, 1 = met
criterion_list = [False]*n_stims

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

# set up handler to look after randomisation of conditions etc
#change nReps here to effect overall rounds of data testing
nRound=1
rounds = data.TrialHandler(nReps=9999, method='sequential', 
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
    #used to note when experiment criterion has been met
    completeFlag=False

    # abbreviate parameter names if possible (e.g. rgb = thisRound.rgb)
    if thisRound != None:
        for paramName in thisRound:
            exec('{} = thisRound[paramName]'.format(paramName))
    #use core.wait() to have more control over wait times
    #delay=30
            
    # Initialize components for Routine "Train_Intro"
    stim_size=250
    outline_size=(stim_size+4,stim_size+4)
    letter_size=(height/40)
    Train_IntroClock = core.Clock()
    
    #check if all criterion has been met and exit if so
    i=0
    while i < n_stims:
        if criterion_list[i]==True:
            completeFlag=True 
        else:
            completeFlag=False
            break
        i=i+1
        
    if completeFlag==True:
        #display a final message
        completeText = visual.TextStim(win, text= 'Great job, you have completed the final memory test!!\n\n\nPlease alert the experimenter.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
        completeText.setAutoDraw(True)
        win.flip()
        core.wait(wait_time2)
        #filename = _dataDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+'final'
        #thisExp.saveAsWideText(filename+'final')
        #thisExp.saveAsPickle(filename+'final')
        logging.flush()
        # make sure everything is closed down
        thisExp.abort()  # or data files will save again on exit
        win.close()
        core.quit()     
        
        #display a message after the first round finishes. 
    if nRound==2:
        endFirstRoundText = visual.TextStim(win, text = 'Great job, you have completed the memory test for the 1st Learning Block!\n\n\nThe test for the next block will begin in a moment.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
        endFirstRoundText.setAutoDraw(True)
        win.flip()
        core.wait(wait_time2)
        endFirstRoundText.setAutoDraw(False)
        win.flip()
    
    Training_instructions_2 = visual.TextStim(win=win, name='Training_instructions_2',
        text='LEARNING BLOCK\n\n\n\n\nYou will view a series of objects.\n\nEach object will move to a specific location on the grid. A red frame will appear when each object reaches its location.\n\nYour goal is to learn the specific location of each object on the grid.\n\nAfter the red frame turns black, you should click on the object to end the trial.\n\n\n\nPlease press the space bar to proceed.....\n',
        font='Arial',
        pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, 
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
        ori=0, pos=[0,0], size=(stim_size, stim_size),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    Mouse3 = event.Mouse(win=win)
    x, y = [None, None]
    Mouse3.mouseClock = core.Clock()
    
    # Initialize components for Routine "Test_Intro"
    Test_IntroClock = core.Clock()
    Training_instructions = visual.TextStim(win=win, name='Training_instructions',
        text='TEST BLOCK\n\n\n\nA object will be presented in the center of the screen on each trial.\n\nClick and drag the object, as accurately as possible, to its specific location on the grid.\n\nYou have the option of changing your initial position by clicking and dragging the object for a second time.\n\nWhen you have selected the final location, a blue frame will appear around the object.\n\nA red frame will then appear around the true location of the object.\n\nIf your selection was approximately correct, the blue frame will turn green.\n\nIf your selection was not accurate, a line will be drawn between your location and the true location.\n\nPlease use this information to learn about the correct location for future trials.\n\n\nPlease press the space bar to proceed.....\n',
        font='Arial',
        pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, 
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
    thisExp.addData('Training_instructions_2.started', Training_instructions_2.tStartRefresh)
    thisExp.addData('Training_instructions_2.stopped', Training_instructions_2.tStopRefresh)
    # check responses
    if Space_to_continue_2.keys in ['', [], None]:  # No response was made
        Space_to_continue_2.keys = None
    thisExp.addData('Space_to_continue_2.keys',Space_to_continue_2.keys)
    if Space_to_continue_2.keys != None:  # we had a response
        thisExp.addData('Space_to_continue_2.rt', Space_to_continue_2.rt)
    thisExp.addData('Space_to_continue_2.started', Space_to_continue_2.tStartRefresh)
    thisExp.addData('Space_to_continue_2.stopped', Space_to_continue_2.tStopRefresh)
    thisExp.nextEntry()
    #returns mouse at the end of the routine
    win.mouseVisible = 1
    # the Routine "Train_Intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    training = data.TrialHandler(nReps=n_stims, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='training')
    thisExp.addLoop(rounds)  # add the loop to the experiment
    thisTrial = training.trialList[0]  # so we can initialize stimuli with some values
   
    #used as index for arrays and matrixes while keeping track of how many stimuli have been displayed for training and testing
    looper=0
    
    #generate random order for each run through of training 
    random.seed()
    order_list=random.sample(range(0, n_stims), n_stims)
    
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
       
    #set up initial matrix during first round only
    if coordFlag == False:
        looper=0
        
        #create a list of random numbers between 1- #number of stims to use to generate the stim images for the experiment
        randStim=random.sample(range(1, 266), n_stims)
        
        #on first run creates random locations for stims divided into four quadrants of the screen 
        #make n_stim divisable by 4
        
        rmaindr=n_stims%4
        tmp_stim=n_stims-rmaindr
        tmp_stim=tmp_stim/4
        
        #1/4 in upper right quadrant 
        while looper < tmp_stim:
            random.seed()
            coord_x_list.append(randint((stim_size/2),((width/2)-stim_size)))
            data_matrix[looper][1]=coord_x_list[looper]
            #make stim a random integer between 1 and 266
            #use sample so no duplicates
            data_matrix[looper][0]=randStim[looper]
            random.seed()
            coord_y_list.append(randint((stim_size/2),((height/2)-stim_size)))
            data_matrix[looper][2]=coord_y_list[looper]
            looper=looper+1
        #1/4 in bottom right quadrant 
        while looper < tmp_stim*2:
            random.seed()
            coord_x_list.append(randint((stim_size/2),((width/2)-stim_size)))
            data_matrix[looper][1]=coord_x_list[looper]
            #make stim a random integer between 1 and 266
            #use sample so no duplicates
            data_matrix[looper][0]=randStim[looper]
            random.seed()
            coord_y_list.append(randint((-(height/2)+stim_size),(-stim_size/2)))
            data_matrix[looper][2]=coord_y_list[looper]
            looper=looper+1
        #1/4 in upper left quadrant     
        while looper < tmp_stim*3:
            random.seed()
            coord_x_list.append(randint((-(width/2)+stim_size),(-stim_size/2)))
            data_matrix[looper][1]=coord_x_list[looper]
            #make stim a random integer between 1 and 266
            #use sample so no duplicates
            data_matrix[looper][0]=randStim[looper]
            random.seed()
            coord_y_list.append(randint((stim_size/2),((height/2)-stim_size)))
            data_matrix[looper][2]=coord_y_list[looper]
            looper=looper+1
        #1/4 in bottom left quadrant 
        while looper < tmp_stim*4:
            random.seed()
            coord_x_list.append(randint((-(width/2)+stim_size),(-stim_size/2)))
            data_matrix[looper][1]=coord_x_list[looper]
            #make stim a random integer between 1 and 266
            #use sample so no duplicates
            data_matrix[looper][0]=randStim[looper]
            random.seed()
            coord_y_list.append(randint((-(height/2)+stim_size),(-stim_size/2)))
            data_matrix[looper][2]=coord_y_list[looper]
            looper=looper+1
        #the remainder randomly distributed 
        while looper < n_stims:
            random.seed()
            coord_x_list.append(randint((-(width/2)+stim_size),((width/2)-stim_size)))
            #make sure random generated location is more then 1/2 stim size pixels from the center
            if coord_x_list[looper]<stim_size/2 and coord_x_list[looper]>=0:
                coord_x_list[looper]=stim_size/2
            if coord_x_list[looper]>(-stim_size/2) and coord_x_list[looper]<=0:
                coord_x_list[looper]=(-stim_size/2)
            data_matrix[looper][1]=coord_x_list[looper]
            #make stim a random integer between 1 and 266
            #use sample so no duplicates
            data_matrix[looper][0]=randStim[looper]
            random.seed()
            coord_y_list.append(randint((-(height/2)+stim_size),((height/2)-stim_size)))
            if coord_x_list[looper]<100 and coord_x_list[looper]>=0:
                coord_x_list[looper]=100
            if coord_x_list[looper]>-100 and coord_x_list[looper]<=0:
                coord_x_list[looper]=-100
            data_matrix[looper][2]=coord_y_list[looper]
            looper=looper+1
        coordFlag = True
    
    looper=0
    order_var=0
    
    #resize matrix adding one collumn 
    new_col = data_matrix.sum(1)[...,None] 
    new_col.shape
    all_data = np.append(data_matrix, new_col, 1)
    all_data.shape
    data_matrix=all_data
    
    for thisTrial in training:
        currentLoop = training
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
      
        if criterion_list[order_list[looper]]==True:
            data_matrix[order_list[looper]][currentCol]=float('nan')
            continueRoutine = False
        else:
            # ------Prepare to start Routine "Training"-------
            #adding data to psychopy file
            training.addData('xCoord', coord_x_list[looper])
            training.addData('yCoord', coord_y_list[looper])
            #set ran flag
            ranFlag=False
            #function that creates grid over screen based upon resolution input
            gridList = [] 
            
            data_matrix[order_list[looper]][currentCol]=order_var+1
            
            #hide the mouse from the user
            win.mouseVisible = 0
            
            #using the fuction to create the grid
            create_grid(gridList)
            
            #creates a two second delay between trials 
            if looper >=1:
                Outline_black_2.opacity = 0
                Stimuli_2.setAutoDraw(False)
                win.flip()
                core.wait(wait_time2)
                
            #set the stim image from the directroy each loop
            Stimuli_2.setImage(str(int(data_matrix[order_list[looper]][0]))+'a.jpg')
        
            #make the mouse invisible
            
            xFlag=0
            yFlag=0
            finalFlag=0
            #set starting position for Stim image (so it starts in the center)
            xPos=0
            yPos=0
            Stimuli_2.setPos((xPos,yPos))
            Stimuli_2.setAutoDraw(True)
            win.flip()
            core.wait(wait_time2)
            #set the movement rates for the Stimuli image
            #rate comes from the excel sheet, this he number of frames it takes for the image to reach its final destination
            xMov=(coord_x_list[order_list[looper]]/expInfo['frameRate'])
            yMov=(coord_y_list[order_list[looper]]/expInfo['frameRate'])
            
            # setup some python lists for storing info about the mouse
            Mouse3.clicked_name = []
            gotValidClick = False  # until a click is received
            # keep track of which components have finished
            TrainingComponents = [Outline_red_2, Outline_black_2, Stimuli_2, Mouse3]
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
                
             # *mouse* updates
            if Mouse3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Mouse3.frameNStart = frameN  # exact frame index
                Mouse3.tStart = t  # local t and not account for scr refresh
                Mouse3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Mouse3, 'tStartRefresh')  # time at next scr refresh
                Mouse3.status = STARTED
                Mouse3.mouseClock.reset()
                prevButtonState = Mouse3.getPressed()  # if button is down already this ISN'T a new click
            if Mouse3.status == STARTED:  # only update if started and not finished!
                buttons = Mouse3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [Stimuli_2]:
                            if obj.contains(Mouse3):
                                gotValidClick = True
                                Mouse3.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
                
            #delays the start of the movement of the images by delay frames
            #if delay >0:
                #delay=delay-1
            #after delay starts here
            #else:              
            #check if xCoord is positive or negative the flags are 1 if positive else remain 0
            if coord_x_list[order_list[looper]]>0:
                xFlag=1 
            #checks if yCoord is positive or negative (see above for flag function)
            if coord_y_list[order_list[looper]]>0:
                yFlag=1
                #while the image hasn't reached it's final coordinates keep animating it
            if finalFlag==0:
                #if final x destination is positive keep moving x while it is less then the final coordinate
                if xFlag==1: 
                    if xPos<coord_x_list[order_list[looper]]:
                        xPos=xPos+xMov
                #otherwise keep moving x while it is greater then the final  =x coordinate
                else:
                    if xPos>coord_x_list[order_list[looper]]:
                        xPos=xPos+xMov
                #do the same as above but for y 
                if yFlag==1:
                    if yPos<coord_y_list[order_list[looper]]:
                        yPos=yPos+yMov
                else:
                    if yPos>coord_y_list[order_list[looper]]:
                            yPos=yPos+yMov
                    #after changing current x and y coordinates reset the position 
                Stimuli_2.setPos((xPos,yPos))
                    #check if the final flag should be set AKA both x and y have reached the final coordinate 
                if xFlag==1 and yFlag==1:
                    if xPos>=coord_x_list[order_list[looper]] and yPos>=coord_y_list[order_list[looper]]:
                        if xPos!=coord_x_list[order_list[looper]]:
                            xPos=coord_x_list[order_list[looper]]
                        if yPos!=coord_y_list[order_list[looper]]:
                            yPos=coord_y_list[order_list[looper]]
                        Stimuli_2.setPos((xPos,yPos))
                        finalFlag=1
                elif xFlag==1 and yFlag==0:
                    if xPos>=coord_x_list[order_list[looper]] and yPos<=coord_y_list[order_list[looper]]:
                        if xPos!=coord_x_list[order_list[looper]]:
                            xPos=coord_x_list[order_list[looper]]
                        if yPos!=coord_y_list[order_list[looper]]:
                            yPos=coord_y_list[order_list[looper]]
                        Stimuli_2.setPos((xPos,yPos))
                        finalFlag=1
                elif xFlag==0 and yFlag==1:
                    if xPos<=coord_x_list[order_list[looper]] and yPos>=coord_y_list[order_list[looper]]:
                        if xPos!=coord_x_list[order_list[looper]]:
                            xPos=coord_x_list[order_list[looper]]
                        if yPos!=coord_y_list[order_list[looper]]:
                            yPos=coord_y_list[order_list[looper]]
                        Stimuli_2.setPos((xPos,yPos))
                        finalFlag=1
                elif xFlag==0 and yFlag==0:
                    if xPos<=coord_x_list[order_list[looper]] and yPos<=coord_y_list[order_list[looper]]:
                        if xPos!=coord_x_list[order_list[looper]]:
                            xPos=coord_x_list[order_list[looper]]
                        if yPos!=coord_y_list[order_list[looper]]:
                            yPos=coord_y_list[order_list[looper]]
                        Stimuli_2.setPos((xPos,yPos))
                        finalFlag=1
            #once the final flag is set begin the termination of the routine 
            if finalFlag==1:
                    #move the outlines to the final position and then use opacity to turn them on and off 
                    #red outline 2 seconds
                    Outline_red_2.setPos((coord_x_list[order_list[looper]],coord_y_list[order_list[looper]]))
                    Outline_red_2.opacity = 1
                    win.flip()
                    if ranFlag==False:
                        core.wait(wait_time1)
                    
                    #black outline on and allow user to click
                    Outline_black_2.setPos((coord_x_list[order_list[looper]],coord_y_list[order_list[looper]]))
                    Outline_black_2.opacity = 1
                    Outline_red_2.opacity = 0
                    if ranFlag==False:
                        Mouse3.setPos((coord_x_list[order_list[looper]],coord_y_list[order_list[looper]]))
                        win.winHandle.Mouse3_x = x  # hack to change pyglet window
                        win.winHandle.Mouse3_y = y
                    win.mouseVisible = 1
                    ranFlag=True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                win.close()
                core.quit()
                
            #skips the training 
            if defaultKeyboard.getKeys(keyList=["s"]):
                training.finished = True
                continueRoutine = False
            
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
                
        if criterion_list[order_list[looper]]==False:
            training.addData('Outline_red_2.started', Outline_red_2.tStartRefresh)
            training.addData('Outline_red_2.stopped', Outline_red_2.tStopRefresh)
            training.addData('Outline_black_2.started', Outline_black_2.tStartRefresh)
            training.addData('Outline_black_2.stopped', Outline_black_2.tStopRefresh)
            training.addData('Stimuli_2.started', Stimuli_2.tStartRefresh)
            training.addData('Stimuli_2.stopped', Stimuli_2.tStopRefresh)
            training.addData('mouse.x', x)
            training.addData('mouse.y', y)
            training.addData('mouse.leftButton', buttons[0])
            training.addData('mouse.midButton', buttons[1])
            training.addData('mouse.rightButton', buttons[2])
            # store data for training (TrialHandler)
            x, y = Mouse3.getPos()
            buttons = Mouse3.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [Stimuli_2]:
                    if obj.contains(Mouse3):
                        gotValidClick = True
                        Mouse3.clicked_name.append(obj.name)
            
            if len(Mouse3.clicked_name):
                thisExp.addData('mouse.clicked_name', Mouse3.clicked_name[0])
            training.addData('mouse.started', Mouse3.tStart)
            training.addData('mouse.stopped', Mouse3.tStop)
            # the Routine "Training" was not non-slip safe, so reset the non-slip timer
            order_var=order_var+1
            
        #make sure the outlines are invisible again before next loop
        looper=looper+1
        routineTimer.reset()
        Outline_red_2.opacity = 0
        Outline_black_2.opacity = 0
        
        #removing the grid
        for line in gridList:
            line.setAutoDraw(False)
        
    #save training data
    thisExp.nextEntry()
    #filename = _dataDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+ '_training'+ str(nRound)
    np.savetxt(filename+ '_training'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
    #training.saveAsWideText(filename, appendFile=True, fileCollisionMethod='rename')
    #filename='pickle'
    #training.saveAsPickle(filename)
    
    # completed 1 repeats of 'training'
    currentCol=currentCol+1
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
    thisExp.addLoop(rounds)  # add the loop to the experiment
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
        #if criterion has been met for this stim skip test
        if criterion_list[order_list[looper]]==True:
            data_matrix[order_list[looper]][currentCol]=float('nan')
            data_matrix[order_list[looper]][currentCol+1]=float('nan')
            continueRoutine = False
        else:
            #update component parameters for each repeat
            #hide the mouse
            win.mouseVisible=0
            Stimuli.setPos((0,0))
            xCoord = []
            yCoord = []
            order = []
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
            TestingComponents = [Outline_red, Outline_black, Outline_green, Outline_blue, Target, Stimuli, Mouse4, Mouse1, Mouse2]
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
                
            win.mouseVisible=1
                #check if mouse is pressed and move stim with mouse
            if Mouse4.isPressedIn(Stimuli, buttons=[0]) and startMouse1==0:
                Stimuli.pos = Mouse4.getPos()
                Outline_blue.pos = Mouse4.getPos()
                mouse_has_been_pressed = True
                    
            if not Mouse4.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True and startMouse1==0:
                mouse_has_been_pressed = False
                startMouse1=1
                    
            else:
                if Mouse1.isPressedIn(Stimuli, buttons=[0]):
                    Stimuli.pos = Mouse4.getPos()
                    Outline_blue.pos = Mouse4.getPos()
                    mouse_has_been_pressed = True    
                        
                if not Mouse1.isPressedIn(Stimuli, buttons=[0]) and mouse_has_been_pressed == True:
                    mouse_has_been_pressed = False
                    Outline_blue.opacity = 1
                    dist=[]
                    dist=np.linalg.norm(Stimuli.pos-Target.pos)
                    #add order and error to data matrix to be output 
                    data_matrix[order_list[looper]][currentCol]=order_var+1
                    data_matrix[order_list[looper]][currentCol+1]=dist  
                     #one the second run on check if error was <= 200, if user got location right twice in a row remove it from runs 
                    if nRound >=2 and data_matrix[order_list[looper]][currentCol+1]<=200 and data_matrix[order_list[looper]][currentCol-2]<=200:
                        criterion_list[order_list[looper]]=True
                        order_var=order_var+1
                        
                    testing.addData('stimPos', Stimuli.pos)
                    testing.addData('targetPos', Target.pos)
                    #just for checking error is being logged correctly 
                    #data_matrix[order_list[looper]][currentCol+2]=Target.pos  
                    
                    if dist<=200:
                        Outline_green.pos = Stimuli.pos
                        Outline_green.opacity = 1
                        Stimuli.pos=Target.pos
                        Outline_blue.pos = Target.pos
                        doneFlag=1
                        win.mouseVisible=0
                        startMouse1=0
                        win.flip()
                        
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
        if criterion_list[order_list[looper]]==False:
            #store other data in psychopy "final" file
            testing.addData('xCoord', coord_x_list[order_list[looper]])
            testing.addData('yCoord', coord_y_list[order_list[looper]])
            testing.addData('Error', dist)
            testing.addData('Outline_red.started', Outline_red.tStartRefresh)
            testing.addData('Outline_red.stopped', Outline_red.tStopRefresh)
            testing.addData('Outline_black.started', Outline_black.tStartRefresh)
            testing.addData('Outline_black.stopped', Outline_black.tStopRefresh)
            testing.addData('Outline_green.started', Outline_green.tStartRefresh)
            testing.addData('Outline_green.stopped', Outline_green.tStopRefresh)
            testing.addData('Outline_blue.started', Outline_blue.tStartRefresh)
            testing.addData('Outline_blue.stopped', Outline_blue.tStopRefresh)
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
            Outline_red.opacity = 0
            Outline_blue.opacity = 0
            Outline_green.opacity = 0
            myLine.setAutoDraw(False)
            win.flip()
            core.wait(wait_time2)
            textWrong = visual.TextStim(win, text='You performed well on '+str(int(100*((n_stims-wrongCounter)/n_stims)))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.',font='Arial',pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
            textRight = visual.TextStim(win, text='Congrats, you performed well on '+str(int(100*((n_stims-wrongCounter)/n_stims)))+'% of trials.\n\n\nPlease continue to pay attention to the location\nof each object during the next learning block.', font='Arial',pos=(0, 0), height=letter_size, wrapWidth=width, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=0.0)
            for line in gridList:
                line.setAutoDraw(False)
            win.flip()
            if wrongCounter>=2:
                win.mouseVisible=0
                textWrong.setAutoDraw(True)
                win.flip()
                core.wait(wait_time2)
            else:
                win.mouseVisible=0
                textRight.setAutoDraw(True)
                win.flip()
                core.wait(wait_time2)
            textRight.setAutoDraw(False)
            textWrong.setAutoDraw(False)
        else:
            #make sure everything is off
            Outline_red.opacity = 0
            Outline_blue.opacity = 0
            Outline_green.opacity = 0
            myLine.setAutoDraw(False)
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
    #filename = _dataDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    #testing.saveAsWideText(filename, appendFile=False, fileCollisionMethod='rename')
    np.savetxt(filename+'_testing_'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
    #filename='pickle'
    #testing.saveAsPickle(filename)
    
    # completed 1 repeats of 'testing'
    #keep track of turrent collums to add more data next run in correct spot
    currentCol=currentCol+2
    #currentCol=currentCol+3
    #keep track of round for output file names 
    nRound = nRound+1       
    # completed 2 repeats of 'rounds'
        
    # Flip one final time so any remaining win.callOnFlip() 
    # and win.timeOnFlip() tasks get executed before quitting
    win.flip()
    thisExp.nextEntry()
    
#saves data out in "final" file
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'final')
#thisExp.saveAsPickle(filename+'final')
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()


