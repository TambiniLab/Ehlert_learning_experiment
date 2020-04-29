#import libraries and toolboxes
from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, monitors, core, data, event, logging, clock, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# import random  
import random

#!/usr/bin/env python
import csv

import os, os.path  # handy system and path functions
import sys  # to get file system encoding
import fnmatch #to grab the file we need

from psychopy.hardware import keyboard

#where output data is saved
_dataDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/data"
#where stimuli are read in from
_thisDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/stimuli/objects"
_textDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/text"
_scramDir = "/Users/lehlert/Documents/PsychoPy/Tambini_2/Files/scramObj"
#save psychopy data out to a seperate directory
_psychPyData = "/Users/lehlert/Documents/PsychoPy/Tambini_2/data/psychoPyData"

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'LDT'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _dataDir + os.sep + u'Subject_'+ expInfo['participant']+'/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lehlert/Desktop/LDT.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
final_files=0
nReps=1
#initialize variables 
stim_list=[]
error_list=[]
current=0
#starts at false
display_flag=False

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
                    row=row+1
                    looper=0
    return matrix

final_files = len(fnmatch.filter(os.listdir(_dataDir+"/Subject_"+expInfo['participant']), '*final_test_*'))
rows=count_rows('final_test_',final_files-1)


#change file name to last testing file of testing to criterion session.   
files = len(fnmatch.filter(os.listdir(_dataDir+"/Subject_"+expInfo['participant']), '*testing_*'))

#import data from final test
cols=3+(files*3)+(final_files*(2*nReps))
currentCol=cols
data_matrix = import_data('final_test_', final_files-1, rows, cols) 

looper=0
#make lists of stims used and last testing error 
while looper < rows:
    stim_list.append(data_matrix[looper][0])
    error_list.append(data_matrix[looper][cols-1])
    looper=looper+1
looper = 0 

#choose 8 stims at random (for now later will calculate from errors) 
use_list = []
#randomly choose 
use_these = random.sample(range(0, rows-1), (int((rows-2)/2)))
 
#add the random 8 to a new list    
for num in use_these:
   use_list.append(stim_list[num])
   
   
#choose timings for each iti
iti_timings = np.zeros((32,2))
looper=0
while looper < 32:
    if looper < 8:
        iti_timings[looper][0]=5
        if looper < 4:
            iti_timings[looper][1]=0  
        else:
            iti_timings[looper][1]=1
    elif looper < 16:
        iti_timings[looper][0]=6
        if looper < 12:
            iti_timings[looper][1]=0  
        else:
            iti_timings[looper][1]=1
    elif looper < 24:
        iti_timings[looper][0]=7
        if looper < 20:
            iti_timings[looper][1]=0  
        else:
            iti_timings[looper][1]=1
    else:
        iti_timings[looper][0]=8
        if looper < 28:
            iti_timings[looper][1]=0  
        else:
            iti_timings[looper][1]=1
    looper=looper+1 

#create an array with three permutations of the thirds set up above
looper=0
curRow=0
order = np.zeros((96,2))

#add data to order array for each third
while looper <3:
    tmp = []
    tmp=np.random.permutation(iti_timings)
    for rows in tmp:
        order[curRow][0]=rows[0]
        order[curRow][1]=rows[1]
        curRow=curRow+1
    looper=looper+1

#save the order array out 
np.savetxt(filename+'_order_'+'.csv', order, delimiter=',',fmt='%.2f')

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
    size=m.getSizePix(), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor=m, color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
