#import libraries and toolboxes
from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = ['PTB']
from psychopy import gui, visual, monitors, core, data, event, logging, clock, hardware
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
_dataDir = "Files/data" 
#where stimuli are read in from
_thisDir = "Files/stimuli/objects"
_textDir = "Files/text"
_scramDir = "Files/scramObj"

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
#logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame
final_files=0
nReps=1
#initialize variables 
stim_list=[]
error_list=[]
stim_choice=0
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
iti_timings = np.zeros((32,4))

# matrix that hold parameters for how experiment should run, first created and then shuffled to make pseudo random 
# col 1 - iti reps 5-8, col 2 - 0 word, 1 pseudo word, col 3 - 0 reexpose, 1 do nothing
# col 4- -1 do nothing, 0-7 stim to reexpose, col 5- 0 left arrow, 1 right arrow
#8 of each iti timing 
#within each 8 1/2 are word and 1/2 are pseudoword 
#first word and pseudo word of each 8 is a reexpose so 8 reexposed throughout 
x=0
looper=0
reexpo_choice = random.sample(range(0,8), 8)
while looper < 32:
    if looper < 8:
        iti_timings[looper][0]=5
        if looper < 4:
            iti_timings[looper][1]=0  
            if looper == 0: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
        else:
            iti_timings[looper][1]=1
            if looper == 4: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
    elif looper < 16:
        iti_timings[looper][0]=6
        if looper < 12:
            iti_timings[looper][1]=0  
            if looper == 8: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
        else:
            iti_timings[looper][1]=1
            if looper == 12: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
    elif looper < 24:
        iti_timings[looper][0]=7
        if looper < 20:
            iti_timings[looper][1]=0  
            if looper == 16: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
        else:
            iti_timings[looper][1]=1
            if looper == 20: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
    else:
        iti_timings[looper][0]=8
        if looper < 28:
            iti_timings[looper][1]=0  
            if looper == 24: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
        else:
            iti_timings[looper][1]=1
            if looper == 28: 
                iti_timings[looper][2]=0
                iti_timings[looper][3]=reexpo_choice[x]
                x=x+1
            else:
                iti_timings[looper][2]=1
                iti_timings[looper][3]=float('nan')
    looper=looper+1 

#create an array with three permutations of the thirds set up above
looper=0
curRow=0
order = np.zeros((96,4))

#add data to order array for each third
while looper <3:
    tmp = []
    tmp=np.random.permutation(iti_timings)
    for rows in tmp:
        order[curRow][0]=rows[0]
        order[curRow][1]=rows[1]
        order[curRow][2]=rows[2]
        order[curRow][3]=rows[3]
        curRow=curRow+1
    looper=looper+1
    
looper = 0
#assign arrow directions 
arrow_dir = []
#save the order array out (this shows, itis col 1, w or pword col 2, reexpose col 3 and what stim is reexposed col 4)
np.savetxt(filename+'_order_'+'.csv', order, delimiter=',',fmt='%.2f')

#use random sample of balanced array to assign 0 or 1 for each arrow assingment 
#make a list of lists
while looper < 96:
    arrow_choices = [0,0,0,0,1,1,1,1]
    arrow_dir.append(random.sample(arrow_choices,  int(order[looper][0])))
    looper=looper+1

looper=0
    