scramble = visual.ImageStim(
    win=win,
    name='scramble', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(350, 350),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
word_or_pseudo = visual.TextStim(win=win, name='word_or_pseudo',
    text='Word or Pseudo-word',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=350, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
w_or_p = keyboard.Keyboard()
# Initialize components for Routine "ITI"

# set arrows up 
arrowVerticesL =[ [200,-50], [200,50], [0,50], [0,100], [-200,0], [0,-100],  [0,-50] ]
arrowVerticesR =[ [-200,50], [-200,-50], [0,-50], [0,-100], [200,0], [0,100],  [0,50] ]

ITIClock = core.Clock()
w_or_p_iti = keyboard.Keyboard()

reexpo = visual.ImageStim(
                win=win,
                name='reexpose', 
                image='sin', mask=None,
                ori=0, pos=[0,0], size=(250, 250),
                color=[1,1,1], colorSpace='rgb', opacity=1,
                flipHoriz=False, flipVert=False,
                texRes=128, interpolate=True, depth=-5.0)

arrowL = visual.ShapeStim(win, 
                 lineColor='black',
                 lineWidth=2.0, #in pixels
                 fillColor='black', #beware, with convex shapes fill colors don't work
                 vertices=arrowVerticesL,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotation and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 autoLog=False)#this stim changes too much for autologging to be useful

arrowR = visual.ShapeStim(win, 
                 lineColor='black',
                 lineWidth=2.0, #in pixels
                 fillColor='black', #beware, with convex shapes fill colors don't work
                 vertices=arrowVerticesR,#choose something from the above or make your own
                 closeShape=True,#do you want the final vertex to complete a loop with 1st?
                 pos= [0,0], #the anchor (rotation and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 autoLog=False)#this stim changes too much for autologging to be useful

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#data matrixes to save out
w_or_p_save = []
iti_w_or_p_save = [[]]
words = []
p_words = []

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=96, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))
looper=0
ran_flag=False

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    w_or_p.keys = []
    w_or_p.rt = []
    # keep track of which components have finished
    trialComponents = [word_or_pseudo, w_or_p, scramble]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    word_list =[]
    pword_list =[]
    #find the word list file and import the words into a list
    
    with open(_textDir+"/"+"word_list.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
                word_list.append(str(lines))
                
    #find pword list text file and add it to a list 
    with open(_textDir+"/"+"pword_list.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
                pword_list.append(str(lines))       
    
    #mac a sample of integers to access the word list 
    random.seed()
    wlist_choice = random.sample(range(0, 99), 99)
    plist_choice = random.sample(range(0, 84), 84)
    
    #choose a scramble image to display
    scramble_choice = random.sample(range(0,96), 96)
    scramble.setImage(_scramDir+'/ScramObj'+str(scramble_choice[looper])+'.jpg')
    looper = 0 
    #add word or pseudo word to appropriate lists 
    while looper < 48:
        #strip quotes and extra characters
        #add to lists
        p_words.append(str(pword_list[plist_choice[looper]].strip("['']")))
        words.append(str(word_list[wlist_choice[looper]].strip("['']")))
        looper=looper+1
    
    
    #reset looper and save out word and pword list files of those used 
    looper=0
    np.savetxt(filename+'_pword_list'+'.csv', p_words, delimiter=' ',fmt='%s')
    np.savetxt(filename+'_word_list_'+'.csv', words, delimiter=' ',fmt='%s')
   
    #set the variables to 0 before first run only
    if ran_flag==False:
        current = 0
        cur_Col=0
        word_iterator = 0
        pword_iterator = 0
        ran_flag=True
        
    #while within one third display choose a timing from the matrix
    #if second collumn is 0 set to word, if seond collum is 1 set to pseudo word
    reps = order[current][0]
    if order[current][1]==0:
        word_or_pseudo.setText(str(words[word_iterator]))
        word_iterator = word_iterator+1
    elif order[current][1]==1:
        word_or_pseudo.setText(str(p_words[pword_iterator]))
        pword_iterator = pword_iterator+1
    
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #autodraw happens last always so draw the scramble making it behind the word
        scramble.draw(win)
        
        # *scramble* updates
        if scramble.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            scramble.frameNStart = frameN  # exact frame index
            scramble.tStart = t  # local t and not account for scr refresh
            scramble.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(scramble, 'tStartRefresh')  # time at next scr refresh
            #scramble.setAutoDraw(True)
            
        if scramble.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > scramble.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                scramble.tStop = t  # not accounting for scr refresh
                scramble.frameNStop = frameN  # exact frame index
                win.timeOnFlip(scramble, 'tStopRefresh')  # time at next scr refresh
                #scramble.setAutoDraw(False)
    
        # *word_or_pseudo* updates
        if word_or_pseudo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            word_or_pseudo.frameNStart = frameN  # exact frame index
            word_or_pseudo.tStart = t  # local t and not account for scr refresh
            word_or_pseudo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(word_or_pseudo, 'tStartRefresh')  # time at next scr refresh
            word_or_pseudo.setAutoDraw(True)
            
        if word_or_pseudo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > word_or_pseudo.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                word_or_pseudo.tStop = t  # not accounting for scr refresh
                word_or_pseudo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(word_or_pseudo, 'tStopRefresh')  # time at next scr refresh
                word_or_pseudo.setAutoDraw(False)
                
        # *w_or_p* updates
        waitOnFlip = False
        if w_or_p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            w_or_p.frameNStart = frameN  # exact frame index
            w_or_p.tStart = t  # local t and not account for scr refresh
            w_or_p.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(w_or_p, 'tStartRefresh')  # time at next scr refresh
            w_or_p.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(w_or_p.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(w_or_p.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if w_or_p.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > w_or_p.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                w_or_p.tStop = t  # not accounting for scr refresh
                w_or_p.frameNStop = frameN  # exact frame index
                win.timeOnFlip(w_or_p, 'tStopRefresh')  # time at next scr refresh
                w_or_p.status = FINISHED
        if w_or_p.status == STARTED and not waitOnFlip:
            theseKeys = w_or_p.getKeys(keyList=['w', 'p'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                w_or_p.keys = theseKeys.name  # just the last key pressed
                w_or_p.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
        #np.savetxt(filename+'_testing_'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
    
    # -------Ending Routine "trial"-------    
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('scramble.started', scramble.tStartRefresh)
    trials.addData('scramble.stopped', scramble.tStopRefresh)
    trials.addData('word_or_pseudo.started', word_or_pseudo.tStartRefresh)
    trials.addData('word_or_pseudo.stopped', word_or_pseudo.tStopRefresh)
    # check responses
    if w_or_p.keys in ['', [], None]:  # No response was made
        w_or_p.keys = None
        w_or_p_save.append('N')
    trials.addData('w_or_p.keys',w_or_p.keys)
    if w_or_p.keys != None:  # we had a response
        trials.addData('w_or_p.rt', w_or_p.rt)
        w_or_p_save(w_or_p.rt)
    trials.addData('w_or_p.started', w_or_p.tStartRefresh)
    trials.addData('w_or_p.stopped', w_or_p.tStopRefresh)
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=reps, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
       
   
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ITI"-------
        routineTimer.add(2.005)
        # update component parameters for each repeat
        w_or_p_iti.keys = []
        w_or_p_iti.rt = []
        # keep track of which components have finished
        ITIComponents = [reexpo, w_or_p_iti, arrowL, arrowR]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        #make a new order of stims everytime they are all gone through once
        if current == 0:
            reexpo_choice = random.sample(range(0,8), 8)
        
        reexpo.setImage(_thisDir+'/'+str(int(use_list[reexpo_choice[current]]))+'a.jpg')
        
        #create arrows left and right approximately 50% of the time each 
        random.seed()
        choice=randint(0,100) 
            
        if choice < 50:
            arrowL.setAutoDraw(True)
        
        else:
            arrowR.setAutoDraw(True)
        
        # -------Run Routine "ITI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *w_or_p_iti* updates
            waitOnFlip = False
            
            # *reexpo* updates
            #only displays right before the next word or pseudoword is displayed, and if the display flag is set 
            if reexpo.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                reexpo.frameNStart = frameN  # exact frame index
                reexpo.tStart = t  # local t and not account for scr refresh
                reexpo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(reexpo, 'tStartRefresh')  # time at next scr refresh
                reexpo.setAutoDraw(True)
                
            if reexpo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > reexpo.tStartRefresh + 2.005-frameTolerance:
                    # keep track of stop time/frame for later
                    reexpo.tStop = t  # not accounting for scr refresh
                    reexpo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(reexpo, 'tStopRefresh')  # time at next scr refresh
                    reexpo.setAutoDraw(False)
                
            if w_or_p_iti.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                w_or_p_iti.frameNStart = frameN  # exact frame index
                w_or_p_iti.tStart = t  # local t and not account for scr refresh
                w_or_p_iti.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(w_or_p_iti, 'tStartRefresh')  # time at next scr refresh
                w_or_p_iti.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(w_or_p_iti.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(w_or_p_iti.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if w_or_p_iti.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > w_or_p_iti.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    w_or_p_iti.tStop = t  # not accounting for scr refresh
                    w_or_p_iti.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(w_or_p_iti, 'tStopRefresh')  # time at next scr refresh
                    w_or_p_iti.status = FINISHED
            if w_or_p_iti.status == STARTED and not waitOnFlip:
                theseKeys = w_or_p_iti.getKeys(keyList=['w', 'p'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    w_or_p_iti.keys = theseKeys.name  # just the last key pressed
                    w_or_p_iti.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        arrowL.setAutoDraw(False)
        arrowR.setAutoDraw(False)   
        looper=looper+1
        
        # check responses
        if w_or_p_iti.keys in ['', [], None]:  # No response was made
            w_or_p_iti.keys = None
        trials_2.addData('w_or_p_iti.keys',w_or_p_iti.keys)
        if w_or_p_iti.keys != None:  # we had a response
            trials_2.addData('w_or_p_iti.rt', w_or_p_iti.rt)
            
        trials_2.addData('reexpo.started', reexpo.tStartRefresh)
        trials_2.addData('reexpo.stopped', reexpo.tStopRefresh)
        trials_2.addData('w_or_p_iti.started', w_or_p_iti.tStartRefresh)
        trials_2.addData('w_or_p_iti.stopped', w_or_p_iti.tStopRefresh)
        thisExp.nextEntry()
   
    #iterate the list of stims when display flag is false, if current is over 7 then reset back to 0 
    if display_flag==True:
        #iterate the list of orders
        current= current+1 
        #set flag to false and resent current if entire list has been iterated through
        display_flag=False
        if current > 7:
            current = 0
            
    # completed 5-8 repeats of 'trials_2' 
    #np.savetxt(filename+'_testing_'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
    thisExp.nextEntry()
    
    
# completed 96 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
#save out the w or p responses for the trails
np.savetxt(filename+'_trial_responses_'+'.csv', w_or_p_save, delimiter=',',fmt='%s')
#save out the w or p responses for the iti
np.savetxt(filename+'_iti_responses_'+'.csv', iti_w_or_p_save, delimiter=',',fmt='%s')

thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()