#save out each list to a line of a csv file
with open(filename+'_arrow_dir_'+'.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(arrow_dir)   

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

# Initialize components for Routine "break"
breakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
      text='Time for a break. ',
      font='Arial',
      pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
      color='white', colorSpace='rgb', opacity=1, 
      languageStyle='LTR',
      depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
      text='When you are ready to continue, please press the space bar.',
      font='Arial',
      pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
      color='white', colorSpace='rgb', opacity=1, 
      languageStyle='LTR',
      depth=-1.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
#np.savetxt(filename+'_testing_'+ str(nRound)+'.csv', data_matrix, delimiter=',',fmt='%.2f')
#data matrixes to save out
w, h = 3, 96;
w_or_p_save = [[0 for x in range(w)] for y in range(h)] 
iti_w_or_p_save = []
words = []
p_words = []
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
scramble_choice = random.sample(range(1,97), 96)
scramble.setImage(_scramDir+'/ScramObj'+str(scramble_choice[looper])+'.jpg')

#add word or pseudo word to appropriate lists 
while looper < 48:
    #strip quotes and extra characters
    #add to lists
    p_words.append(str(pword_list[plist_choice[looper]].strip("['']")))
    words.append(str(word_list[wlist_choice[looper]].strip("['']")))
    looper=looper+1
#reset looper and save out word and pword list files of those used 
np.savetxt(filename+'_pword_list'+'.csv', p_words, delimiter=' ',fmt='%s')
np.savetxt(filename+'_word_list_'+'.csv', words, delimiter=' ',fmt='%s')
current = 0
cur_Col=0
word_iterator = 0
pword_iterator = 0
looper=0

#stores all words to be used in the experiment in order in a new list 
used_words_list = []
while looper < 96: 
    if order[looper][1]==0:
        used_words_list.append(str(words[word_iterator]))
        w_or_p_save[looper][0]='w'
        word_iterator = word_iterator+1
    elif order[looper][1]==1:
        used_words_list.append(str(p_words[pword_iterator]))
        w_or_p_save[looper][0]='p'
        pword_iterator = pword_iterator+1
    looper=looper+1
looper=0

#save out used word list
np.savetxt(filename+'_used_word_list_'+'.csv', used_words_list, delimiter=' ',fmt='%s')

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

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "break"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    # keep track of which components have finished
    breakComponents = [text, text_2, key_resp]
    for thisComponent in breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "break_3"-------
    while continueRoutine and current ==31 or current == 63:
        # get current time
        t = breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_3"-------
    for thisComponent in breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('text.started', text.tStartRefresh)
    thisExp.addData('text.stopped', text.tStopRefresh)
    thisExp.addData('text_2.started', text_2.tStartRefresh)
    thisExp.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
    thisExp.addData('key_resp.started', key_resp.tStartRefresh)
    thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    # the Routine "break_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #while within one third display choose a timing from the matrix
    #if second collumn is 0 set to word, if seond collum is 1 set to pseudo word
    #uses a list to keep track if events have happened (balances displays of stims based upon word or pseudo word being displayed and the length of the reps)
    #displays the first time each of these things happens 
    reps = order[current][0]
    word_or_pseudo.setText(used_words_list[current])
    
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
        if looper==reps-1:
            routineTimer.add(2.05)
        else: 
            routineTimer.add(2.5)
        # update component parameters for each repeat
        w_or_p_iti.keys = []
        w_or_p_iti.rt = []
        tmp = []
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
        
        #set display flag to true when we should reexpose and set the stim to correct image
        if order[current][2]==0:
            display_flag=True 
            reexpo.setImage(_thisDir+'/'+str(int(use_list[int(order[current][3])]))+'a.jpg')
        
        #display the arrows based on order values in 5th collumn
        if arrow_dir[current][looper]==0:
            arrow = arrowL
            tmp.append('w')
        else:
            arrow = arrowR
            tmp.append('p')
        
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
            if reexpo.status == NOT_STARTED and tThisFlip >= 2-frameTolerance and display_flag == True and looper==reps-1:
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
                    
            # *reexpo* updates
            #only displays right before the next word or pseudoword is displayed, and if the display flag is set 
            if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arrow.frameNStart = frameN  # exact frame index
                arrow.tStart = t  # local t and not account for scr refresh
                arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
                arrow.setAutoDraw(True)
                
            if arrow.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > arrow.tStartRefresh + 2.000-frameTolerance:
                    arrow.setAutoDraw(False)
                elif tThisFlipGlobal > arrow.tStartRefresh + 2.5-frameTolerance:
                    # keep track of stop time/frame for later
                    arrow.tStop = t  # not accounting for scr refresh
                    arrow.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(arrow, 'tStopRefresh')  # time at next scr refresh
                
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
                    #continueRoutine = False
            
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
            tmp.append('None')
        else:
            tmp.append(w_or_p_iti.keys)
            
        trials_2.addData('w_or_p_iti.keys',w_or_p_iti.keys)
        
        
        if w_or_p_iti.keys != None:  # we had a response
            trials_2.addData('w_or_p_iti.rt', w_or_p_iti.rt)
            tmp.append(w_or_p_iti.rt)
        else: 
           tmp.append('None')
            
        trials_2.addData('reexpo.started', reexpo.tStartRefresh)
        trials_2.addData('reexpo.stopped', reexpo.tStopRefresh)
        trials_2.addData('w_or_p_iti.started', w_or_p_iti.tStartRefresh)
        trials_2.addData('w_or_p_iti.stopped', w_or_p_iti.tStopRefresh)
        thisExp.nextEntry()
       
        #when display flag is true, after reexposing stim set flag to false
        if display_flag==True and looper==reps-1:
            display_flag=False
        #append the list of responses and response times to the iti save list
        iti_w_or_p_save.append(tmp)     
        
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
    
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True 
    looper=0
    # completed 5-8 repeats of 'trials_2' 
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
                #continueRoutine = False
        
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
    trials.addData('w_or_p.keys',w_or_p.keys)
    w_or_p_save[current][1]=w_or_p.keys
    if w_or_p.keys != None:  # we had a response
        trials.addData('w_or_p.rt', w_or_p.rt)
        w_or_p_save[current][2]=w_or_p.rt
    else:
        w_or_p_save[current][2]=None
    trials.addData('w_or_p.started', w_or_p.tStartRefresh)
    trials.addData('w_or_p.stopped', w_or_p.tStopRefresh)
    thisExp.nextEntry()
# completed 96 repeats of 'trials'
    current=current+1

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
#save out the w or p responses for the trails
np.savetxt(filename+'_trial_responses_'+'.csv', w_or_p_save, delimiter=',',fmt='%s')
#save out the w or p responses for the iti
#save out each list to a line of a csv file
with open(filename+'_iti_responses_'+'.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(iti_w_or_p_save)   

thisExp.saveAsWideText(filename+'final')
#thisExp.saveAsPickle(filename+'final')
#logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()