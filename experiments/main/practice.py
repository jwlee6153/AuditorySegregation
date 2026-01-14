#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on 9월 26, 2024, at 13:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
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

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'consonanceEXP_random'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'gender': '',
    'age': '',
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
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\user\\Desktop\\audi\\consonanEXP_pra_lastrun.py',
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
            size=[1920, 1080], fullscr=True, screen=0,
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
    win.mouseVisible = False
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
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
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
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
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
    
    # --- Initialize components for Routine "pra_ins" ---
    text_9 = visual.TextStim(win=win, name='text_9',
        text='    This is the practice session. \n\nIf a target (a repeating tone) is present, press <S>,\n \nIf no target is present, press <L>.\n\n          Please respond as accurately as possible. \n \n Press the spacebar to start.\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_7 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "blank_2" ---
    # Run 'Begin Experiment' code from code_7
    target_level=0.6
    
    
    text_10 = visual.TextStim(win=win, name='text_10',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    # Run 'Begin Experiment' code from code_4
    c_lower=["wav\E4.wav", "wav\G4.wav", "wav\C5.wav", "wav\E5.wav", "wav\G5.wav","wav\C6.wav"]
    c_upper=["wav\E6.wav", "wav\G6.wav", "wav\C7.wav", "wav\E7.wav", "wav\G7.wav"]
    d_lower=["wav\D4.wav", "wav\D5.wav","wav\D6.wav","wav\F4.wav", "wav\F5.wav", "wav\A4.wav","wav\A5.wav"]
    d_upper=["wav\D7.wav", "wav\F6.wav", "wav\F7.wav", "wav\A6.wav", "wav\A7.wav"]
    e_lower=["wav\E4.wav", "wav\E5.wav", "wav\G4.wav", "wav\G5.wav", "wav\B4.wav", "wav\B5.wav"]
    e_upper=["wav\E6.wav", "wav\E7.wav", "wav\G6.wav", "wav\G7.wav","wav\B6.wav"]
    f_lower=["wav\F4.wav", "wav\F5.wav", "wav\A4.wav", "wav\A5.wav", "wav\C5.wav", "wav\C6.wav"]
    f_upper=["wav\F6.wav", "wav\F7.wav", "wav\A6.wav", "wav\A7.wav", "wav\C7.wav"]
    g_lower=["wav\G4.wav", "wav\G5.wav", "wav\B4.wav", "wav\B5.wav", "wav\D4.wav", "wav\D5.wav", "wav\D6.wav"]
    g_upper=["wav\G6.wav", "wav\G7.wav","wav\B6.wav", "wav\D7.wav"]
    a_lower=["wav\A4.wav", "wav\A5.wav", "wav\C5.wav", "wav\C6.wav", "wav\E4.wav", "wav\E5.wav"]
    a_upper=["wav\A6.wav", "wav\A7.wav",  "wav\C7.wav", "wav\E6.wav", "wav\E7.wav"]
    b_lower=["wav\D4.wav", "wav\D5.wav", "wav\D6.wav", "wav\F4.wav", "wav\F5.wav", "wav\B4.wav", "wav\B5.wav"]
    b_upper=["wav\D7.wav", "wav\F6.wav","wav\F7.wav", "wav\B6.wav"]
    disone_lower=["wav\D4.wav","wav\E4.wav","wav\F#4.wav","wav\G#4.wav","wav\A#4.wav","wav\C5.wav", "wav\D5.wav","wav\E5.wav","wav\F#5.wav","wav\G#5.wav","wav\A#5.wav", "wav\C6.wav", "wav\D6.wav"]
    disone_upper=["wav\E6.wav","wav\F#6.wav","wav\G#6.wav","wav\A#6.wav", "wav\C7.wav", "wav\D7.wav","wav\E7.wav","wav\F#7.wav","wav\G#7.wav","wav\A#7.wav"]
    c_lower2=c_lower.copy()
    c_upper2=c_upper.copy()
    d_lower2=d_lower.copy()
    d_upper2=d_upper.copy()
    e_lower2=e_lower.copy()
    e_upper2=e_upper.copy()
    f_lower2=f_lower.copy()
    f_upper2=f_upper.copy()
    g_lower2=g_lower.copy()
    g_upper2=g_upper.copy()
    a_lower2=a_lower.copy()
    a_upper2=a_upper.copy()
    b_lower2=b_lower.copy()
    b_upper2=b_upper.copy()
    disone_lower2=disone_lower.copy()
    disone_upper2=disone_upper.copy()
    c_lower3=c_lower.copy()
    c_upper3=c_upper.copy()
    d_lower3=d_lower.copy()
    d_upper3=d_upper.copy()
    e_lower3=e_lower.copy()
    e_upper3=e_upper.copy()
    f_lower3=f_lower.copy()
    f_upper3=f_upper.copy()
    g_lower3=g_lower.copy()
    g_upper3=g_upper.copy()
    a_lower3=a_lower.copy()
    a_upper3=a_upper.copy()
    b_lower3=b_lower.copy()
    b_upper3=b_upper.copy()
    disone_lower3=disone_lower.copy()
    disone_upper3=disone_upper.copy()
    c_lower4=c_lower.copy()
    c_upper4=c_upper.copy()
    d_lower4=d_lower.copy()
    d_upper4=d_upper.copy()
    e_lower4=e_lower.copy()
    e_upper4=e_upper.copy()
    f_lower4=f_lower.copy()
    f_upper4=f_upper.copy()
    g_lower4=g_lower.copy()
    g_upper4=g_upper.copy()
    a_lower4=a_lower.copy()
    a_upper4=a_upper.copy()
    b_lower4=b_lower.copy()
    b_upper4=b_upper.copy()
    disone_lower4=disone_lower.copy()
    disone_upper4=disone_upper.copy()
    c_lower5=c_lower.copy()
    c_upper5=c_upper.copy()
    d_lower5=d_lower.copy()
    d_upper5=d_upper.copy()
    e_lower5=e_lower.copy()
    e_upper5=e_upper.copy()
    f_lower5=f_lower.copy()
    f_upper5=f_upper.copy()
    g_lower5=g_lower.copy()
    g_upper5=g_upper.copy()
    a_lower5=a_lower.copy()
    a_upper5=a_upper.copy()
    b_lower5=b_lower.copy()
    b_upper5=b_upper.copy()
    disone_lower5=disone_lower.copy()
    disone_upper5=disone_upper.copy()
    c_lower6=c_lower.copy()
    c_upper6=c_upper.copy()
    d_lower6=d_lower.copy()
    d_upper6=d_upper.copy()
    e_lower6=e_lower.copy()
    e_upper6=e_upper.copy()
    f_lower6=f_lower.copy()
    f_upper6=f_upper.copy()
    g_lower6=g_lower.copy()
    g_upper6=g_upper.copy()
    a_lower6=a_lower.copy()
    a_upper6=a_upper.copy()
    b_lower6=b_lower.copy()
    b_upper6=b_upper.copy()
    disone_lower6=disone_lower.copy()
    disone_upper6=disone_upper.copy()
    disone_lower7=disone_lower.copy()
    disone_upper7=disone_upper.copy()
    disone_lower8=disone_lower.copy()
    disone_upper8=disone_upper.copy()
    disone_lower9=disone_lower.copy()
    disone_upper9=disone_upper.copy()
    disone_lower10=disone_lower.copy()
    disone_upper10=disone_upper.copy()
    disone_lower11=disone_lower.copy()
    disone_upper11=disone_upper.copy()
    disone_lower12=disone_lower.copy()
    disone_upper12=disone_upper.copy()
    disone_lower13=disone_lower.copy()
    disone_upper13=disone_upper.copy()
    disone_lower14=disone_lower.copy()
    disone_upper14=disone_upper.copy()
    disone_lower15=disone_lower.copy()
    disone_upper15=disone_upper.copy()
    disone_lower16=disone_lower.copy()
    disone_upper16=disone_upper.copy()
    disone_lower17=disone_lower.copy()
    disone_upper17=disone_upper.copy()
    disone_lower18=disone_lower.copy()
    disone_upper18=disone_upper.copy()
    disone_lower19=disone_lower.copy()
    disone_upper19=disone_upper.copy()
    disone_lower20=disone_lower.copy()
    disone_upper20=disone_upper.copy()
    disone_lower21=disone_lower.copy()
    disone_upper21=disone_upper.copy()
    disone_lower22=disone_lower.copy()
    disone_upper22=disone_upper.copy()
    disone_lower23=disone_lower.copy()
    disone_upper23=disone_upper.copy()
    disone_lower24=disone_lower.copy()
    disone_upper24=disone_upper.copy()
    disone_lower25=disone_lower.copy()
    disone_upper25=disone_upper.copy()
    disone_lower26=disone_lower.copy()
    disone_upper26=disone_upper.copy()
    disone_lower27=disone_lower.copy()
    disone_upper27=disone_upper.copy()
    disone_lower28=disone_lower.copy()
    disone_upper28=disone_upper.copy()
    disone_lower29=disone_lower.copy()
    disone_upper29=disone_upper.copy()
    disone_lower30=disone_lower.copy()
    disone_upper30=disone_upper.copy()
    disone_lower31=disone_lower.copy()
    disone_upper31=disone_upper.copy()
    disone_lower32=disone_lower.copy()
    disone_upper32=disone_upper.copy()
    disone_lower33=disone_lower.copy()
    disone_upper33=disone_upper.copy()
    disone_lower34=disone_lower.copy()
    disone_upper34=disone_upper.copy()
    disone_lower35=disone_lower.copy()
    disone_upper35=disone_upper.copy()
    disone_lower36=disone_lower.copy()
    disone_upper36=disone_upper.copy()
    disone_lower37=disone_lower.copy()
    disone_upper37=disone_upper.copy()
    disone_lower38=disone_lower.copy()
    disone_upper38=disone_upper.copy()
    disone_lower39=disone_lower.copy()
    disone_upper39=disone_upper.copy()
    disone_lower40=disone_lower.copy()
    disone_upper40=disone_upper.copy()
    c=[c_lower,c_upper]
    d=[d_lower,d_upper]
    e=[e_lower,e_upper]
    f=[f_lower,f_upper]
    g=[g_lower,g_upper]
    a=[a_lower,a_upper]
    b=[b_lower,b_upper]
    c2=[c_lower2,c_upper2]
    d2=[d_lower2,d_upper2]
    e2=[e_lower2,e_upper2]
    f2=[f_lower2,f_upper2]
    g2=[g_lower2,g_upper2]
    a2=[a_lower2,a_upper2]
    b2=[b_lower2,b_upper2]
    c3=[c_lower3,c_upper3]
    d3=[d_lower3,d_upper3]
    e3=[e_lower3,e_upper3]
    f3=[f_lower3,f_upper3]
    g3=[g_lower3,g_upper3]
    a3=[a_lower3,a_upper3]
    b3=[b_lower3,b_upper3]
    c4=[c_lower4,c_upper4]
    d4=[d_lower4,d_upper4]
    e4=[e_lower4,e_upper4]
    f4=[f_lower4,f_upper4]
    g4=[g_lower4,g_upper4]
    a4=[a_lower4,a_upper4]
    b4=[b_lower4,b_upper4]
    c5=[c_lower5,c_upper5]
    d5=[d_lower5,d_upper5]
    e5=[e_lower5,e_upper5]
    f5=[f_lower5,f_upper5]
    g5=[g_lower5,g_upper5]
    a5=[a_lower5,a_upper5]
    b5=[b_lower5,b_upper5]
    c6=[c_lower6,c_upper6]
    d6=[d_lower6,d_upper6]
    e6=[e_lower6,e_upper6]
    f6=[f_lower6,f_upper6]
    g6=[g_lower6,g_upper6]
    a6=[a_lower6,a_upper6]
    b6=[b_lower6,b_upper6]
    disone=[disone_lower,disone_upper]
    disone2=[disone_lower2,disone_upper2]
    disone3=[disone_lower3,disone_upper3]
    disone4=[disone_lower4,disone_upper4]
    disone5=[disone_lower5,disone_upper5]
    disone6=[disone_lower6,disone_upper6]
    disone7=[disone_lower7,disone_upper7]
    disone8=[disone_lower8,disone_upper8]
    disone9=[disone_lower9,disone_upper9]
    disone10=[disone_lower10,disone_upper10]
    disone11=[disone_lower11,disone_upper11]
    disone12=[disone_lower12,disone_upper12]
    disone13=[disone_lower13,disone_upper13]
    disone14=[disone_lower14,disone_upper14]
    disone15=[disone_lower15,disone_upper15]
    disone16=[disone_lower16,disone_upper16]
    disone17=[disone_lower17,disone_upper17]
    disone18=[disone_lower18,disone_upper18]
    disone19=[disone_lower19,disone_upper19]
    disone20=[disone_lower20,disone_upper20]
    disone21=[disone_lower21,disone_upper21]
    disone22=[disone_lower22,disone_upper22]
    disone23=[disone_lower23,disone_upper23]
    disone24=[disone_lower24,disone_upper24]
    disone25=[disone_lower25,disone_upper25]
    disone26=[disone_lower26,disone_upper26]
    disone27=[disone_lower27,disone_upper27]
    disone28=[disone_lower28,disone_upper28]
    disone29=[disone_lower29,disone_upper29]
    disone30=[disone_lower30,disone_upper30]
    disone31=[disone_lower31,disone_upper31]
    disone32=[disone_lower32,disone_upper32]
    disone33=[disone_lower33,disone_upper33]
    disone34=[disone_lower34,disone_upper34]
    disone35=[disone_lower35,disone_upper35]
    disone36=[disone_lower36,disone_upper36]
    disone37=[disone_lower37,disone_upper37]
    disone38=[disone_lower38,disone_upper38]
    disone39=[disone_lower39,disone_upper39]
    disone40=[disone_lower40,disone_upper40]
    
    starttime=[0.56,0.62, 0.68, 0.74, 0.80, 0.86, 0.92, 0.98, 1.04, 1.1, 1.16, 1.22,1.28,1.34,1.4,1.46,1.52,1.58,1.64, 1.7, 1.76, 1.82, 1.88, 1.94, 2, 2.06, 2.12,2.18, 2.24,2.3,2.36,2.42,2.48,2.54,2.6,2.66,2.72,2.78,2.84]
    con_list=[c,d,e,f,g,a,b, c2,d2,e2,f2,g2,a2,b2,c3,d3,e3,f3,g3,a3,b3, c4,d4,e4,f4,g4,a4,b4, c5,d5,e5,f5,g5,a5,b5, c6,d6,e6,f6,g6,a6,b6]
    dis_list=[disone, disone2, disone3, disone4, disone5, disone6, disone7, disone8,disone9,disone10, disone11, disone12,disone13, disone14,disone15,disone16,disone17,disone18, disone19,disone20,disone21,disone22,disone23,disone24,disone25,disone26,disone27,disone28,disone29,disone30,disone31,disone32,disone33,disone34,disone35,disone36,disone37,disone38,disone39,disone40]
    condition_list=[con_list, dis_list]
    tar = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar')
    tar.setVolume(1.0)
    sound1 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1')
    sound1.setVolume(0.3)
    sound1_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_2')
    sound1_2.setVolume(0.3)
    sound1_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_3')
    sound1_3.setVolume(0.3)
    sound1_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_4')
    sound1_4.setVolume(0.3)
    sound1_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_5')
    sound1_5.setVolume(0.3)
    sound1_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_6')
    sound1_6.setVolume(0.3)
    sound1_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_7')
    sound1_7.setVolume(0.3)
    sound1_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound1_8')
    sound1_8.setVolume(0.3)
    sound2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2')
    sound2.setVolume(0.3)
    sound2_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_2')
    sound2_2.setVolume(0.3)
    sound2_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_3')
    sound2_3.setVolume(0.3)
    sound2_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_4')
    sound2_4.setVolume(0.3)
    sound2_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_5')
    sound2_5.setVolume(0.3)
    sound2_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_6')
    sound2_6.setVolume(0.3)
    sound2_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_7')
    sound2_7.setVolume(0.3)
    sound2_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound2_8')
    sound2_8.setVolume(0.3)
    sound3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3')
    sound3.setVolume(0.3)
    sound3_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_2')
    sound3_2.setVolume(0.3)
    sound3_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_3')
    sound3_3.setVolume(0.3)
    sound3_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_4')
    sound3_4.setVolume(0.3)
    sound3_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_5')
    sound3_5.setVolume(0.3)
    sound3_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_6')
    sound3_6.setVolume(0.3)
    sound3_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_7')
    sound3_7.setVolume(0.3)
    sound3_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound3_8')
    sound3_8.setVolume(0.3)
    sound4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4')
    sound4.setVolume(0.3)
    sound4_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_2')
    sound4_2.setVolume(0.3)
    sound4_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_3')
    sound4_3.setVolume(0.3)
    sound4_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_4')
    sound4_4.setVolume(0.3)
    sound4_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_5')
    sound4_5.setVolume(0.3)
    sound4_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_6')
    sound4_6.setVolume(0.3)
    sound4_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_7')
    sound4_7.setVolume(0.3)
    sound4_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound4_8')
    sound4_8.setVolume(0.3)
    sound5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5')
    sound5.setVolume(0.3)
    sound5_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_2')
    sound5_2.setVolume(0.3)
    sound5_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_3')
    sound5_3.setVolume(0.3)
    sound5_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_4')
    sound5_4.setVolume(0.3)
    sound5_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_5')
    sound5_5.setVolume(0.3)
    sound5_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_6')
    sound5_6.setVolume(0.3)
    sound5_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_7')
    sound5_7.setVolume(0.3)
    sound5_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound5_8')
    sound5_8.setVolume(0.3)
    sound6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6')
    sound6.setVolume(0.3)
    sound6_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_2')
    sound6_2.setVolume(0.3)
    sound6_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_3')
    sound6_3.setVolume(0.3)
    sound6_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_4')
    sound6_4.setVolume(0.3)
    sound6_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_5')
    sound6_5.setVolume(0.3)
    sound6_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_6')
    sound6_6.setVolume(0.3)
    sound6_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_7')
    sound6_7.setVolume(0.3)
    sound6_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound6_8')
    sound6_8.setVolume(0.3)
    sound7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7')
    sound7.setVolume(0.3)
    sound7_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_2')
    sound7_2.setVolume(0.3)
    sound7_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_3')
    sound7_3.setVolume(0.3)
    sound7_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_4')
    sound7_4.setVolume(0.3)
    sound7_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_5')
    sound7_5.setVolume(0.3)
    sound7_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_6')
    sound7_6.setVolume(0.3)
    sound7_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_7')
    sound7_7.setVolume(0.3)
    sound7_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound7_8')
    sound7_8.setVolume(0.3)
    sound8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8')
    sound8.setVolume(0.3)
    sound8_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_2')
    sound8_2.setVolume(0.3)
    sound8_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_3')
    sound8_3.setVolume(0.3)
    sound8_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_4')
    sound8_4.setVolume(0.3)
    sound8_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_5')
    sound8_5.setVolume(0.3)
    sound8_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_6')
    sound8_6.setVolume(0.3)
    sound8_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_7')
    sound8_7.setVolume(0.3)
    sound8_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound8_8')
    sound8_8.setVolume(0.3)
    sound9 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9')
    sound9.setVolume(0.3)
    sound9_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_2')
    sound9_2.setVolume(0.3)
    sound9_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_3')
    sound9_3.setVolume(0.3)
    sound9_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_4')
    sound9_4.setVolume(0.3)
    sound9_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_5')
    sound9_5.setVolume(0.3)
    sound9_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_6')
    sound9_6.setVolume(0.3)
    sound9_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_7')
    sound9_7.setVolume(0.3)
    sound9_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound9_8')
    sound9_8.setVolume(0.3)
    sound10 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10')
    sound10.setVolume(0.3)
    sound10_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_2')
    sound10_2.setVolume(0.3)
    sound10_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_3')
    sound10_3.setVolume(0.3)
    sound10_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_4')
    sound10_4.setVolume(0.3)
    sound10_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_5')
    sound10_5.setVolume(0.3)
    sound10_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_6')
    sound10_6.setVolume(0.3)
    sound10_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_7')
    sound10_7.setVolume(0.3)
    sound10_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound10_8')
    sound10_8.setVolume(0.3)
    sound11 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11')
    sound11.setVolume(0.3)
    sound11_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_2')
    sound11_2.setVolume(0.3)
    sound11_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_3')
    sound11_3.setVolume(0.3)
    sound11_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_4')
    sound11_4.setVolume(0.3)
    sound11_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_5')
    sound11_5.setVolume(0.3)
    sound11_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_6')
    sound11_6.setVolume(0.3)
    sound11_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_7')
    sound11_7.setVolume(0.3)
    sound11_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound11_8')
    sound11_8.setVolume(0.3)
    sound12 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12')
    sound12.setVolume(0.3)
    sound12_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_2')
    sound12_2.setVolume(0.3)
    sound12_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_3')
    sound12_3.setVolume(0.3)
    sound12_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_4')
    sound12_4.setVolume(0.3)
    sound12_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_5')
    sound12_5.setVolume(0.3)
    sound12_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_6')
    sound12_6.setVolume(0.3)
    sound12_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_7')
    sound12_7.setVolume(0.3)
    sound12_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound12_8')
    sound12_8.setVolume(0.3)
    sound13 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13')
    sound13.setVolume(0.3)
    sound13_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_2')
    sound13_2.setVolume(0.3)
    sound13_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_3')
    sound13_3.setVolume(0.3)
    sound13_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_4')
    sound13_4.setVolume(0.3)
    sound13_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_5')
    sound13_5.setVolume(0.3)
    sound13_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_6')
    sound13_6.setVolume(0.3)
    sound13_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_7')
    sound13_7.setVolume(0.3)
    sound13_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound13_8')
    sound13_8.setVolume(0.3)
    sound14 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14')
    sound14.setVolume(0.3)
    sound14_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_2')
    sound14_2.setVolume(0.3)
    sound14_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_3')
    sound14_3.setVolume(0.3)
    sound14_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_4')
    sound14_4.setVolume(0.3)
    sound14_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_5')
    sound14_5.setVolume(0.3)
    sound14_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_6')
    sound14_6.setVolume(0.3)
    sound14_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_7')
    sound14_7.setVolume(0.3)
    sound14_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound14_8')
    sound14_8.setVolume(0.3)
    sound15 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15')
    sound15.setVolume(0.3)
    sound15_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_2')
    sound15_2.setVolume(0.3)
    sound15_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_3')
    sound15_3.setVolume(0.3)
    sound15_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_4')
    sound15_4.setVolume(0.3)
    sound15_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_5')
    sound15_5.setVolume(0.3)
    sound15_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_6')
    sound15_6.setVolume(0.3)
    sound15_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_7')
    sound15_7.setVolume(0.3)
    sound15_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound15_8')
    sound15_8.setVolume(0.3)
    spund16 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16')
    spund16.setVolume(0.3)
    spund16_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_2')
    spund16_2.setVolume(0.3)
    spund16_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_3')
    spund16_3.setVolume(0.3)
    spund16_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_4')
    spund16_4.setVolume(0.3)
    spund16_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_5')
    spund16_5.setVolume(0.3)
    spund16_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_6')
    spund16_6.setVolume(0.3)
    spund16_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_7')
    spund16_7.setVolume(0.3)
    spund16_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='spund16_8')
    spund16_8.setVolume(0.3)
    sound17 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17')
    sound17.setVolume(0.3)
    sound17_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_2')
    sound17_2.setVolume(0.3)
    sound17_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_3')
    sound17_3.setVolume(0.3)
    sound17_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_4')
    sound17_4.setVolume(0.3)
    sound17_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_5')
    sound17_5.setVolume(0.3)
    sound17_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_6')
    sound17_6.setVolume(0.3)
    sound17_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_7')
    sound17_7.setVolume(0.3)
    sound17_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound17_8')
    sound17_8.setVolume(0.3)
    sound18 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18')
    sound18.setVolume(0.3)
    sound18_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_2')
    sound18_2.setVolume(0.3)
    sound18_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_3')
    sound18_3.setVolume(0.3)
    sound18_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_4')
    sound18_4.setVolume(0.3)
    sound18_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_5')
    sound18_5.setVolume(0.3)
    sound18_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_6')
    sound18_6.setVolume(0.3)
    sound18_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_7')
    sound18_7.setVolume(0.3)
    sound18_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound18_8')
    sound18_8.setVolume(0.3)
    sound19 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19')
    sound19.setVolume(0.3)
    sound19_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_2')
    sound19_2.setVolume(0.3)
    sound19_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_3')
    sound19_3.setVolume(0.3)
    sound19_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_4')
    sound19_4.setVolume(0.3)
    sound19_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_5')
    sound19_5.setVolume(0.3)
    sound19_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_6')
    sound19_6.setVolume(0.3)
    sound19_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_7')
    sound19_7.setVolume(0.3)
    sound19_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound19_8')
    sound19_8.setVolume(0.3)
    sound20 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20')
    sound20.setVolume(0.3)
    sound20_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_2')
    sound20_2.setVolume(0.3)
    sound20_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_3')
    sound20_3.setVolume(0.3)
    sound20_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_4')
    sound20_4.setVolume(0.3)
    sound20_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_5')
    sound20_5.setVolume(0.3)
    sound20_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_6')
    sound20_6.setVolume(0.3)
    sound20_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_7')
    sound20_7.setVolume(0.3)
    sound20_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound20_8')
    sound20_8.setVolume(0.3)
    sound21 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21')
    sound21.setVolume(0.3)
    sound21_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_2')
    sound21_2.setVolume(0.3)
    sound21_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_3')
    sound21_3.setVolume(0.3)
    sound21_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_4')
    sound21_4.setVolume(0.3)
    sound21_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_5')
    sound21_5.setVolume(0.3)
    sound21_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_6')
    sound21_6.setVolume(0.3)
    sound21_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_7')
    sound21_7.setVolume(0.3)
    sound21_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound21_8')
    sound21_8.setVolume(0.3)
    sound22 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22')
    sound22.setVolume(0.3)
    sound22_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_2')
    sound22_2.setVolume(0.3)
    sound22_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_3')
    sound22_3.setVolume(0.3)
    sound22_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_4')
    sound22_4.setVolume(0.3)
    sound22_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_5')
    sound22_5.setVolume(0.3)
    sound22_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_6')
    sound22_6.setVolume(0.3)
    sound22_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_7')
    sound22_7.setVolume(0.3)
    sound22_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound22_8')
    sound22_8.setVolume(0.3)
    sound23 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23')
    sound23.setVolume(0.3)
    sound23_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_2')
    sound23_2.setVolume(0.3)
    sound23_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_3')
    sound23_3.setVolume(0.3)
    sound23_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_4')
    sound23_4.setVolume(0.3)
    sound23_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_5')
    sound23_5.setVolume(0.3)
    sound23_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_6')
    sound23_6.setVolume(0.3)
    sound23_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_7')
    sound23_7.setVolume(0.3)
    sound23_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound23_8')
    sound23_8.setVolume(0.3)
    sound24 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24')
    sound24.setVolume(0.3)
    sound24_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_2')
    sound24_2.setVolume(0.3)
    sound24_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_3')
    sound24_3.setVolume(0.3)
    sound24_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_4')
    sound24_4.setVolume(0.3)
    sound24_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_5')
    sound24_5.setVolume(0.3)
    sound24_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_6')
    sound24_6.setVolume(0.3)
    sound24_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_7')
    sound24_7.setVolume(0.3)
    sound24_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound24_8')
    sound24_8.setVolume(0.3)
    sound25 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25')
    sound25.setVolume(0.3)
    sound25_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_2')
    sound25_2.setVolume(0.3)
    sound25_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_3')
    sound25_3.setVolume(0.3)
    sound25_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_4')
    sound25_4.setVolume(0.3)
    sound25_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_5')
    sound25_5.setVolume(0.3)
    sound25_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_6')
    sound25_6.setVolume(0.3)
    sound25_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_7')
    sound25_7.setVolume(0.3)
    sound25_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound25_8')
    sound25_8.setVolume(0.3)
    sound26 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26')
    sound26.setVolume(0.3)
    sound26_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_2')
    sound26_2.setVolume(0.3)
    sound26_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_3')
    sound26_3.setVolume(0.3)
    sound26_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_4')
    sound26_4.setVolume(0.3)
    sound26_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_5')
    sound26_5.setVolume(0.3)
    sound26_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_6')
    sound26_6.setVolume(0.3)
    sound26_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_7')
    sound26_7.setVolume(0.3)
    sound26_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound26_8')
    sound26_8.setVolume(0.3)
    sound27 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27')
    sound27.setVolume(0.3)
    sound27_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_2')
    sound27_2.setVolume(0.3)
    sound27_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_3')
    sound27_3.setVolume(0.3)
    sound27_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_4')
    sound27_4.setVolume(0.3)
    sound27_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_5')
    sound27_5.setVolume(0.3)
    sound27_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_6')
    sound27_6.setVolume(0.3)
    sound27_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_7')
    sound27_7.setVolume(0.3)
    sound27_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound27_8')
    sound27_8.setVolume(0.3)
    sound28 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28')
    sound28.setVolume(0.3)
    sound28_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_2')
    sound28_2.setVolume(0.3)
    sound28_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_3')
    sound28_3.setVolume(0.3)
    sound28_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_4')
    sound28_4.setVolume(0.3)
    sound28_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_5')
    sound28_5.setVolume(0.3)
    sound28_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_6')
    sound28_6.setVolume(0.3)
    sound28_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_7')
    sound28_7.setVolume(0.3)
    sound28_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound28_8')
    sound28_8.setVolume(0.3)
    sound29 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29')
    sound29.setVolume(0.3)
    sound29_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_2')
    sound29_2.setVolume(0.3)
    sound29_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_3')
    sound29_3.setVolume(0.3)
    sound29_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_4')
    sound29_4.setVolume(0.3)
    sound29_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_5')
    sound29_5.setVolume(0.3)
    sound29_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_6')
    sound29_6.setVolume(0.3)
    sound29_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_7')
    sound29_7.setVolume(0.3)
    sound29_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound29_8')
    sound29_8.setVolume(0.3)
    sound30 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30')
    sound30.setVolume(0.3)
    sound30_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_2')
    sound30_2.setVolume(0.3)
    sound30_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_3')
    sound30_3.setVolume(0.3)
    sound30_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_4')
    sound30_4.setVolume(0.3)
    sound30_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_5')
    sound30_5.setVolume(0.3)
    sound30_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_6')
    sound30_6.setVolume(0.3)
    sound30_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_7')
    sound30_7.setVolume(0.3)
    sound30_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound30_8')
    sound30_8.setVolume(0.3)
    sound31 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31')
    sound31.setVolume(0.3)
    sound31_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_2')
    sound31_2.setVolume(0.3)
    sound31_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_3')
    sound31_3.setVolume(0.3)
    sound31_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_4')
    sound31_4.setVolume(0.3)
    sound31_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_5')
    sound31_5.setVolume(0.3)
    sound31_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_6')
    sound31_6.setVolume(0.3)
    sound31_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_7')
    sound31_7.setVolume(0.3)
    sound31_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound31_8')
    sound31_8.setVolume(0.3)
    sound32 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32')
    sound32.setVolume(0.3)
    sound32_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_2')
    sound32_2.setVolume(0.3)
    sound32_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_3')
    sound32_3.setVolume(0.3)
    sound32_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_4')
    sound32_4.setVolume(0.3)
    sound32_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_5')
    sound32_5.setVolume(0.3)
    sound32_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_6')
    sound32_6.setVolume(0.3)
    sound32_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_7')
    sound32_7.setVolume(0.3)
    sound32_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound32_8')
    sound32_8.setVolume(0.3)
    sound33 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33')
    sound33.setVolume(0.3)
    sound33_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_2')
    sound33_2.setVolume(0.3)
    sound33_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_3')
    sound33_3.setVolume(0.3)
    sound33_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_4')
    sound33_4.setVolume(0.3)
    sound33_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_5')
    sound33_5.setVolume(0.3)
    sound33_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_6')
    sound33_6.setVolume(0.3)
    sound33_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_7')
    sound33_7.setVolume(0.3)
    sound33_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound33_8')
    sound33_8.setVolume(0.3)
    sound34 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34')
    sound34.setVolume(0.3)
    sound34_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_2')
    sound34_2.setVolume(0.3)
    sound34_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_3')
    sound34_3.setVolume(0.3)
    sound34_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_4')
    sound34_4.setVolume(0.3)
    sound34_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_5')
    sound34_5.setVolume(0.3)
    sound34_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_6')
    sound34_6.setVolume(0.3)
    sound34_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_7')
    sound34_7.setVolume(0.3)
    sound34_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound34_8')
    sound34_8.setVolume(0.3)
    sound35 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35')
    sound35.setVolume(0.3)
    sound35_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_2')
    sound35_2.setVolume(0.3)
    sound35_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_3')
    sound35_3.setVolume(0.3)
    sound35_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_4')
    sound35_4.setVolume(0.3)
    sound35_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_5')
    sound35_5.setVolume(0.3)
    sound35_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_6')
    sound35_6.setVolume(0.3)
    sound35_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_7')
    sound35_7.setVolume(0.3)
    sound35_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound35_8')
    sound35_8.setVolume(0.3)
    sound36 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36')
    sound36.setVolume(0.3)
    sound36_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_2')
    sound36_2.setVolume(0.3)
    sound36_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_3')
    sound36_3.setVolume(0.3)
    sound36_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_4')
    sound36_4.setVolume(0.3)
    sound36_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_5')
    sound36_5.setVolume(0.3)
    sound36_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_6')
    sound36_6.setVolume(0.3)
    sound36_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_7')
    sound36_7.setVolume(0.3)
    sound36_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound36_8')
    sound36_8.setVolume(0.3)
    sound37 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37')
    sound37.setVolume(0.3)
    sound37_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_2')
    sound37_2.setVolume(0.3)
    sound37_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_3')
    sound37_3.setVolume(0.3)
    sound37_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_4')
    sound37_4.setVolume(0.3)
    sound37_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_5')
    sound37_5.setVolume(0.3)
    sound37_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_6')
    sound37_6.setVolume(0.3)
    sound37_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_7')
    sound37_7.setVolume(0.3)
    sound37_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound37_8')
    sound37_8.setVolume(0.3)
    sound38 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38')
    sound38.setVolume(0.3)
    sound38_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_2')
    sound38_2.setVolume(0.3)
    sound38_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_3')
    sound38_3.setVolume(0.3)
    sound38_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_4')
    sound38_4.setVolume(0.3)
    sound38_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_5')
    sound38_5.setVolume(0.3)
    sound38_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_6')
    sound38_6.setVolume(0.3)
    sound38_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_7')
    sound38_7.setVolume(0.3)
    sound38_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound38_8')
    sound38_8.setVolume(0.3)
    sound39 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39')
    sound39.setVolume(0.3)
    sound39_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_2')
    sound39_2.setVolume(0.3)
    sound39_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_3')
    sound39_3.setVolume(0.3)
    sound39_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_4')
    sound39_4.setVolume(0.3)
    sound39_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_5')
    sound39_5.setVolume(0.3)
    sound39_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_6')
    sound39_6.setVolume(0.3)
    sound39_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_7')
    sound39_7.setVolume(0.3)
    sound39_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound39_8')
    sound39_8.setVolume(0.3)
    sound40 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40')
    sound40.setVolume(0.3)
    sound40_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_2')
    sound40_2.setVolume(0.3)
    sound40_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_3')
    sound40_3.setVolume(0.3)
    sound40_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_4')
    sound40_4.setVolume(0.3)
    sound40_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_5')
    sound40_5.setVolume(0.3)
    sound40_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_6')
    sound40_6.setVolume(0.3)
    sound40_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_7')
    sound40_7.setVolume(0.3)
    sound40_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='sound40_8')
    sound40_8.setVolume(0.3)
    key_resp_3 = keyboard.Keyboard()
    tar_2 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_2')
    tar_2.setVolume(1.0)
    tar_3 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_3')
    tar_3.setVolume(1.0)
    tar_4 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_4')
    tar_4.setVolume(1.0)
    tar_5 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_5')
    tar_5.setVolume(1.0)
    tar_6 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_6')
    tar_6.setVolume(1.0)
    tar_7 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_7')
    tar_7.setVolume(1.0)
    tar_8 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_8')
    tar_8.setVolume(1.0)
    tar_9 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_9')
    tar_9.setVolume(1.0)
    tar_10 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_10')
    tar_10.setVolume(1.0)
    tar_11 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_11')
    tar_11.setVolume(1.0)
    tar_12 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_12')
    tar_12.setVolume(1.0)
    tar_13 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_13')
    tar_13.setVolume(1.0)
    tar_14 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_14')
    tar_14.setVolume(1.0)
    tar_15 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_15')
    tar_15.setVolume(1.0)
    tar_16 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_16')
    tar_16.setVolume(1.0)
    tar_17 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_17')
    tar_17.setVolume(1.0)
    tar_18 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_18')
    tar_18.setVolume(1.0)
    tar_19 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_19')
    tar_19.setVolume(1.0)
    tar_20 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_20')
    tar_20.setVolume(1.0)
    tar_21 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_21')
    tar_21.setVolume(1.0)
    tar_22 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_22')
    tar_22.setVolume(1.0)
    tar_23 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_23')
    tar_23.setVolume(1.0)
    tar_24 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_24')
    tar_24.setVolume(1.0)
    tar_25 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_25')
    tar_25.setVolume(1.0)
    tar_26 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_26')
    tar_26.setVolume(1.0)
    tar_27 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_27')
    tar_27.setVolume(1.0)
    tar_28 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_28')
    tar_28.setVolume(1.0)
    tar_29 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_29')
    tar_29.setVolume(1.0)
    tar_30 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_30')
    tar_30.setVolume(1.0)
    tar_31 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_31')
    tar_31.setVolume(1.0)
    tar_32 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_32')
    tar_32.setVolume(1.0)
    tar_33 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_33')
    tar_33.setVolume(1.0)
    tar_34 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_34')
    tar_34.setVolume(1.0)
    tar_35 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_35')
    tar_35.setVolume(1.0)
    tar_36 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_36')
    tar_36.setVolume(1.0)
    tar_37 = sound.Sound('A', secs=0.06, stereo=True, hamming=True,
        name='tar_37')
    tar_37.setVolume(1.0)
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2', vertices='cross',units='deg', 
        size=(0.5, 0.5),
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=-359.0, interpolate=True)
    
    # --- Initialize components for Routine "pra_feed" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end" ---
    text_6 = visual.TextStim(win=win, name='text_6',
        text='The practice session is now complete.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
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
    
    # --- Prepare to start Routine "pra_ins" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('pra_ins.started', globalClock.getTime())
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    pra_insComponents = [text_9, key_resp_7]
    for thisComponent in pra_insComponents:
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
    
    # --- Run Routine "pra_ins" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        
        # if text_9 is starting this frame...
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_9.status = STARTED
            text_9.setAutoDraw(True)
        
        # if text_9 is active this frame...
        if text_9.status == STARTED:
            # update params
            pass
        
        # *key_resp_7* updates
        waitOnFlip = False
        
        # if key_resp_7 is starting this frame...
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                key_resp_7.duration = _key_resp_7_allKeys[-1].duration
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
        for thisComponent in pra_insComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pra_ins" ---
    for thisComponent in pra_insComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('pra_ins.stopped', globalClock.getTime())
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    thisExp.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        thisExp.addData('key_resp_7.rt', key_resp_7.rt)
        thisExp.addData('key_resp_7.duration', key_resp_7.duration)
    thisExp.nextEntry()
    # the Routine "pra_ins" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition_R.xlsx'),
        seed=None, name='trials_3')
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    
    for thisTrial_3 in trials_3:
        currentLoop = trials_3
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
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "blank_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('blank_2.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_7
        breaks=[48]
        if trials_3.thisN in breaks:
            trials_3.finished = True
        # keep track of which components have finished
        blank_2Components = [text_10]
        for thisComponent in blank_2Components:
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
        
        # --- Run Routine "blank_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            
            # if text_10 is starting this frame...
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_10.status = STARTED
                text_10.setAutoDraw(True)
            
            # if text_10 is active this frame...
            if text_10.status == STARTED:
                # update params
                pass
            
            # if text_10 is stopping this frame...
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    # update status
                    text_10.status = FINISHED
                    text_10.setAutoDraw(False)
            
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
            for thisComponent in blank_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank_2" ---
        for thisComponent in blank_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('blank_2.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_4
        import random
        random.shuffle(c_lower)
        random.shuffle(d_lower)
        random.shuffle(e_lower)
        random.shuffle(f_lower)
        random.shuffle(g_lower)
        random.shuffle(a_lower)
        random.shuffle(c_upper)
        random.shuffle(d_upper)
        random.shuffle(e_upper)
        random.shuffle(f_upper)
        random.shuffle(g_upper)
        random.shuffle(a_upper)
        random.shuffle(b_lower)
        random.shuffle(b_upper)
        random.shuffle(disone_lower)
        random.shuffle(disone_upper)
        random.shuffle(c_lower2)
        random.shuffle(d_lower2)
        random.shuffle(e_lower2)
        random.shuffle(f_lower2)
        random.shuffle(g_lower2)
        random.shuffle(a_lower2)
        random.shuffle(c_upper2)
        random.shuffle(d_upper2)
        random.shuffle(e_upper2)
        random.shuffle(f_upper2)
        random.shuffle(g_upper2)
        random.shuffle(a_upper2)
        random.shuffle(b_lower2)
        random.shuffle(b_upper2)
        random.shuffle(disone_lower2)
        random.shuffle(disone_upper2)
        random.shuffle(c_lower3)
        random.shuffle(d_lower3)
        random.shuffle(e_lower3)
        random.shuffle(f_lower3)
        random.shuffle(g_lower3)
        random.shuffle(a_lower3)
        random.shuffle(c_upper3)
        random.shuffle(d_upper3)
        random.shuffle(e_upper3)
        random.shuffle(f_upper3)
        random.shuffle(g_upper3)
        random.shuffle(a_upper3)
        random.shuffle(b_lower3)
        random.shuffle(b_upper3)
        random.shuffle(disone_lower3)
        random.shuffle(disone_upper3)
        random.shuffle(c_lower4)
        random.shuffle(d_lower4)
        random.shuffle(e_lower4)
        random.shuffle(f_lower4)
        random.shuffle(g_lower4)
        random.shuffle(a_lower4)
        random.shuffle(c_upper4)
        random.shuffle(d_upper4)
        random.shuffle(e_upper4)
        random.shuffle(f_upper4)
        random.shuffle(g_upper4)
        random.shuffle(a_upper4)
        random.shuffle(b_lower4)
        random.shuffle(b_upper4)
        random.shuffle(disone_lower4)
        random.shuffle(disone_upper4)
        random.shuffle(c_lower5)
        random.shuffle(d_lower5)
        random.shuffle(e_lower5)
        random.shuffle(f_lower5)
        random.shuffle(g_lower5)
        random.shuffle(a_lower5)
        random.shuffle(c_upper5)
        random.shuffle(d_upper5)
        random.shuffle(e_upper5)
        random.shuffle(f_upper5)
        random.shuffle(g_upper5)
        random.shuffle(a_upper5)
        random.shuffle(b_lower5)
        random.shuffle(b_upper5)
        random.shuffle(disone_lower5)
        random.shuffle(disone_upper5)
        random.shuffle(c_lower6)
        random.shuffle(d_lower6)
        random.shuffle(e_lower6)
        random.shuffle(f_lower6)
        random.shuffle(g_lower6)
        random.shuffle(a_lower6)
        random.shuffle(c_upper6)
        random.shuffle(d_upper6)
        random.shuffle(e_upper6)
        random.shuffle(f_upper6)
        random.shuffle(g_upper6)
        random.shuffle(a_upper6)
        random.shuffle(b_lower6)
        random.shuffle(b_upper6)
        random.shuffle(disone_lower6)
        random.shuffle(disone_upper6)
        random.shuffle(disone_lower7)
        random.shuffle(disone_upper7)
        random.shuffle(disone_lower8)
        random.shuffle(disone_upper8)
        random.shuffle(disone_lower9)
        random.shuffle(disone_upper9)
        random.shuffle(disone_lower10)
        random.shuffle(disone_upper10)
        random.shuffle(disone_lower11)
        random.shuffle(disone_upper11)
        random.shuffle(disone_lower12)
        random.shuffle(disone_upper12)
        random.shuffle(disone_lower13)
        random.shuffle(disone_upper13)
        random.shuffle(disone_lower14)
        random.shuffle(disone_upper14)
        random.shuffle(disone_lower15)
        random.shuffle(disone_upper15)
        random.shuffle(disone_lower16)
        random.shuffle(disone_upper16)
        random.shuffle(disone_lower17)
        random.shuffle(disone_upper17)
        random.shuffle(disone_lower18)
        random.shuffle(disone_upper18)
        random.shuffle(disone_lower19)
        random.shuffle(disone_upper19)
        random.shuffle(disone_lower20)
        random.shuffle(disone_upper20)
        random.shuffle(disone_lower21)
        random.shuffle(disone_upper21)
        random.shuffle(disone_lower22)
        random.shuffle(disone_upper22)
        random.shuffle(disone_lower23)
        random.shuffle(disone_upper23)
        random.shuffle(disone_lower24)
        random.shuffle(disone_upper24)
        random.shuffle(disone_lower26)
        random.shuffle(disone_upper26)
        random.shuffle(disone_lower25)
        random.shuffle(disone_upper25)
        random.shuffle(disone_lower27)
        random.shuffle(disone_upper27)
        random.shuffle(disone_lower28)
        random.shuffle(disone_upper28)
        random.shuffle(disone_lower29)
        random.shuffle(disone_upper29)
        random.shuffle(disone_lower30)
        random.shuffle(disone_upper30)
        random.shuffle(disone_lower31)
        random.shuffle(disone_upper31)
        random.shuffle(disone_lower32)
        random.shuffle(disone_upper32)
        random.shuffle(disone_lower33)
        random.shuffle(disone_upper33)
        random.shuffle(disone_lower34)
        random.shuffle(disone_upper34)
        random.shuffle(disone_lower35)
        random.shuffle(disone_upper35)
        random.shuffle(disone_lower36)
        random.shuffle(disone_upper36)
        random.shuffle(disone_lower37)
        random.shuffle(disone_upper37)
        random.shuffle(disone_lower38)
        random.shuffle(disone_upper38)
        random.shuffle(disone_lower39)
        random.shuffle(disone_upper39)
        random.shuffle(disone_lower40)
        random.shuffle(disone_upper40)
        random.shuffle(con_list)
        random.shuffle(dis_list)
        random.shuffle(condition_list)
        random.shuffle(starttime)
        
        if figure==0:
            tarvolume=0
        elif figure==1:
            tarvolume=target_level
        thisExp.addData("tarvolume", tarvolume)
        if target== "wav\C7.wav":
            c_upper.remove("wav\C7.wav")
            f_upper.remove("wav\C7.wav")
            a_upper.remove("wav\C7.wav")
            disone_upper.remove("wav\C7.wav")
            c_upper2.remove("wav\C7.wav")
            f_upper2.remove("wav\C7.wav")
            a_upper2.remove("wav\C7.wav")
            disone_upper2.remove("wav\C7.wav")
            c_upper3.remove("wav\C7.wav")
            f_upper3.remove("wav\C7.wav")
            a_upper3.remove("wav\C7.wav")
            disone_upper3.remove("wav\C7.wav")
            c_upper4.remove("wav\C7.wav")
            f_upper4.remove("wav\C7.wav")
            a_upper4.remove("wav\C7.wav")
            disone_upper4.remove("wav\C7.wav")
            c_upper5.remove("wav\C7.wav")
            f_upper5.remove("wav\C7.wav")
            a_upper5.remove("wav\C7.wav")
            disone_upper5.remove("wav\C7.wav")
            c_upper6.remove("wav\C7.wav")
            f_upper6.remove("wav\C7.wav")
            a_upper6.remove("wav\C7.wav")
            disone_upper6.remove("wav\C7.wav")
            disone_upper7.remove("wav\C7.wav")
            disone_upper8.remove("wav\C7.wav")
            disone_upper9.remove("wav\C7.wav")
            disone_upper10.remove("wav\C7.wav")
            disone_upper11.remove("wav\C7.wav")
            disone_upper12.remove("wav\C7.wav")
            disone_upper13.remove("wav\C7.wav")
            disone_upper14.remove("wav\C7.wav")
            disone_upper15.remove("wav\C7.wav")
            disone_upper16.remove("wav\C7.wav")
            disone_upper17.remove("wav\C7.wav")
            disone_upper18.remove("wav\C7.wav")
            disone_upper19.remove("wav\C7.wav")
            disone_upper20.remove("wav\C7.wav")  
            disone_upper21.remove("wav\C7.wav")
            disone_upper22.remove("wav\C7.wav")
            disone_upper23.remove("wav\C7.wav")
            disone_upper24.remove("wav\C7.wav")
            disone_upper25.remove("wav\C7.wav")
            disone_upper26.remove("wav\C7.wav")
            disone_upper27.remove("wav\C7.wav")
            disone_upper28.remove("wav\C7.wav")
            disone_upper29.remove("wav\C7.wav")
            disone_upper30.remove("wav\C7.wav")
            disone_upper31.remove("wav\C7.wav")
            disone_upper32.remove("wav\C7.wav")
            disone_upper33.remove("wav\C7.wav")
            disone_upper34.remove("wav\C7.wav")
            disone_upper35.remove("wav\C7.wav")
            disone_upper36.remove("wav\C7.wav")
            disone_upper37.remove("wav\C7.wav")
            disone_upper38.remove("wav\C7.wav")
            disone_upper39.remove("wav\C7.wav")
            disone_upper40.remove("wav\C7.wav")
        elif target== "wav\D7.wav":
            g_upper.remove("wav\D7.wav")
            g_upper.append(g_lower[0])
            g_lower.remove(g_lower[0])
            b_upper.remove("wav\D7.wav")
            b_upper.append(b_lower[0])
            b_lower.remove(b_lower[0])
            disone_upper.remove("wav\D7.wav")
            g_upper2.remove("wav\D7.wav")
            g_upper2.append(g_lower2[0])
            g_lower2.remove(g_lower2[0])
            b_upper2.remove("wav\D7.wav")
            b_upper2.append(b_lower2[0])
            b_lower2.remove(b_lower2[0])
            disone_upper2.remove("wav\D7.wav")
            g_upper3.remove("wav\D7.wav")
            g_upper3.append(g_lower3[0])
            g_lower3.remove(g_lower3[0])
            b_upper3.remove("wav\D7.wav")
            b_upper3.append(b_lower3[0])
            b_lower3.remove(b_lower3[0])
            disone_upper3.remove("wav\D7.wav")
            g_upper4.remove("wav\D7.wav")
            g_upper4.append(g_lower4[0])
            g_lower4.remove(g_lower4[0])
            b_upper4.remove("wav\D7.wav")
            b_upper4.append(b_lower4[0])
            b_lower4.remove(b_lower4[0])
            disone_upper4.remove("wav\D7.wav")
            g_upper5.remove("wav\D7.wav")
            g_upper5.append(g_lower5[0])
            g_lower5.remove(g_lower5[0])
            b_upper5.remove("wav\D7.wav")
            b_upper5.append(b_lower5[0])
            b_lower5.remove(b_lower5[0])
            disone_upper5.remove("wav\D7.wav")
            g_upper6.remove("wav\D7.wav")
            g_upper6.append(g_lower6[0])
            g_lower6.remove(g_lower6[0])
            b_upper6.remove("wav\D7.wav")
            b_upper6.append(b_lower6[0])
            b_lower6.remove(b_lower6[0])
            disone_upper6.remove("wav\D7.wav")
            disone_upper7.remove("wav\D7.wav")
            disone_upper8.remove("wav\D7.wav")
            disone_upper9.remove("wav\D7.wav")
            disone_upper10.remove("wav\D7.wav")
            disone_upper11.remove("wav\D7.wav")
            disone_upper12.remove("wav\D7.wav")
            disone_upper13.remove("wav\D7.wav")
            disone_upper14.remove("wav\D7.wav")
            disone_upper15.remove("wav\D7.wav")
            disone_upper16.remove("wav\D7.wav")
            disone_upper17.remove("wav\D7.wav")
            disone_upper18.remove("wav\D7.wav")
            disone_upper19.remove("wav\D7.wav")
            disone_upper20.remove("wav\D7.wav")
            disone_upper21.remove("wav\D7.wav")
            disone_upper22.remove("wav\D7.wav")
            disone_upper23.remove("wav\D7.wav")
            disone_upper24.remove("wav\D7.wav")
            disone_upper25.remove("wav\D7.wav")
            disone_upper26.remove("wav\D7.wav")
            disone_upper27.remove("wav\D7.wav")
            disone_upper28.remove("wav\D7.wav")
            disone_upper29.remove("wav\D7.wav")
            disone_upper30.remove("wav\D7.wav")
            disone_upper31.remove("wav\D7.wav")
            disone_upper32.remove("wav\D7.wav")
            disone_upper33.remove("wav\D7.wav")
            disone_upper34.remove("wav\D7.wav")
            disone_upper35.remove("wav\D7.wav")
            disone_upper36.remove("wav\D7.wav")
            disone_upper37.remove("wav\D7.wav")
            disone_upper38.remove("wav\D7.wav")
            disone_upper39.remove("wav\D7.wav")
            disone_upper40.remove("wav\D7.wav")
            d_upper.remove("wav\D7.wav")
            d_upper2.remove("wav\D7.wav")
            d_upper3.remove("wav\D7.wav")
            d_upper4.remove("wav\D7.wav")
            d_upper5.remove("wav\D7.wav")
            d_upper6.remove("wav\D7.wav")
        
        if background=='con':
            condition_list[0] = con_list 
        elif background=='dis':
            condition_list[0] = dis_list 
          
        chord_list=[]
        
        tar.setSound(target, secs=0.06, hamming=True)
        tar.setVolume(tarvolume, log=False)
        tar.seek(0)
        sound1.setSound(condition_list[0][0][0][0], secs=0.06, hamming=True)
        sound1.setVolume(0.3, log=False)
        sound1.seek(0)
        sound1_2.setSound(condition_list[0][0][0][1], secs=0.06, hamming=True)
        sound1_2.setVolume(0.3, log=False)
        sound1_2.seek(0)
        sound1_3.setSound(condition_list[0][0][0][2], secs=0.06, hamming=True)
        sound1_3.setVolume(0.3, log=False)
        sound1_3.seek(0)
        sound1_4.setSound(condition_list[0][0][0][3], secs=0.06, hamming=True)
        sound1_4.setVolume(0.3, log=False)
        sound1_4.seek(0)
        sound1_5.setSound(condition_list[0][0][1][0], secs=0.06, hamming=True)
        sound1_5.setVolume(0.3, log=False)
        sound1_5.seek(0)
        sound1_6.setSound(condition_list[0][0][1][1], secs=0.06, hamming=True)
        sound1_6.setVolume(0.3, log=False)
        sound1_6.seek(0)
        sound1_7.setSound(condition_list[0][0][1][2], secs=0.06, hamming=True)
        sound1_7.setVolume(0.3, log=False)
        sound1_7.seek(0)
        sound1_8.setSound(condition_list[0][0][1][3], secs=0.06, hamming=True)
        sound1_8.setVolume(0.3, log=False)
        sound1_8.seek(0)
        sound2.setSound(condition_list[0][1][0][0], secs=0.06, hamming=True)
        sound2.setVolume(0.3, log=False)
        sound2.seek(0)
        sound2_2.setSound(condition_list[0][1][0][1], secs=0.06, hamming=True)
        sound2_2.setVolume(0.3, log=False)
        sound2_2.seek(0)
        sound2_3.setSound(condition_list[0][1][0][2], secs=0.06, hamming=True)
        sound2_3.setVolume(0.3, log=False)
        sound2_3.seek(0)
        sound2_4.setSound(condition_list[0][1][0][3], secs=0.06, hamming=True)
        sound2_4.setVolume(0.3, log=False)
        sound2_4.seek(0)
        sound2_5.setSound(condition_list[0][1][1][0], secs=0.06, hamming=True)
        sound2_5.setVolume(0.3, log=False)
        sound2_5.seek(0)
        sound2_6.setSound(condition_list[0][1][1][1], secs=0.06, hamming=True)
        sound2_6.setVolume(0.3, log=False)
        sound2_6.seek(0)
        sound2_7.setSound(condition_list[0][1][1][2], secs=0.06, hamming=True)
        sound2_7.setVolume(0.3, log=False)
        sound2_7.seek(0)
        sound2_8.setSound(condition_list[0][1][1][3], secs=0.06, hamming=True)
        sound2_8.setVolume(0.3, log=False)
        sound2_8.seek(0)
        sound3.setSound(condition_list[0][2][0][0], secs=0.06, hamming=True)
        sound3.setVolume(0.3, log=False)
        sound3.seek(0)
        sound3_2.setSound(condition_list[0][2][0][1], secs=0.06, hamming=True)
        sound3_2.setVolume(0.3, log=False)
        sound3_2.seek(0)
        sound3_3.setSound(condition_list[0][2][0][2], secs=0.06, hamming=True)
        sound3_3.setVolume(0.3, log=False)
        sound3_3.seek(0)
        sound3_4.setSound(condition_list[0][2][0][3], secs=0.06, hamming=True)
        sound3_4.setVolume(0.3, log=False)
        sound3_4.seek(0)
        sound3_5.setSound(condition_list[0][2][1][0], secs=0.06, hamming=True)
        sound3_5.setVolume(0.3, log=False)
        sound3_5.seek(0)
        sound3_6.setSound(condition_list[0][2][1][1], secs=0.06, hamming=True)
        sound3_6.setVolume(0.3, log=False)
        sound3_6.seek(0)
        sound3_7.setSound(condition_list[0][2][1][2], secs=0.06, hamming=True)
        sound3_7.setVolume(0.3, log=False)
        sound3_7.seek(0)
        sound3_8.setSound(condition_list[0][2][1][3], secs=0.06, hamming=True)
        sound3_8.setVolume(0.3, log=False)
        sound3_8.seek(0)
        sound4.setSound(condition_list[0][3][0][0], secs=0.06, hamming=True)
        sound4.setVolume(0.3, log=False)
        sound4.seek(0)
        sound4_2.setSound(condition_list[0][3][0][1], secs=0.06, hamming=True)
        sound4_2.setVolume(0.3, log=False)
        sound4_2.seek(0)
        sound4_3.setSound(condition_list[0][3][0][2], secs=0.06, hamming=True)
        sound4_3.setVolume(0.3, log=False)
        sound4_3.seek(0)
        sound4_4.setSound(condition_list[0][3][0][3], secs=0.06, hamming=True)
        sound4_4.setVolume(0.3, log=False)
        sound4_4.seek(0)
        sound4_5.setSound(condition_list[0][3][1][0], secs=0.06, hamming=True)
        sound4_5.setVolume(0.3, log=False)
        sound4_5.seek(0)
        sound4_6.setSound(condition_list[0][3][1][1], secs=0.06, hamming=True)
        sound4_6.setVolume(0.3, log=False)
        sound4_6.seek(0)
        sound4_7.setSound(condition_list[0][3][1][2], secs=0.06, hamming=True)
        sound4_7.setVolume(0.3, log=False)
        sound4_7.seek(0)
        sound4_8.setSound(condition_list[0][3][1][3], secs=0.06, hamming=True)
        sound4_8.setVolume(0.3, log=False)
        sound4_8.seek(0)
        sound5.setSound(condition_list[0][4][0][0], secs=0.06, hamming=True)
        sound5.setVolume(0.3, log=False)
        sound5.seek(0)
        sound5_2.setSound(condition_list[0][4][0][1], secs=0.06, hamming=True)
        sound5_2.setVolume(0.3, log=False)
        sound5_2.seek(0)
        sound5_3.setSound(condition_list[0][4][0][2], secs=0.06, hamming=True)
        sound5_3.setVolume(0.3, log=False)
        sound5_3.seek(0)
        sound5_4.setSound(condition_list[0][4][0][3], secs=0.06, hamming=True)
        sound5_4.setVolume(0.3, log=False)
        sound5_4.seek(0)
        sound5_5.setSound(condition_list[0][4][1][0], secs=0.06, hamming=True)
        sound5_5.setVolume(0.3, log=False)
        sound5_5.seek(0)
        sound5_6.setSound(condition_list[0][4][1][1], secs=0.06, hamming=True)
        sound5_6.setVolume(0.3, log=False)
        sound5_6.seek(0)
        sound5_7.setSound(condition_list[0][4][1][2], secs=0.06, hamming=True)
        sound5_7.setVolume(0.3, log=False)
        sound5_7.seek(0)
        sound5_8.setSound(condition_list[0][4][1][3], secs=0.06, hamming=True)
        sound5_8.setVolume(0.3, log=False)
        sound5_8.seek(0)
        sound6.setSound(condition_list[0][5][0][0], secs=0.06, hamming=True)
        sound6.setVolume(0.3, log=False)
        sound6.seek(0)
        sound6_2.setSound(condition_list[0][5][0][1], secs=0.06, hamming=True)
        sound6_2.setVolume(0.3, log=False)
        sound6_2.seek(0)
        sound6_3.setSound(condition_list[0][5][0][2], secs=0.06, hamming=True)
        sound6_3.setVolume(0.3, log=False)
        sound6_3.seek(0)
        sound6_4.setSound(condition_list[0][5][0][3], secs=0.06, hamming=True)
        sound6_4.setVolume(0.3, log=False)
        sound6_4.seek(0)
        sound6_5.setSound(condition_list[0][5][1][0], secs=0.06, hamming=True)
        sound6_5.setVolume(0.3, log=False)
        sound6_5.seek(0)
        sound6_6.setSound(condition_list[0][5][1][1], secs=0.06, hamming=True)
        sound6_6.setVolume(0.3, log=False)
        sound6_6.seek(0)
        sound6_7.setSound(condition_list[0][5][1][2], secs=0.06, hamming=True)
        sound6_7.setVolume(0.3, log=False)
        sound6_7.seek(0)
        sound6_8.setSound(condition_list[0][5][1][3], secs=0.06, hamming=True)
        sound6_8.setVolume(0.3, log=False)
        sound6_8.seek(0)
        sound7.setSound(condition_list[0][6][0][0], secs=0.06, hamming=True)
        sound7.setVolume(0.3, log=False)
        sound7.seek(0)
        sound7_2.setSound(condition_list[0][6][0][1], secs=0.06, hamming=True)
        sound7_2.setVolume(0.3, log=False)
        sound7_2.seek(0)
        sound7_3.setSound(condition_list[0][6][0][2], secs=0.06, hamming=True)
        sound7_3.setVolume(0.3, log=False)
        sound7_3.seek(0)
        sound7_4.setSound(condition_list[0][6][0][3], secs=0.06, hamming=True)
        sound7_4.setVolume(0.3, log=False)
        sound7_4.seek(0)
        sound7_5.setSound(condition_list[0][6][1][0], secs=0.06, hamming=True)
        sound7_5.setVolume(0.3, log=False)
        sound7_5.seek(0)
        sound7_6.setSound(condition_list[0][6][1][1], secs=0.06, hamming=True)
        sound7_6.setVolume(0.3, log=False)
        sound7_6.seek(0)
        sound7_7.setSound(condition_list[0][6][1][2], secs=0.06, hamming=True)
        sound7_7.setVolume(0.3, log=False)
        sound7_7.seek(0)
        sound7_8.setSound(condition_list[0][6][1][3], secs=0.06, hamming=True)
        sound7_8.setVolume(0.3, log=False)
        sound7_8.seek(0)
        sound8.setSound(condition_list[0][7][0][0], secs=0.06, hamming=True)
        sound8.setVolume(0.3, log=False)
        sound8.seek(0)
        sound8_2.setSound(condition_list[0][7][0][1], secs=0.06, hamming=True)
        sound8_2.setVolume(0.3, log=False)
        sound8_2.seek(0)
        sound8_3.setSound(condition_list[0][7][0][2], secs=0.06, hamming=True)
        sound8_3.setVolume(0.3, log=False)
        sound8_3.seek(0)
        sound8_4.setSound(condition_list[0][7][0][3], secs=0.06, hamming=True)
        sound8_4.setVolume(0.3, log=False)
        sound8_4.seek(0)
        sound8_5.setSound(condition_list[0][7][1][0], secs=0.06, hamming=True)
        sound8_5.setVolume(0.3, log=False)
        sound8_5.seek(0)
        sound8_6.setSound(condition_list[0][7][1][1], secs=0.06, hamming=True)
        sound8_6.setVolume(0.3, log=False)
        sound8_6.seek(0)
        sound8_7.setSound(condition_list[0][7][1][2], secs=0.06, hamming=True)
        sound8_7.setVolume(0.3, log=False)
        sound8_7.seek(0)
        sound8_8.setSound(condition_list[0][7][1][3], secs=0.06, hamming=True)
        sound8_8.setVolume(0.3, log=False)
        sound8_8.seek(0)
        sound9.setSound(condition_list[0][8][0][0], secs=0.06, hamming=True)
        sound9.setVolume(0.3, log=False)
        sound9.seek(0)
        sound9_2.setSound(condition_list[0][8][0][1], secs=0.06, hamming=True)
        sound9_2.setVolume(0.3, log=False)
        sound9_2.seek(0)
        sound9_3.setSound(condition_list[0][8][0][2], secs=0.06, hamming=True)
        sound9_3.setVolume(0.3, log=False)
        sound9_3.seek(0)
        sound9_4.setSound(condition_list[0][8][0][3], secs=0.06, hamming=True)
        sound9_4.setVolume(0.3, log=False)
        sound9_4.seek(0)
        sound9_5.setSound(condition_list[0][8][1][0], secs=0.06, hamming=True)
        sound9_5.setVolume(0.3, log=False)
        sound9_5.seek(0)
        sound9_6.setSound(condition_list[0][8][1][1], secs=0.06, hamming=True)
        sound9_6.setVolume(0.3, log=False)
        sound9_6.seek(0)
        sound9_7.setSound(condition_list[0][8][1][2], secs=0.06, hamming=True)
        sound9_7.setVolume(0.3, log=False)
        sound9_7.seek(0)
        sound9_8.setSound(condition_list[0][8][1][3], secs=0.06, hamming=True)
        sound9_8.setVolume(0.3, log=False)
        sound9_8.seek(0)
        sound10.setSound(condition_list[0][9][0][0], secs=0.06, hamming=True)
        sound10.setVolume(0.3, log=False)
        sound10.seek(0)
        sound10_2.setSound(condition_list[0][9][0][1], secs=0.06, hamming=True)
        sound10_2.setVolume(0.3, log=False)
        sound10_2.seek(0)
        sound10_3.setSound(condition_list[0][9][0][2], secs=0.06, hamming=True)
        sound10_3.setVolume(0.3, log=False)
        sound10_3.seek(0)
        sound10_4.setSound(condition_list[0][9][0][3], secs=0.06, hamming=True)
        sound10_4.setVolume(0.3, log=False)
        sound10_4.seek(0)
        sound10_5.setSound(condition_list[0][9][1][0], secs=0.06, hamming=True)
        sound10_5.setVolume(0.3, log=False)
        sound10_5.seek(0)
        sound10_6.setSound(condition_list[0][9][1][1], secs=0.06, hamming=True)
        sound10_6.setVolume(0.3, log=False)
        sound10_6.seek(0)
        sound10_7.setSound(condition_list[0][9][1][2], secs=0.06, hamming=True)
        sound10_7.setVolume(0.3, log=False)
        sound10_7.seek(0)
        sound10_8.setSound(condition_list[0][9][1][3], secs=0.06, hamming=True)
        sound10_8.setVolume(0.3, log=False)
        sound10_8.seek(0)
        sound11.setSound(condition_list[0][10][0][0], secs=0.06, hamming=True)
        sound11.setVolume(0.3, log=False)
        sound11.seek(0)
        sound11_2.setSound(condition_list[0][10][0][1], secs=0.06, hamming=True)
        sound11_2.setVolume(0.3, log=False)
        sound11_2.seek(0)
        sound11_3.setSound(condition_list[0][10][0][2], secs=0.06, hamming=True)
        sound11_3.setVolume(0.3, log=False)
        sound11_3.seek(0)
        sound11_4.setSound(condition_list[0][10][0][3], secs=0.06, hamming=True)
        sound11_4.setVolume(0.3, log=False)
        sound11_4.seek(0)
        sound11_5.setSound(condition_list[0][10][1][0], secs=0.06, hamming=True)
        sound11_5.setVolume(0.3, log=False)
        sound11_5.seek(0)
        sound11_6.setSound(condition_list[0][10][1][1], secs=0.06, hamming=True)
        sound11_6.setVolume(0.3, log=False)
        sound11_6.seek(0)
        sound11_7.setSound(condition_list[0][10][1][2], secs=0.06, hamming=True)
        sound11_7.setVolume(0.3, log=False)
        sound11_7.seek(0)
        sound11_8.setSound(condition_list[0][10][1][3], secs=0.06, hamming=True)
        sound11_8.setVolume(0.3, log=False)
        sound11_8.seek(0)
        sound12.setSound(condition_list[0][11][0][0], secs=0.06, hamming=True)
        sound12.setVolume(0.3, log=False)
        sound12.seek(0)
        sound12_2.setSound(condition_list[0][11][0][1], secs=0.06, hamming=True)
        sound12_2.setVolume(0.3, log=False)
        sound12_2.seek(0)
        sound12_3.setSound(condition_list[0][11][0][2], secs=0.06, hamming=True)
        sound12_3.setVolume(0.3, log=False)
        sound12_3.seek(0)
        sound12_4.setSound(condition_list[0][11][0][3], secs=0.06, hamming=True)
        sound12_4.setVolume(0.3, log=False)
        sound12_4.seek(0)
        sound12_5.setSound(condition_list[0][11][1][0], secs=0.06, hamming=True)
        sound12_5.setVolume(0.3, log=False)
        sound12_5.seek(0)
        sound12_6.setSound(condition_list[0][11][1][1], secs=0.06, hamming=True)
        sound12_6.setVolume(0.3, log=False)
        sound12_6.seek(0)
        sound12_7.setSound(condition_list[0][11][1][2], secs=0.06, hamming=True)
        sound12_7.setVolume(0.3, log=False)
        sound12_7.seek(0)
        sound12_8.setSound(condition_list[0][11][1][3], secs=0.06, hamming=True)
        sound12_8.setVolume(0.3, log=False)
        sound12_8.seek(0)
        sound13.setSound(condition_list[0][12][0][0], secs=0.06, hamming=True)
        sound13.setVolume(0.3, log=False)
        sound13.seek(0)
        sound13_2.setSound(condition_list[0][12][0][1], secs=0.06, hamming=True)
        sound13_2.setVolume(0.3, log=False)
        sound13_2.seek(0)
        sound13_3.setSound(condition_list[0][12][0][2], secs=0.06, hamming=True)
        sound13_3.setVolume(0.3, log=False)
        sound13_3.seek(0)
        sound13_4.setSound(condition_list[0][12][0][3], secs=0.06, hamming=True)
        sound13_4.setVolume(0.3, log=False)
        sound13_4.seek(0)
        sound13_5.setSound(condition_list[0][12][1][0], secs=0.06, hamming=True)
        sound13_5.setVolume(0.3, log=False)
        sound13_5.seek(0)
        sound13_6.setSound(condition_list[0][12][1][1], secs=0.06, hamming=True)
        sound13_6.setVolume(0.3, log=False)
        sound13_6.seek(0)
        sound13_7.setSound(condition_list[0][12][1][2], secs=0.06, hamming=True)
        sound13_7.setVolume(0.3, log=False)
        sound13_7.seek(0)
        sound13_8.setSound(condition_list[0][12][1][3], secs=0.06, hamming=True)
        sound13_8.setVolume(0.3, log=False)
        sound13_8.seek(0)
        sound14.setSound(condition_list[0][13][0][0], secs=0.06, hamming=True)
        sound14.setVolume(0.3, log=False)
        sound14.seek(0)
        sound14_2.setSound(condition_list[0][13][0][1], secs=0.06, hamming=True)
        sound14_2.setVolume(0.3, log=False)
        sound14_2.seek(0)
        sound14_3.setSound(condition_list[0][13][0][2], secs=0.06, hamming=True)
        sound14_3.setVolume(0.3, log=False)
        sound14_3.seek(0)
        sound14_4.setSound(condition_list[0][13][0][3], secs=0.06, hamming=True)
        sound14_4.setVolume(0.3, log=False)
        sound14_4.seek(0)
        sound14_5.setSound(condition_list[0][13][1][0], secs=0.06, hamming=True)
        sound14_5.setVolume(0.3, log=False)
        sound14_5.seek(0)
        sound14_6.setSound(condition_list[0][13][1][1], secs=0.06, hamming=True)
        sound14_6.setVolume(0.3, log=False)
        sound14_6.seek(0)
        sound14_7.setSound(condition_list[0][13][1][2], secs=0.06, hamming=True)
        sound14_7.setVolume(0.3, log=False)
        sound14_7.seek(0)
        sound14_8.setSound(condition_list[0][13][1][3], secs=0.06, hamming=True)
        sound14_8.setVolume(0.3, log=False)
        sound14_8.seek(0)
        sound15.setSound(condition_list[0][14][0][0], secs=0.06, hamming=True)
        sound15.setVolume(0.3, log=False)
        sound15.seek(0)
        sound15_2.setSound(condition_list[0][14][0][1], secs=0.06, hamming=True)
        sound15_2.setVolume(0.3, log=False)
        sound15_2.seek(0)
        sound15_3.setSound(condition_list[0][14][0][2], secs=0.06, hamming=True)
        sound15_3.setVolume(0.3, log=False)
        sound15_3.seek(0)
        sound15_4.setSound(condition_list[0][14][0][3], secs=0.06, hamming=True)
        sound15_4.setVolume(0.3, log=False)
        sound15_4.seek(0)
        sound15_5.setSound(condition_list[0][14][1][0], secs=0.06, hamming=True)
        sound15_5.setVolume(0.3, log=False)
        sound15_5.seek(0)
        sound15_6.setSound(condition_list[0][14][1][1], secs=0.06, hamming=True)
        sound15_6.setVolume(0.3, log=False)
        sound15_6.seek(0)
        sound15_7.setSound(condition_list[0][14][1][2], secs=0.06, hamming=True)
        sound15_7.setVolume(0.3, log=False)
        sound15_7.seek(0)
        sound15_8.setSound(condition_list[0][14][1][3], secs=0.06, hamming=True)
        sound15_8.setVolume(0.3, log=False)
        sound15_8.seek(0)
        spund16.setSound(condition_list[0][15][0][0], secs=0.06, hamming=True)
        spund16.setVolume(0.3, log=False)
        spund16.seek(0)
        spund16_2.setSound(condition_list[0][15][0][1], secs=0.06, hamming=True)
        spund16_2.setVolume(0.3, log=False)
        spund16_2.seek(0)
        spund16_3.setSound(condition_list[0][15][0][2], secs=0.06, hamming=True)
        spund16_3.setVolume(0.3, log=False)
        spund16_3.seek(0)
        spund16_4.setSound(condition_list[0][15][0][3], secs=0.06, hamming=True)
        spund16_4.setVolume(0.3, log=False)
        spund16_4.seek(0)
        spund16_5.setSound(condition_list[0][15][1][0], secs=0.06, hamming=True)
        spund16_5.setVolume(0.3, log=False)
        spund16_5.seek(0)
        spund16_6.setSound(condition_list[0][15][1][1], secs=0.06, hamming=True)
        spund16_6.setVolume(0.3, log=False)
        spund16_6.seek(0)
        spund16_7.setSound(condition_list[0][15][1][2], secs=0.06, hamming=True)
        spund16_7.setVolume(0.3, log=False)
        spund16_7.seek(0)
        spund16_8.setSound(condition_list[0][15][1][3], secs=0.06, hamming=True)
        spund16_8.setVolume(0.3, log=False)
        spund16_8.seek(0)
        sound17.setSound(condition_list[0][16][0][0], secs=0.06, hamming=True)
        sound17.setVolume(0.3, log=False)
        sound17.seek(0)
        sound17_2.setSound(condition_list[0][16][0][2], secs=0.06, hamming=True)
        sound17_2.setVolume(0.3, log=False)
        sound17_2.seek(0)
        sound17_3.setSound(condition_list[0][16][0][1], secs=0.06, hamming=True)
        sound17_3.setVolume(0.3, log=False)
        sound17_3.seek(0)
        sound17_4.setSound(condition_list[0][16][0][3], secs=0.06, hamming=True)
        sound17_4.setVolume(0.3, log=False)
        sound17_4.seek(0)
        sound17_5.setSound(condition_list[0][16][1][0], secs=0.06, hamming=True)
        sound17_5.setVolume(0.3, log=False)
        sound17_5.seek(0)
        sound17_6.setSound(condition_list[0][16][1][1], secs=0.06, hamming=True)
        sound17_6.setVolume(0.3, log=False)
        sound17_6.seek(0)
        sound17_7.setSound(condition_list[0][16][1][2], secs=0.06, hamming=True)
        sound17_7.setVolume(0.3, log=False)
        sound17_7.seek(0)
        sound17_8.setSound(condition_list[0][16][1][3], secs=0.06, hamming=True)
        sound17_8.setVolume(0.3, log=False)
        sound17_8.seek(0)
        sound18.setSound(condition_list[0][17][0][0], secs=0.06, hamming=True)
        sound18.setVolume(0.3, log=False)
        sound18.seek(0)
        sound18_2.setSound(condition_list[0][17][0][1], secs=0.06, hamming=True)
        sound18_2.setVolume(0.3, log=False)
        sound18_2.seek(0)
        sound18_3.setSound(condition_list[0][17][0][2], secs=0.06, hamming=True)
        sound18_3.setVolume(0.3, log=False)
        sound18_3.seek(0)
        sound18_4.setSound(condition_list[0][17][0][3], secs=0.06, hamming=True)
        sound18_4.setVolume(0.3, log=False)
        sound18_4.seek(0)
        sound18_5.setSound(condition_list[0][17][1][0], secs=0.06, hamming=True)
        sound18_5.setVolume(0.3, log=False)
        sound18_5.seek(0)
        sound18_6.setSound(condition_list[0][17][1][1], secs=0.06, hamming=True)
        sound18_6.setVolume(0.3, log=False)
        sound18_6.seek(0)
        sound18_7.setSound(condition_list[0][17][1][2], secs=0.06, hamming=True)
        sound18_7.setVolume(0.3, log=False)
        sound18_7.seek(0)
        sound18_8.setSound(condition_list[0][17][1][3], secs=0.06, hamming=True)
        sound18_8.setVolume(0.3, log=False)
        sound18_8.seek(0)
        sound19.setSound(condition_list[0][18][0][0], secs=0.06, hamming=True)
        sound19.setVolume(0.3, log=False)
        sound19.seek(0)
        sound19_2.setSound(condition_list[0][18][0][1], secs=0.06, hamming=True)
        sound19_2.setVolume(0.3, log=False)
        sound19_2.seek(0)
        sound19_3.setSound(condition_list[0][18][0][2], secs=0.06, hamming=True)
        sound19_3.setVolume(0.3, log=False)
        sound19_3.seek(0)
        sound19_4.setSound(condition_list[0][18][0][3], secs=0.06, hamming=True)
        sound19_4.setVolume(0.3, log=False)
        sound19_4.seek(0)
        sound19_5.setSound(condition_list[0][18][1][0], secs=0.06, hamming=True)
        sound19_5.setVolume(0.3, log=False)
        sound19_5.seek(0)
        sound19_6.setSound(condition_list[0][18][1][1], secs=0.06, hamming=True)
        sound19_6.setVolume(0.3, log=False)
        sound19_6.seek(0)
        sound19_7.setSound(condition_list[0][18][1][2], secs=0.06, hamming=True)
        sound19_7.setVolume(0.3, log=False)
        sound19_7.seek(0)
        sound19_8.setSound(condition_list[0][18][1][3], secs=0.06, hamming=True)
        sound19_8.setVolume(0.3, log=False)
        sound19_8.seek(0)
        sound20.setSound(condition_list[0][19][0][0], secs=0.06, hamming=True)
        sound20.setVolume(0.3, log=False)
        sound20.seek(0)
        sound20_2.setSound(condition_list[0][19][0][1], secs=0.06, hamming=True)
        sound20_2.setVolume(0.3, log=False)
        sound20_2.seek(0)
        sound20_3.setSound(condition_list[0][19][0][2], secs=0.06, hamming=True)
        sound20_3.setVolume(0.3, log=False)
        sound20_3.seek(0)
        sound20_4.setSound(condition_list[0][19][0][3], secs=0.06, hamming=True)
        sound20_4.setVolume(0.3, log=False)
        sound20_4.seek(0)
        sound20_5.setSound(condition_list[0][19][1][0], secs=0.06, hamming=True)
        sound20_5.setVolume(0.3, log=False)
        sound20_5.seek(0)
        sound20_6.setSound(condition_list[0][19][1][1], secs=0.06, hamming=True)
        sound20_6.setVolume(0.3, log=False)
        sound20_6.seek(0)
        sound20_7.setSound(condition_list[0][19][1][2], secs=0.06, hamming=True)
        sound20_7.setVolume(0.3, log=False)
        sound20_7.seek(0)
        sound20_8.setSound(condition_list[0][19][1][3], secs=0.06, hamming=True)
        sound20_8.setVolume(0.3, log=False)
        sound20_8.seek(0)
        sound21.setSound(condition_list[0][20][0][0], secs=0.06, hamming=True)
        sound21.setVolume(0.3, log=False)
        sound21.seek(0)
        sound21_2.setSound(condition_list[0][20][0][1], secs=0.06, hamming=True)
        sound21_2.setVolume(0.3, log=False)
        sound21_2.seek(0)
        sound21_3.setSound(condition_list[0][20][0][2], secs=0.06, hamming=True)
        sound21_3.setVolume(0.3, log=False)
        sound21_3.seek(0)
        sound21_4.setSound(condition_list[0][20][0][3], secs=0.06, hamming=True)
        sound21_4.setVolume(0.3, log=False)
        sound21_4.seek(0)
        sound21_5.setSound(condition_list[0][20][1][0], secs=0.06, hamming=True)
        sound21_5.setVolume(0.3, log=False)
        sound21_5.seek(0)
        sound21_6.setSound(condition_list[0][20][1][1], secs=0.06, hamming=True)
        sound21_6.setVolume(0.3, log=False)
        sound21_6.seek(0)
        sound21_7.setSound(condition_list[0][20][1][2], secs=0.06, hamming=True)
        sound21_7.setVolume(0.3, log=False)
        sound21_7.seek(0)
        sound21_8.setSound(condition_list[0][20][1][3], secs=0.06, hamming=True)
        sound21_8.setVolume(0.3, log=False)
        sound21_8.seek(0)
        sound22.setSound(condition_list[0][21][0][0], secs=0.06, hamming=True)
        sound22.setVolume(0.3, log=False)
        sound22.seek(0)
        sound22_2.setSound(condition_list[0][21][0][1], secs=0.06, hamming=True)
        sound22_2.setVolume(0.3, log=False)
        sound22_2.seek(0)
        sound22_3.setSound(condition_list[0][21][0][2], secs=0.06, hamming=True)
        sound22_3.setVolume(0.3, log=False)
        sound22_3.seek(0)
        sound22_4.setSound(condition_list[0][21][0][3], secs=0.06, hamming=True)
        sound22_4.setVolume(0.3, log=False)
        sound22_4.seek(0)
        sound22_5.setSound(condition_list[0][21][1][0], secs=0.06, hamming=True)
        sound22_5.setVolume(0.3, log=False)
        sound22_5.seek(0)
        sound22_6.setSound(condition_list[0][21][1][1], secs=0.06, hamming=True)
        sound22_6.setVolume(0.3, log=False)
        sound22_6.seek(0)
        sound22_7.setSound(condition_list[0][21][1][2], secs=0.06, hamming=True)
        sound22_7.setVolume(0.3, log=False)
        sound22_7.seek(0)
        sound22_8.setSound(condition_list[0][21][1][3], secs=0.06, hamming=True)
        sound22_8.setVolume(0.3, log=False)
        sound22_8.seek(0)
        sound23.setSound(condition_list[0][22][0][0], secs=0.06, hamming=True)
        sound23.setVolume(0.3, log=False)
        sound23.seek(0)
        sound23_2.setSound(condition_list[0][22][0][1], secs=0.06, hamming=True)
        sound23_2.setVolume(0.3, log=False)
        sound23_2.seek(0)
        sound23_3.setSound(condition_list[0][22][0][2], secs=0.06, hamming=True)
        sound23_3.setVolume(0.3, log=False)
        sound23_3.seek(0)
        sound23_4.setSound(condition_list[0][22][0][3], secs=0.06, hamming=True)
        sound23_4.setVolume(0.3, log=False)
        sound23_4.seek(0)
        sound23_5.setSound(condition_list[0][22][1][0], secs=0.06, hamming=True)
        sound23_5.setVolume(0.3, log=False)
        sound23_5.seek(0)
        sound23_6.setSound(condition_list[0][22][1][1], secs=0.06, hamming=True)
        sound23_6.setVolume(0.3, log=False)
        sound23_6.seek(0)
        sound23_7.setSound(condition_list[0][22][1][2], secs=0.06, hamming=True)
        sound23_7.setVolume(0.3, log=False)
        sound23_7.seek(0)
        sound23_8.setSound(condition_list[0][22][1][3], secs=0.06, hamming=True)
        sound23_8.setVolume(0.3, log=False)
        sound23_8.seek(0)
        sound24.setSound(condition_list[0][23][0][0], secs=0.06, hamming=True)
        sound24.setVolume(0.3, log=False)
        sound24.seek(0)
        sound24_2.setSound(condition_list[0][23][0][1], secs=0.06, hamming=True)
        sound24_2.setVolume(0.3, log=False)
        sound24_2.seek(0)
        sound24_3.setSound(condition_list[0][23][0][2], secs=0.06, hamming=True)
        sound24_3.setVolume(0.3, log=False)
        sound24_3.seek(0)
        sound24_4.setSound(condition_list[0][23][0][3], secs=0.06, hamming=True)
        sound24_4.setVolume(0.3, log=False)
        sound24_4.seek(0)
        sound24_5.setSound(condition_list[0][23][1][0], secs=0.06, hamming=True)
        sound24_5.setVolume(0.3, log=False)
        sound24_5.seek(0)
        sound24_6.setSound(condition_list[0][23][1][1], secs=0.06, hamming=True)
        sound24_6.setVolume(0.3, log=False)
        sound24_6.seek(0)
        sound24_7.setSound(condition_list[0][23][1][2], secs=0.06, hamming=True)
        sound24_7.setVolume(0.3, log=False)
        sound24_7.seek(0)
        sound24_8.setSound(condition_list[0][23][1][3], secs=0.06, hamming=True)
        sound24_8.setVolume(0.3, log=False)
        sound24_8.seek(0)
        sound25.setSound(condition_list[0][24][0][0], secs=0.06, hamming=True)
        sound25.setVolume(0.3, log=False)
        sound25.seek(0)
        sound25_2.setSound(condition_list[0][24][0][1], secs=0.06, hamming=True)
        sound25_2.setVolume(0.3, log=False)
        sound25_2.seek(0)
        sound25_3.setSound(condition_list[0][24][0][2], secs=0.06, hamming=True)
        sound25_3.setVolume(0.3, log=False)
        sound25_3.seek(0)
        sound25_4.setSound(condition_list[0][24][0][3], secs=0.06, hamming=True)
        sound25_4.setVolume(0.3, log=False)
        sound25_4.seek(0)
        sound25_5.setSound(condition_list[0][24][1][0], secs=0.06, hamming=True)
        sound25_5.setVolume(0.3, log=False)
        sound25_5.seek(0)
        sound25_6.setSound(condition_list[0][24][1][1], secs=0.06, hamming=True)
        sound25_6.setVolume(0.3, log=False)
        sound25_6.seek(0)
        sound25_7.setSound(condition_list[0][24][1][2], secs=0.06, hamming=True)
        sound25_7.setVolume(0.3, log=False)
        sound25_7.seek(0)
        sound25_8.setSound(condition_list[0][24][1][3], secs=0.06, hamming=True)
        sound25_8.setVolume(0.3, log=False)
        sound25_8.seek(0)
        sound26.setSound(condition_list[0][25][0][0], secs=0.06, hamming=True)
        sound26.setVolume(0.3, log=False)
        sound26.seek(0)
        sound26_2.setSound(condition_list[0][25][0][1], secs=0.06, hamming=True)
        sound26_2.setVolume(0.3, log=False)
        sound26_2.seek(0)
        sound26_3.setSound(condition_list[0][25][0][2], secs=0.06, hamming=True)
        sound26_3.setVolume(0.3, log=False)
        sound26_3.seek(0)
        sound26_4.setSound(condition_list[0][25][0][3], secs=0.06, hamming=True)
        sound26_4.setVolume(0.3, log=False)
        sound26_4.seek(0)
        sound26_5.setSound(condition_list[0][25][1][0], secs=0.06, hamming=True)
        sound26_5.setVolume(0.3, log=False)
        sound26_5.seek(0)
        sound26_6.setSound(condition_list[0][25][1][1], secs=0.06, hamming=True)
        sound26_6.setVolume(0.3, log=False)
        sound26_6.seek(0)
        sound26_7.setSound(condition_list[0][25][1][2], secs=0.06, hamming=True)
        sound26_7.setVolume(0.3, log=False)
        sound26_7.seek(0)
        sound26_8.setSound(condition_list[0][25][1][3], secs=0.06, hamming=True)
        sound26_8.setVolume(0.3, log=False)
        sound26_8.seek(0)
        sound27.setSound(condition_list[0][26][0][0], secs=0.06, hamming=True)
        sound27.setVolume(0.3, log=False)
        sound27.seek(0)
        sound27_2.setSound(condition_list[0][26][0][1], secs=0.06, hamming=True)
        sound27_2.setVolume(0.3, log=False)
        sound27_2.seek(0)
        sound27_3.setSound(condition_list[0][26][0][2], secs=0.06, hamming=True)
        sound27_3.setVolume(0.3, log=False)
        sound27_3.seek(0)
        sound27_4.setSound(condition_list[0][26][0][3], secs=0.06, hamming=True)
        sound27_4.setVolume(0.3, log=False)
        sound27_4.seek(0)
        sound27_5.setSound(condition_list[0][26][1][0], secs=0.06, hamming=True)
        sound27_5.setVolume(0.3, log=False)
        sound27_5.seek(0)
        sound27_6.setSound(condition_list[0][26][1][1], secs=0.06, hamming=True)
        sound27_6.setVolume(0.3, log=False)
        sound27_6.seek(0)
        sound27_7.setSound(condition_list[0][26][1][2], secs=0.06, hamming=True)
        sound27_7.setVolume(0.3, log=False)
        sound27_7.seek(0)
        sound27_8.setSound(condition_list[0][26][1][3], secs=0.06, hamming=True)
        sound27_8.setVolume(0.3, log=False)
        sound27_8.seek(0)
        sound28.setSound(condition_list[0][27][0][0], secs=0.06, hamming=True)
        sound28.setVolume(0.3, log=False)
        sound28.seek(0)
        sound28_2.setSound(condition_list[0][27][0][1], secs=0.06, hamming=True)
        sound28_2.setVolume(0.3, log=False)
        sound28_2.seek(0)
        sound28_3.setSound(condition_list[0][27][0][2], secs=0.06, hamming=True)
        sound28_3.setVolume(0.3, log=False)
        sound28_3.seek(0)
        sound28_4.setSound(condition_list[0][27][0][3], secs=0.06, hamming=True)
        sound28_4.setVolume(0.3, log=False)
        sound28_4.seek(0)
        sound28_5.setSound(condition_list[0][27][1][0], secs=0.06, hamming=True)
        sound28_5.setVolume(0.3, log=False)
        sound28_5.seek(0)
        sound28_6.setSound(condition_list[0][27][1][1], secs=0.06, hamming=True)
        sound28_6.setVolume(0.3, log=False)
        sound28_6.seek(0)
        sound28_7.setSound(condition_list[0][27][1][2], secs=0.06, hamming=True)
        sound28_7.setVolume(0.3, log=False)
        sound28_7.seek(0)
        sound28_8.setSound(condition_list[0][27][1][3], secs=0.06, hamming=True)
        sound28_8.setVolume(0.3, log=False)
        sound28_8.seek(0)
        sound29.setSound(condition_list[0][28][0][0], secs=0.06, hamming=True)
        sound29.setVolume(0.3, log=False)
        sound29.seek(0)
        sound29_2.setSound(condition_list[0][28][0][1], secs=0.06, hamming=True)
        sound29_2.setVolume(0.3, log=False)
        sound29_2.seek(0)
        sound29_3.setSound(condition_list[0][28][0][2], secs=0.06, hamming=True)
        sound29_3.setVolume(0.3, log=False)
        sound29_3.seek(0)
        sound29_4.setSound(condition_list[0][28][0][3], secs=0.06, hamming=True)
        sound29_4.setVolume(0.3, log=False)
        sound29_4.seek(0)
        sound29_5.setSound(condition_list[0][28][1][0], secs=0.06, hamming=True)
        sound29_5.setVolume(0.3, log=False)
        sound29_5.seek(0)
        sound29_6.setSound(condition_list[0][28][1][1], secs=0.06, hamming=True)
        sound29_6.setVolume(0.3, log=False)
        sound29_6.seek(0)
        sound29_7.setSound(condition_list[0][28][1][2], secs=0.06, hamming=True)
        sound29_7.setVolume(0.3, log=False)
        sound29_7.seek(0)
        sound29_8.setSound(condition_list[0][28][1][3], secs=0.06, hamming=True)
        sound29_8.setVolume(0.3, log=False)
        sound29_8.seek(0)
        sound30.setSound(condition_list[0][29][0][0], secs=0.06, hamming=True)
        sound30.setVolume(0.3, log=False)
        sound30.seek(0)
        sound30_2.setSound(condition_list[0][29][0][1], secs=0.06, hamming=True)
        sound30_2.setVolume(0.3, log=False)
        sound30_2.seek(0)
        sound30_3.setSound(condition_list[0][29][0][2], secs=0.06, hamming=True)
        sound30_3.setVolume(0.3, log=False)
        sound30_3.seek(0)
        sound30_4.setSound(condition_list[0][29][0][3], secs=0.06, hamming=True)
        sound30_4.setVolume(0.3, log=False)
        sound30_4.seek(0)
        sound30_5.setSound(condition_list[0][29][1][0], secs=0.06, hamming=True)
        sound30_5.setVolume(0.3, log=False)
        sound30_5.seek(0)
        sound30_6.setSound(condition_list[0][29][1][1], secs=0.06, hamming=True)
        sound30_6.setVolume(0.3, log=False)
        sound30_6.seek(0)
        sound30_7.setSound(condition_list[0][29][1][2], secs=0.06, hamming=True)
        sound30_7.setVolume(0.3, log=False)
        sound30_7.seek(0)
        sound30_8.setSound(condition_list[0][29][1][3], secs=0.06, hamming=True)
        sound30_8.setVolume(0.3, log=False)
        sound30_8.seek(0)
        sound31.setSound(condition_list[0][30][0][0], secs=0.06, hamming=True)
        sound31.setVolume(0.3, log=False)
        sound31.seek(0)
        sound31_2.setSound(condition_list[0][30][0][1], secs=0.06, hamming=True)
        sound31_2.setVolume(0.3, log=False)
        sound31_2.seek(0)
        sound31_3.setSound(condition_list[0][30][0][2], secs=0.06, hamming=True)
        sound31_3.setVolume(0.3, log=False)
        sound31_3.seek(0)
        sound31_4.setSound(condition_list[0][30][0][3], secs=0.06, hamming=True)
        sound31_4.setVolume(0.3, log=False)
        sound31_4.seek(0)
        sound31_5.setSound(condition_list[0][30][1][0], secs=0.06, hamming=True)
        sound31_5.setVolume(0.3, log=False)
        sound31_5.seek(0)
        sound31_6.setSound(condition_list[0][30][1][1], secs=0.06, hamming=True)
        sound31_6.setVolume(0.3, log=False)
        sound31_6.seek(0)
        sound31_7.setSound(condition_list[0][30][1][2], secs=0.06, hamming=True)
        sound31_7.setVolume(0.3, log=False)
        sound31_7.seek(0)
        sound31_8.setSound(condition_list[0][30][1][3], secs=0.06, hamming=True)
        sound31_8.setVolume(0.3, log=False)
        sound31_8.seek(0)
        sound32.setSound(condition_list[0][31][0][0], secs=0.06, hamming=True)
        sound32.setVolume(0.3, log=False)
        sound32.seek(0)
        sound32_2.setSound(condition_list[0][31][0][1], secs=0.06, hamming=True)
        sound32_2.setVolume(0.3, log=False)
        sound32_2.seek(0)
        sound32_3.setSound(condition_list[0][31][0][2], secs=0.06, hamming=True)
        sound32_3.setVolume(0.3, log=False)
        sound32_3.seek(0)
        sound32_4.setSound(condition_list[0][31][0][3], secs=0.06, hamming=True)
        sound32_4.setVolume(0.3, log=False)
        sound32_4.seek(0)
        sound32_5.setSound(condition_list[0][31][1][0], secs=0.06, hamming=True)
        sound32_5.setVolume(0.3, log=False)
        sound32_5.seek(0)
        sound32_6.setSound(condition_list[0][31][1][1], secs=0.06, hamming=True)
        sound32_6.setVolume(0.3, log=False)
        sound32_6.seek(0)
        sound32_7.setSound(condition_list[0][31][1][2], secs=0.06, hamming=True)
        sound32_7.setVolume(0.3, log=False)
        sound32_7.seek(0)
        sound32_8.setSound(condition_list[0][31][1][3], secs=0.06, hamming=True)
        sound32_8.setVolume(0.3, log=False)
        sound32_8.seek(0)
        sound33.setSound(condition_list[0][32][0][0], secs=0.06, hamming=True)
        sound33.setVolume(0.3, log=False)
        sound33.seek(0)
        sound33_2.setSound(condition_list[0][32][0][1], secs=0.06, hamming=True)
        sound33_2.setVolume(0.3, log=False)
        sound33_2.seek(0)
        sound33_3.setSound(condition_list[0][32][0][2], secs=0.06, hamming=True)
        sound33_3.setVolume(0.3, log=False)
        sound33_3.seek(0)
        sound33_4.setSound(condition_list[0][32][0][3], secs=0.06, hamming=True)
        sound33_4.setVolume(0.3, log=False)
        sound33_4.seek(0)
        sound33_5.setSound(condition_list[0][32][1][0], secs=0.06, hamming=True)
        sound33_5.setVolume(0.3, log=False)
        sound33_5.seek(0)
        sound33_6.setSound(condition_list[0][32][1][1], secs=0.06, hamming=True)
        sound33_6.setVolume(0.3, log=False)
        sound33_6.seek(0)
        sound33_7.setSound(condition_list[0][32][1][2], secs=0.06, hamming=True)
        sound33_7.setVolume(0.3, log=False)
        sound33_7.seek(0)
        sound33_8.setSound(condition_list[0][32][1][3], secs=0.06, hamming=True)
        sound33_8.setVolume(0.3, log=False)
        sound33_8.seek(0)
        sound34.setSound(condition_list[0][33][0][0], secs=0.06, hamming=True)
        sound34.setVolume(0.3, log=False)
        sound34.seek(0)
        sound34_2.setSound(condition_list[0][33][0][1], secs=0.06, hamming=True)
        sound34_2.setVolume(0.3, log=False)
        sound34_2.seek(0)
        sound34_3.setSound(condition_list[0][33][0][2], secs=0.06, hamming=True)
        sound34_3.setVolume(0.3, log=False)
        sound34_3.seek(0)
        sound34_4.setSound(condition_list[0][33][0][3], secs=0.06, hamming=True)
        sound34_4.setVolume(0.3, log=False)
        sound34_4.seek(0)
        sound34_5.setSound(condition_list[0][33][1][0], secs=0.06, hamming=True)
        sound34_5.setVolume(0.3, log=False)
        sound34_5.seek(0)
        sound34_6.setSound(condition_list[0][33][1][1], secs=0.06, hamming=True)
        sound34_6.setVolume(0.3, log=False)
        sound34_6.seek(0)
        sound34_7.setSound(condition_list[0][33][1][2], secs=0.06, hamming=True)
        sound34_7.setVolume(0.3, log=False)
        sound34_7.seek(0)
        sound34_8.setSound(condition_list[0][33][1][3], secs=0.06, hamming=True)
        sound34_8.setVolume(0.3, log=False)
        sound34_8.seek(0)
        sound35.setSound(condition_list[0][34][0][0], secs=0.06, hamming=True)
        sound35.setVolume(0.3, log=False)
        sound35.seek(0)
        sound35_2.setSound(condition_list[0][34][0][1], secs=0.06, hamming=True)
        sound35_2.setVolume(0.3, log=False)
        sound35_2.seek(0)
        sound35_3.setSound(condition_list[0][34][0][2], secs=0.06, hamming=True)
        sound35_3.setVolume(0.3, log=False)
        sound35_3.seek(0)
        sound35_4.setSound(condition_list[0][34][0][3], secs=0.06, hamming=True)
        sound35_4.setVolume(0.3, log=False)
        sound35_4.seek(0)
        sound35_5.setSound(condition_list[0][34][1][0], secs=0.06, hamming=True)
        sound35_5.setVolume(0.3, log=False)
        sound35_5.seek(0)
        sound35_6.setSound(condition_list[0][34][1][1], secs=0.06, hamming=True)
        sound35_6.setVolume(0.3, log=False)
        sound35_6.seek(0)
        sound35_7.setSound(condition_list[0][34][1][2], secs=0.06, hamming=True)
        sound35_7.setVolume(0.3, log=False)
        sound35_7.seek(0)
        sound35_8.setSound(condition_list[0][34][1][3], secs=0.06, hamming=True)
        sound35_8.setVolume(0.3, log=False)
        sound35_8.seek(0)
        sound36.setSound(condition_list[0][35][0][0], secs=0.06, hamming=True)
        sound36.setVolume(0.3, log=False)
        sound36.seek(0)
        sound36_2.setSound(condition_list[0][35][0][1], secs=0.06, hamming=True)
        sound36_2.setVolume(0.3, log=False)
        sound36_2.seek(0)
        sound36_3.setSound(condition_list[0][35][0][2], secs=0.06, hamming=True)
        sound36_3.setVolume(0.3, log=False)
        sound36_3.seek(0)
        sound36_4.setSound(condition_list[0][35][0][3], secs=0.06, hamming=True)
        sound36_4.setVolume(0.3, log=False)
        sound36_4.seek(0)
        sound36_5.setSound(condition_list[0][35][1][0], secs=0.06, hamming=True)
        sound36_5.setVolume(0.3, log=False)
        sound36_5.seek(0)
        sound36_6.setSound(condition_list[0][35][1][1], secs=0.06, hamming=True)
        sound36_6.setVolume(0.3, log=False)
        sound36_6.seek(0)
        sound36_7.setSound(condition_list[0][35][1][2], secs=0.06, hamming=True)
        sound36_7.setVolume(0.3, log=False)
        sound36_7.seek(0)
        sound36_8.setSound(condition_list[0][35][1][3], secs=0.06, hamming=True)
        sound36_8.setVolume(0.3, log=False)
        sound36_8.seek(0)
        sound37.setSound(condition_list[0][36][0][0], secs=0.06, hamming=True)
        sound37.setVolume(0.3, log=False)
        sound37.seek(0)
        sound37_2.setSound(condition_list[0][36][0][1], secs=0.06, hamming=True)
        sound37_2.setVolume(0.3, log=False)
        sound37_2.seek(0)
        sound37_3.setSound(condition_list[0][36][0][2], secs=0.06, hamming=True)
        sound37_3.setVolume(0.3, log=False)
        sound37_3.seek(0)
        sound37_4.setSound(condition_list[0][36][0][3], secs=0.06, hamming=True)
        sound37_4.setVolume(0.3, log=False)
        sound37_4.seek(0)
        sound37_5.setSound(condition_list[0][36][1][0], secs=0.06, hamming=True)
        sound37_5.setVolume(0.3, log=False)
        sound37_5.seek(0)
        sound37_6.setSound(condition_list[0][36][1][1], secs=0.06, hamming=True)
        sound37_6.setVolume(0.3, log=False)
        sound37_6.seek(0)
        sound37_7.setSound(condition_list[0][36][1][2], secs=0.06, hamming=True)
        sound37_7.setVolume(0.3, log=False)
        sound37_7.seek(0)
        sound37_8.setSound(condition_list[0][36][1][3], secs=0.06, hamming=True)
        sound37_8.setVolume(0.3, log=False)
        sound37_8.seek(0)
        sound38.setSound(condition_list[0][37][0][0], secs=0.06, hamming=True)
        sound38.setVolume(0.3, log=False)
        sound38.seek(0)
        sound38_2.setSound(condition_list[0][37][0][1], secs=0.06, hamming=True)
        sound38_2.setVolume(0.3, log=False)
        sound38_2.seek(0)
        sound38_3.setSound(condition_list[0][37][0][2], secs=0.06, hamming=True)
        sound38_3.setVolume(0.3, log=False)
        sound38_3.seek(0)
        sound38_4.setSound(condition_list[0][37][0][3], secs=0.06, hamming=True)
        sound38_4.setVolume(0.3, log=False)
        sound38_4.seek(0)
        sound38_5.setSound(condition_list[0][37][1][0], secs=0.06, hamming=True)
        sound38_5.setVolume(0.3, log=False)
        sound38_5.seek(0)
        sound38_6.setSound(condition_list[0][37][1][1], secs=0.06, hamming=True)
        sound38_6.setVolume(0.3, log=False)
        sound38_6.seek(0)
        sound38_7.setSound(condition_list[0][37][1][2], secs=0.06, hamming=True)
        sound38_7.setVolume(0.3, log=False)
        sound38_7.seek(0)
        sound38_8.setSound(condition_list[0][37][1][3], secs=0.06, hamming=True)
        sound38_8.setVolume(0.3, log=False)
        sound38_8.seek(0)
        sound39.setSound(condition_list[0][38][0][0], secs=0.06, hamming=True)
        sound39.setVolume(0.3, log=False)
        sound39.seek(0)
        sound39_2.setSound(condition_list[0][38][0][1], secs=0.06, hamming=True)
        sound39_2.setVolume(0.3, log=False)
        sound39_2.seek(0)
        sound39_3.setSound(condition_list[0][38][0][2], secs=0.06, hamming=True)
        sound39_3.setVolume(0.3, log=False)
        sound39_3.seek(0)
        sound39_4.setSound(condition_list[0][38][0][3], secs=0.06, hamming=True)
        sound39_4.setVolume(0.3, log=False)
        sound39_4.seek(0)
        sound39_5.setSound(condition_list[0][38][1][0], secs=0.06, hamming=True)
        sound39_5.setVolume(0.3, log=False)
        sound39_5.seek(0)
        sound39_6.setSound(condition_list[0][38][1][1], secs=0.06, hamming=True)
        sound39_6.setVolume(0.3, log=False)
        sound39_6.seek(0)
        sound39_7.setSound(condition_list[0][38][1][2], secs=0.06, hamming=True)
        sound39_7.setVolume(0.3, log=False)
        sound39_7.seek(0)
        sound39_8.setSound(condition_list[0][38][1][3], secs=0.06, hamming=True)
        sound39_8.setVolume(0.3, log=False)
        sound39_8.seek(0)
        sound40.setSound(condition_list[0][39][0][0], secs=0.06, hamming=True)
        sound40.setVolume(0.3, log=False)
        sound40.seek(0)
        sound40_2.setSound(condition_list[0][39][0][1], secs=0.06, hamming=True)
        sound40_2.setVolume(0.3, log=False)
        sound40_2.seek(0)
        sound40_3.setSound(condition_list[0][39][0][2], secs=0.06, hamming=True)
        sound40_3.setVolume(0.3, log=False)
        sound40_3.seek(0)
        sound40_4.setSound(condition_list[0][39][0][3], secs=0.06, hamming=True)
        sound40_4.setVolume(0.3, log=False)
        sound40_4.seek(0)
        sound40_5.setSound(condition_list[0][39][1][0], secs=0.06, hamming=True)
        sound40_5.setVolume(0.3, log=False)
        sound40_5.seek(0)
        sound40_6.setSound(condition_list[0][39][1][1], secs=0.06, hamming=True)
        sound40_6.setVolume(0.3, log=False)
        sound40_6.seek(0)
        sound40_7.setSound(condition_list[0][39][1][2], secs=0.06, hamming=True)
        sound40_7.setVolume(0.3, log=False)
        sound40_7.seek(0)
        sound40_8.setSound(condition_list[0][39][1][3], secs=0.06, hamming=True)
        sound40_8.setVolume(0.3, log=False)
        sound40_8.seek(0)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        tar_2.setSound(target, secs=0.06, hamming=True)
        tar_2.setVolume(tarvolume, log=False)
        tar_2.seek(0)
        tar_3.setSound(target, secs=0.06, hamming=True)
        tar_3.setVolume(tarvolume, log=False)
        tar_3.seek(0)
        tar_4.setSound(target, secs=0.06, hamming=True)
        tar_4.setVolume(tarvolume, log=False)
        tar_4.seek(0)
        tar_5.setSound(target, secs=0.06, hamming=True)
        tar_5.setVolume(tarvolume, log=False)
        tar_5.seek(0)
        tar_6.setSound(target, secs=0.06, hamming=True)
        tar_6.setVolume(tarvolume, log=False)
        tar_6.seek(0)
        tar_7.setSound(target, secs=0.06, hamming=True)
        tar_7.setVolume(tarvolume, log=False)
        tar_7.seek(0)
        tar_8.setSound(target, secs=0.06, hamming=True)
        tar_8.setVolume(tarvolume, log=False)
        tar_8.seek(0)
        tar_9.setSound(target, secs=0.06, hamming=True)
        tar_9.setVolume(tarvolume, log=False)
        tar_9.seek(0)
        tar_10.setSound(target, secs=0.06, hamming=True)
        tar_10.setVolume(tarvolume, log=False)
        tar_10.seek(0)
        tar_11.setSound(target, secs=0.06, hamming=True)
        tar_11.setVolume(tarvolume, log=False)
        tar_11.seek(0)
        tar_12.setSound(target, secs=0.06, hamming=True)
        tar_12.setVolume(tarvolume, log=False)
        tar_12.seek(0)
        tar_13.setSound(target, secs=0.06, hamming=True)
        tar_13.setVolume(tarvolume, log=False)
        tar_13.seek(0)
        tar_14.setSound(target, secs=0.06, hamming=True)
        tar_14.setVolume(tarvolume, log=False)
        tar_14.seek(0)
        tar_15.setSound(target, secs=0.06, hamming=True)
        tar_15.setVolume(tarvolume, log=False)
        tar_15.seek(0)
        tar_16.setSound(target, secs=0.06, hamming=True)
        tar_16.setVolume(tarvolume, log=False)
        tar_16.seek(0)
        tar_17.setSound(target, secs=0.06, hamming=True)
        tar_17.setVolume(tarvolume, log=False)
        tar_17.seek(0)
        tar_18.setSound(target, secs=0.06, hamming=True)
        tar_18.setVolume(tarvolume, log=False)
        tar_18.seek(0)
        tar_19.setSound(target, secs=0.06, hamming=True)
        tar_19.setVolume(tarvolume, log=False)
        tar_19.seek(0)
        tar_20.setSound(target, secs=0.06, hamming=True)
        tar_20.setVolume(tarvolume, log=False)
        tar_20.seek(0)
        tar_21.setSound(target, secs=0.06, hamming=True)
        tar_21.setVolume(tarvolume, log=False)
        tar_21.seek(0)
        tar_22.setSound(target, secs=0.06, hamming=True)
        tar_22.setVolume(tarvolume, log=False)
        tar_22.seek(0)
        tar_23.setSound(target, secs=0.06, hamming=True)
        tar_23.setVolume(tarvolume, log=False)
        tar_23.seek(0)
        tar_24.setSound(target, secs=0.06, hamming=True)
        tar_24.setVolume(tarvolume, log=False)
        tar_24.seek(0)
        tar_25.setSound(target, secs=0.06, hamming=True)
        tar_25.setVolume(tarvolume, log=False)
        tar_25.seek(0)
        tar_26.setSound(target, secs=0.06, hamming=True)
        tar_26.setVolume(tarvolume, log=False)
        tar_26.seek(0)
        tar_27.setSound(target, secs=0.06, hamming=True)
        tar_27.setVolume(tarvolume, log=False)
        tar_27.seek(0)
        tar_28.setSound(target, secs=0.06, hamming=True)
        tar_28.setVolume(tarvolume, log=False)
        tar_28.seek(0)
        tar_29.setSound(target, secs=0.06, hamming=True)
        tar_29.setVolume(tarvolume, log=False)
        tar_29.seek(0)
        tar_30.setSound(target, secs=0.06, hamming=True)
        tar_30.setVolume(tarvolume, log=False)
        tar_30.seek(0)
        tar_31.setSound(target, secs=0.06, hamming=True)
        tar_31.setVolume(tarvolume, log=False)
        tar_31.seek(0)
        tar_32.setSound(target, secs=0.06, hamming=True)
        tar_32.setVolume(tarvolume, log=False)
        tar_32.seek(0)
        tar_33.setSound(target, secs=0.06, hamming=True)
        tar_33.setVolume(tarvolume, log=False)
        tar_33.seek(0)
        tar_34.setSound(target, secs=0.06, hamming=True)
        tar_34.setVolume(tarvolume, log=False)
        tar_34.seek(0)
        tar_35.setSound(target, secs=0.06, hamming=True)
        tar_35.setVolume(tarvolume, log=False)
        tar_35.seek(0)
        tar_36.setSound(target, secs=0.06, hamming=True)
        tar_36.setVolume(tarvolume, log=False)
        tar_36.seek(0)
        tar_37.setSound(target, secs=0.06, hamming=True)
        tar_37.setVolume(tarvolume, log=False)
        tar_37.seek(0)
        # keep track of which components have finished
        trialComponents = [tar, sound1, sound1_2, sound1_3, sound1_4, sound1_5, sound1_6, sound1_7, sound1_8, sound2, sound2_2, sound2_3, sound2_4, sound2_5, sound2_6, sound2_7, sound2_8, sound3, sound3_2, sound3_3, sound3_4, sound3_5, sound3_6, sound3_7, sound3_8, sound4, sound4_2, sound4_3, sound4_4, sound4_5, sound4_6, sound4_7, sound4_8, sound5, sound5_2, sound5_3, sound5_4, sound5_5, sound5_6, sound5_7, sound5_8, sound6, sound6_2, sound6_3, sound6_4, sound6_5, sound6_6, sound6_7, sound6_8, sound7, sound7_2, sound7_3, sound7_4, sound7_5, sound7_6, sound7_7, sound7_8, sound8, sound8_2, sound8_3, sound8_4, sound8_5, sound8_6, sound8_7, sound8_8, sound9, sound9_2, sound9_3, sound9_4, sound9_5, sound9_6, sound9_7, sound9_8, sound10, sound10_2, sound10_3, sound10_4, sound10_5, sound10_6, sound10_7, sound10_8, sound11, sound11_2, sound11_3, sound11_4, sound11_5, sound11_6, sound11_7, sound11_8, sound12, sound12_2, sound12_3, sound12_4, sound12_5, sound12_6, sound12_7, sound12_8, sound13, sound13_2, sound13_3, sound13_4, sound13_5, sound13_6, sound13_7, sound13_8, sound14, sound14_2, sound14_3, sound14_4, sound14_5, sound14_6, sound14_7, sound14_8, sound15, sound15_2, sound15_3, sound15_4, sound15_5, sound15_6, sound15_7, sound15_8, spund16, spund16_2, spund16_3, spund16_4, spund16_5, spund16_6, spund16_7, spund16_8, sound17, sound17_2, sound17_3, sound17_4, sound17_5, sound17_6, sound17_7, sound17_8, sound18, sound18_2, sound18_3, sound18_4, sound18_5, sound18_6, sound18_7, sound18_8, sound19, sound19_2, sound19_3, sound19_4, sound19_5, sound19_6, sound19_7, sound19_8, sound20, sound20_2, sound20_3, sound20_4, sound20_5, sound20_6, sound20_7, sound20_8, sound21, sound21_2, sound21_3, sound21_4, sound21_5, sound21_6, sound21_7, sound21_8, sound22, sound22_2, sound22_3, sound22_4, sound22_5, sound22_6, sound22_7, sound22_8, sound23, sound23_2, sound23_3, sound23_4, sound23_5, sound23_6, sound23_7, sound23_8, sound24, sound24_2, sound24_3, sound24_4, sound24_5, sound24_6, sound24_7, sound24_8, sound25, sound25_2, sound25_3, sound25_4, sound25_5, sound25_6, sound25_7, sound25_8, sound26, sound26_2, sound26_3, sound26_4, sound26_5, sound26_6, sound26_7, sound26_8, sound27, sound27_2, sound27_3, sound27_4, sound27_5, sound27_6, sound27_7, sound27_8, sound28, sound28_2, sound28_3, sound28_4, sound28_5, sound28_6, sound28_7, sound28_8, sound29, sound29_2, sound29_3, sound29_4, sound29_5, sound29_6, sound29_7, sound29_8, sound30, sound30_2, sound30_3, sound30_4, sound30_5, sound30_6, sound30_7, sound30_8, sound31, sound31_2, sound31_3, sound31_4, sound31_5, sound31_6, sound31_7, sound31_8, sound32, sound32_2, sound32_3, sound32_4, sound32_5, sound32_6, sound32_7, sound32_8, sound33, sound33_2, sound33_3, sound33_4, sound33_5, sound33_6, sound33_7, sound33_8, sound34, sound34_2, sound34_3, sound34_4, sound34_5, sound34_6, sound34_7, sound34_8, sound35, sound35_2, sound35_3, sound35_4, sound35_5, sound35_6, sound35_7, sound35_8, sound36, sound36_2, sound36_3, sound36_4, sound36_5, sound36_6, sound36_7, sound36_8, sound37, sound37_2, sound37_3, sound37_4, sound37_5, sound37_6, sound37_7, sound37_8, sound38, sound38_2, sound38_3, sound38_4, sound38_5, sound38_6, sound38_7, sound38_8, sound39, sound39_2, sound39_3, sound39_4, sound39_5, sound39_6, sound39_7, sound39_8, sound40, sound40_2, sound40_3, sound40_4, sound40_5, sound40_6, sound40_7, sound40_8, key_resp_3, tar_2, tar_3, tar_4, tar_5, tar_6, tar_7, tar_8, tar_9, tar_10, tar_11, tar_12, tar_13, tar_14, tar_15, tar_16, tar_17, tar_18, tar_19, tar_20, tar_21, tar_22, tar_23, tar_24, tar_25, tar_26, tar_27, tar_28, tar_29, tar_30, tar_31, tar_32, tar_33, tar_34, tar_35, tar_36, tar_37, polygon_2]
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
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if tar is starting this frame...
            if tar.status == NOT_STARTED and tThisFlip >= 0.62-frameTolerance:
                # keep track of start time/frame for later
                tar.frameNStart = frameN  # exact frame index
                tar.tStart = t  # local t and not account for scr refresh
                tar.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar.status = STARTED
                tar.play(when=win)  # sync with win flip
            
            # if tar is stopping this frame...
            if tar.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar.tStop = t  # not accounting for scr refresh
                    tar.frameNStop = frameN  # exact frame index
                    # update status
                    tar.status = FINISHED
                    tar.stop()
            # update tar status according to whether it's playing
            if tar.isPlaying:
                tar.status = STARTED
            elif tar.isFinished:
                tar.status = FINISHED
            
            # if sound1 is starting this frame...
            if sound1.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1.frameNStart = frameN  # exact frame index
                sound1.tStart = t  # local t and not account for scr refresh
                sound1.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1.status = STARTED
                sound1.play(when=win)  # sync with win flip
            
            # if sound1 is stopping this frame...
            if sound1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1.tStop = t  # not accounting for scr refresh
                    sound1.frameNStop = frameN  # exact frame index
                    # update status
                    sound1.status = FINISHED
                    sound1.stop()
            # update sound1 status according to whether it's playing
            if sound1.isPlaying:
                sound1.status = STARTED
            elif sound1.isFinished:
                sound1.status = FINISHED
            
            # if sound1_2 is starting this frame...
            if sound1_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_2.frameNStart = frameN  # exact frame index
                sound1_2.tStart = t  # local t and not account for scr refresh
                sound1_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_2.status = STARTED
                sound1_2.play(when=win)  # sync with win flip
            
            # if sound1_2 is stopping this frame...
            if sound1_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_2.tStop = t  # not accounting for scr refresh
                    sound1_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_2.status = FINISHED
                    sound1_2.stop()
            # update sound1_2 status according to whether it's playing
            if sound1_2.isPlaying:
                sound1_2.status = STARTED
            elif sound1_2.isFinished:
                sound1_2.status = FINISHED
            
            # if sound1_3 is starting this frame...
            if sound1_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_3.frameNStart = frameN  # exact frame index
                sound1_3.tStart = t  # local t and not account for scr refresh
                sound1_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_3.status = STARTED
                sound1_3.play(when=win)  # sync with win flip
            
            # if sound1_3 is stopping this frame...
            if sound1_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_3.tStop = t  # not accounting for scr refresh
                    sound1_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_3.status = FINISHED
                    sound1_3.stop()
            # update sound1_3 status according to whether it's playing
            if sound1_3.isPlaying:
                sound1_3.status = STARTED
            elif sound1_3.isFinished:
                sound1_3.status = FINISHED
            
            # if sound1_4 is starting this frame...
            if sound1_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_4.frameNStart = frameN  # exact frame index
                sound1_4.tStart = t  # local t and not account for scr refresh
                sound1_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_4.status = STARTED
                sound1_4.play(when=win)  # sync with win flip
            
            # if sound1_4 is stopping this frame...
            if sound1_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_4.tStop = t  # not accounting for scr refresh
                    sound1_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_4.status = FINISHED
                    sound1_4.stop()
            # update sound1_4 status according to whether it's playing
            if sound1_4.isPlaying:
                sound1_4.status = STARTED
            elif sound1_4.isFinished:
                sound1_4.status = FINISHED
            
            # if sound1_5 is starting this frame...
            if sound1_5.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_5.frameNStart = frameN  # exact frame index
                sound1_5.tStart = t  # local t and not account for scr refresh
                sound1_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_5.status = STARTED
                sound1_5.play(when=win)  # sync with win flip
            
            # if sound1_5 is stopping this frame...
            if sound1_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_5.tStop = t  # not accounting for scr refresh
                    sound1_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_5.status = FINISHED
                    sound1_5.stop()
            # update sound1_5 status according to whether it's playing
            if sound1_5.isPlaying:
                sound1_5.status = STARTED
            elif sound1_5.isFinished:
                sound1_5.status = FINISHED
            
            # if sound1_6 is starting this frame...
            if sound1_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_6.frameNStart = frameN  # exact frame index
                sound1_6.tStart = t  # local t and not account for scr refresh
                sound1_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_6.status = STARTED
                sound1_6.play(when=win)  # sync with win flip
            
            # if sound1_6 is stopping this frame...
            if sound1_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_6.tStop = t  # not accounting for scr refresh
                    sound1_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_6.status = FINISHED
                    sound1_6.stop()
            # update sound1_6 status according to whether it's playing
            if sound1_6.isPlaying:
                sound1_6.status = STARTED
            elif sound1_6.isFinished:
                sound1_6.status = FINISHED
            
            # if sound1_7 is starting this frame...
            if sound1_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_7.frameNStart = frameN  # exact frame index
                sound1_7.tStart = t  # local t and not account for scr refresh
                sound1_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_7.status = STARTED
                sound1_7.play(when=win)  # sync with win flip
            
            # if sound1_7 is stopping this frame...
            if sound1_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_7.tStop = t  # not accounting for scr refresh
                    sound1_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_7.status = FINISHED
                    sound1_7.stop()
            # update sound1_7 status according to whether it's playing
            if sound1_7.isPlaying:
                sound1_7.status = STARTED
            elif sound1_7.isFinished:
                sound1_7.status = FINISHED
            
            # if sound1_8 is starting this frame...
            if sound1_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                sound1_8.frameNStart = frameN  # exact frame index
                sound1_8.tStart = t  # local t and not account for scr refresh
                sound1_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound1_8.status = STARTED
                sound1_8.play(when=win)  # sync with win flip
            
            # if sound1_8 is stopping this frame...
            if sound1_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound1_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound1_8.tStop = t  # not accounting for scr refresh
                    sound1_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound1_8.status = FINISHED
                    sound1_8.stop()
            # update sound1_8 status according to whether it's playing
            if sound1_8.isPlaying:
                sound1_8.status = STARTED
            elif sound1_8.isFinished:
                sound1_8.status = FINISHED
            
            # if sound2 is starting this frame...
            if sound2.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2.frameNStart = frameN  # exact frame index
                sound2.tStart = t  # local t and not account for scr refresh
                sound2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2.status = STARTED
                sound2.play(when=win)  # sync with win flip
            
            # if sound2 is stopping this frame...
            if sound2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2.tStop = t  # not accounting for scr refresh
                    sound2.frameNStop = frameN  # exact frame index
                    # update status
                    sound2.status = FINISHED
                    sound2.stop()
            # update sound2 status according to whether it's playing
            if sound2.isPlaying:
                sound2.status = STARTED
            elif sound2.isFinished:
                sound2.status = FINISHED
            
            # if sound2_2 is starting this frame...
            if sound2_2.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_2.frameNStart = frameN  # exact frame index
                sound2_2.tStart = t  # local t and not account for scr refresh
                sound2_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_2.status = STARTED
                sound2_2.play(when=win)  # sync with win flip
            
            # if sound2_2 is stopping this frame...
            if sound2_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_2.tStop = t  # not accounting for scr refresh
                    sound2_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_2.status = FINISHED
                    sound2_2.stop()
            # update sound2_2 status according to whether it's playing
            if sound2_2.isPlaying:
                sound2_2.status = STARTED
            elif sound2_2.isFinished:
                sound2_2.status = FINISHED
            
            # if sound2_3 is starting this frame...
            if sound2_3.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_3.frameNStart = frameN  # exact frame index
                sound2_3.tStart = t  # local t and not account for scr refresh
                sound2_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_3.status = STARTED
                sound2_3.play(when=win)  # sync with win flip
            
            # if sound2_3 is stopping this frame...
            if sound2_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_3.tStop = t  # not accounting for scr refresh
                    sound2_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_3.status = FINISHED
                    sound2_3.stop()
            # update sound2_3 status according to whether it's playing
            if sound2_3.isPlaying:
                sound2_3.status = STARTED
            elif sound2_3.isFinished:
                sound2_3.status = FINISHED
            
            # if sound2_4 is starting this frame...
            if sound2_4.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_4.frameNStart = frameN  # exact frame index
                sound2_4.tStart = t  # local t and not account for scr refresh
                sound2_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_4.status = STARTED
                sound2_4.play(when=win)  # sync with win flip
            
            # if sound2_4 is stopping this frame...
            if sound2_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_4.tStop = t  # not accounting for scr refresh
                    sound2_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_4.status = FINISHED
                    sound2_4.stop()
            # update sound2_4 status according to whether it's playing
            if sound2_4.isPlaying:
                sound2_4.status = STARTED
            elif sound2_4.isFinished:
                sound2_4.status = FINISHED
            
            # if sound2_5 is starting this frame...
            if sound2_5.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_5.frameNStart = frameN  # exact frame index
                sound2_5.tStart = t  # local t and not account for scr refresh
                sound2_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_5.status = STARTED
                sound2_5.play(when=win)  # sync with win flip
            
            # if sound2_5 is stopping this frame...
            if sound2_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_5.tStop = t  # not accounting for scr refresh
                    sound2_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_5.status = FINISHED
                    sound2_5.stop()
            # update sound2_5 status according to whether it's playing
            if sound2_5.isPlaying:
                sound2_5.status = STARTED
            elif sound2_5.isFinished:
                sound2_5.status = FINISHED
            
            # if sound2_6 is starting this frame...
            if sound2_6.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_6.frameNStart = frameN  # exact frame index
                sound2_6.tStart = t  # local t and not account for scr refresh
                sound2_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_6.status = STARTED
                sound2_6.play(when=win)  # sync with win flip
            
            # if sound2_6 is stopping this frame...
            if sound2_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_6.tStop = t  # not accounting for scr refresh
                    sound2_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_6.status = FINISHED
                    sound2_6.stop()
            # update sound2_6 status according to whether it's playing
            if sound2_6.isPlaying:
                sound2_6.status = STARTED
            elif sound2_6.isFinished:
                sound2_6.status = FINISHED
            
            # if sound2_7 is starting this frame...
            if sound2_7.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_7.frameNStart = frameN  # exact frame index
                sound2_7.tStart = t  # local t and not account for scr refresh
                sound2_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_7.status = STARTED
                sound2_7.play(when=win)  # sync with win flip
            
            # if sound2_7 is stopping this frame...
            if sound2_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_7.tStop = t  # not accounting for scr refresh
                    sound2_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_7.status = FINISHED
                    sound2_7.stop()
            # update sound2_7 status according to whether it's playing
            if sound2_7.isPlaying:
                sound2_7.status = STARTED
            elif sound2_7.isFinished:
                sound2_7.status = FINISHED
            
            # if sound2_8 is starting this frame...
            if sound2_8.status == NOT_STARTED and tThisFlip >= starttime[0]-frameTolerance:
                # keep track of start time/frame for later
                sound2_8.frameNStart = frameN  # exact frame index
                sound2_8.tStart = t  # local t and not account for scr refresh
                sound2_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound2_8.status = STARTED
                sound2_8.play(when=win)  # sync with win flip
            
            # if sound2_8 is stopping this frame...
            if sound2_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound2_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound2_8.tStop = t  # not accounting for scr refresh
                    sound2_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound2_8.status = FINISHED
                    sound2_8.stop()
            # update sound2_8 status according to whether it's playing
            if sound2_8.isPlaying:
                sound2_8.status = STARTED
            elif sound2_8.isFinished:
                sound2_8.status = FINISHED
            
            # if sound3 is starting this frame...
            if sound3.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3.frameNStart = frameN  # exact frame index
                sound3.tStart = t  # local t and not account for scr refresh
                sound3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3.status = STARTED
                sound3.play(when=win)  # sync with win flip
            
            # if sound3 is stopping this frame...
            if sound3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3.tStop = t  # not accounting for scr refresh
                    sound3.frameNStop = frameN  # exact frame index
                    # update status
                    sound3.status = FINISHED
                    sound3.stop()
            # update sound3 status according to whether it's playing
            if sound3.isPlaying:
                sound3.status = STARTED
            elif sound3.isFinished:
                sound3.status = FINISHED
            
            # if sound3_2 is starting this frame...
            if sound3_2.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_2.frameNStart = frameN  # exact frame index
                sound3_2.tStart = t  # local t and not account for scr refresh
                sound3_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_2.status = STARTED
                sound3_2.play(when=win)  # sync with win flip
            
            # if sound3_2 is stopping this frame...
            if sound3_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_2.tStop = t  # not accounting for scr refresh
                    sound3_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_2.status = FINISHED
                    sound3_2.stop()
            # update sound3_2 status according to whether it's playing
            if sound3_2.isPlaying:
                sound3_2.status = STARTED
            elif sound3_2.isFinished:
                sound3_2.status = FINISHED
            
            # if sound3_3 is starting this frame...
            if sound3_3.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_3.frameNStart = frameN  # exact frame index
                sound3_3.tStart = t  # local t and not account for scr refresh
                sound3_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_3.status = STARTED
                sound3_3.play(when=win)  # sync with win flip
            
            # if sound3_3 is stopping this frame...
            if sound3_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_3.tStop = t  # not accounting for scr refresh
                    sound3_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_3.status = FINISHED
                    sound3_3.stop()
            # update sound3_3 status according to whether it's playing
            if sound3_3.isPlaying:
                sound3_3.status = STARTED
            elif sound3_3.isFinished:
                sound3_3.status = FINISHED
            
            # if sound3_4 is starting this frame...
            if sound3_4.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_4.frameNStart = frameN  # exact frame index
                sound3_4.tStart = t  # local t and not account for scr refresh
                sound3_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_4.status = STARTED
                sound3_4.play(when=win)  # sync with win flip
            
            # if sound3_4 is stopping this frame...
            if sound3_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_4.tStop = t  # not accounting for scr refresh
                    sound3_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_4.status = FINISHED
                    sound3_4.stop()
            # update sound3_4 status according to whether it's playing
            if sound3_4.isPlaying:
                sound3_4.status = STARTED
            elif sound3_4.isFinished:
                sound3_4.status = FINISHED
            
            # if sound3_5 is starting this frame...
            if sound3_5.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_5.frameNStart = frameN  # exact frame index
                sound3_5.tStart = t  # local t and not account for scr refresh
                sound3_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_5.status = STARTED
                sound3_5.play(when=win)  # sync with win flip
            
            # if sound3_5 is stopping this frame...
            if sound3_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_5.tStop = t  # not accounting for scr refresh
                    sound3_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_5.status = FINISHED
                    sound3_5.stop()
            # update sound3_5 status according to whether it's playing
            if sound3_5.isPlaying:
                sound3_5.status = STARTED
            elif sound3_5.isFinished:
                sound3_5.status = FINISHED
            
            # if sound3_6 is starting this frame...
            if sound3_6.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_6.frameNStart = frameN  # exact frame index
                sound3_6.tStart = t  # local t and not account for scr refresh
                sound3_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_6.status = STARTED
                sound3_6.play(when=win)  # sync with win flip
            
            # if sound3_6 is stopping this frame...
            if sound3_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_6.tStop = t  # not accounting for scr refresh
                    sound3_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_6.status = FINISHED
                    sound3_6.stop()
            # update sound3_6 status according to whether it's playing
            if sound3_6.isPlaying:
                sound3_6.status = STARTED
            elif sound3_6.isFinished:
                sound3_6.status = FINISHED
            
            # if sound3_7 is starting this frame...
            if sound3_7.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_7.frameNStart = frameN  # exact frame index
                sound3_7.tStart = t  # local t and not account for scr refresh
                sound3_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_7.status = STARTED
                sound3_7.play(when=win)  # sync with win flip
            
            # if sound3_7 is stopping this frame...
            if sound3_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_7.tStop = t  # not accounting for scr refresh
                    sound3_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_7.status = FINISHED
                    sound3_7.stop()
            # update sound3_7 status according to whether it's playing
            if sound3_7.isPlaying:
                sound3_7.status = STARTED
            elif sound3_7.isFinished:
                sound3_7.status = FINISHED
            
            # if sound3_8 is starting this frame...
            if sound3_8.status == NOT_STARTED and tThisFlip >= starttime[1]-frameTolerance:
                # keep track of start time/frame for later
                sound3_8.frameNStart = frameN  # exact frame index
                sound3_8.tStart = t  # local t and not account for scr refresh
                sound3_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound3_8.status = STARTED
                sound3_8.play(when=win)  # sync with win flip
            
            # if sound3_8 is stopping this frame...
            if sound3_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound3_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound3_8.tStop = t  # not accounting for scr refresh
                    sound3_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound3_8.status = FINISHED
                    sound3_8.stop()
            # update sound3_8 status according to whether it's playing
            if sound3_8.isPlaying:
                sound3_8.status = STARTED
            elif sound3_8.isFinished:
                sound3_8.status = FINISHED
            
            # if sound4 is starting this frame...
            if sound4.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4.frameNStart = frameN  # exact frame index
                sound4.tStart = t  # local t and not account for scr refresh
                sound4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4.status = STARTED
                sound4.play(when=win)  # sync with win flip
            
            # if sound4 is stopping this frame...
            if sound4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4.tStop = t  # not accounting for scr refresh
                    sound4.frameNStop = frameN  # exact frame index
                    # update status
                    sound4.status = FINISHED
                    sound4.stop()
            # update sound4 status according to whether it's playing
            if sound4.isPlaying:
                sound4.status = STARTED
            elif sound4.isFinished:
                sound4.status = FINISHED
            
            # if sound4_2 is starting this frame...
            if sound4_2.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_2.frameNStart = frameN  # exact frame index
                sound4_2.tStart = t  # local t and not account for scr refresh
                sound4_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_2.status = STARTED
                sound4_2.play(when=win)  # sync with win flip
            
            # if sound4_2 is stopping this frame...
            if sound4_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_2.tStop = t  # not accounting for scr refresh
                    sound4_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_2.status = FINISHED
                    sound4_2.stop()
            # update sound4_2 status according to whether it's playing
            if sound4_2.isPlaying:
                sound4_2.status = STARTED
            elif sound4_2.isFinished:
                sound4_2.status = FINISHED
            
            # if sound4_3 is starting this frame...
            if sound4_3.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_3.frameNStart = frameN  # exact frame index
                sound4_3.tStart = t  # local t and not account for scr refresh
                sound4_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_3.status = STARTED
                sound4_3.play(when=win)  # sync with win flip
            
            # if sound4_3 is stopping this frame...
            if sound4_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_3.tStop = t  # not accounting for scr refresh
                    sound4_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_3.status = FINISHED
                    sound4_3.stop()
            # update sound4_3 status according to whether it's playing
            if sound4_3.isPlaying:
                sound4_3.status = STARTED
            elif sound4_3.isFinished:
                sound4_3.status = FINISHED
            
            # if sound4_4 is starting this frame...
            if sound4_4.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_4.frameNStart = frameN  # exact frame index
                sound4_4.tStart = t  # local t and not account for scr refresh
                sound4_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_4.status = STARTED
                sound4_4.play(when=win)  # sync with win flip
            
            # if sound4_4 is stopping this frame...
            if sound4_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_4.tStop = t  # not accounting for scr refresh
                    sound4_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_4.status = FINISHED
                    sound4_4.stop()
            # update sound4_4 status according to whether it's playing
            if sound4_4.isPlaying:
                sound4_4.status = STARTED
            elif sound4_4.isFinished:
                sound4_4.status = FINISHED
            
            # if sound4_5 is starting this frame...
            if sound4_5.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_5.frameNStart = frameN  # exact frame index
                sound4_5.tStart = t  # local t and not account for scr refresh
                sound4_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_5.status = STARTED
                sound4_5.play(when=win)  # sync with win flip
            
            # if sound4_5 is stopping this frame...
            if sound4_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_5.tStop = t  # not accounting for scr refresh
                    sound4_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_5.status = FINISHED
                    sound4_5.stop()
            # update sound4_5 status according to whether it's playing
            if sound4_5.isPlaying:
                sound4_5.status = STARTED
            elif sound4_5.isFinished:
                sound4_5.status = FINISHED
            
            # if sound4_6 is starting this frame...
            if sound4_6.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_6.frameNStart = frameN  # exact frame index
                sound4_6.tStart = t  # local t and not account for scr refresh
                sound4_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_6.status = STARTED
                sound4_6.play(when=win)  # sync with win flip
            
            # if sound4_6 is stopping this frame...
            if sound4_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_6.tStop = t  # not accounting for scr refresh
                    sound4_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_6.status = FINISHED
                    sound4_6.stop()
            # update sound4_6 status according to whether it's playing
            if sound4_6.isPlaying:
                sound4_6.status = STARTED
            elif sound4_6.isFinished:
                sound4_6.status = FINISHED
            
            # if sound4_7 is starting this frame...
            if sound4_7.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_7.frameNStart = frameN  # exact frame index
                sound4_7.tStart = t  # local t and not account for scr refresh
                sound4_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_7.status = STARTED
                sound4_7.play(when=win)  # sync with win flip
            
            # if sound4_7 is stopping this frame...
            if sound4_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_7.tStop = t  # not accounting for scr refresh
                    sound4_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_7.status = FINISHED
                    sound4_7.stop()
            # update sound4_7 status according to whether it's playing
            if sound4_7.isPlaying:
                sound4_7.status = STARTED
            elif sound4_7.isFinished:
                sound4_7.status = FINISHED
            
            # if sound4_8 is starting this frame...
            if sound4_8.status == NOT_STARTED and tThisFlip >= starttime[2]-frameTolerance:
                # keep track of start time/frame for later
                sound4_8.frameNStart = frameN  # exact frame index
                sound4_8.tStart = t  # local t and not account for scr refresh
                sound4_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound4_8.status = STARTED
                sound4_8.play(when=win)  # sync with win flip
            
            # if sound4_8 is stopping this frame...
            if sound4_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound4_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound4_8.tStop = t  # not accounting for scr refresh
                    sound4_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound4_8.status = FINISHED
                    sound4_8.stop()
            # update sound4_8 status according to whether it's playing
            if sound4_8.isPlaying:
                sound4_8.status = STARTED
            elif sound4_8.isFinished:
                sound4_8.status = FINISHED
            
            # if sound5 is starting this frame...
            if sound5.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5.frameNStart = frameN  # exact frame index
                sound5.tStart = t  # local t and not account for scr refresh
                sound5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5.status = STARTED
                sound5.play(when=win)  # sync with win flip
            
            # if sound5 is stopping this frame...
            if sound5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5.tStop = t  # not accounting for scr refresh
                    sound5.frameNStop = frameN  # exact frame index
                    # update status
                    sound5.status = FINISHED
                    sound5.stop()
            # update sound5 status according to whether it's playing
            if sound5.isPlaying:
                sound5.status = STARTED
            elif sound5.isFinished:
                sound5.status = FINISHED
            
            # if sound5_2 is starting this frame...
            if sound5_2.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_2.frameNStart = frameN  # exact frame index
                sound5_2.tStart = t  # local t and not account for scr refresh
                sound5_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_2.status = STARTED
                sound5_2.play(when=win)  # sync with win flip
            
            # if sound5_2 is stopping this frame...
            if sound5_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_2.tStop = t  # not accounting for scr refresh
                    sound5_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_2.status = FINISHED
                    sound5_2.stop()
            # update sound5_2 status according to whether it's playing
            if sound5_2.isPlaying:
                sound5_2.status = STARTED
            elif sound5_2.isFinished:
                sound5_2.status = FINISHED
            
            # if sound5_3 is starting this frame...
            if sound5_3.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_3.frameNStart = frameN  # exact frame index
                sound5_3.tStart = t  # local t and not account for scr refresh
                sound5_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_3.status = STARTED
                sound5_3.play(when=win)  # sync with win flip
            
            # if sound5_3 is stopping this frame...
            if sound5_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_3.tStop = t  # not accounting for scr refresh
                    sound5_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_3.status = FINISHED
                    sound5_3.stop()
            # update sound5_3 status according to whether it's playing
            if sound5_3.isPlaying:
                sound5_3.status = STARTED
            elif sound5_3.isFinished:
                sound5_3.status = FINISHED
            
            # if sound5_4 is starting this frame...
            if sound5_4.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_4.frameNStart = frameN  # exact frame index
                sound5_4.tStart = t  # local t and not account for scr refresh
                sound5_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_4.status = STARTED
                sound5_4.play(when=win)  # sync with win flip
            
            # if sound5_4 is stopping this frame...
            if sound5_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_4.tStop = t  # not accounting for scr refresh
                    sound5_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_4.status = FINISHED
                    sound5_4.stop()
            # update sound5_4 status according to whether it's playing
            if sound5_4.isPlaying:
                sound5_4.status = STARTED
            elif sound5_4.isFinished:
                sound5_4.status = FINISHED
            
            # if sound5_5 is starting this frame...
            if sound5_5.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_5.frameNStart = frameN  # exact frame index
                sound5_5.tStart = t  # local t and not account for scr refresh
                sound5_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_5.status = STARTED
                sound5_5.play(when=win)  # sync with win flip
            
            # if sound5_5 is stopping this frame...
            if sound5_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_5.tStop = t  # not accounting for scr refresh
                    sound5_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_5.status = FINISHED
                    sound5_5.stop()
            # update sound5_5 status according to whether it's playing
            if sound5_5.isPlaying:
                sound5_5.status = STARTED
            elif sound5_5.isFinished:
                sound5_5.status = FINISHED
            
            # if sound5_6 is starting this frame...
            if sound5_6.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_6.frameNStart = frameN  # exact frame index
                sound5_6.tStart = t  # local t and not account for scr refresh
                sound5_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_6.status = STARTED
                sound5_6.play(when=win)  # sync with win flip
            
            # if sound5_6 is stopping this frame...
            if sound5_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_6.tStop = t  # not accounting for scr refresh
                    sound5_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_6.status = FINISHED
                    sound5_6.stop()
            # update sound5_6 status according to whether it's playing
            if sound5_6.isPlaying:
                sound5_6.status = STARTED
            elif sound5_6.isFinished:
                sound5_6.status = FINISHED
            
            # if sound5_7 is starting this frame...
            if sound5_7.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_7.frameNStart = frameN  # exact frame index
                sound5_7.tStart = t  # local t and not account for scr refresh
                sound5_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_7.status = STARTED
                sound5_7.play(when=win)  # sync with win flip
            
            # if sound5_7 is stopping this frame...
            if sound5_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_7.tStop = t  # not accounting for scr refresh
                    sound5_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_7.status = FINISHED
                    sound5_7.stop()
            # update sound5_7 status according to whether it's playing
            if sound5_7.isPlaying:
                sound5_7.status = STARTED
            elif sound5_7.isFinished:
                sound5_7.status = FINISHED
            
            # if sound5_8 is starting this frame...
            if sound5_8.status == NOT_STARTED and tThisFlip >= starttime[3]-frameTolerance:
                # keep track of start time/frame for later
                sound5_8.frameNStart = frameN  # exact frame index
                sound5_8.tStart = t  # local t and not account for scr refresh
                sound5_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound5_8.status = STARTED
                sound5_8.play(when=win)  # sync with win flip
            
            # if sound5_8 is stopping this frame...
            if sound5_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound5_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound5_8.tStop = t  # not accounting for scr refresh
                    sound5_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound5_8.status = FINISHED
                    sound5_8.stop()
            # update sound5_8 status according to whether it's playing
            if sound5_8.isPlaying:
                sound5_8.status = STARTED
            elif sound5_8.isFinished:
                sound5_8.status = FINISHED
            
            # if sound6 is starting this frame...
            if sound6.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6.frameNStart = frameN  # exact frame index
                sound6.tStart = t  # local t and not account for scr refresh
                sound6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6.status = STARTED
                sound6.play(when=win)  # sync with win flip
            
            # if sound6 is stopping this frame...
            if sound6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6.tStop = t  # not accounting for scr refresh
                    sound6.frameNStop = frameN  # exact frame index
                    # update status
                    sound6.status = FINISHED
                    sound6.stop()
            # update sound6 status according to whether it's playing
            if sound6.isPlaying:
                sound6.status = STARTED
            elif sound6.isFinished:
                sound6.status = FINISHED
            
            # if sound6_2 is starting this frame...
            if sound6_2.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_2.frameNStart = frameN  # exact frame index
                sound6_2.tStart = t  # local t and not account for scr refresh
                sound6_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_2.status = STARTED
                sound6_2.play(when=win)  # sync with win flip
            
            # if sound6_2 is stopping this frame...
            if sound6_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_2.tStop = t  # not accounting for scr refresh
                    sound6_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_2.status = FINISHED
                    sound6_2.stop()
            # update sound6_2 status according to whether it's playing
            if sound6_2.isPlaying:
                sound6_2.status = STARTED
            elif sound6_2.isFinished:
                sound6_2.status = FINISHED
            
            # if sound6_3 is starting this frame...
            if sound6_3.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_3.frameNStart = frameN  # exact frame index
                sound6_3.tStart = t  # local t and not account for scr refresh
                sound6_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_3.status = STARTED
                sound6_3.play(when=win)  # sync with win flip
            
            # if sound6_3 is stopping this frame...
            if sound6_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_3.tStop = t  # not accounting for scr refresh
                    sound6_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_3.status = FINISHED
                    sound6_3.stop()
            # update sound6_3 status according to whether it's playing
            if sound6_3.isPlaying:
                sound6_3.status = STARTED
            elif sound6_3.isFinished:
                sound6_3.status = FINISHED
            
            # if sound6_4 is starting this frame...
            if sound6_4.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_4.frameNStart = frameN  # exact frame index
                sound6_4.tStart = t  # local t and not account for scr refresh
                sound6_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_4.status = STARTED
                sound6_4.play(when=win)  # sync with win flip
            
            # if sound6_4 is stopping this frame...
            if sound6_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_4.tStop = t  # not accounting for scr refresh
                    sound6_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_4.status = FINISHED
                    sound6_4.stop()
            # update sound6_4 status according to whether it's playing
            if sound6_4.isPlaying:
                sound6_4.status = STARTED
            elif sound6_4.isFinished:
                sound6_4.status = FINISHED
            
            # if sound6_5 is starting this frame...
            if sound6_5.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_5.frameNStart = frameN  # exact frame index
                sound6_5.tStart = t  # local t and not account for scr refresh
                sound6_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_5.status = STARTED
                sound6_5.play(when=win)  # sync with win flip
            
            # if sound6_5 is stopping this frame...
            if sound6_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_5.tStop = t  # not accounting for scr refresh
                    sound6_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_5.status = FINISHED
                    sound6_5.stop()
            # update sound6_5 status according to whether it's playing
            if sound6_5.isPlaying:
                sound6_5.status = STARTED
            elif sound6_5.isFinished:
                sound6_5.status = FINISHED
            
            # if sound6_6 is starting this frame...
            if sound6_6.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_6.frameNStart = frameN  # exact frame index
                sound6_6.tStart = t  # local t and not account for scr refresh
                sound6_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_6.status = STARTED
                sound6_6.play(when=win)  # sync with win flip
            
            # if sound6_6 is stopping this frame...
            if sound6_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_6.tStop = t  # not accounting for scr refresh
                    sound6_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_6.status = FINISHED
                    sound6_6.stop()
            # update sound6_6 status according to whether it's playing
            if sound6_6.isPlaying:
                sound6_6.status = STARTED
            elif sound6_6.isFinished:
                sound6_6.status = FINISHED
            
            # if sound6_7 is starting this frame...
            if sound6_7.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_7.frameNStart = frameN  # exact frame index
                sound6_7.tStart = t  # local t and not account for scr refresh
                sound6_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_7.status = STARTED
                sound6_7.play(when=win)  # sync with win flip
            
            # if sound6_7 is stopping this frame...
            if sound6_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_7.tStop = t  # not accounting for scr refresh
                    sound6_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_7.status = FINISHED
                    sound6_7.stop()
            # update sound6_7 status according to whether it's playing
            if sound6_7.isPlaying:
                sound6_7.status = STARTED
            elif sound6_7.isFinished:
                sound6_7.status = FINISHED
            
            # if sound6_8 is starting this frame...
            if sound6_8.status == NOT_STARTED and tThisFlip >= starttime[4]-frameTolerance:
                # keep track of start time/frame for later
                sound6_8.frameNStart = frameN  # exact frame index
                sound6_8.tStart = t  # local t and not account for scr refresh
                sound6_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound6_8.status = STARTED
                sound6_8.play(when=win)  # sync with win flip
            
            # if sound6_8 is stopping this frame...
            if sound6_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound6_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound6_8.tStop = t  # not accounting for scr refresh
                    sound6_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound6_8.status = FINISHED
                    sound6_8.stop()
            # update sound6_8 status according to whether it's playing
            if sound6_8.isPlaying:
                sound6_8.status = STARTED
            elif sound6_8.isFinished:
                sound6_8.status = FINISHED
            
            # if sound7 is starting this frame...
            if sound7.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7.frameNStart = frameN  # exact frame index
                sound7.tStart = t  # local t and not account for scr refresh
                sound7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7.status = STARTED
                sound7.play(when=win)  # sync with win flip
            
            # if sound7 is stopping this frame...
            if sound7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7.tStop = t  # not accounting for scr refresh
                    sound7.frameNStop = frameN  # exact frame index
                    # update status
                    sound7.status = FINISHED
                    sound7.stop()
            # update sound7 status according to whether it's playing
            if sound7.isPlaying:
                sound7.status = STARTED
            elif sound7.isFinished:
                sound7.status = FINISHED
            
            # if sound7_2 is starting this frame...
            if sound7_2.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_2.frameNStart = frameN  # exact frame index
                sound7_2.tStart = t  # local t and not account for scr refresh
                sound7_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_2.status = STARTED
                sound7_2.play(when=win)  # sync with win flip
            
            # if sound7_2 is stopping this frame...
            if sound7_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_2.tStop = t  # not accounting for scr refresh
                    sound7_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_2.status = FINISHED
                    sound7_2.stop()
            # update sound7_2 status according to whether it's playing
            if sound7_2.isPlaying:
                sound7_2.status = STARTED
            elif sound7_2.isFinished:
                sound7_2.status = FINISHED
            
            # if sound7_3 is starting this frame...
            if sound7_3.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_3.frameNStart = frameN  # exact frame index
                sound7_3.tStart = t  # local t and not account for scr refresh
                sound7_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_3.status = STARTED
                sound7_3.play(when=win)  # sync with win flip
            
            # if sound7_3 is stopping this frame...
            if sound7_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_3.tStop = t  # not accounting for scr refresh
                    sound7_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_3.status = FINISHED
                    sound7_3.stop()
            # update sound7_3 status according to whether it's playing
            if sound7_3.isPlaying:
                sound7_3.status = STARTED
            elif sound7_3.isFinished:
                sound7_3.status = FINISHED
            
            # if sound7_4 is starting this frame...
            if sound7_4.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_4.frameNStart = frameN  # exact frame index
                sound7_4.tStart = t  # local t and not account for scr refresh
                sound7_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_4.status = STARTED
                sound7_4.play(when=win)  # sync with win flip
            
            # if sound7_4 is stopping this frame...
            if sound7_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_4.tStop = t  # not accounting for scr refresh
                    sound7_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_4.status = FINISHED
                    sound7_4.stop()
            # update sound7_4 status according to whether it's playing
            if sound7_4.isPlaying:
                sound7_4.status = STARTED
            elif sound7_4.isFinished:
                sound7_4.status = FINISHED
            
            # if sound7_5 is starting this frame...
            if sound7_5.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_5.frameNStart = frameN  # exact frame index
                sound7_5.tStart = t  # local t and not account for scr refresh
                sound7_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_5.status = STARTED
                sound7_5.play(when=win)  # sync with win flip
            
            # if sound7_5 is stopping this frame...
            if sound7_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_5.tStop = t  # not accounting for scr refresh
                    sound7_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_5.status = FINISHED
                    sound7_5.stop()
            # update sound7_5 status according to whether it's playing
            if sound7_5.isPlaying:
                sound7_5.status = STARTED
            elif sound7_5.isFinished:
                sound7_5.status = FINISHED
            
            # if sound7_6 is starting this frame...
            if sound7_6.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_6.frameNStart = frameN  # exact frame index
                sound7_6.tStart = t  # local t and not account for scr refresh
                sound7_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_6.status = STARTED
                sound7_6.play(when=win)  # sync with win flip
            
            # if sound7_6 is stopping this frame...
            if sound7_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_6.tStop = t  # not accounting for scr refresh
                    sound7_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_6.status = FINISHED
                    sound7_6.stop()
            # update sound7_6 status according to whether it's playing
            if sound7_6.isPlaying:
                sound7_6.status = STARTED
            elif sound7_6.isFinished:
                sound7_6.status = FINISHED
            
            # if sound7_7 is starting this frame...
            if sound7_7.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_7.frameNStart = frameN  # exact frame index
                sound7_7.tStart = t  # local t and not account for scr refresh
                sound7_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_7.status = STARTED
                sound7_7.play(when=win)  # sync with win flip
            
            # if sound7_7 is stopping this frame...
            if sound7_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_7.tStop = t  # not accounting for scr refresh
                    sound7_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_7.status = FINISHED
                    sound7_7.stop()
            # update sound7_7 status according to whether it's playing
            if sound7_7.isPlaying:
                sound7_7.status = STARTED
            elif sound7_7.isFinished:
                sound7_7.status = FINISHED
            
            # if sound7_8 is starting this frame...
            if sound7_8.status == NOT_STARTED and tThisFlip >= starttime[5]-frameTolerance:
                # keep track of start time/frame for later
                sound7_8.frameNStart = frameN  # exact frame index
                sound7_8.tStart = t  # local t and not account for scr refresh
                sound7_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound7_8.status = STARTED
                sound7_8.play(when=win)  # sync with win flip
            
            # if sound7_8 is stopping this frame...
            if sound7_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound7_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound7_8.tStop = t  # not accounting for scr refresh
                    sound7_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound7_8.status = FINISHED
                    sound7_8.stop()
            # update sound7_8 status according to whether it's playing
            if sound7_8.isPlaying:
                sound7_8.status = STARTED
            elif sound7_8.isFinished:
                sound7_8.status = FINISHED
            
            # if sound8 is starting this frame...
            if sound8.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8.frameNStart = frameN  # exact frame index
                sound8.tStart = t  # local t and not account for scr refresh
                sound8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8.status = STARTED
                sound8.play(when=win)  # sync with win flip
            
            # if sound8 is stopping this frame...
            if sound8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8.tStop = t  # not accounting for scr refresh
                    sound8.frameNStop = frameN  # exact frame index
                    # update status
                    sound8.status = FINISHED
                    sound8.stop()
            # update sound8 status according to whether it's playing
            if sound8.isPlaying:
                sound8.status = STARTED
            elif sound8.isFinished:
                sound8.status = FINISHED
            
            # if sound8_2 is starting this frame...
            if sound8_2.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_2.frameNStart = frameN  # exact frame index
                sound8_2.tStart = t  # local t and not account for scr refresh
                sound8_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_2.status = STARTED
                sound8_2.play(when=win)  # sync with win flip
            
            # if sound8_2 is stopping this frame...
            if sound8_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_2.tStop = t  # not accounting for scr refresh
                    sound8_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_2.status = FINISHED
                    sound8_2.stop()
            # update sound8_2 status according to whether it's playing
            if sound8_2.isPlaying:
                sound8_2.status = STARTED
            elif sound8_2.isFinished:
                sound8_2.status = FINISHED
            
            # if sound8_3 is starting this frame...
            if sound8_3.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_3.frameNStart = frameN  # exact frame index
                sound8_3.tStart = t  # local t and not account for scr refresh
                sound8_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_3.status = STARTED
                sound8_3.play(when=win)  # sync with win flip
            
            # if sound8_3 is stopping this frame...
            if sound8_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_3.tStop = t  # not accounting for scr refresh
                    sound8_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_3.status = FINISHED
                    sound8_3.stop()
            # update sound8_3 status according to whether it's playing
            if sound8_3.isPlaying:
                sound8_3.status = STARTED
            elif sound8_3.isFinished:
                sound8_3.status = FINISHED
            
            # if sound8_4 is starting this frame...
            if sound8_4.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_4.frameNStart = frameN  # exact frame index
                sound8_4.tStart = t  # local t and not account for scr refresh
                sound8_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_4.status = STARTED
                sound8_4.play(when=win)  # sync with win flip
            
            # if sound8_4 is stopping this frame...
            if sound8_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_4.tStop = t  # not accounting for scr refresh
                    sound8_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_4.status = FINISHED
                    sound8_4.stop()
            # update sound8_4 status according to whether it's playing
            if sound8_4.isPlaying:
                sound8_4.status = STARTED
            elif sound8_4.isFinished:
                sound8_4.status = FINISHED
            
            # if sound8_5 is starting this frame...
            if sound8_5.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_5.frameNStart = frameN  # exact frame index
                sound8_5.tStart = t  # local t and not account for scr refresh
                sound8_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_5.status = STARTED
                sound8_5.play(when=win)  # sync with win flip
            
            # if sound8_5 is stopping this frame...
            if sound8_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_5.tStop = t  # not accounting for scr refresh
                    sound8_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_5.status = FINISHED
                    sound8_5.stop()
            # update sound8_5 status according to whether it's playing
            if sound8_5.isPlaying:
                sound8_5.status = STARTED
            elif sound8_5.isFinished:
                sound8_5.status = FINISHED
            
            # if sound8_6 is starting this frame...
            if sound8_6.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_6.frameNStart = frameN  # exact frame index
                sound8_6.tStart = t  # local t and not account for scr refresh
                sound8_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_6.status = STARTED
                sound8_6.play(when=win)  # sync with win flip
            
            # if sound8_6 is stopping this frame...
            if sound8_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_6.tStop = t  # not accounting for scr refresh
                    sound8_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_6.status = FINISHED
                    sound8_6.stop()
            # update sound8_6 status according to whether it's playing
            if sound8_6.isPlaying:
                sound8_6.status = STARTED
            elif sound8_6.isFinished:
                sound8_6.status = FINISHED
            
            # if sound8_7 is starting this frame...
            if sound8_7.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_7.frameNStart = frameN  # exact frame index
                sound8_7.tStart = t  # local t and not account for scr refresh
                sound8_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_7.status = STARTED
                sound8_7.play(when=win)  # sync with win flip
            
            # if sound8_7 is stopping this frame...
            if sound8_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_7.tStop = t  # not accounting for scr refresh
                    sound8_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_7.status = FINISHED
                    sound8_7.stop()
            # update sound8_7 status according to whether it's playing
            if sound8_7.isPlaying:
                sound8_7.status = STARTED
            elif sound8_7.isFinished:
                sound8_7.status = FINISHED
            
            # if sound8_8 is starting this frame...
            if sound8_8.status == NOT_STARTED and tThisFlip >= starttime[6]-frameTolerance:
                # keep track of start time/frame for later
                sound8_8.frameNStart = frameN  # exact frame index
                sound8_8.tStart = t  # local t and not account for scr refresh
                sound8_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound8_8.status = STARTED
                sound8_8.play(when=win)  # sync with win flip
            
            # if sound8_8 is stopping this frame...
            if sound8_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound8_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound8_8.tStop = t  # not accounting for scr refresh
                    sound8_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound8_8.status = FINISHED
                    sound8_8.stop()
            # update sound8_8 status according to whether it's playing
            if sound8_8.isPlaying:
                sound8_8.status = STARTED
            elif sound8_8.isFinished:
                sound8_8.status = FINISHED
            
            # if sound9 is starting this frame...
            if sound9.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9.frameNStart = frameN  # exact frame index
                sound9.tStart = t  # local t and not account for scr refresh
                sound9.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9.status = STARTED
                sound9.play(when=win)  # sync with win flip
            
            # if sound9 is stopping this frame...
            if sound9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9.tStop = t  # not accounting for scr refresh
                    sound9.frameNStop = frameN  # exact frame index
                    # update status
                    sound9.status = FINISHED
                    sound9.stop()
            # update sound9 status according to whether it's playing
            if sound9.isPlaying:
                sound9.status = STARTED
            elif sound9.isFinished:
                sound9.status = FINISHED
            
            # if sound9_2 is starting this frame...
            if sound9_2.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_2.frameNStart = frameN  # exact frame index
                sound9_2.tStart = t  # local t and not account for scr refresh
                sound9_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_2.status = STARTED
                sound9_2.play(when=win)  # sync with win flip
            
            # if sound9_2 is stopping this frame...
            if sound9_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_2.tStop = t  # not accounting for scr refresh
                    sound9_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_2.status = FINISHED
                    sound9_2.stop()
            # update sound9_2 status according to whether it's playing
            if sound9_2.isPlaying:
                sound9_2.status = STARTED
            elif sound9_2.isFinished:
                sound9_2.status = FINISHED
            
            # if sound9_3 is starting this frame...
            if sound9_3.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_3.frameNStart = frameN  # exact frame index
                sound9_3.tStart = t  # local t and not account for scr refresh
                sound9_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_3.status = STARTED
                sound9_3.play(when=win)  # sync with win flip
            
            # if sound9_3 is stopping this frame...
            if sound9_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_3.tStop = t  # not accounting for scr refresh
                    sound9_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_3.status = FINISHED
                    sound9_3.stop()
            # update sound9_3 status according to whether it's playing
            if sound9_3.isPlaying:
                sound9_3.status = STARTED
            elif sound9_3.isFinished:
                sound9_3.status = FINISHED
            
            # if sound9_4 is starting this frame...
            if sound9_4.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_4.frameNStart = frameN  # exact frame index
                sound9_4.tStart = t  # local t and not account for scr refresh
                sound9_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_4.status = STARTED
                sound9_4.play(when=win)  # sync with win flip
            
            # if sound9_4 is stopping this frame...
            if sound9_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_4.tStop = t  # not accounting for scr refresh
                    sound9_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_4.status = FINISHED
                    sound9_4.stop()
            # update sound9_4 status according to whether it's playing
            if sound9_4.isPlaying:
                sound9_4.status = STARTED
            elif sound9_4.isFinished:
                sound9_4.status = FINISHED
            
            # if sound9_5 is starting this frame...
            if sound9_5.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_5.frameNStart = frameN  # exact frame index
                sound9_5.tStart = t  # local t and not account for scr refresh
                sound9_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_5.status = STARTED
                sound9_5.play(when=win)  # sync with win flip
            
            # if sound9_5 is stopping this frame...
            if sound9_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_5.tStop = t  # not accounting for scr refresh
                    sound9_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_5.status = FINISHED
                    sound9_5.stop()
            # update sound9_5 status according to whether it's playing
            if sound9_5.isPlaying:
                sound9_5.status = STARTED
            elif sound9_5.isFinished:
                sound9_5.status = FINISHED
            
            # if sound9_6 is starting this frame...
            if sound9_6.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_6.frameNStart = frameN  # exact frame index
                sound9_6.tStart = t  # local t and not account for scr refresh
                sound9_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_6.status = STARTED
                sound9_6.play(when=win)  # sync with win flip
            
            # if sound9_6 is stopping this frame...
            if sound9_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_6.tStop = t  # not accounting for scr refresh
                    sound9_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_6.status = FINISHED
                    sound9_6.stop()
            # update sound9_6 status according to whether it's playing
            if sound9_6.isPlaying:
                sound9_6.status = STARTED
            elif sound9_6.isFinished:
                sound9_6.status = FINISHED
            
            # if sound9_7 is starting this frame...
            if sound9_7.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_7.frameNStart = frameN  # exact frame index
                sound9_7.tStart = t  # local t and not account for scr refresh
                sound9_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_7.status = STARTED
                sound9_7.play(when=win)  # sync with win flip
            
            # if sound9_7 is stopping this frame...
            if sound9_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_7.tStop = t  # not accounting for scr refresh
                    sound9_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_7.status = FINISHED
                    sound9_7.stop()
            # update sound9_7 status according to whether it's playing
            if sound9_7.isPlaying:
                sound9_7.status = STARTED
            elif sound9_7.isFinished:
                sound9_7.status = FINISHED
            
            # if sound9_8 is starting this frame...
            if sound9_8.status == NOT_STARTED and tThisFlip >= starttime[7]-frameTolerance:
                # keep track of start time/frame for later
                sound9_8.frameNStart = frameN  # exact frame index
                sound9_8.tStart = t  # local t and not account for scr refresh
                sound9_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound9_8.status = STARTED
                sound9_8.play(when=win)  # sync with win flip
            
            # if sound9_8 is stopping this frame...
            if sound9_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound9_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound9_8.tStop = t  # not accounting for scr refresh
                    sound9_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound9_8.status = FINISHED
                    sound9_8.stop()
            # update sound9_8 status according to whether it's playing
            if sound9_8.isPlaying:
                sound9_8.status = STARTED
            elif sound9_8.isFinished:
                sound9_8.status = FINISHED
            
            # if sound10 is starting this frame...
            if sound10.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10.frameNStart = frameN  # exact frame index
                sound10.tStart = t  # local t and not account for scr refresh
                sound10.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10.status = STARTED
                sound10.play(when=win)  # sync with win flip
            
            # if sound10 is stopping this frame...
            if sound10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10.tStop = t  # not accounting for scr refresh
                    sound10.frameNStop = frameN  # exact frame index
                    # update status
                    sound10.status = FINISHED
                    sound10.stop()
            # update sound10 status according to whether it's playing
            if sound10.isPlaying:
                sound10.status = STARTED
            elif sound10.isFinished:
                sound10.status = FINISHED
            
            # if sound10_2 is starting this frame...
            if sound10_2.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_2.frameNStart = frameN  # exact frame index
                sound10_2.tStart = t  # local t and not account for scr refresh
                sound10_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_2.status = STARTED
                sound10_2.play(when=win)  # sync with win flip
            
            # if sound10_2 is stopping this frame...
            if sound10_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_2.tStop = t  # not accounting for scr refresh
                    sound10_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_2.status = FINISHED
                    sound10_2.stop()
            # update sound10_2 status according to whether it's playing
            if sound10_2.isPlaying:
                sound10_2.status = STARTED
            elif sound10_2.isFinished:
                sound10_2.status = FINISHED
            
            # if sound10_3 is starting this frame...
            if sound10_3.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_3.frameNStart = frameN  # exact frame index
                sound10_3.tStart = t  # local t and not account for scr refresh
                sound10_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_3.status = STARTED
                sound10_3.play(when=win)  # sync with win flip
            
            # if sound10_3 is stopping this frame...
            if sound10_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_3.tStop = t  # not accounting for scr refresh
                    sound10_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_3.status = FINISHED
                    sound10_3.stop()
            # update sound10_3 status according to whether it's playing
            if sound10_3.isPlaying:
                sound10_3.status = STARTED
            elif sound10_3.isFinished:
                sound10_3.status = FINISHED
            
            # if sound10_4 is starting this frame...
            if sound10_4.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_4.frameNStart = frameN  # exact frame index
                sound10_4.tStart = t  # local t and not account for scr refresh
                sound10_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_4.status = STARTED
                sound10_4.play(when=win)  # sync with win flip
            
            # if sound10_4 is stopping this frame...
            if sound10_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_4.tStop = t  # not accounting for scr refresh
                    sound10_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_4.status = FINISHED
                    sound10_4.stop()
            # update sound10_4 status according to whether it's playing
            if sound10_4.isPlaying:
                sound10_4.status = STARTED
            elif sound10_4.isFinished:
                sound10_4.status = FINISHED
            
            # if sound10_5 is starting this frame...
            if sound10_5.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_5.frameNStart = frameN  # exact frame index
                sound10_5.tStart = t  # local t and not account for scr refresh
                sound10_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_5.status = STARTED
                sound10_5.play(when=win)  # sync with win flip
            
            # if sound10_5 is stopping this frame...
            if sound10_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_5.tStop = t  # not accounting for scr refresh
                    sound10_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_5.status = FINISHED
                    sound10_5.stop()
            # update sound10_5 status according to whether it's playing
            if sound10_5.isPlaying:
                sound10_5.status = STARTED
            elif sound10_5.isFinished:
                sound10_5.status = FINISHED
            
            # if sound10_6 is starting this frame...
            if sound10_6.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_6.frameNStart = frameN  # exact frame index
                sound10_6.tStart = t  # local t and not account for scr refresh
                sound10_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_6.status = STARTED
                sound10_6.play(when=win)  # sync with win flip
            
            # if sound10_6 is stopping this frame...
            if sound10_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_6.tStop = t  # not accounting for scr refresh
                    sound10_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_6.status = FINISHED
                    sound10_6.stop()
            # update sound10_6 status according to whether it's playing
            if sound10_6.isPlaying:
                sound10_6.status = STARTED
            elif sound10_6.isFinished:
                sound10_6.status = FINISHED
            
            # if sound10_7 is starting this frame...
            if sound10_7.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_7.frameNStart = frameN  # exact frame index
                sound10_7.tStart = t  # local t and not account for scr refresh
                sound10_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_7.status = STARTED
                sound10_7.play(when=win)  # sync with win flip
            
            # if sound10_7 is stopping this frame...
            if sound10_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_7.tStop = t  # not accounting for scr refresh
                    sound10_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_7.status = FINISHED
                    sound10_7.stop()
            # update sound10_7 status according to whether it's playing
            if sound10_7.isPlaying:
                sound10_7.status = STARTED
            elif sound10_7.isFinished:
                sound10_7.status = FINISHED
            
            # if sound10_8 is starting this frame...
            if sound10_8.status == NOT_STARTED and tThisFlip >= starttime[8]-frameTolerance:
                # keep track of start time/frame for later
                sound10_8.frameNStart = frameN  # exact frame index
                sound10_8.tStart = t  # local t and not account for scr refresh
                sound10_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound10_8.status = STARTED
                sound10_8.play(when=win)  # sync with win flip
            
            # if sound10_8 is stopping this frame...
            if sound10_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound10_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound10_8.tStop = t  # not accounting for scr refresh
                    sound10_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound10_8.status = FINISHED
                    sound10_8.stop()
            # update sound10_8 status according to whether it's playing
            if sound10_8.isPlaying:
                sound10_8.status = STARTED
            elif sound10_8.isFinished:
                sound10_8.status = FINISHED
            
            # if sound11 is starting this frame...
            if sound11.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11.frameNStart = frameN  # exact frame index
                sound11.tStart = t  # local t and not account for scr refresh
                sound11.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11.status = STARTED
                sound11.play(when=win)  # sync with win flip
            
            # if sound11 is stopping this frame...
            if sound11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11.tStop = t  # not accounting for scr refresh
                    sound11.frameNStop = frameN  # exact frame index
                    # update status
                    sound11.status = FINISHED
                    sound11.stop()
            # update sound11 status according to whether it's playing
            if sound11.isPlaying:
                sound11.status = STARTED
            elif sound11.isFinished:
                sound11.status = FINISHED
            
            # if sound11_2 is starting this frame...
            if sound11_2.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_2.frameNStart = frameN  # exact frame index
                sound11_2.tStart = t  # local t and not account for scr refresh
                sound11_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_2.status = STARTED
                sound11_2.play(when=win)  # sync with win flip
            
            # if sound11_2 is stopping this frame...
            if sound11_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_2.tStop = t  # not accounting for scr refresh
                    sound11_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_2.status = FINISHED
                    sound11_2.stop()
            # update sound11_2 status according to whether it's playing
            if sound11_2.isPlaying:
                sound11_2.status = STARTED
            elif sound11_2.isFinished:
                sound11_2.status = FINISHED
            
            # if sound11_3 is starting this frame...
            if sound11_3.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_3.frameNStart = frameN  # exact frame index
                sound11_3.tStart = t  # local t and not account for scr refresh
                sound11_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_3.status = STARTED
                sound11_3.play(when=win)  # sync with win flip
            
            # if sound11_3 is stopping this frame...
            if sound11_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_3.tStop = t  # not accounting for scr refresh
                    sound11_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_3.status = FINISHED
                    sound11_3.stop()
            # update sound11_3 status according to whether it's playing
            if sound11_3.isPlaying:
                sound11_3.status = STARTED
            elif sound11_3.isFinished:
                sound11_3.status = FINISHED
            
            # if sound11_4 is starting this frame...
            if sound11_4.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_4.frameNStart = frameN  # exact frame index
                sound11_4.tStart = t  # local t and not account for scr refresh
                sound11_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_4.status = STARTED
                sound11_4.play(when=win)  # sync with win flip
            
            # if sound11_4 is stopping this frame...
            if sound11_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_4.tStop = t  # not accounting for scr refresh
                    sound11_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_4.status = FINISHED
                    sound11_4.stop()
            # update sound11_4 status according to whether it's playing
            if sound11_4.isPlaying:
                sound11_4.status = STARTED
            elif sound11_4.isFinished:
                sound11_4.status = FINISHED
            
            # if sound11_5 is starting this frame...
            if sound11_5.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_5.frameNStart = frameN  # exact frame index
                sound11_5.tStart = t  # local t and not account for scr refresh
                sound11_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_5.status = STARTED
                sound11_5.play(when=win)  # sync with win flip
            
            # if sound11_5 is stopping this frame...
            if sound11_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_5.tStop = t  # not accounting for scr refresh
                    sound11_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_5.status = FINISHED
                    sound11_5.stop()
            # update sound11_5 status according to whether it's playing
            if sound11_5.isPlaying:
                sound11_5.status = STARTED
            elif sound11_5.isFinished:
                sound11_5.status = FINISHED
            
            # if sound11_6 is starting this frame...
            if sound11_6.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_6.frameNStart = frameN  # exact frame index
                sound11_6.tStart = t  # local t and not account for scr refresh
                sound11_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_6.status = STARTED
                sound11_6.play(when=win)  # sync with win flip
            
            # if sound11_6 is stopping this frame...
            if sound11_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_6.tStop = t  # not accounting for scr refresh
                    sound11_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_6.status = FINISHED
                    sound11_6.stop()
            # update sound11_6 status according to whether it's playing
            if sound11_6.isPlaying:
                sound11_6.status = STARTED
            elif sound11_6.isFinished:
                sound11_6.status = FINISHED
            
            # if sound11_7 is starting this frame...
            if sound11_7.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_7.frameNStart = frameN  # exact frame index
                sound11_7.tStart = t  # local t and not account for scr refresh
                sound11_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_7.status = STARTED
                sound11_7.play(when=win)  # sync with win flip
            
            # if sound11_7 is stopping this frame...
            if sound11_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_7.tStop = t  # not accounting for scr refresh
                    sound11_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_7.status = FINISHED
                    sound11_7.stop()
            # update sound11_7 status according to whether it's playing
            if sound11_7.isPlaying:
                sound11_7.status = STARTED
            elif sound11_7.isFinished:
                sound11_7.status = FINISHED
            
            # if sound11_8 is starting this frame...
            if sound11_8.status == NOT_STARTED and tThisFlip >= starttime[9]-frameTolerance:
                # keep track of start time/frame for later
                sound11_8.frameNStart = frameN  # exact frame index
                sound11_8.tStart = t  # local t and not account for scr refresh
                sound11_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound11_8.status = STARTED
                sound11_8.play(when=win)  # sync with win flip
            
            # if sound11_8 is stopping this frame...
            if sound11_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound11_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound11_8.tStop = t  # not accounting for scr refresh
                    sound11_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound11_8.status = FINISHED
                    sound11_8.stop()
            # update sound11_8 status according to whether it's playing
            if sound11_8.isPlaying:
                sound11_8.status = STARTED
            elif sound11_8.isFinished:
                sound11_8.status = FINISHED
            
            # if sound12 is starting this frame...
            if sound12.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12.frameNStart = frameN  # exact frame index
                sound12.tStart = t  # local t and not account for scr refresh
                sound12.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12.status = STARTED
                sound12.play(when=win)  # sync with win flip
            
            # if sound12 is stopping this frame...
            if sound12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12.tStop = t  # not accounting for scr refresh
                    sound12.frameNStop = frameN  # exact frame index
                    # update status
                    sound12.status = FINISHED
                    sound12.stop()
            # update sound12 status according to whether it's playing
            if sound12.isPlaying:
                sound12.status = STARTED
            elif sound12.isFinished:
                sound12.status = FINISHED
            
            # if sound12_2 is starting this frame...
            if sound12_2.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_2.frameNStart = frameN  # exact frame index
                sound12_2.tStart = t  # local t and not account for scr refresh
                sound12_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_2.status = STARTED
                sound12_2.play(when=win)  # sync with win flip
            
            # if sound12_2 is stopping this frame...
            if sound12_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_2.tStop = t  # not accounting for scr refresh
                    sound12_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_2.status = FINISHED
                    sound12_2.stop()
            # update sound12_2 status according to whether it's playing
            if sound12_2.isPlaying:
                sound12_2.status = STARTED
            elif sound12_2.isFinished:
                sound12_2.status = FINISHED
            
            # if sound12_3 is starting this frame...
            if sound12_3.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_3.frameNStart = frameN  # exact frame index
                sound12_3.tStart = t  # local t and not account for scr refresh
                sound12_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_3.status = STARTED
                sound12_3.play(when=win)  # sync with win flip
            
            # if sound12_3 is stopping this frame...
            if sound12_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_3.tStop = t  # not accounting for scr refresh
                    sound12_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_3.status = FINISHED
                    sound12_3.stop()
            # update sound12_3 status according to whether it's playing
            if sound12_3.isPlaying:
                sound12_3.status = STARTED
            elif sound12_3.isFinished:
                sound12_3.status = FINISHED
            
            # if sound12_4 is starting this frame...
            if sound12_4.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_4.frameNStart = frameN  # exact frame index
                sound12_4.tStart = t  # local t and not account for scr refresh
                sound12_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_4.status = STARTED
                sound12_4.play(when=win)  # sync with win flip
            
            # if sound12_4 is stopping this frame...
            if sound12_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_4.tStop = t  # not accounting for scr refresh
                    sound12_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_4.status = FINISHED
                    sound12_4.stop()
            # update sound12_4 status according to whether it's playing
            if sound12_4.isPlaying:
                sound12_4.status = STARTED
            elif sound12_4.isFinished:
                sound12_4.status = FINISHED
            
            # if sound12_5 is starting this frame...
            if sound12_5.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_5.frameNStart = frameN  # exact frame index
                sound12_5.tStart = t  # local t and not account for scr refresh
                sound12_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_5.status = STARTED
                sound12_5.play(when=win)  # sync with win flip
            
            # if sound12_5 is stopping this frame...
            if sound12_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_5.tStop = t  # not accounting for scr refresh
                    sound12_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_5.status = FINISHED
                    sound12_5.stop()
            # update sound12_5 status according to whether it's playing
            if sound12_5.isPlaying:
                sound12_5.status = STARTED
            elif sound12_5.isFinished:
                sound12_5.status = FINISHED
            
            # if sound12_6 is starting this frame...
            if sound12_6.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_6.frameNStart = frameN  # exact frame index
                sound12_6.tStart = t  # local t and not account for scr refresh
                sound12_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_6.status = STARTED
                sound12_6.play(when=win)  # sync with win flip
            
            # if sound12_6 is stopping this frame...
            if sound12_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_6.tStop = t  # not accounting for scr refresh
                    sound12_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_6.status = FINISHED
                    sound12_6.stop()
            # update sound12_6 status according to whether it's playing
            if sound12_6.isPlaying:
                sound12_6.status = STARTED
            elif sound12_6.isFinished:
                sound12_6.status = FINISHED
            
            # if sound12_7 is starting this frame...
            if sound12_7.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_7.frameNStart = frameN  # exact frame index
                sound12_7.tStart = t  # local t and not account for scr refresh
                sound12_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_7.status = STARTED
                sound12_7.play(when=win)  # sync with win flip
            
            # if sound12_7 is stopping this frame...
            if sound12_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_7.tStop = t  # not accounting for scr refresh
                    sound12_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_7.status = FINISHED
                    sound12_7.stop()
            # update sound12_7 status according to whether it's playing
            if sound12_7.isPlaying:
                sound12_7.status = STARTED
            elif sound12_7.isFinished:
                sound12_7.status = FINISHED
            
            # if sound12_8 is starting this frame...
            if sound12_8.status == NOT_STARTED and tThisFlip >= starttime[10]-frameTolerance:
                # keep track of start time/frame for later
                sound12_8.frameNStart = frameN  # exact frame index
                sound12_8.tStart = t  # local t and not account for scr refresh
                sound12_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound12_8.status = STARTED
                sound12_8.play(when=win)  # sync with win flip
            
            # if sound12_8 is stopping this frame...
            if sound12_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound12_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound12_8.tStop = t  # not accounting for scr refresh
                    sound12_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound12_8.status = FINISHED
                    sound12_8.stop()
            # update sound12_8 status according to whether it's playing
            if sound12_8.isPlaying:
                sound12_8.status = STARTED
            elif sound12_8.isFinished:
                sound12_8.status = FINISHED
            
            # if sound13 is starting this frame...
            if sound13.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13.frameNStart = frameN  # exact frame index
                sound13.tStart = t  # local t and not account for scr refresh
                sound13.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13.status = STARTED
                sound13.play(when=win)  # sync with win flip
            
            # if sound13 is stopping this frame...
            if sound13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13.tStop = t  # not accounting for scr refresh
                    sound13.frameNStop = frameN  # exact frame index
                    # update status
                    sound13.status = FINISHED
                    sound13.stop()
            # update sound13 status according to whether it's playing
            if sound13.isPlaying:
                sound13.status = STARTED
            elif sound13.isFinished:
                sound13.status = FINISHED
            
            # if sound13_2 is starting this frame...
            if sound13_2.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_2.frameNStart = frameN  # exact frame index
                sound13_2.tStart = t  # local t and not account for scr refresh
                sound13_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_2.status = STARTED
                sound13_2.play(when=win)  # sync with win flip
            
            # if sound13_2 is stopping this frame...
            if sound13_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_2.tStop = t  # not accounting for scr refresh
                    sound13_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_2.status = FINISHED
                    sound13_2.stop()
            # update sound13_2 status according to whether it's playing
            if sound13_2.isPlaying:
                sound13_2.status = STARTED
            elif sound13_2.isFinished:
                sound13_2.status = FINISHED
            
            # if sound13_3 is starting this frame...
            if sound13_3.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_3.frameNStart = frameN  # exact frame index
                sound13_3.tStart = t  # local t and not account for scr refresh
                sound13_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_3.status = STARTED
                sound13_3.play(when=win)  # sync with win flip
            
            # if sound13_3 is stopping this frame...
            if sound13_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_3.tStop = t  # not accounting for scr refresh
                    sound13_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_3.status = FINISHED
                    sound13_3.stop()
            # update sound13_3 status according to whether it's playing
            if sound13_3.isPlaying:
                sound13_3.status = STARTED
            elif sound13_3.isFinished:
                sound13_3.status = FINISHED
            
            # if sound13_4 is starting this frame...
            if sound13_4.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_4.frameNStart = frameN  # exact frame index
                sound13_4.tStart = t  # local t and not account for scr refresh
                sound13_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_4.status = STARTED
                sound13_4.play(when=win)  # sync with win flip
            
            # if sound13_4 is stopping this frame...
            if sound13_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_4.tStop = t  # not accounting for scr refresh
                    sound13_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_4.status = FINISHED
                    sound13_4.stop()
            # update sound13_4 status according to whether it's playing
            if sound13_4.isPlaying:
                sound13_4.status = STARTED
            elif sound13_4.isFinished:
                sound13_4.status = FINISHED
            
            # if sound13_5 is starting this frame...
            if sound13_5.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_5.frameNStart = frameN  # exact frame index
                sound13_5.tStart = t  # local t and not account for scr refresh
                sound13_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_5.status = STARTED
                sound13_5.play(when=win)  # sync with win flip
            
            # if sound13_5 is stopping this frame...
            if sound13_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_5.tStop = t  # not accounting for scr refresh
                    sound13_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_5.status = FINISHED
                    sound13_5.stop()
            # update sound13_5 status according to whether it's playing
            if sound13_5.isPlaying:
                sound13_5.status = STARTED
            elif sound13_5.isFinished:
                sound13_5.status = FINISHED
            
            # if sound13_6 is starting this frame...
            if sound13_6.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_6.frameNStart = frameN  # exact frame index
                sound13_6.tStart = t  # local t and not account for scr refresh
                sound13_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_6.status = STARTED
                sound13_6.play(when=win)  # sync with win flip
            
            # if sound13_6 is stopping this frame...
            if sound13_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_6.tStop = t  # not accounting for scr refresh
                    sound13_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_6.status = FINISHED
                    sound13_6.stop()
            # update sound13_6 status according to whether it's playing
            if sound13_6.isPlaying:
                sound13_6.status = STARTED
            elif sound13_6.isFinished:
                sound13_6.status = FINISHED
            
            # if sound13_7 is starting this frame...
            if sound13_7.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_7.frameNStart = frameN  # exact frame index
                sound13_7.tStart = t  # local t and not account for scr refresh
                sound13_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_7.status = STARTED
                sound13_7.play(when=win)  # sync with win flip
            
            # if sound13_7 is stopping this frame...
            if sound13_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_7.tStop = t  # not accounting for scr refresh
                    sound13_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_7.status = FINISHED
                    sound13_7.stop()
            # update sound13_7 status according to whether it's playing
            if sound13_7.isPlaying:
                sound13_7.status = STARTED
            elif sound13_7.isFinished:
                sound13_7.status = FINISHED
            
            # if sound13_8 is starting this frame...
            if sound13_8.status == NOT_STARTED and tThisFlip >= starttime[11]-frameTolerance:
                # keep track of start time/frame for later
                sound13_8.frameNStart = frameN  # exact frame index
                sound13_8.tStart = t  # local t and not account for scr refresh
                sound13_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound13_8.status = STARTED
                sound13_8.play(when=win)  # sync with win flip
            
            # if sound13_8 is stopping this frame...
            if sound13_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound13_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound13_8.tStop = t  # not accounting for scr refresh
                    sound13_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound13_8.status = FINISHED
                    sound13_8.stop()
            # update sound13_8 status according to whether it's playing
            if sound13_8.isPlaying:
                sound13_8.status = STARTED
            elif sound13_8.isFinished:
                sound13_8.status = FINISHED
            
            # if sound14 is starting this frame...
            if sound14.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14.frameNStart = frameN  # exact frame index
                sound14.tStart = t  # local t and not account for scr refresh
                sound14.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14.status = STARTED
                sound14.play(when=win)  # sync with win flip
            
            # if sound14 is stopping this frame...
            if sound14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14.tStop = t  # not accounting for scr refresh
                    sound14.frameNStop = frameN  # exact frame index
                    # update status
                    sound14.status = FINISHED
                    sound14.stop()
            # update sound14 status according to whether it's playing
            if sound14.isPlaying:
                sound14.status = STARTED
            elif sound14.isFinished:
                sound14.status = FINISHED
            
            # if sound14_2 is starting this frame...
            if sound14_2.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_2.frameNStart = frameN  # exact frame index
                sound14_2.tStart = t  # local t and not account for scr refresh
                sound14_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_2.status = STARTED
                sound14_2.play(when=win)  # sync with win flip
            
            # if sound14_2 is stopping this frame...
            if sound14_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_2.tStop = t  # not accounting for scr refresh
                    sound14_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_2.status = FINISHED
                    sound14_2.stop()
            # update sound14_2 status according to whether it's playing
            if sound14_2.isPlaying:
                sound14_2.status = STARTED
            elif sound14_2.isFinished:
                sound14_2.status = FINISHED
            
            # if sound14_3 is starting this frame...
            if sound14_3.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_3.frameNStart = frameN  # exact frame index
                sound14_3.tStart = t  # local t and not account for scr refresh
                sound14_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_3.status = STARTED
                sound14_3.play(when=win)  # sync with win flip
            
            # if sound14_3 is stopping this frame...
            if sound14_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_3.tStop = t  # not accounting for scr refresh
                    sound14_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_3.status = FINISHED
                    sound14_3.stop()
            # update sound14_3 status according to whether it's playing
            if sound14_3.isPlaying:
                sound14_3.status = STARTED
            elif sound14_3.isFinished:
                sound14_3.status = FINISHED
            
            # if sound14_4 is starting this frame...
            if sound14_4.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_4.frameNStart = frameN  # exact frame index
                sound14_4.tStart = t  # local t and not account for scr refresh
                sound14_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_4.status = STARTED
                sound14_4.play(when=win)  # sync with win flip
            
            # if sound14_4 is stopping this frame...
            if sound14_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_4.tStop = t  # not accounting for scr refresh
                    sound14_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_4.status = FINISHED
                    sound14_4.stop()
            # update sound14_4 status according to whether it's playing
            if sound14_4.isPlaying:
                sound14_4.status = STARTED
            elif sound14_4.isFinished:
                sound14_4.status = FINISHED
            
            # if sound14_5 is starting this frame...
            if sound14_5.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_5.frameNStart = frameN  # exact frame index
                sound14_5.tStart = t  # local t and not account for scr refresh
                sound14_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_5.status = STARTED
                sound14_5.play(when=win)  # sync with win flip
            
            # if sound14_5 is stopping this frame...
            if sound14_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_5.tStop = t  # not accounting for scr refresh
                    sound14_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_5.status = FINISHED
                    sound14_5.stop()
            # update sound14_5 status according to whether it's playing
            if sound14_5.isPlaying:
                sound14_5.status = STARTED
            elif sound14_5.isFinished:
                sound14_5.status = FINISHED
            
            # if sound14_6 is starting this frame...
            if sound14_6.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_6.frameNStart = frameN  # exact frame index
                sound14_6.tStart = t  # local t and not account for scr refresh
                sound14_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_6.status = STARTED
                sound14_6.play(when=win)  # sync with win flip
            
            # if sound14_6 is stopping this frame...
            if sound14_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_6.tStop = t  # not accounting for scr refresh
                    sound14_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_6.status = FINISHED
                    sound14_6.stop()
            # update sound14_6 status according to whether it's playing
            if sound14_6.isPlaying:
                sound14_6.status = STARTED
            elif sound14_6.isFinished:
                sound14_6.status = FINISHED
            
            # if sound14_7 is starting this frame...
            if sound14_7.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_7.frameNStart = frameN  # exact frame index
                sound14_7.tStart = t  # local t and not account for scr refresh
                sound14_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_7.status = STARTED
                sound14_7.play(when=win)  # sync with win flip
            
            # if sound14_7 is stopping this frame...
            if sound14_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_7.tStop = t  # not accounting for scr refresh
                    sound14_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_7.status = FINISHED
                    sound14_7.stop()
            # update sound14_7 status according to whether it's playing
            if sound14_7.isPlaying:
                sound14_7.status = STARTED
            elif sound14_7.isFinished:
                sound14_7.status = FINISHED
            
            # if sound14_8 is starting this frame...
            if sound14_8.status == NOT_STARTED and tThisFlip >= starttime[12]-frameTolerance:
                # keep track of start time/frame for later
                sound14_8.frameNStart = frameN  # exact frame index
                sound14_8.tStart = t  # local t and not account for scr refresh
                sound14_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound14_8.status = STARTED
                sound14_8.play(when=win)  # sync with win flip
            
            # if sound14_8 is stopping this frame...
            if sound14_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound14_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound14_8.tStop = t  # not accounting for scr refresh
                    sound14_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound14_8.status = FINISHED
                    sound14_8.stop()
            # update sound14_8 status according to whether it's playing
            if sound14_8.isPlaying:
                sound14_8.status = STARTED
            elif sound14_8.isFinished:
                sound14_8.status = FINISHED
            
            # if sound15 is starting this frame...
            if sound15.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15.frameNStart = frameN  # exact frame index
                sound15.tStart = t  # local t and not account for scr refresh
                sound15.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15.status = STARTED
                sound15.play(when=win)  # sync with win flip
            
            # if sound15 is stopping this frame...
            if sound15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15.tStop = t  # not accounting for scr refresh
                    sound15.frameNStop = frameN  # exact frame index
                    # update status
                    sound15.status = FINISHED
                    sound15.stop()
            # update sound15 status according to whether it's playing
            if sound15.isPlaying:
                sound15.status = STARTED
            elif sound15.isFinished:
                sound15.status = FINISHED
            
            # if sound15_2 is starting this frame...
            if sound15_2.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_2.frameNStart = frameN  # exact frame index
                sound15_2.tStart = t  # local t and not account for scr refresh
                sound15_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_2.status = STARTED
                sound15_2.play(when=win)  # sync with win flip
            
            # if sound15_2 is stopping this frame...
            if sound15_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_2.tStop = t  # not accounting for scr refresh
                    sound15_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_2.status = FINISHED
                    sound15_2.stop()
            # update sound15_2 status according to whether it's playing
            if sound15_2.isPlaying:
                sound15_2.status = STARTED
            elif sound15_2.isFinished:
                sound15_2.status = FINISHED
            
            # if sound15_3 is starting this frame...
            if sound15_3.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_3.frameNStart = frameN  # exact frame index
                sound15_3.tStart = t  # local t and not account for scr refresh
                sound15_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_3.status = STARTED
                sound15_3.play(when=win)  # sync with win flip
            
            # if sound15_3 is stopping this frame...
            if sound15_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_3.tStop = t  # not accounting for scr refresh
                    sound15_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_3.status = FINISHED
                    sound15_3.stop()
            # update sound15_3 status according to whether it's playing
            if sound15_3.isPlaying:
                sound15_3.status = STARTED
            elif sound15_3.isFinished:
                sound15_3.status = FINISHED
            
            # if sound15_4 is starting this frame...
            if sound15_4.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_4.frameNStart = frameN  # exact frame index
                sound15_4.tStart = t  # local t and not account for scr refresh
                sound15_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_4.status = STARTED
                sound15_4.play(when=win)  # sync with win flip
            
            # if sound15_4 is stopping this frame...
            if sound15_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_4.tStop = t  # not accounting for scr refresh
                    sound15_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_4.status = FINISHED
                    sound15_4.stop()
            # update sound15_4 status according to whether it's playing
            if sound15_4.isPlaying:
                sound15_4.status = STARTED
            elif sound15_4.isFinished:
                sound15_4.status = FINISHED
            
            # if sound15_5 is starting this frame...
            if sound15_5.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_5.frameNStart = frameN  # exact frame index
                sound15_5.tStart = t  # local t and not account for scr refresh
                sound15_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_5.status = STARTED
                sound15_5.play(when=win)  # sync with win flip
            
            # if sound15_5 is stopping this frame...
            if sound15_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_5.tStop = t  # not accounting for scr refresh
                    sound15_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_5.status = FINISHED
                    sound15_5.stop()
            # update sound15_5 status according to whether it's playing
            if sound15_5.isPlaying:
                sound15_5.status = STARTED
            elif sound15_5.isFinished:
                sound15_5.status = FINISHED
            
            # if sound15_6 is starting this frame...
            if sound15_6.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_6.frameNStart = frameN  # exact frame index
                sound15_6.tStart = t  # local t and not account for scr refresh
                sound15_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_6.status = STARTED
                sound15_6.play(when=win)  # sync with win flip
            
            # if sound15_6 is stopping this frame...
            if sound15_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_6.tStop = t  # not accounting for scr refresh
                    sound15_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_6.status = FINISHED
                    sound15_6.stop()
            # update sound15_6 status according to whether it's playing
            if sound15_6.isPlaying:
                sound15_6.status = STARTED
            elif sound15_6.isFinished:
                sound15_6.status = FINISHED
            
            # if sound15_7 is starting this frame...
            if sound15_7.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_7.frameNStart = frameN  # exact frame index
                sound15_7.tStart = t  # local t and not account for scr refresh
                sound15_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_7.status = STARTED
                sound15_7.play(when=win)  # sync with win flip
            
            # if sound15_7 is stopping this frame...
            if sound15_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_7.tStop = t  # not accounting for scr refresh
                    sound15_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_7.status = FINISHED
                    sound15_7.stop()
            # update sound15_7 status according to whether it's playing
            if sound15_7.isPlaying:
                sound15_7.status = STARTED
            elif sound15_7.isFinished:
                sound15_7.status = FINISHED
            
            # if sound15_8 is starting this frame...
            if sound15_8.status == NOT_STARTED and tThisFlip >= starttime[13]-frameTolerance:
                # keep track of start time/frame for later
                sound15_8.frameNStart = frameN  # exact frame index
                sound15_8.tStart = t  # local t and not account for scr refresh
                sound15_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound15_8.status = STARTED
                sound15_8.play(when=win)  # sync with win flip
            
            # if sound15_8 is stopping this frame...
            if sound15_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound15_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound15_8.tStop = t  # not accounting for scr refresh
                    sound15_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound15_8.status = FINISHED
                    sound15_8.stop()
            # update sound15_8 status according to whether it's playing
            if sound15_8.isPlaying:
                sound15_8.status = STARTED
            elif sound15_8.isFinished:
                sound15_8.status = FINISHED
            
            # if spund16 is starting this frame...
            if spund16.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16.frameNStart = frameN  # exact frame index
                spund16.tStart = t  # local t and not account for scr refresh
                spund16.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16.status = STARTED
                spund16.play(when=win)  # sync with win flip
            
            # if spund16 is stopping this frame...
            if spund16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16.tStop = t  # not accounting for scr refresh
                    spund16.frameNStop = frameN  # exact frame index
                    # update status
                    spund16.status = FINISHED
                    spund16.stop()
            # update spund16 status according to whether it's playing
            if spund16.isPlaying:
                spund16.status = STARTED
            elif spund16.isFinished:
                spund16.status = FINISHED
            
            # if spund16_2 is starting this frame...
            if spund16_2.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_2.frameNStart = frameN  # exact frame index
                spund16_2.tStart = t  # local t and not account for scr refresh
                spund16_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_2.status = STARTED
                spund16_2.play(when=win)  # sync with win flip
            
            # if spund16_2 is stopping this frame...
            if spund16_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_2.tStop = t  # not accounting for scr refresh
                    spund16_2.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_2.status = FINISHED
                    spund16_2.stop()
            # update spund16_2 status according to whether it's playing
            if spund16_2.isPlaying:
                spund16_2.status = STARTED
            elif spund16_2.isFinished:
                spund16_2.status = FINISHED
            
            # if spund16_3 is starting this frame...
            if spund16_3.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_3.frameNStart = frameN  # exact frame index
                spund16_3.tStart = t  # local t and not account for scr refresh
                spund16_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_3.status = STARTED
                spund16_3.play(when=win)  # sync with win flip
            
            # if spund16_3 is stopping this frame...
            if spund16_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_3.tStop = t  # not accounting for scr refresh
                    spund16_3.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_3.status = FINISHED
                    spund16_3.stop()
            # update spund16_3 status according to whether it's playing
            if spund16_3.isPlaying:
                spund16_3.status = STARTED
            elif spund16_3.isFinished:
                spund16_3.status = FINISHED
            
            # if spund16_4 is starting this frame...
            if spund16_4.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_4.frameNStart = frameN  # exact frame index
                spund16_4.tStart = t  # local t and not account for scr refresh
                spund16_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_4.status = STARTED
                spund16_4.play(when=win)  # sync with win flip
            
            # if spund16_4 is stopping this frame...
            if spund16_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_4.tStop = t  # not accounting for scr refresh
                    spund16_4.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_4.status = FINISHED
                    spund16_4.stop()
            # update spund16_4 status according to whether it's playing
            if spund16_4.isPlaying:
                spund16_4.status = STARTED
            elif spund16_4.isFinished:
                spund16_4.status = FINISHED
            
            # if spund16_5 is starting this frame...
            if spund16_5.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_5.frameNStart = frameN  # exact frame index
                spund16_5.tStart = t  # local t and not account for scr refresh
                spund16_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_5.status = STARTED
                spund16_5.play(when=win)  # sync with win flip
            
            # if spund16_5 is stopping this frame...
            if spund16_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_5.tStop = t  # not accounting for scr refresh
                    spund16_5.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_5.status = FINISHED
                    spund16_5.stop()
            # update spund16_5 status according to whether it's playing
            if spund16_5.isPlaying:
                spund16_5.status = STARTED
            elif spund16_5.isFinished:
                spund16_5.status = FINISHED
            
            # if spund16_6 is starting this frame...
            if spund16_6.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_6.frameNStart = frameN  # exact frame index
                spund16_6.tStart = t  # local t and not account for scr refresh
                spund16_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_6.status = STARTED
                spund16_6.play(when=win)  # sync with win flip
            
            # if spund16_6 is stopping this frame...
            if spund16_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_6.tStop = t  # not accounting for scr refresh
                    spund16_6.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_6.status = FINISHED
                    spund16_6.stop()
            # update spund16_6 status according to whether it's playing
            if spund16_6.isPlaying:
                spund16_6.status = STARTED
            elif spund16_6.isFinished:
                spund16_6.status = FINISHED
            
            # if spund16_7 is starting this frame...
            if spund16_7.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_7.frameNStart = frameN  # exact frame index
                spund16_7.tStart = t  # local t and not account for scr refresh
                spund16_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_7.status = STARTED
                spund16_7.play(when=win)  # sync with win flip
            
            # if spund16_7 is stopping this frame...
            if spund16_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_7.tStop = t  # not accounting for scr refresh
                    spund16_7.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_7.status = FINISHED
                    spund16_7.stop()
            # update spund16_7 status according to whether it's playing
            if spund16_7.isPlaying:
                spund16_7.status = STARTED
            elif spund16_7.isFinished:
                spund16_7.status = FINISHED
            
            # if spund16_8 is starting this frame...
            if spund16_8.status == NOT_STARTED and tThisFlip >= starttime[14]-frameTolerance:
                # keep track of start time/frame for later
                spund16_8.frameNStart = frameN  # exact frame index
                spund16_8.tStart = t  # local t and not account for scr refresh
                spund16_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                spund16_8.status = STARTED
                spund16_8.play(when=win)  # sync with win flip
            
            # if spund16_8 is stopping this frame...
            if spund16_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > spund16_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    spund16_8.tStop = t  # not accounting for scr refresh
                    spund16_8.frameNStop = frameN  # exact frame index
                    # update status
                    spund16_8.status = FINISHED
                    spund16_8.stop()
            # update spund16_8 status according to whether it's playing
            if spund16_8.isPlaying:
                spund16_8.status = STARTED
            elif spund16_8.isFinished:
                spund16_8.status = FINISHED
            
            # if sound17 is starting this frame...
            if sound17.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17.frameNStart = frameN  # exact frame index
                sound17.tStart = t  # local t and not account for scr refresh
                sound17.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17.status = STARTED
                sound17.play(when=win)  # sync with win flip
            
            # if sound17 is stopping this frame...
            if sound17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17.tStop = t  # not accounting for scr refresh
                    sound17.frameNStop = frameN  # exact frame index
                    # update status
                    sound17.status = FINISHED
                    sound17.stop()
            # update sound17 status according to whether it's playing
            if sound17.isPlaying:
                sound17.status = STARTED
            elif sound17.isFinished:
                sound17.status = FINISHED
            
            # if sound17_2 is starting this frame...
            if sound17_2.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_2.frameNStart = frameN  # exact frame index
                sound17_2.tStart = t  # local t and not account for scr refresh
                sound17_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_2.status = STARTED
                sound17_2.play(when=win)  # sync with win flip
            
            # if sound17_2 is stopping this frame...
            if sound17_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_2.tStop = t  # not accounting for scr refresh
                    sound17_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_2.status = FINISHED
                    sound17_2.stop()
            # update sound17_2 status according to whether it's playing
            if sound17_2.isPlaying:
                sound17_2.status = STARTED
            elif sound17_2.isFinished:
                sound17_2.status = FINISHED
            
            # if sound17_3 is starting this frame...
            if sound17_3.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_3.frameNStart = frameN  # exact frame index
                sound17_3.tStart = t  # local t and not account for scr refresh
                sound17_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_3.status = STARTED
                sound17_3.play(when=win)  # sync with win flip
            
            # if sound17_3 is stopping this frame...
            if sound17_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_3.tStop = t  # not accounting for scr refresh
                    sound17_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_3.status = FINISHED
                    sound17_3.stop()
            # update sound17_3 status according to whether it's playing
            if sound17_3.isPlaying:
                sound17_3.status = STARTED
            elif sound17_3.isFinished:
                sound17_3.status = FINISHED
            
            # if sound17_4 is starting this frame...
            if sound17_4.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_4.frameNStart = frameN  # exact frame index
                sound17_4.tStart = t  # local t and not account for scr refresh
                sound17_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_4.status = STARTED
                sound17_4.play(when=win)  # sync with win flip
            
            # if sound17_4 is stopping this frame...
            if sound17_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_4.tStop = t  # not accounting for scr refresh
                    sound17_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_4.status = FINISHED
                    sound17_4.stop()
            # update sound17_4 status according to whether it's playing
            if sound17_4.isPlaying:
                sound17_4.status = STARTED
            elif sound17_4.isFinished:
                sound17_4.status = FINISHED
            
            # if sound17_5 is starting this frame...
            if sound17_5.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_5.frameNStart = frameN  # exact frame index
                sound17_5.tStart = t  # local t and not account for scr refresh
                sound17_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_5.status = STARTED
                sound17_5.play(when=win)  # sync with win flip
            
            # if sound17_5 is stopping this frame...
            if sound17_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_5.tStop = t  # not accounting for scr refresh
                    sound17_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_5.status = FINISHED
                    sound17_5.stop()
            # update sound17_5 status according to whether it's playing
            if sound17_5.isPlaying:
                sound17_5.status = STARTED
            elif sound17_5.isFinished:
                sound17_5.status = FINISHED
            
            # if sound17_6 is starting this frame...
            if sound17_6.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_6.frameNStart = frameN  # exact frame index
                sound17_6.tStart = t  # local t and not account for scr refresh
                sound17_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_6.status = STARTED
                sound17_6.play(when=win)  # sync with win flip
            
            # if sound17_6 is stopping this frame...
            if sound17_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_6.tStop = t  # not accounting for scr refresh
                    sound17_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_6.status = FINISHED
                    sound17_6.stop()
            # update sound17_6 status according to whether it's playing
            if sound17_6.isPlaying:
                sound17_6.status = STARTED
            elif sound17_6.isFinished:
                sound17_6.status = FINISHED
            
            # if sound17_7 is starting this frame...
            if sound17_7.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_7.frameNStart = frameN  # exact frame index
                sound17_7.tStart = t  # local t and not account for scr refresh
                sound17_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_7.status = STARTED
                sound17_7.play(when=win)  # sync with win flip
            
            # if sound17_7 is stopping this frame...
            if sound17_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_7.tStop = t  # not accounting for scr refresh
                    sound17_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_7.status = FINISHED
                    sound17_7.stop()
            # update sound17_7 status according to whether it's playing
            if sound17_7.isPlaying:
                sound17_7.status = STARTED
            elif sound17_7.isFinished:
                sound17_7.status = FINISHED
            
            # if sound17_8 is starting this frame...
            if sound17_8.status == NOT_STARTED and tThisFlip >= starttime[15]-frameTolerance:
                # keep track of start time/frame for later
                sound17_8.frameNStart = frameN  # exact frame index
                sound17_8.tStart = t  # local t and not account for scr refresh
                sound17_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound17_8.status = STARTED
                sound17_8.play(when=win)  # sync with win flip
            
            # if sound17_8 is stopping this frame...
            if sound17_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound17_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound17_8.tStop = t  # not accounting for scr refresh
                    sound17_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound17_8.status = FINISHED
                    sound17_8.stop()
            # update sound17_8 status according to whether it's playing
            if sound17_8.isPlaying:
                sound17_8.status = STARTED
            elif sound17_8.isFinished:
                sound17_8.status = FINISHED
            
            # if sound18 is starting this frame...
            if sound18.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18.frameNStart = frameN  # exact frame index
                sound18.tStart = t  # local t and not account for scr refresh
                sound18.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18.status = STARTED
                sound18.play(when=win)  # sync with win flip
            
            # if sound18 is stopping this frame...
            if sound18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18.tStop = t  # not accounting for scr refresh
                    sound18.frameNStop = frameN  # exact frame index
                    # update status
                    sound18.status = FINISHED
                    sound18.stop()
            # update sound18 status according to whether it's playing
            if sound18.isPlaying:
                sound18.status = STARTED
            elif sound18.isFinished:
                sound18.status = FINISHED
            
            # if sound18_2 is starting this frame...
            if sound18_2.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_2.frameNStart = frameN  # exact frame index
                sound18_2.tStart = t  # local t and not account for scr refresh
                sound18_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_2.status = STARTED
                sound18_2.play(when=win)  # sync with win flip
            
            # if sound18_2 is stopping this frame...
            if sound18_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_2.tStop = t  # not accounting for scr refresh
                    sound18_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_2.status = FINISHED
                    sound18_2.stop()
            # update sound18_2 status according to whether it's playing
            if sound18_2.isPlaying:
                sound18_2.status = STARTED
            elif sound18_2.isFinished:
                sound18_2.status = FINISHED
            
            # if sound18_3 is starting this frame...
            if sound18_3.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_3.frameNStart = frameN  # exact frame index
                sound18_3.tStart = t  # local t and not account for scr refresh
                sound18_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_3.status = STARTED
                sound18_3.play(when=win)  # sync with win flip
            
            # if sound18_3 is stopping this frame...
            if sound18_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_3.tStop = t  # not accounting for scr refresh
                    sound18_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_3.status = FINISHED
                    sound18_3.stop()
            # update sound18_3 status according to whether it's playing
            if sound18_3.isPlaying:
                sound18_3.status = STARTED
            elif sound18_3.isFinished:
                sound18_3.status = FINISHED
            
            # if sound18_4 is starting this frame...
            if sound18_4.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_4.frameNStart = frameN  # exact frame index
                sound18_4.tStart = t  # local t and not account for scr refresh
                sound18_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_4.status = STARTED
                sound18_4.play(when=win)  # sync with win flip
            
            # if sound18_4 is stopping this frame...
            if sound18_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_4.tStop = t  # not accounting for scr refresh
                    sound18_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_4.status = FINISHED
                    sound18_4.stop()
            # update sound18_4 status according to whether it's playing
            if sound18_4.isPlaying:
                sound18_4.status = STARTED
            elif sound18_4.isFinished:
                sound18_4.status = FINISHED
            
            # if sound18_5 is starting this frame...
            if sound18_5.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_5.frameNStart = frameN  # exact frame index
                sound18_5.tStart = t  # local t and not account for scr refresh
                sound18_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_5.status = STARTED
                sound18_5.play(when=win)  # sync with win flip
            
            # if sound18_5 is stopping this frame...
            if sound18_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_5.tStop = t  # not accounting for scr refresh
                    sound18_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_5.status = FINISHED
                    sound18_5.stop()
            # update sound18_5 status according to whether it's playing
            if sound18_5.isPlaying:
                sound18_5.status = STARTED
            elif sound18_5.isFinished:
                sound18_5.status = FINISHED
            
            # if sound18_6 is starting this frame...
            if sound18_6.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_6.frameNStart = frameN  # exact frame index
                sound18_6.tStart = t  # local t and not account for scr refresh
                sound18_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_6.status = STARTED
                sound18_6.play(when=win)  # sync with win flip
            
            # if sound18_6 is stopping this frame...
            if sound18_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_6.tStop = t  # not accounting for scr refresh
                    sound18_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_6.status = FINISHED
                    sound18_6.stop()
            # update sound18_6 status according to whether it's playing
            if sound18_6.isPlaying:
                sound18_6.status = STARTED
            elif sound18_6.isFinished:
                sound18_6.status = FINISHED
            
            # if sound18_7 is starting this frame...
            if sound18_7.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_7.frameNStart = frameN  # exact frame index
                sound18_7.tStart = t  # local t and not account for scr refresh
                sound18_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_7.status = STARTED
                sound18_7.play(when=win)  # sync with win flip
            
            # if sound18_7 is stopping this frame...
            if sound18_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_7.tStop = t  # not accounting for scr refresh
                    sound18_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_7.status = FINISHED
                    sound18_7.stop()
            # update sound18_7 status according to whether it's playing
            if sound18_7.isPlaying:
                sound18_7.status = STARTED
            elif sound18_7.isFinished:
                sound18_7.status = FINISHED
            
            # if sound18_8 is starting this frame...
            if sound18_8.status == NOT_STARTED and tThisFlip >= starttime[16]-frameTolerance:
                # keep track of start time/frame for later
                sound18_8.frameNStart = frameN  # exact frame index
                sound18_8.tStart = t  # local t and not account for scr refresh
                sound18_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound18_8.status = STARTED
                sound18_8.play(when=win)  # sync with win flip
            
            # if sound18_8 is stopping this frame...
            if sound18_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound18_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound18_8.tStop = t  # not accounting for scr refresh
                    sound18_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound18_8.status = FINISHED
                    sound18_8.stop()
            # update sound18_8 status according to whether it's playing
            if sound18_8.isPlaying:
                sound18_8.status = STARTED
            elif sound18_8.isFinished:
                sound18_8.status = FINISHED
            
            # if sound19 is starting this frame...
            if sound19.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19.frameNStart = frameN  # exact frame index
                sound19.tStart = t  # local t and not account for scr refresh
                sound19.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19.status = STARTED
                sound19.play(when=win)  # sync with win flip
            
            # if sound19 is stopping this frame...
            if sound19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19.tStop = t  # not accounting for scr refresh
                    sound19.frameNStop = frameN  # exact frame index
                    # update status
                    sound19.status = FINISHED
                    sound19.stop()
            # update sound19 status according to whether it's playing
            if sound19.isPlaying:
                sound19.status = STARTED
            elif sound19.isFinished:
                sound19.status = FINISHED
            
            # if sound19_2 is starting this frame...
            if sound19_2.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_2.frameNStart = frameN  # exact frame index
                sound19_2.tStart = t  # local t and not account for scr refresh
                sound19_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_2.status = STARTED
                sound19_2.play(when=win)  # sync with win flip
            
            # if sound19_2 is stopping this frame...
            if sound19_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_2.tStop = t  # not accounting for scr refresh
                    sound19_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_2.status = FINISHED
                    sound19_2.stop()
            # update sound19_2 status according to whether it's playing
            if sound19_2.isPlaying:
                sound19_2.status = STARTED
            elif sound19_2.isFinished:
                sound19_2.status = FINISHED
            
            # if sound19_3 is starting this frame...
            if sound19_3.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_3.frameNStart = frameN  # exact frame index
                sound19_3.tStart = t  # local t and not account for scr refresh
                sound19_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_3.status = STARTED
                sound19_3.play(when=win)  # sync with win flip
            
            # if sound19_3 is stopping this frame...
            if sound19_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_3.tStop = t  # not accounting for scr refresh
                    sound19_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_3.status = FINISHED
                    sound19_3.stop()
            # update sound19_3 status according to whether it's playing
            if sound19_3.isPlaying:
                sound19_3.status = STARTED
            elif sound19_3.isFinished:
                sound19_3.status = FINISHED
            
            # if sound19_4 is starting this frame...
            if sound19_4.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_4.frameNStart = frameN  # exact frame index
                sound19_4.tStart = t  # local t and not account for scr refresh
                sound19_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_4.status = STARTED
                sound19_4.play(when=win)  # sync with win flip
            
            # if sound19_4 is stopping this frame...
            if sound19_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_4.tStop = t  # not accounting for scr refresh
                    sound19_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_4.status = FINISHED
                    sound19_4.stop()
            # update sound19_4 status according to whether it's playing
            if sound19_4.isPlaying:
                sound19_4.status = STARTED
            elif sound19_4.isFinished:
                sound19_4.status = FINISHED
            
            # if sound19_5 is starting this frame...
            if sound19_5.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_5.frameNStart = frameN  # exact frame index
                sound19_5.tStart = t  # local t and not account for scr refresh
                sound19_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_5.status = STARTED
                sound19_5.play(when=win)  # sync with win flip
            
            # if sound19_5 is stopping this frame...
            if sound19_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_5.tStop = t  # not accounting for scr refresh
                    sound19_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_5.status = FINISHED
                    sound19_5.stop()
            # update sound19_5 status according to whether it's playing
            if sound19_5.isPlaying:
                sound19_5.status = STARTED
            elif sound19_5.isFinished:
                sound19_5.status = FINISHED
            
            # if sound19_6 is starting this frame...
            if sound19_6.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_6.frameNStart = frameN  # exact frame index
                sound19_6.tStart = t  # local t and not account for scr refresh
                sound19_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_6.status = STARTED
                sound19_6.play(when=win)  # sync with win flip
            
            # if sound19_6 is stopping this frame...
            if sound19_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_6.tStop = t  # not accounting for scr refresh
                    sound19_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_6.status = FINISHED
                    sound19_6.stop()
            # update sound19_6 status according to whether it's playing
            if sound19_6.isPlaying:
                sound19_6.status = STARTED
            elif sound19_6.isFinished:
                sound19_6.status = FINISHED
            
            # if sound19_7 is starting this frame...
            if sound19_7.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_7.frameNStart = frameN  # exact frame index
                sound19_7.tStart = t  # local t and not account for scr refresh
                sound19_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_7.status = STARTED
                sound19_7.play(when=win)  # sync with win flip
            
            # if sound19_7 is stopping this frame...
            if sound19_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_7.tStop = t  # not accounting for scr refresh
                    sound19_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_7.status = FINISHED
                    sound19_7.stop()
            # update sound19_7 status according to whether it's playing
            if sound19_7.isPlaying:
                sound19_7.status = STARTED
            elif sound19_7.isFinished:
                sound19_7.status = FINISHED
            
            # if sound19_8 is starting this frame...
            if sound19_8.status == NOT_STARTED and tThisFlip >= starttime[17]-frameTolerance:
                # keep track of start time/frame for later
                sound19_8.frameNStart = frameN  # exact frame index
                sound19_8.tStart = t  # local t and not account for scr refresh
                sound19_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound19_8.status = STARTED
                sound19_8.play(when=win)  # sync with win flip
            
            # if sound19_8 is stopping this frame...
            if sound19_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound19_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound19_8.tStop = t  # not accounting for scr refresh
                    sound19_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound19_8.status = FINISHED
                    sound19_8.stop()
            # update sound19_8 status according to whether it's playing
            if sound19_8.isPlaying:
                sound19_8.status = STARTED
            elif sound19_8.isFinished:
                sound19_8.status = FINISHED
            
            # if sound20 is starting this frame...
            if sound20.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20.frameNStart = frameN  # exact frame index
                sound20.tStart = t  # local t and not account for scr refresh
                sound20.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20.status = STARTED
                sound20.play(when=win)  # sync with win flip
            
            # if sound20 is stopping this frame...
            if sound20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20.tStop = t  # not accounting for scr refresh
                    sound20.frameNStop = frameN  # exact frame index
                    # update status
                    sound20.status = FINISHED
                    sound20.stop()
            # update sound20 status according to whether it's playing
            if sound20.isPlaying:
                sound20.status = STARTED
            elif sound20.isFinished:
                sound20.status = FINISHED
            
            # if sound20_2 is starting this frame...
            if sound20_2.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_2.frameNStart = frameN  # exact frame index
                sound20_2.tStart = t  # local t and not account for scr refresh
                sound20_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_2.status = STARTED
                sound20_2.play(when=win)  # sync with win flip
            
            # if sound20_2 is stopping this frame...
            if sound20_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_2.tStop = t  # not accounting for scr refresh
                    sound20_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_2.status = FINISHED
                    sound20_2.stop()
            # update sound20_2 status according to whether it's playing
            if sound20_2.isPlaying:
                sound20_2.status = STARTED
            elif sound20_2.isFinished:
                sound20_2.status = FINISHED
            
            # if sound20_3 is starting this frame...
            if sound20_3.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_3.frameNStart = frameN  # exact frame index
                sound20_3.tStart = t  # local t and not account for scr refresh
                sound20_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_3.status = STARTED
                sound20_3.play(when=win)  # sync with win flip
            
            # if sound20_3 is stopping this frame...
            if sound20_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_3.tStop = t  # not accounting for scr refresh
                    sound20_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_3.status = FINISHED
                    sound20_3.stop()
            # update sound20_3 status according to whether it's playing
            if sound20_3.isPlaying:
                sound20_3.status = STARTED
            elif sound20_3.isFinished:
                sound20_3.status = FINISHED
            
            # if sound20_4 is starting this frame...
            if sound20_4.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_4.frameNStart = frameN  # exact frame index
                sound20_4.tStart = t  # local t and not account for scr refresh
                sound20_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_4.status = STARTED
                sound20_4.play(when=win)  # sync with win flip
            
            # if sound20_4 is stopping this frame...
            if sound20_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_4.tStop = t  # not accounting for scr refresh
                    sound20_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_4.status = FINISHED
                    sound20_4.stop()
            # update sound20_4 status according to whether it's playing
            if sound20_4.isPlaying:
                sound20_4.status = STARTED
            elif sound20_4.isFinished:
                sound20_4.status = FINISHED
            
            # if sound20_5 is starting this frame...
            if sound20_5.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_5.frameNStart = frameN  # exact frame index
                sound20_5.tStart = t  # local t and not account for scr refresh
                sound20_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_5.status = STARTED
                sound20_5.play(when=win)  # sync with win flip
            
            # if sound20_5 is stopping this frame...
            if sound20_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_5.tStop = t  # not accounting for scr refresh
                    sound20_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_5.status = FINISHED
                    sound20_5.stop()
            # update sound20_5 status according to whether it's playing
            if sound20_5.isPlaying:
                sound20_5.status = STARTED
            elif sound20_5.isFinished:
                sound20_5.status = FINISHED
            
            # if sound20_6 is starting this frame...
            if sound20_6.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_6.frameNStart = frameN  # exact frame index
                sound20_6.tStart = t  # local t and not account for scr refresh
                sound20_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_6.status = STARTED
                sound20_6.play(when=win)  # sync with win flip
            
            # if sound20_6 is stopping this frame...
            if sound20_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_6.tStop = t  # not accounting for scr refresh
                    sound20_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_6.status = FINISHED
                    sound20_6.stop()
            # update sound20_6 status according to whether it's playing
            if sound20_6.isPlaying:
                sound20_6.status = STARTED
            elif sound20_6.isFinished:
                sound20_6.status = FINISHED
            
            # if sound20_7 is starting this frame...
            if sound20_7.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_7.frameNStart = frameN  # exact frame index
                sound20_7.tStart = t  # local t and not account for scr refresh
                sound20_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_7.status = STARTED
                sound20_7.play(when=win)  # sync with win flip
            
            # if sound20_7 is stopping this frame...
            if sound20_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_7.tStop = t  # not accounting for scr refresh
                    sound20_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_7.status = FINISHED
                    sound20_7.stop()
            # update sound20_7 status according to whether it's playing
            if sound20_7.isPlaying:
                sound20_7.status = STARTED
            elif sound20_7.isFinished:
                sound20_7.status = FINISHED
            
            # if sound20_8 is starting this frame...
            if sound20_8.status == NOT_STARTED and tThisFlip >= starttime[18]-frameTolerance:
                # keep track of start time/frame for later
                sound20_8.frameNStart = frameN  # exact frame index
                sound20_8.tStart = t  # local t and not account for scr refresh
                sound20_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound20_8.status = STARTED
                sound20_8.play(when=win)  # sync with win flip
            
            # if sound20_8 is stopping this frame...
            if sound20_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound20_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound20_8.tStop = t  # not accounting for scr refresh
                    sound20_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound20_8.status = FINISHED
                    sound20_8.stop()
            # update sound20_8 status according to whether it's playing
            if sound20_8.isPlaying:
                sound20_8.status = STARTED
            elif sound20_8.isFinished:
                sound20_8.status = FINISHED
            
            # if sound21 is starting this frame...
            if sound21.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21.frameNStart = frameN  # exact frame index
                sound21.tStart = t  # local t and not account for scr refresh
                sound21.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21.status = STARTED
                sound21.play(when=win)  # sync with win flip
            
            # if sound21 is stopping this frame...
            if sound21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21.tStop = t  # not accounting for scr refresh
                    sound21.frameNStop = frameN  # exact frame index
                    # update status
                    sound21.status = FINISHED
                    sound21.stop()
            # update sound21 status according to whether it's playing
            if sound21.isPlaying:
                sound21.status = STARTED
            elif sound21.isFinished:
                sound21.status = FINISHED
            
            # if sound21_2 is starting this frame...
            if sound21_2.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_2.frameNStart = frameN  # exact frame index
                sound21_2.tStart = t  # local t and not account for scr refresh
                sound21_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_2.status = STARTED
                sound21_2.play(when=win)  # sync with win flip
            
            # if sound21_2 is stopping this frame...
            if sound21_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_2.tStop = t  # not accounting for scr refresh
                    sound21_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_2.status = FINISHED
                    sound21_2.stop()
            # update sound21_2 status according to whether it's playing
            if sound21_2.isPlaying:
                sound21_2.status = STARTED
            elif sound21_2.isFinished:
                sound21_2.status = FINISHED
            
            # if sound21_3 is starting this frame...
            if sound21_3.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_3.frameNStart = frameN  # exact frame index
                sound21_3.tStart = t  # local t and not account for scr refresh
                sound21_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_3.status = STARTED
                sound21_3.play(when=win)  # sync with win flip
            
            # if sound21_3 is stopping this frame...
            if sound21_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_3.tStop = t  # not accounting for scr refresh
                    sound21_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_3.status = FINISHED
                    sound21_3.stop()
            # update sound21_3 status according to whether it's playing
            if sound21_3.isPlaying:
                sound21_3.status = STARTED
            elif sound21_3.isFinished:
                sound21_3.status = FINISHED
            
            # if sound21_4 is starting this frame...
            if sound21_4.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_4.frameNStart = frameN  # exact frame index
                sound21_4.tStart = t  # local t and not account for scr refresh
                sound21_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_4.status = STARTED
                sound21_4.play(when=win)  # sync with win flip
            
            # if sound21_4 is stopping this frame...
            if sound21_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_4.tStop = t  # not accounting for scr refresh
                    sound21_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_4.status = FINISHED
                    sound21_4.stop()
            # update sound21_4 status according to whether it's playing
            if sound21_4.isPlaying:
                sound21_4.status = STARTED
            elif sound21_4.isFinished:
                sound21_4.status = FINISHED
            
            # if sound21_5 is starting this frame...
            if sound21_5.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_5.frameNStart = frameN  # exact frame index
                sound21_5.tStart = t  # local t and not account for scr refresh
                sound21_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_5.status = STARTED
                sound21_5.play(when=win)  # sync with win flip
            
            # if sound21_5 is stopping this frame...
            if sound21_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_5.tStop = t  # not accounting for scr refresh
                    sound21_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_5.status = FINISHED
                    sound21_5.stop()
            # update sound21_5 status according to whether it's playing
            if sound21_5.isPlaying:
                sound21_5.status = STARTED
            elif sound21_5.isFinished:
                sound21_5.status = FINISHED
            
            # if sound21_6 is starting this frame...
            if sound21_6.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_6.frameNStart = frameN  # exact frame index
                sound21_6.tStart = t  # local t and not account for scr refresh
                sound21_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_6.status = STARTED
                sound21_6.play(when=win)  # sync with win flip
            
            # if sound21_6 is stopping this frame...
            if sound21_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_6.tStop = t  # not accounting for scr refresh
                    sound21_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_6.status = FINISHED
                    sound21_6.stop()
            # update sound21_6 status according to whether it's playing
            if sound21_6.isPlaying:
                sound21_6.status = STARTED
            elif sound21_6.isFinished:
                sound21_6.status = FINISHED
            
            # if sound21_7 is starting this frame...
            if sound21_7.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_7.frameNStart = frameN  # exact frame index
                sound21_7.tStart = t  # local t and not account for scr refresh
                sound21_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_7.status = STARTED
                sound21_7.play(when=win)  # sync with win flip
            
            # if sound21_7 is stopping this frame...
            if sound21_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_7.tStop = t  # not accounting for scr refresh
                    sound21_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_7.status = FINISHED
                    sound21_7.stop()
            # update sound21_7 status according to whether it's playing
            if sound21_7.isPlaying:
                sound21_7.status = STARTED
            elif sound21_7.isFinished:
                sound21_7.status = FINISHED
            
            # if sound21_8 is starting this frame...
            if sound21_8.status == NOT_STARTED and tThisFlip >= starttime[19]-frameTolerance:
                # keep track of start time/frame for later
                sound21_8.frameNStart = frameN  # exact frame index
                sound21_8.tStart = t  # local t and not account for scr refresh
                sound21_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound21_8.status = STARTED
                sound21_8.play(when=win)  # sync with win flip
            
            # if sound21_8 is stopping this frame...
            if sound21_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound21_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound21_8.tStop = t  # not accounting for scr refresh
                    sound21_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound21_8.status = FINISHED
                    sound21_8.stop()
            # update sound21_8 status according to whether it's playing
            if sound21_8.isPlaying:
                sound21_8.status = STARTED
            elif sound21_8.isFinished:
                sound21_8.status = FINISHED
            
            # if sound22 is starting this frame...
            if sound22.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22.frameNStart = frameN  # exact frame index
                sound22.tStart = t  # local t and not account for scr refresh
                sound22.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22.status = STARTED
                sound22.play(when=win)  # sync with win flip
            
            # if sound22 is stopping this frame...
            if sound22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22.tStop = t  # not accounting for scr refresh
                    sound22.frameNStop = frameN  # exact frame index
                    # update status
                    sound22.status = FINISHED
                    sound22.stop()
            # update sound22 status according to whether it's playing
            if sound22.isPlaying:
                sound22.status = STARTED
            elif sound22.isFinished:
                sound22.status = FINISHED
            
            # if sound22_2 is starting this frame...
            if sound22_2.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_2.frameNStart = frameN  # exact frame index
                sound22_2.tStart = t  # local t and not account for scr refresh
                sound22_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_2.status = STARTED
                sound22_2.play(when=win)  # sync with win flip
            
            # if sound22_2 is stopping this frame...
            if sound22_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_2.tStop = t  # not accounting for scr refresh
                    sound22_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_2.status = FINISHED
                    sound22_2.stop()
            # update sound22_2 status according to whether it's playing
            if sound22_2.isPlaying:
                sound22_2.status = STARTED
            elif sound22_2.isFinished:
                sound22_2.status = FINISHED
            
            # if sound22_3 is starting this frame...
            if sound22_3.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_3.frameNStart = frameN  # exact frame index
                sound22_3.tStart = t  # local t and not account for scr refresh
                sound22_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_3.status = STARTED
                sound22_3.play(when=win)  # sync with win flip
            
            # if sound22_3 is stopping this frame...
            if sound22_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_3.tStop = t  # not accounting for scr refresh
                    sound22_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_3.status = FINISHED
                    sound22_3.stop()
            # update sound22_3 status according to whether it's playing
            if sound22_3.isPlaying:
                sound22_3.status = STARTED
            elif sound22_3.isFinished:
                sound22_3.status = FINISHED
            
            # if sound22_4 is starting this frame...
            if sound22_4.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_4.frameNStart = frameN  # exact frame index
                sound22_4.tStart = t  # local t and not account for scr refresh
                sound22_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_4.status = STARTED
                sound22_4.play(when=win)  # sync with win flip
            
            # if sound22_4 is stopping this frame...
            if sound22_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_4.tStop = t  # not accounting for scr refresh
                    sound22_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_4.status = FINISHED
                    sound22_4.stop()
            # update sound22_4 status according to whether it's playing
            if sound22_4.isPlaying:
                sound22_4.status = STARTED
            elif sound22_4.isFinished:
                sound22_4.status = FINISHED
            
            # if sound22_5 is starting this frame...
            if sound22_5.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_5.frameNStart = frameN  # exact frame index
                sound22_5.tStart = t  # local t and not account for scr refresh
                sound22_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_5.status = STARTED
                sound22_5.play(when=win)  # sync with win flip
            
            # if sound22_5 is stopping this frame...
            if sound22_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_5.tStop = t  # not accounting for scr refresh
                    sound22_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_5.status = FINISHED
                    sound22_5.stop()
            # update sound22_5 status according to whether it's playing
            if sound22_5.isPlaying:
                sound22_5.status = STARTED
            elif sound22_5.isFinished:
                sound22_5.status = FINISHED
            
            # if sound22_6 is starting this frame...
            if sound22_6.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_6.frameNStart = frameN  # exact frame index
                sound22_6.tStart = t  # local t and not account for scr refresh
                sound22_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_6.status = STARTED
                sound22_6.play(when=win)  # sync with win flip
            
            # if sound22_6 is stopping this frame...
            if sound22_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_6.tStop = t  # not accounting for scr refresh
                    sound22_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_6.status = FINISHED
                    sound22_6.stop()
            # update sound22_6 status according to whether it's playing
            if sound22_6.isPlaying:
                sound22_6.status = STARTED
            elif sound22_6.isFinished:
                sound22_6.status = FINISHED
            
            # if sound22_7 is starting this frame...
            if sound22_7.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_7.frameNStart = frameN  # exact frame index
                sound22_7.tStart = t  # local t and not account for scr refresh
                sound22_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_7.status = STARTED
                sound22_7.play(when=win)  # sync with win flip
            
            # if sound22_7 is stopping this frame...
            if sound22_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_7.tStop = t  # not accounting for scr refresh
                    sound22_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_7.status = FINISHED
                    sound22_7.stop()
            # update sound22_7 status according to whether it's playing
            if sound22_7.isPlaying:
                sound22_7.status = STARTED
            elif sound22_7.isFinished:
                sound22_7.status = FINISHED
            
            # if sound22_8 is starting this frame...
            if sound22_8.status == NOT_STARTED and tThisFlip >= starttime[20]-frameTolerance:
                # keep track of start time/frame for later
                sound22_8.frameNStart = frameN  # exact frame index
                sound22_8.tStart = t  # local t and not account for scr refresh
                sound22_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound22_8.status = STARTED
                sound22_8.play(when=win)  # sync with win flip
            
            # if sound22_8 is stopping this frame...
            if sound22_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound22_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound22_8.tStop = t  # not accounting for scr refresh
                    sound22_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound22_8.status = FINISHED
                    sound22_8.stop()
            # update sound22_8 status according to whether it's playing
            if sound22_8.isPlaying:
                sound22_8.status = STARTED
            elif sound22_8.isFinished:
                sound22_8.status = FINISHED
            
            # if sound23 is starting this frame...
            if sound23.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23.frameNStart = frameN  # exact frame index
                sound23.tStart = t  # local t and not account for scr refresh
                sound23.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23.status = STARTED
                sound23.play(when=win)  # sync with win flip
            
            # if sound23 is stopping this frame...
            if sound23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23.tStop = t  # not accounting for scr refresh
                    sound23.frameNStop = frameN  # exact frame index
                    # update status
                    sound23.status = FINISHED
                    sound23.stop()
            # update sound23 status according to whether it's playing
            if sound23.isPlaying:
                sound23.status = STARTED
            elif sound23.isFinished:
                sound23.status = FINISHED
            
            # if sound23_2 is starting this frame...
            if sound23_2.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_2.frameNStart = frameN  # exact frame index
                sound23_2.tStart = t  # local t and not account for scr refresh
                sound23_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_2.status = STARTED
                sound23_2.play(when=win)  # sync with win flip
            
            # if sound23_2 is stopping this frame...
            if sound23_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_2.tStop = t  # not accounting for scr refresh
                    sound23_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_2.status = FINISHED
                    sound23_2.stop()
            # update sound23_2 status according to whether it's playing
            if sound23_2.isPlaying:
                sound23_2.status = STARTED
            elif sound23_2.isFinished:
                sound23_2.status = FINISHED
            
            # if sound23_3 is starting this frame...
            if sound23_3.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_3.frameNStart = frameN  # exact frame index
                sound23_3.tStart = t  # local t and not account for scr refresh
                sound23_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_3.status = STARTED
                sound23_3.play(when=win)  # sync with win flip
            
            # if sound23_3 is stopping this frame...
            if sound23_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_3.tStop = t  # not accounting for scr refresh
                    sound23_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_3.status = FINISHED
                    sound23_3.stop()
            # update sound23_3 status according to whether it's playing
            if sound23_3.isPlaying:
                sound23_3.status = STARTED
            elif sound23_3.isFinished:
                sound23_3.status = FINISHED
            
            # if sound23_4 is starting this frame...
            if sound23_4.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_4.frameNStart = frameN  # exact frame index
                sound23_4.tStart = t  # local t and not account for scr refresh
                sound23_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_4.status = STARTED
                sound23_4.play(when=win)  # sync with win flip
            
            # if sound23_4 is stopping this frame...
            if sound23_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_4.tStop = t  # not accounting for scr refresh
                    sound23_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_4.status = FINISHED
                    sound23_4.stop()
            # update sound23_4 status according to whether it's playing
            if sound23_4.isPlaying:
                sound23_4.status = STARTED
            elif sound23_4.isFinished:
                sound23_4.status = FINISHED
            
            # if sound23_5 is starting this frame...
            if sound23_5.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_5.frameNStart = frameN  # exact frame index
                sound23_5.tStart = t  # local t and not account for scr refresh
                sound23_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_5.status = STARTED
                sound23_5.play(when=win)  # sync with win flip
            
            # if sound23_5 is stopping this frame...
            if sound23_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_5.tStop = t  # not accounting for scr refresh
                    sound23_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_5.status = FINISHED
                    sound23_5.stop()
            # update sound23_5 status according to whether it's playing
            if sound23_5.isPlaying:
                sound23_5.status = STARTED
            elif sound23_5.isFinished:
                sound23_5.status = FINISHED
            
            # if sound23_6 is starting this frame...
            if sound23_6.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_6.frameNStart = frameN  # exact frame index
                sound23_6.tStart = t  # local t and not account for scr refresh
                sound23_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_6.status = STARTED
                sound23_6.play(when=win)  # sync with win flip
            
            # if sound23_6 is stopping this frame...
            if sound23_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_6.tStop = t  # not accounting for scr refresh
                    sound23_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_6.status = FINISHED
                    sound23_6.stop()
            # update sound23_6 status according to whether it's playing
            if sound23_6.isPlaying:
                sound23_6.status = STARTED
            elif sound23_6.isFinished:
                sound23_6.status = FINISHED
            
            # if sound23_7 is starting this frame...
            if sound23_7.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_7.frameNStart = frameN  # exact frame index
                sound23_7.tStart = t  # local t and not account for scr refresh
                sound23_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_7.status = STARTED
                sound23_7.play(when=win)  # sync with win flip
            
            # if sound23_7 is stopping this frame...
            if sound23_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_7.tStop = t  # not accounting for scr refresh
                    sound23_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_7.status = FINISHED
                    sound23_7.stop()
            # update sound23_7 status according to whether it's playing
            if sound23_7.isPlaying:
                sound23_7.status = STARTED
            elif sound23_7.isFinished:
                sound23_7.status = FINISHED
            
            # if sound23_8 is starting this frame...
            if sound23_8.status == NOT_STARTED and tThisFlip >= starttime[21]-frameTolerance:
                # keep track of start time/frame for later
                sound23_8.frameNStart = frameN  # exact frame index
                sound23_8.tStart = t  # local t and not account for scr refresh
                sound23_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound23_8.status = STARTED
                sound23_8.play(when=win)  # sync with win flip
            
            # if sound23_8 is stopping this frame...
            if sound23_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound23_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound23_8.tStop = t  # not accounting for scr refresh
                    sound23_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound23_8.status = FINISHED
                    sound23_8.stop()
            # update sound23_8 status according to whether it's playing
            if sound23_8.isPlaying:
                sound23_8.status = STARTED
            elif sound23_8.isFinished:
                sound23_8.status = FINISHED
            
            # if sound24 is starting this frame...
            if sound24.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24.frameNStart = frameN  # exact frame index
                sound24.tStart = t  # local t and not account for scr refresh
                sound24.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24.status = STARTED
                sound24.play(when=win)  # sync with win flip
            
            # if sound24 is stopping this frame...
            if sound24.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24.tStop = t  # not accounting for scr refresh
                    sound24.frameNStop = frameN  # exact frame index
                    # update status
                    sound24.status = FINISHED
                    sound24.stop()
            # update sound24 status according to whether it's playing
            if sound24.isPlaying:
                sound24.status = STARTED
            elif sound24.isFinished:
                sound24.status = FINISHED
            
            # if sound24_2 is starting this frame...
            if sound24_2.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_2.frameNStart = frameN  # exact frame index
                sound24_2.tStart = t  # local t and not account for scr refresh
                sound24_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_2.status = STARTED
                sound24_2.play(when=win)  # sync with win flip
            
            # if sound24_2 is stopping this frame...
            if sound24_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_2.tStop = t  # not accounting for scr refresh
                    sound24_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_2.status = FINISHED
                    sound24_2.stop()
            # update sound24_2 status according to whether it's playing
            if sound24_2.isPlaying:
                sound24_2.status = STARTED
            elif sound24_2.isFinished:
                sound24_2.status = FINISHED
            
            # if sound24_3 is starting this frame...
            if sound24_3.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_3.frameNStart = frameN  # exact frame index
                sound24_3.tStart = t  # local t and not account for scr refresh
                sound24_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_3.status = STARTED
                sound24_3.play(when=win)  # sync with win flip
            
            # if sound24_3 is stopping this frame...
            if sound24_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_3.tStop = t  # not accounting for scr refresh
                    sound24_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_3.status = FINISHED
                    sound24_3.stop()
            # update sound24_3 status according to whether it's playing
            if sound24_3.isPlaying:
                sound24_3.status = STARTED
            elif sound24_3.isFinished:
                sound24_3.status = FINISHED
            
            # if sound24_4 is starting this frame...
            if sound24_4.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_4.frameNStart = frameN  # exact frame index
                sound24_4.tStart = t  # local t and not account for scr refresh
                sound24_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_4.status = STARTED
                sound24_4.play(when=win)  # sync with win flip
            
            # if sound24_4 is stopping this frame...
            if sound24_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_4.tStop = t  # not accounting for scr refresh
                    sound24_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_4.status = FINISHED
                    sound24_4.stop()
            # update sound24_4 status according to whether it's playing
            if sound24_4.isPlaying:
                sound24_4.status = STARTED
            elif sound24_4.isFinished:
                sound24_4.status = FINISHED
            
            # if sound24_5 is starting this frame...
            if sound24_5.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_5.frameNStart = frameN  # exact frame index
                sound24_5.tStart = t  # local t and not account for scr refresh
                sound24_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_5.status = STARTED
                sound24_5.play(when=win)  # sync with win flip
            
            # if sound24_5 is stopping this frame...
            if sound24_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_5.tStop = t  # not accounting for scr refresh
                    sound24_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_5.status = FINISHED
                    sound24_5.stop()
            # update sound24_5 status according to whether it's playing
            if sound24_5.isPlaying:
                sound24_5.status = STARTED
            elif sound24_5.isFinished:
                sound24_5.status = FINISHED
            
            # if sound24_6 is starting this frame...
            if sound24_6.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_6.frameNStart = frameN  # exact frame index
                sound24_6.tStart = t  # local t and not account for scr refresh
                sound24_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_6.status = STARTED
                sound24_6.play(when=win)  # sync with win flip
            
            # if sound24_6 is stopping this frame...
            if sound24_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_6.tStop = t  # not accounting for scr refresh
                    sound24_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_6.status = FINISHED
                    sound24_6.stop()
            # update sound24_6 status according to whether it's playing
            if sound24_6.isPlaying:
                sound24_6.status = STARTED
            elif sound24_6.isFinished:
                sound24_6.status = FINISHED
            
            # if sound24_7 is starting this frame...
            if sound24_7.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_7.frameNStart = frameN  # exact frame index
                sound24_7.tStart = t  # local t and not account for scr refresh
                sound24_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_7.status = STARTED
                sound24_7.play(when=win)  # sync with win flip
            
            # if sound24_7 is stopping this frame...
            if sound24_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_7.tStop = t  # not accounting for scr refresh
                    sound24_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_7.status = FINISHED
                    sound24_7.stop()
            # update sound24_7 status according to whether it's playing
            if sound24_7.isPlaying:
                sound24_7.status = STARTED
            elif sound24_7.isFinished:
                sound24_7.status = FINISHED
            
            # if sound24_8 is starting this frame...
            if sound24_8.status == NOT_STARTED and tThisFlip >= starttime[22]-frameTolerance:
                # keep track of start time/frame for later
                sound24_8.frameNStart = frameN  # exact frame index
                sound24_8.tStart = t  # local t and not account for scr refresh
                sound24_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound24_8.status = STARTED
                sound24_8.play(when=win)  # sync with win flip
            
            # if sound24_8 is stopping this frame...
            if sound24_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound24_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound24_8.tStop = t  # not accounting for scr refresh
                    sound24_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound24_8.status = FINISHED
                    sound24_8.stop()
            # update sound24_8 status according to whether it's playing
            if sound24_8.isPlaying:
                sound24_8.status = STARTED
            elif sound24_8.isFinished:
                sound24_8.status = FINISHED
            
            # if sound25 is starting this frame...
            if sound25.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25.frameNStart = frameN  # exact frame index
                sound25.tStart = t  # local t and not account for scr refresh
                sound25.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25.status = STARTED
                sound25.play(when=win)  # sync with win flip
            
            # if sound25 is stopping this frame...
            if sound25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25.tStop = t  # not accounting for scr refresh
                    sound25.frameNStop = frameN  # exact frame index
                    # update status
                    sound25.status = FINISHED
                    sound25.stop()
            # update sound25 status according to whether it's playing
            if sound25.isPlaying:
                sound25.status = STARTED
            elif sound25.isFinished:
                sound25.status = FINISHED
            
            # if sound25_2 is starting this frame...
            if sound25_2.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_2.frameNStart = frameN  # exact frame index
                sound25_2.tStart = t  # local t and not account for scr refresh
                sound25_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_2.status = STARTED
                sound25_2.play(when=win)  # sync with win flip
            
            # if sound25_2 is stopping this frame...
            if sound25_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_2.tStop = t  # not accounting for scr refresh
                    sound25_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_2.status = FINISHED
                    sound25_2.stop()
            # update sound25_2 status according to whether it's playing
            if sound25_2.isPlaying:
                sound25_2.status = STARTED
            elif sound25_2.isFinished:
                sound25_2.status = FINISHED
            
            # if sound25_3 is starting this frame...
            if sound25_3.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_3.frameNStart = frameN  # exact frame index
                sound25_3.tStart = t  # local t and not account for scr refresh
                sound25_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_3.status = STARTED
                sound25_3.play(when=win)  # sync with win flip
            
            # if sound25_3 is stopping this frame...
            if sound25_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_3.tStop = t  # not accounting for scr refresh
                    sound25_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_3.status = FINISHED
                    sound25_3.stop()
            # update sound25_3 status according to whether it's playing
            if sound25_3.isPlaying:
                sound25_3.status = STARTED
            elif sound25_3.isFinished:
                sound25_3.status = FINISHED
            
            # if sound25_4 is starting this frame...
            if sound25_4.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_4.frameNStart = frameN  # exact frame index
                sound25_4.tStart = t  # local t and not account for scr refresh
                sound25_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_4.status = STARTED
                sound25_4.play(when=win)  # sync with win flip
            
            # if sound25_4 is stopping this frame...
            if sound25_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_4.tStop = t  # not accounting for scr refresh
                    sound25_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_4.status = FINISHED
                    sound25_4.stop()
            # update sound25_4 status according to whether it's playing
            if sound25_4.isPlaying:
                sound25_4.status = STARTED
            elif sound25_4.isFinished:
                sound25_4.status = FINISHED
            
            # if sound25_5 is starting this frame...
            if sound25_5.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_5.frameNStart = frameN  # exact frame index
                sound25_5.tStart = t  # local t and not account for scr refresh
                sound25_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_5.status = STARTED
                sound25_5.play(when=win)  # sync with win flip
            
            # if sound25_5 is stopping this frame...
            if sound25_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_5.tStop = t  # not accounting for scr refresh
                    sound25_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_5.status = FINISHED
                    sound25_5.stop()
            # update sound25_5 status according to whether it's playing
            if sound25_5.isPlaying:
                sound25_5.status = STARTED
            elif sound25_5.isFinished:
                sound25_5.status = FINISHED
            
            # if sound25_6 is starting this frame...
            if sound25_6.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_6.frameNStart = frameN  # exact frame index
                sound25_6.tStart = t  # local t and not account for scr refresh
                sound25_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_6.status = STARTED
                sound25_6.play(when=win)  # sync with win flip
            
            # if sound25_6 is stopping this frame...
            if sound25_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_6.tStop = t  # not accounting for scr refresh
                    sound25_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_6.status = FINISHED
                    sound25_6.stop()
            # update sound25_6 status according to whether it's playing
            if sound25_6.isPlaying:
                sound25_6.status = STARTED
            elif sound25_6.isFinished:
                sound25_6.status = FINISHED
            
            # if sound25_7 is starting this frame...
            if sound25_7.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_7.frameNStart = frameN  # exact frame index
                sound25_7.tStart = t  # local t and not account for scr refresh
                sound25_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_7.status = STARTED
                sound25_7.play(when=win)  # sync with win flip
            
            # if sound25_7 is stopping this frame...
            if sound25_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_7.tStop = t  # not accounting for scr refresh
                    sound25_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_7.status = FINISHED
                    sound25_7.stop()
            # update sound25_7 status according to whether it's playing
            if sound25_7.isPlaying:
                sound25_7.status = STARTED
            elif sound25_7.isFinished:
                sound25_7.status = FINISHED
            
            # if sound25_8 is starting this frame...
            if sound25_8.status == NOT_STARTED and tThisFlip >= starttime[23]-frameTolerance:
                # keep track of start time/frame for later
                sound25_8.frameNStart = frameN  # exact frame index
                sound25_8.tStart = t  # local t and not account for scr refresh
                sound25_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound25_8.status = STARTED
                sound25_8.play(when=win)  # sync with win flip
            
            # if sound25_8 is stopping this frame...
            if sound25_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound25_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound25_8.tStop = t  # not accounting for scr refresh
                    sound25_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound25_8.status = FINISHED
                    sound25_8.stop()
            # update sound25_8 status according to whether it's playing
            if sound25_8.isPlaying:
                sound25_8.status = STARTED
            elif sound25_8.isFinished:
                sound25_8.status = FINISHED
            
            # if sound26 is starting this frame...
            if sound26.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26.frameNStart = frameN  # exact frame index
                sound26.tStart = t  # local t and not account for scr refresh
                sound26.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26.status = STARTED
                sound26.play(when=win)  # sync with win flip
            
            # if sound26 is stopping this frame...
            if sound26.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26.tStop = t  # not accounting for scr refresh
                    sound26.frameNStop = frameN  # exact frame index
                    # update status
                    sound26.status = FINISHED
                    sound26.stop()
            # update sound26 status according to whether it's playing
            if sound26.isPlaying:
                sound26.status = STARTED
            elif sound26.isFinished:
                sound26.status = FINISHED
            
            # if sound26_2 is starting this frame...
            if sound26_2.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_2.frameNStart = frameN  # exact frame index
                sound26_2.tStart = t  # local t and not account for scr refresh
                sound26_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_2.status = STARTED
                sound26_2.play(when=win)  # sync with win flip
            
            # if sound26_2 is stopping this frame...
            if sound26_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_2.tStop = t  # not accounting for scr refresh
                    sound26_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_2.status = FINISHED
                    sound26_2.stop()
            # update sound26_2 status according to whether it's playing
            if sound26_2.isPlaying:
                sound26_2.status = STARTED
            elif sound26_2.isFinished:
                sound26_2.status = FINISHED
            
            # if sound26_3 is starting this frame...
            if sound26_3.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_3.frameNStart = frameN  # exact frame index
                sound26_3.tStart = t  # local t and not account for scr refresh
                sound26_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_3.status = STARTED
                sound26_3.play(when=win)  # sync with win flip
            
            # if sound26_3 is stopping this frame...
            if sound26_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_3.tStop = t  # not accounting for scr refresh
                    sound26_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_3.status = FINISHED
                    sound26_3.stop()
            # update sound26_3 status according to whether it's playing
            if sound26_3.isPlaying:
                sound26_3.status = STARTED
            elif sound26_3.isFinished:
                sound26_3.status = FINISHED
            
            # if sound26_4 is starting this frame...
            if sound26_4.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_4.frameNStart = frameN  # exact frame index
                sound26_4.tStart = t  # local t and not account for scr refresh
                sound26_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_4.status = STARTED
                sound26_4.play(when=win)  # sync with win flip
            
            # if sound26_4 is stopping this frame...
            if sound26_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_4.tStop = t  # not accounting for scr refresh
                    sound26_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_4.status = FINISHED
                    sound26_4.stop()
            # update sound26_4 status according to whether it's playing
            if sound26_4.isPlaying:
                sound26_4.status = STARTED
            elif sound26_4.isFinished:
                sound26_4.status = FINISHED
            
            # if sound26_5 is starting this frame...
            if sound26_5.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_5.frameNStart = frameN  # exact frame index
                sound26_5.tStart = t  # local t and not account for scr refresh
                sound26_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_5.status = STARTED
                sound26_5.play(when=win)  # sync with win flip
            
            # if sound26_5 is stopping this frame...
            if sound26_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_5.tStop = t  # not accounting for scr refresh
                    sound26_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_5.status = FINISHED
                    sound26_5.stop()
            # update sound26_5 status according to whether it's playing
            if sound26_5.isPlaying:
                sound26_5.status = STARTED
            elif sound26_5.isFinished:
                sound26_5.status = FINISHED
            
            # if sound26_6 is starting this frame...
            if sound26_6.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_6.frameNStart = frameN  # exact frame index
                sound26_6.tStart = t  # local t and not account for scr refresh
                sound26_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_6.status = STARTED
                sound26_6.play(when=win)  # sync with win flip
            
            # if sound26_6 is stopping this frame...
            if sound26_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_6.tStop = t  # not accounting for scr refresh
                    sound26_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_6.status = FINISHED
                    sound26_6.stop()
            # update sound26_6 status according to whether it's playing
            if sound26_6.isPlaying:
                sound26_6.status = STARTED
            elif sound26_6.isFinished:
                sound26_6.status = FINISHED
            
            # if sound26_7 is starting this frame...
            if sound26_7.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_7.frameNStart = frameN  # exact frame index
                sound26_7.tStart = t  # local t and not account for scr refresh
                sound26_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_7.status = STARTED
                sound26_7.play(when=win)  # sync with win flip
            
            # if sound26_7 is stopping this frame...
            if sound26_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_7.tStop = t  # not accounting for scr refresh
                    sound26_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_7.status = FINISHED
                    sound26_7.stop()
            # update sound26_7 status according to whether it's playing
            if sound26_7.isPlaying:
                sound26_7.status = STARTED
            elif sound26_7.isFinished:
                sound26_7.status = FINISHED
            
            # if sound26_8 is starting this frame...
            if sound26_8.status == NOT_STARTED and tThisFlip >= starttime[24]-frameTolerance:
                # keep track of start time/frame for later
                sound26_8.frameNStart = frameN  # exact frame index
                sound26_8.tStart = t  # local t and not account for scr refresh
                sound26_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound26_8.status = STARTED
                sound26_8.play(when=win)  # sync with win flip
            
            # if sound26_8 is stopping this frame...
            if sound26_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound26_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound26_8.tStop = t  # not accounting for scr refresh
                    sound26_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound26_8.status = FINISHED
                    sound26_8.stop()
            # update sound26_8 status according to whether it's playing
            if sound26_8.isPlaying:
                sound26_8.status = STARTED
            elif sound26_8.isFinished:
                sound26_8.status = FINISHED
            
            # if sound27 is starting this frame...
            if sound27.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27.frameNStart = frameN  # exact frame index
                sound27.tStart = t  # local t and not account for scr refresh
                sound27.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27.status = STARTED
                sound27.play(when=win)  # sync with win flip
            
            # if sound27 is stopping this frame...
            if sound27.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27.tStop = t  # not accounting for scr refresh
                    sound27.frameNStop = frameN  # exact frame index
                    # update status
                    sound27.status = FINISHED
                    sound27.stop()
            # update sound27 status according to whether it's playing
            if sound27.isPlaying:
                sound27.status = STARTED
            elif sound27.isFinished:
                sound27.status = FINISHED
            
            # if sound27_2 is starting this frame...
            if sound27_2.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_2.frameNStart = frameN  # exact frame index
                sound27_2.tStart = t  # local t and not account for scr refresh
                sound27_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_2.status = STARTED
                sound27_2.play(when=win)  # sync with win flip
            
            # if sound27_2 is stopping this frame...
            if sound27_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_2.tStop = t  # not accounting for scr refresh
                    sound27_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_2.status = FINISHED
                    sound27_2.stop()
            # update sound27_2 status according to whether it's playing
            if sound27_2.isPlaying:
                sound27_2.status = STARTED
            elif sound27_2.isFinished:
                sound27_2.status = FINISHED
            
            # if sound27_3 is starting this frame...
            if sound27_3.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_3.frameNStart = frameN  # exact frame index
                sound27_3.tStart = t  # local t and not account for scr refresh
                sound27_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_3.status = STARTED
                sound27_3.play(when=win)  # sync with win flip
            
            # if sound27_3 is stopping this frame...
            if sound27_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_3.tStop = t  # not accounting for scr refresh
                    sound27_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_3.status = FINISHED
                    sound27_3.stop()
            # update sound27_3 status according to whether it's playing
            if sound27_3.isPlaying:
                sound27_3.status = STARTED
            elif sound27_3.isFinished:
                sound27_3.status = FINISHED
            
            # if sound27_4 is starting this frame...
            if sound27_4.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_4.frameNStart = frameN  # exact frame index
                sound27_4.tStart = t  # local t and not account for scr refresh
                sound27_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_4.status = STARTED
                sound27_4.play(when=win)  # sync with win flip
            
            # if sound27_4 is stopping this frame...
            if sound27_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_4.tStop = t  # not accounting for scr refresh
                    sound27_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_4.status = FINISHED
                    sound27_4.stop()
            # update sound27_4 status according to whether it's playing
            if sound27_4.isPlaying:
                sound27_4.status = STARTED
            elif sound27_4.isFinished:
                sound27_4.status = FINISHED
            
            # if sound27_5 is starting this frame...
            if sound27_5.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_5.frameNStart = frameN  # exact frame index
                sound27_5.tStart = t  # local t and not account for scr refresh
                sound27_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_5.status = STARTED
                sound27_5.play(when=win)  # sync with win flip
            
            # if sound27_5 is stopping this frame...
            if sound27_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_5.tStop = t  # not accounting for scr refresh
                    sound27_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_5.status = FINISHED
                    sound27_5.stop()
            # update sound27_5 status according to whether it's playing
            if sound27_5.isPlaying:
                sound27_5.status = STARTED
            elif sound27_5.isFinished:
                sound27_5.status = FINISHED
            
            # if sound27_6 is starting this frame...
            if sound27_6.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_6.frameNStart = frameN  # exact frame index
                sound27_6.tStart = t  # local t and not account for scr refresh
                sound27_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_6.status = STARTED
                sound27_6.play(when=win)  # sync with win flip
            
            # if sound27_6 is stopping this frame...
            if sound27_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_6.tStop = t  # not accounting for scr refresh
                    sound27_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_6.status = FINISHED
                    sound27_6.stop()
            # update sound27_6 status according to whether it's playing
            if sound27_6.isPlaying:
                sound27_6.status = STARTED
            elif sound27_6.isFinished:
                sound27_6.status = FINISHED
            
            # if sound27_7 is starting this frame...
            if sound27_7.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_7.frameNStart = frameN  # exact frame index
                sound27_7.tStart = t  # local t and not account for scr refresh
                sound27_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_7.status = STARTED
                sound27_7.play(when=win)  # sync with win flip
            
            # if sound27_7 is stopping this frame...
            if sound27_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_7.tStop = t  # not accounting for scr refresh
                    sound27_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_7.status = FINISHED
                    sound27_7.stop()
            # update sound27_7 status according to whether it's playing
            if sound27_7.isPlaying:
                sound27_7.status = STARTED
            elif sound27_7.isFinished:
                sound27_7.status = FINISHED
            
            # if sound27_8 is starting this frame...
            if sound27_8.status == NOT_STARTED and tThisFlip >= starttime[25]-frameTolerance:
                # keep track of start time/frame for later
                sound27_8.frameNStart = frameN  # exact frame index
                sound27_8.tStart = t  # local t and not account for scr refresh
                sound27_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound27_8.status = STARTED
                sound27_8.play(when=win)  # sync with win flip
            
            # if sound27_8 is stopping this frame...
            if sound27_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound27_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound27_8.tStop = t  # not accounting for scr refresh
                    sound27_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound27_8.status = FINISHED
                    sound27_8.stop()
            # update sound27_8 status according to whether it's playing
            if sound27_8.isPlaying:
                sound27_8.status = STARTED
            elif sound27_8.isFinished:
                sound27_8.status = FINISHED
            
            # if sound28 is starting this frame...
            if sound28.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28.frameNStart = frameN  # exact frame index
                sound28.tStart = t  # local t and not account for scr refresh
                sound28.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28.status = STARTED
                sound28.play(when=win)  # sync with win flip
            
            # if sound28 is stopping this frame...
            if sound28.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28.tStop = t  # not accounting for scr refresh
                    sound28.frameNStop = frameN  # exact frame index
                    # update status
                    sound28.status = FINISHED
                    sound28.stop()
            # update sound28 status according to whether it's playing
            if sound28.isPlaying:
                sound28.status = STARTED
            elif sound28.isFinished:
                sound28.status = FINISHED
            
            # if sound28_2 is starting this frame...
            if sound28_2.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_2.frameNStart = frameN  # exact frame index
                sound28_2.tStart = t  # local t and not account for scr refresh
                sound28_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_2.status = STARTED
                sound28_2.play(when=win)  # sync with win flip
            
            # if sound28_2 is stopping this frame...
            if sound28_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_2.tStop = t  # not accounting for scr refresh
                    sound28_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_2.status = FINISHED
                    sound28_2.stop()
            # update sound28_2 status according to whether it's playing
            if sound28_2.isPlaying:
                sound28_2.status = STARTED
            elif sound28_2.isFinished:
                sound28_2.status = FINISHED
            
            # if sound28_3 is starting this frame...
            if sound28_3.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_3.frameNStart = frameN  # exact frame index
                sound28_3.tStart = t  # local t and not account for scr refresh
                sound28_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_3.status = STARTED
                sound28_3.play(when=win)  # sync with win flip
            
            # if sound28_3 is stopping this frame...
            if sound28_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_3.tStop = t  # not accounting for scr refresh
                    sound28_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_3.status = FINISHED
                    sound28_3.stop()
            # update sound28_3 status according to whether it's playing
            if sound28_3.isPlaying:
                sound28_3.status = STARTED
            elif sound28_3.isFinished:
                sound28_3.status = FINISHED
            
            # if sound28_4 is starting this frame...
            if sound28_4.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_4.frameNStart = frameN  # exact frame index
                sound28_4.tStart = t  # local t and not account for scr refresh
                sound28_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_4.status = STARTED
                sound28_4.play(when=win)  # sync with win flip
            
            # if sound28_4 is stopping this frame...
            if sound28_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_4.tStop = t  # not accounting for scr refresh
                    sound28_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_4.status = FINISHED
                    sound28_4.stop()
            # update sound28_4 status according to whether it's playing
            if sound28_4.isPlaying:
                sound28_4.status = STARTED
            elif sound28_4.isFinished:
                sound28_4.status = FINISHED
            
            # if sound28_5 is starting this frame...
            if sound28_5.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_5.frameNStart = frameN  # exact frame index
                sound28_5.tStart = t  # local t and not account for scr refresh
                sound28_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_5.status = STARTED
                sound28_5.play(when=win)  # sync with win flip
            
            # if sound28_5 is stopping this frame...
            if sound28_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_5.tStop = t  # not accounting for scr refresh
                    sound28_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_5.status = FINISHED
                    sound28_5.stop()
            # update sound28_5 status according to whether it's playing
            if sound28_5.isPlaying:
                sound28_5.status = STARTED
            elif sound28_5.isFinished:
                sound28_5.status = FINISHED
            
            # if sound28_6 is starting this frame...
            if sound28_6.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_6.frameNStart = frameN  # exact frame index
                sound28_6.tStart = t  # local t and not account for scr refresh
                sound28_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_6.status = STARTED
                sound28_6.play(when=win)  # sync with win flip
            
            # if sound28_6 is stopping this frame...
            if sound28_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_6.tStop = t  # not accounting for scr refresh
                    sound28_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_6.status = FINISHED
                    sound28_6.stop()
            # update sound28_6 status according to whether it's playing
            if sound28_6.isPlaying:
                sound28_6.status = STARTED
            elif sound28_6.isFinished:
                sound28_6.status = FINISHED
            
            # if sound28_7 is starting this frame...
            if sound28_7.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_7.frameNStart = frameN  # exact frame index
                sound28_7.tStart = t  # local t and not account for scr refresh
                sound28_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_7.status = STARTED
                sound28_7.play(when=win)  # sync with win flip
            
            # if sound28_7 is stopping this frame...
            if sound28_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_7.tStop = t  # not accounting for scr refresh
                    sound28_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_7.status = FINISHED
                    sound28_7.stop()
            # update sound28_7 status according to whether it's playing
            if sound28_7.isPlaying:
                sound28_7.status = STARTED
            elif sound28_7.isFinished:
                sound28_7.status = FINISHED
            
            # if sound28_8 is starting this frame...
            if sound28_8.status == NOT_STARTED and tThisFlip >= starttime[26]-frameTolerance:
                # keep track of start time/frame for later
                sound28_8.frameNStart = frameN  # exact frame index
                sound28_8.tStart = t  # local t and not account for scr refresh
                sound28_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound28_8.status = STARTED
                sound28_8.play(when=win)  # sync with win flip
            
            # if sound28_8 is stopping this frame...
            if sound28_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound28_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound28_8.tStop = t  # not accounting for scr refresh
                    sound28_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound28_8.status = FINISHED
                    sound28_8.stop()
            # update sound28_8 status according to whether it's playing
            if sound28_8.isPlaying:
                sound28_8.status = STARTED
            elif sound28_8.isFinished:
                sound28_8.status = FINISHED
            
            # if sound29 is starting this frame...
            if sound29.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29.frameNStart = frameN  # exact frame index
                sound29.tStart = t  # local t and not account for scr refresh
                sound29.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29.status = STARTED
                sound29.play(when=win)  # sync with win flip
            
            # if sound29 is stopping this frame...
            if sound29.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29.tStop = t  # not accounting for scr refresh
                    sound29.frameNStop = frameN  # exact frame index
                    # update status
                    sound29.status = FINISHED
                    sound29.stop()
            # update sound29 status according to whether it's playing
            if sound29.isPlaying:
                sound29.status = STARTED
            elif sound29.isFinished:
                sound29.status = FINISHED
            
            # if sound29_2 is starting this frame...
            if sound29_2.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_2.frameNStart = frameN  # exact frame index
                sound29_2.tStart = t  # local t and not account for scr refresh
                sound29_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_2.status = STARTED
                sound29_2.play(when=win)  # sync with win flip
            
            # if sound29_2 is stopping this frame...
            if sound29_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_2.tStop = t  # not accounting for scr refresh
                    sound29_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_2.status = FINISHED
                    sound29_2.stop()
            # update sound29_2 status according to whether it's playing
            if sound29_2.isPlaying:
                sound29_2.status = STARTED
            elif sound29_2.isFinished:
                sound29_2.status = FINISHED
            
            # if sound29_3 is starting this frame...
            if sound29_3.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_3.frameNStart = frameN  # exact frame index
                sound29_3.tStart = t  # local t and not account for scr refresh
                sound29_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_3.status = STARTED
                sound29_3.play(when=win)  # sync with win flip
            
            # if sound29_3 is stopping this frame...
            if sound29_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_3.tStop = t  # not accounting for scr refresh
                    sound29_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_3.status = FINISHED
                    sound29_3.stop()
            # update sound29_3 status according to whether it's playing
            if sound29_3.isPlaying:
                sound29_3.status = STARTED
            elif sound29_3.isFinished:
                sound29_3.status = FINISHED
            
            # if sound29_4 is starting this frame...
            if sound29_4.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_4.frameNStart = frameN  # exact frame index
                sound29_4.tStart = t  # local t and not account for scr refresh
                sound29_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_4.status = STARTED
                sound29_4.play(when=win)  # sync with win flip
            
            # if sound29_4 is stopping this frame...
            if sound29_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_4.tStop = t  # not accounting for scr refresh
                    sound29_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_4.status = FINISHED
                    sound29_4.stop()
            # update sound29_4 status according to whether it's playing
            if sound29_4.isPlaying:
                sound29_4.status = STARTED
            elif sound29_4.isFinished:
                sound29_4.status = FINISHED
            
            # if sound29_5 is starting this frame...
            if sound29_5.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_5.frameNStart = frameN  # exact frame index
                sound29_5.tStart = t  # local t and not account for scr refresh
                sound29_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_5.status = STARTED
                sound29_5.play(when=win)  # sync with win flip
            
            # if sound29_5 is stopping this frame...
            if sound29_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_5.tStop = t  # not accounting for scr refresh
                    sound29_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_5.status = FINISHED
                    sound29_5.stop()
            # update sound29_5 status according to whether it's playing
            if sound29_5.isPlaying:
                sound29_5.status = STARTED
            elif sound29_5.isFinished:
                sound29_5.status = FINISHED
            
            # if sound29_6 is starting this frame...
            if sound29_6.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_6.frameNStart = frameN  # exact frame index
                sound29_6.tStart = t  # local t and not account for scr refresh
                sound29_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_6.status = STARTED
                sound29_6.play(when=win)  # sync with win flip
            
            # if sound29_6 is stopping this frame...
            if sound29_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_6.tStop = t  # not accounting for scr refresh
                    sound29_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_6.status = FINISHED
                    sound29_6.stop()
            # update sound29_6 status according to whether it's playing
            if sound29_6.isPlaying:
                sound29_6.status = STARTED
            elif sound29_6.isFinished:
                sound29_6.status = FINISHED
            
            # if sound29_7 is starting this frame...
            if sound29_7.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_7.frameNStart = frameN  # exact frame index
                sound29_7.tStart = t  # local t and not account for scr refresh
                sound29_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_7.status = STARTED
                sound29_7.play(when=win)  # sync with win flip
            
            # if sound29_7 is stopping this frame...
            if sound29_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_7.tStop = t  # not accounting for scr refresh
                    sound29_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_7.status = FINISHED
                    sound29_7.stop()
            # update sound29_7 status according to whether it's playing
            if sound29_7.isPlaying:
                sound29_7.status = STARTED
            elif sound29_7.isFinished:
                sound29_7.status = FINISHED
            
            # if sound29_8 is starting this frame...
            if sound29_8.status == NOT_STARTED and tThisFlip >= starttime[27]-frameTolerance:
                # keep track of start time/frame for later
                sound29_8.frameNStart = frameN  # exact frame index
                sound29_8.tStart = t  # local t and not account for scr refresh
                sound29_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound29_8.status = STARTED
                sound29_8.play(when=win)  # sync with win flip
            
            # if sound29_8 is stopping this frame...
            if sound29_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound29_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound29_8.tStop = t  # not accounting for scr refresh
                    sound29_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound29_8.status = FINISHED
                    sound29_8.stop()
            # update sound29_8 status according to whether it's playing
            if sound29_8.isPlaying:
                sound29_8.status = STARTED
            elif sound29_8.isFinished:
                sound29_8.status = FINISHED
            
            # if sound30 is starting this frame...
            if sound30.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30.frameNStart = frameN  # exact frame index
                sound30.tStart = t  # local t and not account for scr refresh
                sound30.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30.status = STARTED
                sound30.play(when=win)  # sync with win flip
            
            # if sound30 is stopping this frame...
            if sound30.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30.tStop = t  # not accounting for scr refresh
                    sound30.frameNStop = frameN  # exact frame index
                    # update status
                    sound30.status = FINISHED
                    sound30.stop()
            # update sound30 status according to whether it's playing
            if sound30.isPlaying:
                sound30.status = STARTED
            elif sound30.isFinished:
                sound30.status = FINISHED
            
            # if sound30_2 is starting this frame...
            if sound30_2.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_2.frameNStart = frameN  # exact frame index
                sound30_2.tStart = t  # local t and not account for scr refresh
                sound30_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_2.status = STARTED
                sound30_2.play(when=win)  # sync with win flip
            
            # if sound30_2 is stopping this frame...
            if sound30_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_2.tStop = t  # not accounting for scr refresh
                    sound30_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_2.status = FINISHED
                    sound30_2.stop()
            # update sound30_2 status according to whether it's playing
            if sound30_2.isPlaying:
                sound30_2.status = STARTED
            elif sound30_2.isFinished:
                sound30_2.status = FINISHED
            
            # if sound30_3 is starting this frame...
            if sound30_3.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_3.frameNStart = frameN  # exact frame index
                sound30_3.tStart = t  # local t and not account for scr refresh
                sound30_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_3.status = STARTED
                sound30_3.play(when=win)  # sync with win flip
            
            # if sound30_3 is stopping this frame...
            if sound30_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_3.tStop = t  # not accounting for scr refresh
                    sound30_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_3.status = FINISHED
                    sound30_3.stop()
            # update sound30_3 status according to whether it's playing
            if sound30_3.isPlaying:
                sound30_3.status = STARTED
            elif sound30_3.isFinished:
                sound30_3.status = FINISHED
            
            # if sound30_4 is starting this frame...
            if sound30_4.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_4.frameNStart = frameN  # exact frame index
                sound30_4.tStart = t  # local t and not account for scr refresh
                sound30_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_4.status = STARTED
                sound30_4.play(when=win)  # sync with win flip
            
            # if sound30_4 is stopping this frame...
            if sound30_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_4.tStop = t  # not accounting for scr refresh
                    sound30_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_4.status = FINISHED
                    sound30_4.stop()
            # update sound30_4 status according to whether it's playing
            if sound30_4.isPlaying:
                sound30_4.status = STARTED
            elif sound30_4.isFinished:
                sound30_4.status = FINISHED
            
            # if sound30_5 is starting this frame...
            if sound30_5.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_5.frameNStart = frameN  # exact frame index
                sound30_5.tStart = t  # local t and not account for scr refresh
                sound30_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_5.status = STARTED
                sound30_5.play(when=win)  # sync with win flip
            
            # if sound30_5 is stopping this frame...
            if sound30_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_5.tStop = t  # not accounting for scr refresh
                    sound30_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_5.status = FINISHED
                    sound30_5.stop()
            # update sound30_5 status according to whether it's playing
            if sound30_5.isPlaying:
                sound30_5.status = STARTED
            elif sound30_5.isFinished:
                sound30_5.status = FINISHED
            
            # if sound30_6 is starting this frame...
            if sound30_6.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_6.frameNStart = frameN  # exact frame index
                sound30_6.tStart = t  # local t and not account for scr refresh
                sound30_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_6.status = STARTED
                sound30_6.play(when=win)  # sync with win flip
            
            # if sound30_6 is stopping this frame...
            if sound30_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_6.tStop = t  # not accounting for scr refresh
                    sound30_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_6.status = FINISHED
                    sound30_6.stop()
            # update sound30_6 status according to whether it's playing
            if sound30_6.isPlaying:
                sound30_6.status = STARTED
            elif sound30_6.isFinished:
                sound30_6.status = FINISHED
            
            # if sound30_7 is starting this frame...
            if sound30_7.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_7.frameNStart = frameN  # exact frame index
                sound30_7.tStart = t  # local t and not account for scr refresh
                sound30_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_7.status = STARTED
                sound30_7.play(when=win)  # sync with win flip
            
            # if sound30_7 is stopping this frame...
            if sound30_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_7.tStop = t  # not accounting for scr refresh
                    sound30_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_7.status = FINISHED
                    sound30_7.stop()
            # update sound30_7 status according to whether it's playing
            if sound30_7.isPlaying:
                sound30_7.status = STARTED
            elif sound30_7.isFinished:
                sound30_7.status = FINISHED
            
            # if sound30_8 is starting this frame...
            if sound30_8.status == NOT_STARTED and tThisFlip >= starttime[28]-frameTolerance:
                # keep track of start time/frame for later
                sound30_8.frameNStart = frameN  # exact frame index
                sound30_8.tStart = t  # local t and not account for scr refresh
                sound30_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound30_8.status = STARTED
                sound30_8.play(when=win)  # sync with win flip
            
            # if sound30_8 is stopping this frame...
            if sound30_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound30_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound30_8.tStop = t  # not accounting for scr refresh
                    sound30_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound30_8.status = FINISHED
                    sound30_8.stop()
            # update sound30_8 status according to whether it's playing
            if sound30_8.isPlaying:
                sound30_8.status = STARTED
            elif sound30_8.isFinished:
                sound30_8.status = FINISHED
            
            # if sound31 is starting this frame...
            if sound31.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31.frameNStart = frameN  # exact frame index
                sound31.tStart = t  # local t and not account for scr refresh
                sound31.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31.status = STARTED
                sound31.play(when=win)  # sync with win flip
            
            # if sound31 is stopping this frame...
            if sound31.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31.tStop = t  # not accounting for scr refresh
                    sound31.frameNStop = frameN  # exact frame index
                    # update status
                    sound31.status = FINISHED
                    sound31.stop()
            # update sound31 status according to whether it's playing
            if sound31.isPlaying:
                sound31.status = STARTED
            elif sound31.isFinished:
                sound31.status = FINISHED
            
            # if sound31_2 is starting this frame...
            if sound31_2.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_2.frameNStart = frameN  # exact frame index
                sound31_2.tStart = t  # local t and not account for scr refresh
                sound31_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_2.status = STARTED
                sound31_2.play(when=win)  # sync with win flip
            
            # if sound31_2 is stopping this frame...
            if sound31_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_2.tStop = t  # not accounting for scr refresh
                    sound31_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_2.status = FINISHED
                    sound31_2.stop()
            # update sound31_2 status according to whether it's playing
            if sound31_2.isPlaying:
                sound31_2.status = STARTED
            elif sound31_2.isFinished:
                sound31_2.status = FINISHED
            
            # if sound31_3 is starting this frame...
            if sound31_3.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_3.frameNStart = frameN  # exact frame index
                sound31_3.tStart = t  # local t and not account for scr refresh
                sound31_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_3.status = STARTED
                sound31_3.play(when=win)  # sync with win flip
            
            # if sound31_3 is stopping this frame...
            if sound31_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_3.tStop = t  # not accounting for scr refresh
                    sound31_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_3.status = FINISHED
                    sound31_3.stop()
            # update sound31_3 status according to whether it's playing
            if sound31_3.isPlaying:
                sound31_3.status = STARTED
            elif sound31_3.isFinished:
                sound31_3.status = FINISHED
            
            # if sound31_4 is starting this frame...
            if sound31_4.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_4.frameNStart = frameN  # exact frame index
                sound31_4.tStart = t  # local t and not account for scr refresh
                sound31_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_4.status = STARTED
                sound31_4.play(when=win)  # sync with win flip
            
            # if sound31_4 is stopping this frame...
            if sound31_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_4.tStop = t  # not accounting for scr refresh
                    sound31_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_4.status = FINISHED
                    sound31_4.stop()
            # update sound31_4 status according to whether it's playing
            if sound31_4.isPlaying:
                sound31_4.status = STARTED
            elif sound31_4.isFinished:
                sound31_4.status = FINISHED
            
            # if sound31_5 is starting this frame...
            if sound31_5.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_5.frameNStart = frameN  # exact frame index
                sound31_5.tStart = t  # local t and not account for scr refresh
                sound31_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_5.status = STARTED
                sound31_5.play(when=win)  # sync with win flip
            
            # if sound31_5 is stopping this frame...
            if sound31_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_5.tStop = t  # not accounting for scr refresh
                    sound31_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_5.status = FINISHED
                    sound31_5.stop()
            # update sound31_5 status according to whether it's playing
            if sound31_5.isPlaying:
                sound31_5.status = STARTED
            elif sound31_5.isFinished:
                sound31_5.status = FINISHED
            
            # if sound31_6 is starting this frame...
            if sound31_6.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_6.frameNStart = frameN  # exact frame index
                sound31_6.tStart = t  # local t and not account for scr refresh
                sound31_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_6.status = STARTED
                sound31_6.play(when=win)  # sync with win flip
            
            # if sound31_6 is stopping this frame...
            if sound31_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_6.tStop = t  # not accounting for scr refresh
                    sound31_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_6.status = FINISHED
                    sound31_6.stop()
            # update sound31_6 status according to whether it's playing
            if sound31_6.isPlaying:
                sound31_6.status = STARTED
            elif sound31_6.isFinished:
                sound31_6.status = FINISHED
            
            # if sound31_7 is starting this frame...
            if sound31_7.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_7.frameNStart = frameN  # exact frame index
                sound31_7.tStart = t  # local t and not account for scr refresh
                sound31_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_7.status = STARTED
                sound31_7.play(when=win)  # sync with win flip
            
            # if sound31_7 is stopping this frame...
            if sound31_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_7.tStop = t  # not accounting for scr refresh
                    sound31_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_7.status = FINISHED
                    sound31_7.stop()
            # update sound31_7 status according to whether it's playing
            if sound31_7.isPlaying:
                sound31_7.status = STARTED
            elif sound31_7.isFinished:
                sound31_7.status = FINISHED
            
            # if sound31_8 is starting this frame...
            if sound31_8.status == NOT_STARTED and tThisFlip >= starttime[29]-frameTolerance:
                # keep track of start time/frame for later
                sound31_8.frameNStart = frameN  # exact frame index
                sound31_8.tStart = t  # local t and not account for scr refresh
                sound31_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound31_8.status = STARTED
                sound31_8.play(when=win)  # sync with win flip
            
            # if sound31_8 is stopping this frame...
            if sound31_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound31_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound31_8.tStop = t  # not accounting for scr refresh
                    sound31_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound31_8.status = FINISHED
                    sound31_8.stop()
            # update sound31_8 status according to whether it's playing
            if sound31_8.isPlaying:
                sound31_8.status = STARTED
            elif sound31_8.isFinished:
                sound31_8.status = FINISHED
            
            # if sound32 is starting this frame...
            if sound32.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32.frameNStart = frameN  # exact frame index
                sound32.tStart = t  # local t and not account for scr refresh
                sound32.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32.status = STARTED
                sound32.play(when=win)  # sync with win flip
            
            # if sound32 is stopping this frame...
            if sound32.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32.tStop = t  # not accounting for scr refresh
                    sound32.frameNStop = frameN  # exact frame index
                    # update status
                    sound32.status = FINISHED
                    sound32.stop()
            # update sound32 status according to whether it's playing
            if sound32.isPlaying:
                sound32.status = STARTED
            elif sound32.isFinished:
                sound32.status = FINISHED
            
            # if sound32_2 is starting this frame...
            if sound32_2.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_2.frameNStart = frameN  # exact frame index
                sound32_2.tStart = t  # local t and not account for scr refresh
                sound32_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_2.status = STARTED
                sound32_2.play(when=win)  # sync with win flip
            
            # if sound32_2 is stopping this frame...
            if sound32_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_2.tStop = t  # not accounting for scr refresh
                    sound32_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_2.status = FINISHED
                    sound32_2.stop()
            # update sound32_2 status according to whether it's playing
            if sound32_2.isPlaying:
                sound32_2.status = STARTED
            elif sound32_2.isFinished:
                sound32_2.status = FINISHED
            
            # if sound32_3 is starting this frame...
            if sound32_3.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_3.frameNStart = frameN  # exact frame index
                sound32_3.tStart = t  # local t and not account for scr refresh
                sound32_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_3.status = STARTED
                sound32_3.play(when=win)  # sync with win flip
            
            # if sound32_3 is stopping this frame...
            if sound32_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_3.tStop = t  # not accounting for scr refresh
                    sound32_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_3.status = FINISHED
                    sound32_3.stop()
            # update sound32_3 status according to whether it's playing
            if sound32_3.isPlaying:
                sound32_3.status = STARTED
            elif sound32_3.isFinished:
                sound32_3.status = FINISHED
            
            # if sound32_4 is starting this frame...
            if sound32_4.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_4.frameNStart = frameN  # exact frame index
                sound32_4.tStart = t  # local t and not account for scr refresh
                sound32_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_4.status = STARTED
                sound32_4.play(when=win)  # sync with win flip
            
            # if sound32_4 is stopping this frame...
            if sound32_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_4.tStop = t  # not accounting for scr refresh
                    sound32_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_4.status = FINISHED
                    sound32_4.stop()
            # update sound32_4 status according to whether it's playing
            if sound32_4.isPlaying:
                sound32_4.status = STARTED
            elif sound32_4.isFinished:
                sound32_4.status = FINISHED
            
            # if sound32_5 is starting this frame...
            if sound32_5.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_5.frameNStart = frameN  # exact frame index
                sound32_5.tStart = t  # local t and not account for scr refresh
                sound32_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_5.status = STARTED
                sound32_5.play(when=win)  # sync with win flip
            
            # if sound32_5 is stopping this frame...
            if sound32_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_5.tStop = t  # not accounting for scr refresh
                    sound32_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_5.status = FINISHED
                    sound32_5.stop()
            # update sound32_5 status according to whether it's playing
            if sound32_5.isPlaying:
                sound32_5.status = STARTED
            elif sound32_5.isFinished:
                sound32_5.status = FINISHED
            
            # if sound32_6 is starting this frame...
            if sound32_6.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_6.frameNStart = frameN  # exact frame index
                sound32_6.tStart = t  # local t and not account for scr refresh
                sound32_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_6.status = STARTED
                sound32_6.play(when=win)  # sync with win flip
            
            # if sound32_6 is stopping this frame...
            if sound32_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_6.tStop = t  # not accounting for scr refresh
                    sound32_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_6.status = FINISHED
                    sound32_6.stop()
            # update sound32_6 status according to whether it's playing
            if sound32_6.isPlaying:
                sound32_6.status = STARTED
            elif sound32_6.isFinished:
                sound32_6.status = FINISHED
            
            # if sound32_7 is starting this frame...
            if sound32_7.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_7.frameNStart = frameN  # exact frame index
                sound32_7.tStart = t  # local t and not account for scr refresh
                sound32_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_7.status = STARTED
                sound32_7.play(when=win)  # sync with win flip
            
            # if sound32_7 is stopping this frame...
            if sound32_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_7.tStop = t  # not accounting for scr refresh
                    sound32_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_7.status = FINISHED
                    sound32_7.stop()
            # update sound32_7 status according to whether it's playing
            if sound32_7.isPlaying:
                sound32_7.status = STARTED
            elif sound32_7.isFinished:
                sound32_7.status = FINISHED
            
            # if sound32_8 is starting this frame...
            if sound32_8.status == NOT_STARTED and tThisFlip >= starttime[30]-frameTolerance:
                # keep track of start time/frame for later
                sound32_8.frameNStart = frameN  # exact frame index
                sound32_8.tStart = t  # local t and not account for scr refresh
                sound32_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound32_8.status = STARTED
                sound32_8.play(when=win)  # sync with win flip
            
            # if sound32_8 is stopping this frame...
            if sound32_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound32_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound32_8.tStop = t  # not accounting for scr refresh
                    sound32_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound32_8.status = FINISHED
                    sound32_8.stop()
            # update sound32_8 status according to whether it's playing
            if sound32_8.isPlaying:
                sound32_8.status = STARTED
            elif sound32_8.isFinished:
                sound32_8.status = FINISHED
            
            # if sound33 is starting this frame...
            if sound33.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33.frameNStart = frameN  # exact frame index
                sound33.tStart = t  # local t and not account for scr refresh
                sound33.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33.status = STARTED
                sound33.play(when=win)  # sync with win flip
            
            # if sound33 is stopping this frame...
            if sound33.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33.tStop = t  # not accounting for scr refresh
                    sound33.frameNStop = frameN  # exact frame index
                    # update status
                    sound33.status = FINISHED
                    sound33.stop()
            # update sound33 status according to whether it's playing
            if sound33.isPlaying:
                sound33.status = STARTED
            elif sound33.isFinished:
                sound33.status = FINISHED
            
            # if sound33_2 is starting this frame...
            if sound33_2.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_2.frameNStart = frameN  # exact frame index
                sound33_2.tStart = t  # local t and not account for scr refresh
                sound33_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_2.status = STARTED
                sound33_2.play(when=win)  # sync with win flip
            
            # if sound33_2 is stopping this frame...
            if sound33_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_2.tStop = t  # not accounting for scr refresh
                    sound33_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_2.status = FINISHED
                    sound33_2.stop()
            # update sound33_2 status according to whether it's playing
            if sound33_2.isPlaying:
                sound33_2.status = STARTED
            elif sound33_2.isFinished:
                sound33_2.status = FINISHED
            
            # if sound33_3 is starting this frame...
            if sound33_3.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_3.frameNStart = frameN  # exact frame index
                sound33_3.tStart = t  # local t and not account for scr refresh
                sound33_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_3.status = STARTED
                sound33_3.play(when=win)  # sync with win flip
            
            # if sound33_3 is stopping this frame...
            if sound33_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_3.tStop = t  # not accounting for scr refresh
                    sound33_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_3.status = FINISHED
                    sound33_3.stop()
            # update sound33_3 status according to whether it's playing
            if sound33_3.isPlaying:
                sound33_3.status = STARTED
            elif sound33_3.isFinished:
                sound33_3.status = FINISHED
            
            # if sound33_4 is starting this frame...
            if sound33_4.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_4.frameNStart = frameN  # exact frame index
                sound33_4.tStart = t  # local t and not account for scr refresh
                sound33_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_4.status = STARTED
                sound33_4.play(when=win)  # sync with win flip
            
            # if sound33_4 is stopping this frame...
            if sound33_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_4.tStop = t  # not accounting for scr refresh
                    sound33_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_4.status = FINISHED
                    sound33_4.stop()
            # update sound33_4 status according to whether it's playing
            if sound33_4.isPlaying:
                sound33_4.status = STARTED
            elif sound33_4.isFinished:
                sound33_4.status = FINISHED
            
            # if sound33_5 is starting this frame...
            if sound33_5.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_5.frameNStart = frameN  # exact frame index
                sound33_5.tStart = t  # local t and not account for scr refresh
                sound33_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_5.status = STARTED
                sound33_5.play(when=win)  # sync with win flip
            
            # if sound33_5 is stopping this frame...
            if sound33_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_5.tStop = t  # not accounting for scr refresh
                    sound33_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_5.status = FINISHED
                    sound33_5.stop()
            # update sound33_5 status according to whether it's playing
            if sound33_5.isPlaying:
                sound33_5.status = STARTED
            elif sound33_5.isFinished:
                sound33_5.status = FINISHED
            
            # if sound33_6 is starting this frame...
            if sound33_6.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_6.frameNStart = frameN  # exact frame index
                sound33_6.tStart = t  # local t and not account for scr refresh
                sound33_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_6.status = STARTED
                sound33_6.play(when=win)  # sync with win flip
            
            # if sound33_6 is stopping this frame...
            if sound33_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_6.tStop = t  # not accounting for scr refresh
                    sound33_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_6.status = FINISHED
                    sound33_6.stop()
            # update sound33_6 status according to whether it's playing
            if sound33_6.isPlaying:
                sound33_6.status = STARTED
            elif sound33_6.isFinished:
                sound33_6.status = FINISHED
            
            # if sound33_7 is starting this frame...
            if sound33_7.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_7.frameNStart = frameN  # exact frame index
                sound33_7.tStart = t  # local t and not account for scr refresh
                sound33_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_7.status = STARTED
                sound33_7.play(when=win)  # sync with win flip
            
            # if sound33_7 is stopping this frame...
            if sound33_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_7.tStop = t  # not accounting for scr refresh
                    sound33_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_7.status = FINISHED
                    sound33_7.stop()
            # update sound33_7 status according to whether it's playing
            if sound33_7.isPlaying:
                sound33_7.status = STARTED
            elif sound33_7.isFinished:
                sound33_7.status = FINISHED
            
            # if sound33_8 is starting this frame...
            if sound33_8.status == NOT_STARTED and tThisFlip >= starttime[31]-frameTolerance:
                # keep track of start time/frame for later
                sound33_8.frameNStart = frameN  # exact frame index
                sound33_8.tStart = t  # local t and not account for scr refresh
                sound33_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound33_8.status = STARTED
                sound33_8.play(when=win)  # sync with win flip
            
            # if sound33_8 is stopping this frame...
            if sound33_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound33_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound33_8.tStop = t  # not accounting for scr refresh
                    sound33_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound33_8.status = FINISHED
                    sound33_8.stop()
            # update sound33_8 status according to whether it's playing
            if sound33_8.isPlaying:
                sound33_8.status = STARTED
            elif sound33_8.isFinished:
                sound33_8.status = FINISHED
            
            # if sound34 is starting this frame...
            if sound34.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34.frameNStart = frameN  # exact frame index
                sound34.tStart = t  # local t and not account for scr refresh
                sound34.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34.status = STARTED
                sound34.play(when=win)  # sync with win flip
            
            # if sound34 is stopping this frame...
            if sound34.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34.tStop = t  # not accounting for scr refresh
                    sound34.frameNStop = frameN  # exact frame index
                    # update status
                    sound34.status = FINISHED
                    sound34.stop()
            # update sound34 status according to whether it's playing
            if sound34.isPlaying:
                sound34.status = STARTED
            elif sound34.isFinished:
                sound34.status = FINISHED
            
            # if sound34_2 is starting this frame...
            if sound34_2.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_2.frameNStart = frameN  # exact frame index
                sound34_2.tStart = t  # local t and not account for scr refresh
                sound34_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_2.status = STARTED
                sound34_2.play(when=win)  # sync with win flip
            
            # if sound34_2 is stopping this frame...
            if sound34_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_2.tStop = t  # not accounting for scr refresh
                    sound34_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_2.status = FINISHED
                    sound34_2.stop()
            # update sound34_2 status according to whether it's playing
            if sound34_2.isPlaying:
                sound34_2.status = STARTED
            elif sound34_2.isFinished:
                sound34_2.status = FINISHED
            
            # if sound34_3 is starting this frame...
            if sound34_3.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_3.frameNStart = frameN  # exact frame index
                sound34_3.tStart = t  # local t and not account for scr refresh
                sound34_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_3.status = STARTED
                sound34_3.play(when=win)  # sync with win flip
            
            # if sound34_3 is stopping this frame...
            if sound34_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_3.tStop = t  # not accounting for scr refresh
                    sound34_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_3.status = FINISHED
                    sound34_3.stop()
            # update sound34_3 status according to whether it's playing
            if sound34_3.isPlaying:
                sound34_3.status = STARTED
            elif sound34_3.isFinished:
                sound34_3.status = FINISHED
            
            # if sound34_4 is starting this frame...
            if sound34_4.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_4.frameNStart = frameN  # exact frame index
                sound34_4.tStart = t  # local t and not account for scr refresh
                sound34_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_4.status = STARTED
                sound34_4.play(when=win)  # sync with win flip
            
            # if sound34_4 is stopping this frame...
            if sound34_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_4.tStop = t  # not accounting for scr refresh
                    sound34_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_4.status = FINISHED
                    sound34_4.stop()
            # update sound34_4 status according to whether it's playing
            if sound34_4.isPlaying:
                sound34_4.status = STARTED
            elif sound34_4.isFinished:
                sound34_4.status = FINISHED
            
            # if sound34_5 is starting this frame...
            if sound34_5.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_5.frameNStart = frameN  # exact frame index
                sound34_5.tStart = t  # local t and not account for scr refresh
                sound34_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_5.status = STARTED
                sound34_5.play(when=win)  # sync with win flip
            
            # if sound34_5 is stopping this frame...
            if sound34_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_5.tStop = t  # not accounting for scr refresh
                    sound34_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_5.status = FINISHED
                    sound34_5.stop()
            # update sound34_5 status according to whether it's playing
            if sound34_5.isPlaying:
                sound34_5.status = STARTED
            elif sound34_5.isFinished:
                sound34_5.status = FINISHED
            
            # if sound34_6 is starting this frame...
            if sound34_6.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_6.frameNStart = frameN  # exact frame index
                sound34_6.tStart = t  # local t and not account for scr refresh
                sound34_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_6.status = STARTED
                sound34_6.play(when=win)  # sync with win flip
            
            # if sound34_6 is stopping this frame...
            if sound34_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_6.tStop = t  # not accounting for scr refresh
                    sound34_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_6.status = FINISHED
                    sound34_6.stop()
            # update sound34_6 status according to whether it's playing
            if sound34_6.isPlaying:
                sound34_6.status = STARTED
            elif sound34_6.isFinished:
                sound34_6.status = FINISHED
            
            # if sound34_7 is starting this frame...
            if sound34_7.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_7.frameNStart = frameN  # exact frame index
                sound34_7.tStart = t  # local t and not account for scr refresh
                sound34_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_7.status = STARTED
                sound34_7.play(when=win)  # sync with win flip
            
            # if sound34_7 is stopping this frame...
            if sound34_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_7.tStop = t  # not accounting for scr refresh
                    sound34_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_7.status = FINISHED
                    sound34_7.stop()
            # update sound34_7 status according to whether it's playing
            if sound34_7.isPlaying:
                sound34_7.status = STARTED
            elif sound34_7.isFinished:
                sound34_7.status = FINISHED
            
            # if sound34_8 is starting this frame...
            if sound34_8.status == NOT_STARTED and tThisFlip >= starttime[32]-frameTolerance:
                # keep track of start time/frame for later
                sound34_8.frameNStart = frameN  # exact frame index
                sound34_8.tStart = t  # local t and not account for scr refresh
                sound34_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound34_8.status = STARTED
                sound34_8.play(when=win)  # sync with win flip
            
            # if sound34_8 is stopping this frame...
            if sound34_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound34_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound34_8.tStop = t  # not accounting for scr refresh
                    sound34_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound34_8.status = FINISHED
                    sound34_8.stop()
            # update sound34_8 status according to whether it's playing
            if sound34_8.isPlaying:
                sound34_8.status = STARTED
            elif sound34_8.isFinished:
                sound34_8.status = FINISHED
            
            # if sound35 is starting this frame...
            if sound35.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35.frameNStart = frameN  # exact frame index
                sound35.tStart = t  # local t and not account for scr refresh
                sound35.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35.status = STARTED
                sound35.play(when=win)  # sync with win flip
            
            # if sound35 is stopping this frame...
            if sound35.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35.tStop = t  # not accounting for scr refresh
                    sound35.frameNStop = frameN  # exact frame index
                    # update status
                    sound35.status = FINISHED
                    sound35.stop()
            # update sound35 status according to whether it's playing
            if sound35.isPlaying:
                sound35.status = STARTED
            elif sound35.isFinished:
                sound35.status = FINISHED
            
            # if sound35_2 is starting this frame...
            if sound35_2.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_2.frameNStart = frameN  # exact frame index
                sound35_2.tStart = t  # local t and not account for scr refresh
                sound35_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_2.status = STARTED
                sound35_2.play(when=win)  # sync with win flip
            
            # if sound35_2 is stopping this frame...
            if sound35_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_2.tStop = t  # not accounting for scr refresh
                    sound35_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_2.status = FINISHED
                    sound35_2.stop()
            # update sound35_2 status according to whether it's playing
            if sound35_2.isPlaying:
                sound35_2.status = STARTED
            elif sound35_2.isFinished:
                sound35_2.status = FINISHED
            
            # if sound35_3 is starting this frame...
            if sound35_3.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_3.frameNStart = frameN  # exact frame index
                sound35_3.tStart = t  # local t and not account for scr refresh
                sound35_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_3.status = STARTED
                sound35_3.play(when=win)  # sync with win flip
            
            # if sound35_3 is stopping this frame...
            if sound35_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_3.tStop = t  # not accounting for scr refresh
                    sound35_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_3.status = FINISHED
                    sound35_3.stop()
            # update sound35_3 status according to whether it's playing
            if sound35_3.isPlaying:
                sound35_3.status = STARTED
            elif sound35_3.isFinished:
                sound35_3.status = FINISHED
            
            # if sound35_4 is starting this frame...
            if sound35_4.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_4.frameNStart = frameN  # exact frame index
                sound35_4.tStart = t  # local t and not account for scr refresh
                sound35_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_4.status = STARTED
                sound35_4.play(when=win)  # sync with win flip
            
            # if sound35_4 is stopping this frame...
            if sound35_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_4.tStop = t  # not accounting for scr refresh
                    sound35_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_4.status = FINISHED
                    sound35_4.stop()
            # update sound35_4 status according to whether it's playing
            if sound35_4.isPlaying:
                sound35_4.status = STARTED
            elif sound35_4.isFinished:
                sound35_4.status = FINISHED
            
            # if sound35_5 is starting this frame...
            if sound35_5.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_5.frameNStart = frameN  # exact frame index
                sound35_5.tStart = t  # local t and not account for scr refresh
                sound35_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_5.status = STARTED
                sound35_5.play(when=win)  # sync with win flip
            
            # if sound35_5 is stopping this frame...
            if sound35_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_5.tStop = t  # not accounting for scr refresh
                    sound35_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_5.status = FINISHED
                    sound35_5.stop()
            # update sound35_5 status according to whether it's playing
            if sound35_5.isPlaying:
                sound35_5.status = STARTED
            elif sound35_5.isFinished:
                sound35_5.status = FINISHED
            
            # if sound35_6 is starting this frame...
            if sound35_6.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_6.frameNStart = frameN  # exact frame index
                sound35_6.tStart = t  # local t and not account for scr refresh
                sound35_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_6.status = STARTED
                sound35_6.play(when=win)  # sync with win flip
            
            # if sound35_6 is stopping this frame...
            if sound35_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_6.tStop = t  # not accounting for scr refresh
                    sound35_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_6.status = FINISHED
                    sound35_6.stop()
            # update sound35_6 status according to whether it's playing
            if sound35_6.isPlaying:
                sound35_6.status = STARTED
            elif sound35_6.isFinished:
                sound35_6.status = FINISHED
            
            # if sound35_7 is starting this frame...
            if sound35_7.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_7.frameNStart = frameN  # exact frame index
                sound35_7.tStart = t  # local t and not account for scr refresh
                sound35_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_7.status = STARTED
                sound35_7.play(when=win)  # sync with win flip
            
            # if sound35_7 is stopping this frame...
            if sound35_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_7.tStop = t  # not accounting for scr refresh
                    sound35_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_7.status = FINISHED
                    sound35_7.stop()
            # update sound35_7 status according to whether it's playing
            if sound35_7.isPlaying:
                sound35_7.status = STARTED
            elif sound35_7.isFinished:
                sound35_7.status = FINISHED
            
            # if sound35_8 is starting this frame...
            if sound35_8.status == NOT_STARTED and tThisFlip >= starttime[33]-frameTolerance:
                # keep track of start time/frame for later
                sound35_8.frameNStart = frameN  # exact frame index
                sound35_8.tStart = t  # local t and not account for scr refresh
                sound35_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound35_8.status = STARTED
                sound35_8.play(when=win)  # sync with win flip
            
            # if sound35_8 is stopping this frame...
            if sound35_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound35_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound35_8.tStop = t  # not accounting for scr refresh
                    sound35_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound35_8.status = FINISHED
                    sound35_8.stop()
            # update sound35_8 status according to whether it's playing
            if sound35_8.isPlaying:
                sound35_8.status = STARTED
            elif sound35_8.isFinished:
                sound35_8.status = FINISHED
            
            # if sound36 is starting this frame...
            if sound36.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36.frameNStart = frameN  # exact frame index
                sound36.tStart = t  # local t and not account for scr refresh
                sound36.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36.status = STARTED
                sound36.play(when=win)  # sync with win flip
            
            # if sound36 is stopping this frame...
            if sound36.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36.tStop = t  # not accounting for scr refresh
                    sound36.frameNStop = frameN  # exact frame index
                    # update status
                    sound36.status = FINISHED
                    sound36.stop()
            # update sound36 status according to whether it's playing
            if sound36.isPlaying:
                sound36.status = STARTED
            elif sound36.isFinished:
                sound36.status = FINISHED
            
            # if sound36_2 is starting this frame...
            if sound36_2.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_2.frameNStart = frameN  # exact frame index
                sound36_2.tStart = t  # local t and not account for scr refresh
                sound36_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_2.status = STARTED
                sound36_2.play(when=win)  # sync with win flip
            
            # if sound36_2 is stopping this frame...
            if sound36_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_2.tStop = t  # not accounting for scr refresh
                    sound36_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_2.status = FINISHED
                    sound36_2.stop()
            # update sound36_2 status according to whether it's playing
            if sound36_2.isPlaying:
                sound36_2.status = STARTED
            elif sound36_2.isFinished:
                sound36_2.status = FINISHED
            
            # if sound36_3 is starting this frame...
            if sound36_3.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_3.frameNStart = frameN  # exact frame index
                sound36_3.tStart = t  # local t and not account for scr refresh
                sound36_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_3.status = STARTED
                sound36_3.play(when=win)  # sync with win flip
            
            # if sound36_3 is stopping this frame...
            if sound36_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_3.tStop = t  # not accounting for scr refresh
                    sound36_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_3.status = FINISHED
                    sound36_3.stop()
            # update sound36_3 status according to whether it's playing
            if sound36_3.isPlaying:
                sound36_3.status = STARTED
            elif sound36_3.isFinished:
                sound36_3.status = FINISHED
            
            # if sound36_4 is starting this frame...
            if sound36_4.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_4.frameNStart = frameN  # exact frame index
                sound36_4.tStart = t  # local t and not account for scr refresh
                sound36_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_4.status = STARTED
                sound36_4.play(when=win)  # sync with win flip
            
            # if sound36_4 is stopping this frame...
            if sound36_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_4.tStop = t  # not accounting for scr refresh
                    sound36_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_4.status = FINISHED
                    sound36_4.stop()
            # update sound36_4 status according to whether it's playing
            if sound36_4.isPlaying:
                sound36_4.status = STARTED
            elif sound36_4.isFinished:
                sound36_4.status = FINISHED
            
            # if sound36_5 is starting this frame...
            if sound36_5.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_5.frameNStart = frameN  # exact frame index
                sound36_5.tStart = t  # local t and not account for scr refresh
                sound36_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_5.status = STARTED
                sound36_5.play(when=win)  # sync with win flip
            
            # if sound36_5 is stopping this frame...
            if sound36_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_5.tStop = t  # not accounting for scr refresh
                    sound36_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_5.status = FINISHED
                    sound36_5.stop()
            # update sound36_5 status according to whether it's playing
            if sound36_5.isPlaying:
                sound36_5.status = STARTED
            elif sound36_5.isFinished:
                sound36_5.status = FINISHED
            
            # if sound36_6 is starting this frame...
            if sound36_6.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_6.frameNStart = frameN  # exact frame index
                sound36_6.tStart = t  # local t and not account for scr refresh
                sound36_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_6.status = STARTED
                sound36_6.play(when=win)  # sync with win flip
            
            # if sound36_6 is stopping this frame...
            if sound36_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_6.tStop = t  # not accounting for scr refresh
                    sound36_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_6.status = FINISHED
                    sound36_6.stop()
            # update sound36_6 status according to whether it's playing
            if sound36_6.isPlaying:
                sound36_6.status = STARTED
            elif sound36_6.isFinished:
                sound36_6.status = FINISHED
            
            # if sound36_7 is starting this frame...
            if sound36_7.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_7.frameNStart = frameN  # exact frame index
                sound36_7.tStart = t  # local t and not account for scr refresh
                sound36_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_7.status = STARTED
                sound36_7.play(when=win)  # sync with win flip
            
            # if sound36_7 is stopping this frame...
            if sound36_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_7.tStop = t  # not accounting for scr refresh
                    sound36_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_7.status = FINISHED
                    sound36_7.stop()
            # update sound36_7 status according to whether it's playing
            if sound36_7.isPlaying:
                sound36_7.status = STARTED
            elif sound36_7.isFinished:
                sound36_7.status = FINISHED
            
            # if sound36_8 is starting this frame...
            if sound36_8.status == NOT_STARTED and tThisFlip >= starttime[34]-frameTolerance:
                # keep track of start time/frame for later
                sound36_8.frameNStart = frameN  # exact frame index
                sound36_8.tStart = t  # local t and not account for scr refresh
                sound36_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound36_8.status = STARTED
                sound36_8.play(when=win)  # sync with win flip
            
            # if sound36_8 is stopping this frame...
            if sound36_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound36_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound36_8.tStop = t  # not accounting for scr refresh
                    sound36_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound36_8.status = FINISHED
                    sound36_8.stop()
            # update sound36_8 status according to whether it's playing
            if sound36_8.isPlaying:
                sound36_8.status = STARTED
            elif sound36_8.isFinished:
                sound36_8.status = FINISHED
            
            # if sound37 is starting this frame...
            if sound37.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37.frameNStart = frameN  # exact frame index
                sound37.tStart = t  # local t and not account for scr refresh
                sound37.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37.status = STARTED
                sound37.play(when=win)  # sync with win flip
            
            # if sound37 is stopping this frame...
            if sound37.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37.tStop = t  # not accounting for scr refresh
                    sound37.frameNStop = frameN  # exact frame index
                    # update status
                    sound37.status = FINISHED
                    sound37.stop()
            # update sound37 status according to whether it's playing
            if sound37.isPlaying:
                sound37.status = STARTED
            elif sound37.isFinished:
                sound37.status = FINISHED
            
            # if sound37_2 is starting this frame...
            if sound37_2.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_2.frameNStart = frameN  # exact frame index
                sound37_2.tStart = t  # local t and not account for scr refresh
                sound37_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_2.status = STARTED
                sound37_2.play(when=win)  # sync with win flip
            
            # if sound37_2 is stopping this frame...
            if sound37_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_2.tStop = t  # not accounting for scr refresh
                    sound37_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_2.status = FINISHED
                    sound37_2.stop()
            # update sound37_2 status according to whether it's playing
            if sound37_2.isPlaying:
                sound37_2.status = STARTED
            elif sound37_2.isFinished:
                sound37_2.status = FINISHED
            
            # if sound37_3 is starting this frame...
            if sound37_3.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_3.frameNStart = frameN  # exact frame index
                sound37_3.tStart = t  # local t and not account for scr refresh
                sound37_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_3.status = STARTED
                sound37_3.play(when=win)  # sync with win flip
            
            # if sound37_3 is stopping this frame...
            if sound37_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_3.tStop = t  # not accounting for scr refresh
                    sound37_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_3.status = FINISHED
                    sound37_3.stop()
            # update sound37_3 status according to whether it's playing
            if sound37_3.isPlaying:
                sound37_3.status = STARTED
            elif sound37_3.isFinished:
                sound37_3.status = FINISHED
            
            # if sound37_4 is starting this frame...
            if sound37_4.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_4.frameNStart = frameN  # exact frame index
                sound37_4.tStart = t  # local t and not account for scr refresh
                sound37_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_4.status = STARTED
                sound37_4.play(when=win)  # sync with win flip
            
            # if sound37_4 is stopping this frame...
            if sound37_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_4.tStop = t  # not accounting for scr refresh
                    sound37_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_4.status = FINISHED
                    sound37_4.stop()
            # update sound37_4 status according to whether it's playing
            if sound37_4.isPlaying:
                sound37_4.status = STARTED
            elif sound37_4.isFinished:
                sound37_4.status = FINISHED
            
            # if sound37_5 is starting this frame...
            if sound37_5.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_5.frameNStart = frameN  # exact frame index
                sound37_5.tStart = t  # local t and not account for scr refresh
                sound37_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_5.status = STARTED
                sound37_5.play(when=win)  # sync with win flip
            
            # if sound37_5 is stopping this frame...
            if sound37_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_5.tStop = t  # not accounting for scr refresh
                    sound37_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_5.status = FINISHED
                    sound37_5.stop()
            # update sound37_5 status according to whether it's playing
            if sound37_5.isPlaying:
                sound37_5.status = STARTED
            elif sound37_5.isFinished:
                sound37_5.status = FINISHED
            
            # if sound37_6 is starting this frame...
            if sound37_6.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_6.frameNStart = frameN  # exact frame index
                sound37_6.tStart = t  # local t and not account for scr refresh
                sound37_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_6.status = STARTED
                sound37_6.play(when=win)  # sync with win flip
            
            # if sound37_6 is stopping this frame...
            if sound37_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_6.tStop = t  # not accounting for scr refresh
                    sound37_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_6.status = FINISHED
                    sound37_6.stop()
            # update sound37_6 status according to whether it's playing
            if sound37_6.isPlaying:
                sound37_6.status = STARTED
            elif sound37_6.isFinished:
                sound37_6.status = FINISHED
            
            # if sound37_7 is starting this frame...
            if sound37_7.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_7.frameNStart = frameN  # exact frame index
                sound37_7.tStart = t  # local t and not account for scr refresh
                sound37_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_7.status = STARTED
                sound37_7.play(when=win)  # sync with win flip
            
            # if sound37_7 is stopping this frame...
            if sound37_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_7.tStop = t  # not accounting for scr refresh
                    sound37_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_7.status = FINISHED
                    sound37_7.stop()
            # update sound37_7 status according to whether it's playing
            if sound37_7.isPlaying:
                sound37_7.status = STARTED
            elif sound37_7.isFinished:
                sound37_7.status = FINISHED
            
            # if sound37_8 is starting this frame...
            if sound37_8.status == NOT_STARTED and tThisFlip >= starttime[35]-frameTolerance:
                # keep track of start time/frame for later
                sound37_8.frameNStart = frameN  # exact frame index
                sound37_8.tStart = t  # local t and not account for scr refresh
                sound37_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound37_8.status = STARTED
                sound37_8.play(when=win)  # sync with win flip
            
            # if sound37_8 is stopping this frame...
            if sound37_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound37_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound37_8.tStop = t  # not accounting for scr refresh
                    sound37_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound37_8.status = FINISHED
                    sound37_8.stop()
            # update sound37_8 status according to whether it's playing
            if sound37_8.isPlaying:
                sound37_8.status = STARTED
            elif sound37_8.isFinished:
                sound37_8.status = FINISHED
            
            # if sound38 is starting this frame...
            if sound38.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38.frameNStart = frameN  # exact frame index
                sound38.tStart = t  # local t and not account for scr refresh
                sound38.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38.status = STARTED
                sound38.play(when=win)  # sync with win flip
            
            # if sound38 is stopping this frame...
            if sound38.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38.tStop = t  # not accounting for scr refresh
                    sound38.frameNStop = frameN  # exact frame index
                    # update status
                    sound38.status = FINISHED
                    sound38.stop()
            # update sound38 status according to whether it's playing
            if sound38.isPlaying:
                sound38.status = STARTED
            elif sound38.isFinished:
                sound38.status = FINISHED
            
            # if sound38_2 is starting this frame...
            if sound38_2.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_2.frameNStart = frameN  # exact frame index
                sound38_2.tStart = t  # local t and not account for scr refresh
                sound38_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_2.status = STARTED
                sound38_2.play(when=win)  # sync with win flip
            
            # if sound38_2 is stopping this frame...
            if sound38_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_2.tStop = t  # not accounting for scr refresh
                    sound38_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_2.status = FINISHED
                    sound38_2.stop()
            # update sound38_2 status according to whether it's playing
            if sound38_2.isPlaying:
                sound38_2.status = STARTED
            elif sound38_2.isFinished:
                sound38_2.status = FINISHED
            
            # if sound38_3 is starting this frame...
            if sound38_3.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_3.frameNStart = frameN  # exact frame index
                sound38_3.tStart = t  # local t and not account for scr refresh
                sound38_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_3.status = STARTED
                sound38_3.play(when=win)  # sync with win flip
            
            # if sound38_3 is stopping this frame...
            if sound38_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_3.tStop = t  # not accounting for scr refresh
                    sound38_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_3.status = FINISHED
                    sound38_3.stop()
            # update sound38_3 status according to whether it's playing
            if sound38_3.isPlaying:
                sound38_3.status = STARTED
            elif sound38_3.isFinished:
                sound38_3.status = FINISHED
            
            # if sound38_4 is starting this frame...
            if sound38_4.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_4.frameNStart = frameN  # exact frame index
                sound38_4.tStart = t  # local t and not account for scr refresh
                sound38_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_4.status = STARTED
                sound38_4.play(when=win)  # sync with win flip
            
            # if sound38_4 is stopping this frame...
            if sound38_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_4.tStop = t  # not accounting for scr refresh
                    sound38_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_4.status = FINISHED
                    sound38_4.stop()
            # update sound38_4 status according to whether it's playing
            if sound38_4.isPlaying:
                sound38_4.status = STARTED
            elif sound38_4.isFinished:
                sound38_4.status = FINISHED
            
            # if sound38_5 is starting this frame...
            if sound38_5.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_5.frameNStart = frameN  # exact frame index
                sound38_5.tStart = t  # local t and not account for scr refresh
                sound38_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_5.status = STARTED
                sound38_5.play(when=win)  # sync with win flip
            
            # if sound38_5 is stopping this frame...
            if sound38_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_5.tStop = t  # not accounting for scr refresh
                    sound38_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_5.status = FINISHED
                    sound38_5.stop()
            # update sound38_5 status according to whether it's playing
            if sound38_5.isPlaying:
                sound38_5.status = STARTED
            elif sound38_5.isFinished:
                sound38_5.status = FINISHED
            
            # if sound38_6 is starting this frame...
            if sound38_6.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_6.frameNStart = frameN  # exact frame index
                sound38_6.tStart = t  # local t and not account for scr refresh
                sound38_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_6.status = STARTED
                sound38_6.play(when=win)  # sync with win flip
            
            # if sound38_6 is stopping this frame...
            if sound38_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_6.tStop = t  # not accounting for scr refresh
                    sound38_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_6.status = FINISHED
                    sound38_6.stop()
            # update sound38_6 status according to whether it's playing
            if sound38_6.isPlaying:
                sound38_6.status = STARTED
            elif sound38_6.isFinished:
                sound38_6.status = FINISHED
            
            # if sound38_7 is starting this frame...
            if sound38_7.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_7.frameNStart = frameN  # exact frame index
                sound38_7.tStart = t  # local t and not account for scr refresh
                sound38_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_7.status = STARTED
                sound38_7.play(when=win)  # sync with win flip
            
            # if sound38_7 is stopping this frame...
            if sound38_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_7.tStop = t  # not accounting for scr refresh
                    sound38_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_7.status = FINISHED
                    sound38_7.stop()
            # update sound38_7 status according to whether it's playing
            if sound38_7.isPlaying:
                sound38_7.status = STARTED
            elif sound38_7.isFinished:
                sound38_7.status = FINISHED
            
            # if sound38_8 is starting this frame...
            if sound38_8.status == NOT_STARTED and tThisFlip >= starttime[36]-frameTolerance:
                # keep track of start time/frame for later
                sound38_8.frameNStart = frameN  # exact frame index
                sound38_8.tStart = t  # local t and not account for scr refresh
                sound38_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound38_8.status = STARTED
                sound38_8.play(when=win)  # sync with win flip
            
            # if sound38_8 is stopping this frame...
            if sound38_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound38_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound38_8.tStop = t  # not accounting for scr refresh
                    sound38_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound38_8.status = FINISHED
                    sound38_8.stop()
            # update sound38_8 status according to whether it's playing
            if sound38_8.isPlaying:
                sound38_8.status = STARTED
            elif sound38_8.isFinished:
                sound38_8.status = FINISHED
            
            # if sound39 is starting this frame...
            if sound39.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39.frameNStart = frameN  # exact frame index
                sound39.tStart = t  # local t and not account for scr refresh
                sound39.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39.status = STARTED
                sound39.play(when=win)  # sync with win flip
            
            # if sound39 is stopping this frame...
            if sound39.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39.tStop = t  # not accounting for scr refresh
                    sound39.frameNStop = frameN  # exact frame index
                    # update status
                    sound39.status = FINISHED
                    sound39.stop()
            # update sound39 status according to whether it's playing
            if sound39.isPlaying:
                sound39.status = STARTED
            elif sound39.isFinished:
                sound39.status = FINISHED
            
            # if sound39_2 is starting this frame...
            if sound39_2.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_2.frameNStart = frameN  # exact frame index
                sound39_2.tStart = t  # local t and not account for scr refresh
                sound39_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_2.status = STARTED
                sound39_2.play(when=win)  # sync with win flip
            
            # if sound39_2 is stopping this frame...
            if sound39_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_2.tStop = t  # not accounting for scr refresh
                    sound39_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_2.status = FINISHED
                    sound39_2.stop()
            # update sound39_2 status according to whether it's playing
            if sound39_2.isPlaying:
                sound39_2.status = STARTED
            elif sound39_2.isFinished:
                sound39_2.status = FINISHED
            
            # if sound39_3 is starting this frame...
            if sound39_3.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_3.frameNStart = frameN  # exact frame index
                sound39_3.tStart = t  # local t and not account for scr refresh
                sound39_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_3.status = STARTED
                sound39_3.play(when=win)  # sync with win flip
            
            # if sound39_3 is stopping this frame...
            if sound39_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_3.tStop = t  # not accounting for scr refresh
                    sound39_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_3.status = FINISHED
                    sound39_3.stop()
            # update sound39_3 status according to whether it's playing
            if sound39_3.isPlaying:
                sound39_3.status = STARTED
            elif sound39_3.isFinished:
                sound39_3.status = FINISHED
            
            # if sound39_4 is starting this frame...
            if sound39_4.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_4.frameNStart = frameN  # exact frame index
                sound39_4.tStart = t  # local t and not account for scr refresh
                sound39_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_4.status = STARTED
                sound39_4.play(when=win)  # sync with win flip
            
            # if sound39_4 is stopping this frame...
            if sound39_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_4.tStop = t  # not accounting for scr refresh
                    sound39_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_4.status = FINISHED
                    sound39_4.stop()
            # update sound39_4 status according to whether it's playing
            if sound39_4.isPlaying:
                sound39_4.status = STARTED
            elif sound39_4.isFinished:
                sound39_4.status = FINISHED
            
            # if sound39_5 is starting this frame...
            if sound39_5.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_5.frameNStart = frameN  # exact frame index
                sound39_5.tStart = t  # local t and not account for scr refresh
                sound39_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_5.status = STARTED
                sound39_5.play(when=win)  # sync with win flip
            
            # if sound39_5 is stopping this frame...
            if sound39_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_5.tStop = t  # not accounting for scr refresh
                    sound39_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_5.status = FINISHED
                    sound39_5.stop()
            # update sound39_5 status according to whether it's playing
            if sound39_5.isPlaying:
                sound39_5.status = STARTED
            elif sound39_5.isFinished:
                sound39_5.status = FINISHED
            
            # if sound39_6 is starting this frame...
            if sound39_6.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_6.frameNStart = frameN  # exact frame index
                sound39_6.tStart = t  # local t and not account for scr refresh
                sound39_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_6.status = STARTED
                sound39_6.play(when=win)  # sync with win flip
            
            # if sound39_6 is stopping this frame...
            if sound39_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_6.tStop = t  # not accounting for scr refresh
                    sound39_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_6.status = FINISHED
                    sound39_6.stop()
            # update sound39_6 status according to whether it's playing
            if sound39_6.isPlaying:
                sound39_6.status = STARTED
            elif sound39_6.isFinished:
                sound39_6.status = FINISHED
            
            # if sound39_7 is starting this frame...
            if sound39_7.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_7.frameNStart = frameN  # exact frame index
                sound39_7.tStart = t  # local t and not account for scr refresh
                sound39_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_7.status = STARTED
                sound39_7.play(when=win)  # sync with win flip
            
            # if sound39_7 is stopping this frame...
            if sound39_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_7.tStop = t  # not accounting for scr refresh
                    sound39_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_7.status = FINISHED
                    sound39_7.stop()
            # update sound39_7 status according to whether it's playing
            if sound39_7.isPlaying:
                sound39_7.status = STARTED
            elif sound39_7.isFinished:
                sound39_7.status = FINISHED
            
            # if sound39_8 is starting this frame...
            if sound39_8.status == NOT_STARTED and tThisFlip >= starttime[37]-frameTolerance:
                # keep track of start time/frame for later
                sound39_8.frameNStart = frameN  # exact frame index
                sound39_8.tStart = t  # local t and not account for scr refresh
                sound39_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound39_8.status = STARTED
                sound39_8.play(when=win)  # sync with win flip
            
            # if sound39_8 is stopping this frame...
            if sound39_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound39_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound39_8.tStop = t  # not accounting for scr refresh
                    sound39_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound39_8.status = FINISHED
                    sound39_8.stop()
            # update sound39_8 status according to whether it's playing
            if sound39_8.isPlaying:
                sound39_8.status = STARTED
            elif sound39_8.isFinished:
                sound39_8.status = FINISHED
            
            # if sound40 is starting this frame...
            if sound40.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40.frameNStart = frameN  # exact frame index
                sound40.tStart = t  # local t and not account for scr refresh
                sound40.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40.status = STARTED
                sound40.play(when=win)  # sync with win flip
            
            # if sound40 is stopping this frame...
            if sound40.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40.tStop = t  # not accounting for scr refresh
                    sound40.frameNStop = frameN  # exact frame index
                    # update status
                    sound40.status = FINISHED
                    sound40.stop()
            # update sound40 status according to whether it's playing
            if sound40.isPlaying:
                sound40.status = STARTED
            elif sound40.isFinished:
                sound40.status = FINISHED
            
            # if sound40_2 is starting this frame...
            if sound40_2.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_2.frameNStart = frameN  # exact frame index
                sound40_2.tStart = t  # local t and not account for scr refresh
                sound40_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_2.status = STARTED
                sound40_2.play(when=win)  # sync with win flip
            
            # if sound40_2 is stopping this frame...
            if sound40_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_2.tStop = t  # not accounting for scr refresh
                    sound40_2.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_2.status = FINISHED
                    sound40_2.stop()
            # update sound40_2 status according to whether it's playing
            if sound40_2.isPlaying:
                sound40_2.status = STARTED
            elif sound40_2.isFinished:
                sound40_2.status = FINISHED
            
            # if sound40_3 is starting this frame...
            if sound40_3.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_3.frameNStart = frameN  # exact frame index
                sound40_3.tStart = t  # local t and not account for scr refresh
                sound40_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_3.status = STARTED
                sound40_3.play(when=win)  # sync with win flip
            
            # if sound40_3 is stopping this frame...
            if sound40_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_3.tStop = t  # not accounting for scr refresh
                    sound40_3.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_3.status = FINISHED
                    sound40_3.stop()
            # update sound40_3 status according to whether it's playing
            if sound40_3.isPlaying:
                sound40_3.status = STARTED
            elif sound40_3.isFinished:
                sound40_3.status = FINISHED
            
            # if sound40_4 is starting this frame...
            if sound40_4.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_4.frameNStart = frameN  # exact frame index
                sound40_4.tStart = t  # local t and not account for scr refresh
                sound40_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_4.status = STARTED
                sound40_4.play(when=win)  # sync with win flip
            
            # if sound40_4 is stopping this frame...
            if sound40_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_4.tStop = t  # not accounting for scr refresh
                    sound40_4.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_4.status = FINISHED
                    sound40_4.stop()
            # update sound40_4 status according to whether it's playing
            if sound40_4.isPlaying:
                sound40_4.status = STARTED
            elif sound40_4.isFinished:
                sound40_4.status = FINISHED
            
            # if sound40_5 is starting this frame...
            if sound40_5.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_5.frameNStart = frameN  # exact frame index
                sound40_5.tStart = t  # local t and not account for scr refresh
                sound40_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_5.status = STARTED
                sound40_5.play(when=win)  # sync with win flip
            
            # if sound40_5 is stopping this frame...
            if sound40_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_5.tStop = t  # not accounting for scr refresh
                    sound40_5.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_5.status = FINISHED
                    sound40_5.stop()
            # update sound40_5 status according to whether it's playing
            if sound40_5.isPlaying:
                sound40_5.status = STARTED
            elif sound40_5.isFinished:
                sound40_5.status = FINISHED
            
            # if sound40_6 is starting this frame...
            if sound40_6.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_6.frameNStart = frameN  # exact frame index
                sound40_6.tStart = t  # local t and not account for scr refresh
                sound40_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_6.status = STARTED
                sound40_6.play(when=win)  # sync with win flip
            
            # if sound40_6 is stopping this frame...
            if sound40_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_6.tStop = t  # not accounting for scr refresh
                    sound40_6.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_6.status = FINISHED
                    sound40_6.stop()
            # update sound40_6 status according to whether it's playing
            if sound40_6.isPlaying:
                sound40_6.status = STARTED
            elif sound40_6.isFinished:
                sound40_6.status = FINISHED
            
            # if sound40_7 is starting this frame...
            if sound40_7.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_7.frameNStart = frameN  # exact frame index
                sound40_7.tStart = t  # local t and not account for scr refresh
                sound40_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_7.status = STARTED
                sound40_7.play(when=win)  # sync with win flip
            
            # if sound40_7 is stopping this frame...
            if sound40_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_7.tStop = t  # not accounting for scr refresh
                    sound40_7.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_7.status = FINISHED
                    sound40_7.stop()
            # update sound40_7 status according to whether it's playing
            if sound40_7.isPlaying:
                sound40_7.status = STARTED
            elif sound40_7.isFinished:
                sound40_7.status = FINISHED
            
            # if sound40_8 is starting this frame...
            if sound40_8.status == NOT_STARTED and tThisFlip >= starttime[38]-frameTolerance:
                # keep track of start time/frame for later
                sound40_8.frameNStart = frameN  # exact frame index
                sound40_8.tStart = t  # local t and not account for scr refresh
                sound40_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                sound40_8.status = STARTED
                sound40_8.play(when=win)  # sync with win flip
            
            # if sound40_8 is stopping this frame...
            if sound40_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound40_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    sound40_8.tStop = t  # not accounting for scr refresh
                    sound40_8.frameNStop = frameN  # exact frame index
                    # update status
                    sound40_8.status = FINISHED
                    sound40_8.stop()
            # update sound40_8 status according to whether it's playing
            if sound40_8.isPlaying:
                sound40_8.status = STARTED
            elif sound40_8.isFinished:
                sound40_8.status = FINISHED
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['l','s'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_3.keys == str(correct)) or (key_resp_3.keys == correct):
                        key_resp_3.corr = 1
                    else:
                        key_resp_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # if tar_2 is starting this frame...
            if tar_2.status == NOT_STARTED and tThisFlip >= 0.68-frameTolerance:
                # keep track of start time/frame for later
                tar_2.frameNStart = frameN  # exact frame index
                tar_2.tStart = t  # local t and not account for scr refresh
                tar_2.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_2.status = STARTED
                tar_2.play(when=win)  # sync with win flip
            
            # if tar_2 is stopping this frame...
            if tar_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_2.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_2.tStop = t  # not accounting for scr refresh
                    tar_2.frameNStop = frameN  # exact frame index
                    # update status
                    tar_2.status = FINISHED
                    tar_2.stop()
            # update tar_2 status according to whether it's playing
            if tar_2.isPlaying:
                tar_2.status = STARTED
            elif tar_2.isFinished:
                tar_2.status = FINISHED
            
            # if tar_3 is starting this frame...
            if tar_3.status == NOT_STARTED and tThisFlip >= 0.74-frameTolerance:
                # keep track of start time/frame for later
                tar_3.frameNStart = frameN  # exact frame index
                tar_3.tStart = t  # local t and not account for scr refresh
                tar_3.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_3.status = STARTED
                tar_3.play(when=win)  # sync with win flip
            
            # if tar_3 is stopping this frame...
            if tar_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_3.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_3.tStop = t  # not accounting for scr refresh
                    tar_3.frameNStop = frameN  # exact frame index
                    # update status
                    tar_3.status = FINISHED
                    tar_3.stop()
            # update tar_3 status according to whether it's playing
            if tar_3.isPlaying:
                tar_3.status = STARTED
            elif tar_3.isFinished:
                tar_3.status = FINISHED
            
            # if tar_4 is starting this frame...
            if tar_4.status == NOT_STARTED and tThisFlip >= 0.80-frameTolerance:
                # keep track of start time/frame for later
                tar_4.frameNStart = frameN  # exact frame index
                tar_4.tStart = t  # local t and not account for scr refresh
                tar_4.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_4.status = STARTED
                tar_4.play(when=win)  # sync with win flip
            
            # if tar_4 is stopping this frame...
            if tar_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_4.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_4.tStop = t  # not accounting for scr refresh
                    tar_4.frameNStop = frameN  # exact frame index
                    # update status
                    tar_4.status = FINISHED
                    tar_4.stop()
            # update tar_4 status according to whether it's playing
            if tar_4.isPlaying:
                tar_4.status = STARTED
            elif tar_4.isFinished:
                tar_4.status = FINISHED
            
            # if tar_5 is starting this frame...
            if tar_5.status == NOT_STARTED and tThisFlip >= 0.86-frameTolerance:
                # keep track of start time/frame for later
                tar_5.frameNStart = frameN  # exact frame index
                tar_5.tStart = t  # local t and not account for scr refresh
                tar_5.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_5.status = STARTED
                tar_5.play(when=win)  # sync with win flip
            
            # if tar_5 is stopping this frame...
            if tar_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_5.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_5.tStop = t  # not accounting for scr refresh
                    tar_5.frameNStop = frameN  # exact frame index
                    # update status
                    tar_5.status = FINISHED
                    tar_5.stop()
            # update tar_5 status according to whether it's playing
            if tar_5.isPlaying:
                tar_5.status = STARTED
            elif tar_5.isFinished:
                tar_5.status = FINISHED
            
            # if tar_6 is starting this frame...
            if tar_6.status == NOT_STARTED and tThisFlip >= 0.92-frameTolerance:
                # keep track of start time/frame for later
                tar_6.frameNStart = frameN  # exact frame index
                tar_6.tStart = t  # local t and not account for scr refresh
                tar_6.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_6.status = STARTED
                tar_6.play(when=win)  # sync with win flip
            
            # if tar_6 is stopping this frame...
            if tar_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_6.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_6.tStop = t  # not accounting for scr refresh
                    tar_6.frameNStop = frameN  # exact frame index
                    # update status
                    tar_6.status = FINISHED
                    tar_6.stop()
            # update tar_6 status according to whether it's playing
            if tar_6.isPlaying:
                tar_6.status = STARTED
            elif tar_6.isFinished:
                tar_6.status = FINISHED
            
            # if tar_7 is starting this frame...
            if tar_7.status == NOT_STARTED and tThisFlip >= 0.98-frameTolerance:
                # keep track of start time/frame for later
                tar_7.frameNStart = frameN  # exact frame index
                tar_7.tStart = t  # local t and not account for scr refresh
                tar_7.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_7.status = STARTED
                tar_7.play(when=win)  # sync with win flip
            
            # if tar_7 is stopping this frame...
            if tar_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_7.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_7.tStop = t  # not accounting for scr refresh
                    tar_7.frameNStop = frameN  # exact frame index
                    # update status
                    tar_7.status = FINISHED
                    tar_7.stop()
            # update tar_7 status according to whether it's playing
            if tar_7.isPlaying:
                tar_7.status = STARTED
            elif tar_7.isFinished:
                tar_7.status = FINISHED
            
            # if tar_8 is starting this frame...
            if tar_8.status == NOT_STARTED and tThisFlip >= 1.04-frameTolerance:
                # keep track of start time/frame for later
                tar_8.frameNStart = frameN  # exact frame index
                tar_8.tStart = t  # local t and not account for scr refresh
                tar_8.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_8.status = STARTED
                tar_8.play(when=win)  # sync with win flip
            
            # if tar_8 is stopping this frame...
            if tar_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_8.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_8.tStop = t  # not accounting for scr refresh
                    tar_8.frameNStop = frameN  # exact frame index
                    # update status
                    tar_8.status = FINISHED
                    tar_8.stop()
            # update tar_8 status according to whether it's playing
            if tar_8.isPlaying:
                tar_8.status = STARTED
            elif tar_8.isFinished:
                tar_8.status = FINISHED
            
            # if tar_9 is starting this frame...
            if tar_9.status == NOT_STARTED and tThisFlip >= 1.1-frameTolerance:
                # keep track of start time/frame for later
                tar_9.frameNStart = frameN  # exact frame index
                tar_9.tStart = t  # local t and not account for scr refresh
                tar_9.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('tar_9.started', tThisFlipGlobal)
                # update status
                tar_9.status = STARTED
                tar_9.play(when=win)  # sync with win flip
            
            # if tar_9 is stopping this frame...
            if tar_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_9.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_9.tStop = t  # not accounting for scr refresh
                    tar_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tar_9.stopped')
                    # update status
                    tar_9.status = FINISHED
                    tar_9.stop()
            # update tar_9 status according to whether it's playing
            if tar_9.isPlaying:
                tar_9.status = STARTED
            elif tar_9.isFinished:
                tar_9.status = FINISHED
            
            # if tar_10 is starting this frame...
            if tar_10.status == NOT_STARTED and tThisFlip >= 1.16-frameTolerance:
                # keep track of start time/frame for later
                tar_10.frameNStart = frameN  # exact frame index
                tar_10.tStart = t  # local t and not account for scr refresh
                tar_10.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_10.status = STARTED
                tar_10.play(when=win)  # sync with win flip
            
            # if tar_10 is stopping this frame...
            if tar_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_10.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_10.tStop = t  # not accounting for scr refresh
                    tar_10.frameNStop = frameN  # exact frame index
                    # update status
                    tar_10.status = FINISHED
                    tar_10.stop()
            # update tar_10 status according to whether it's playing
            if tar_10.isPlaying:
                tar_10.status = STARTED
            elif tar_10.isFinished:
                tar_10.status = FINISHED
            
            # if tar_11 is starting this frame...
            if tar_11.status == NOT_STARTED and tThisFlip >= 1.22-frameTolerance:
                # keep track of start time/frame for later
                tar_11.frameNStart = frameN  # exact frame index
                tar_11.tStart = t  # local t and not account for scr refresh
                tar_11.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_11.status = STARTED
                tar_11.play(when=win)  # sync with win flip
            
            # if tar_11 is stopping this frame...
            if tar_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_11.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_11.tStop = t  # not accounting for scr refresh
                    tar_11.frameNStop = frameN  # exact frame index
                    # update status
                    tar_11.status = FINISHED
                    tar_11.stop()
            # update tar_11 status according to whether it's playing
            if tar_11.isPlaying:
                tar_11.status = STARTED
            elif tar_11.isFinished:
                tar_11.status = FINISHED
            
            # if tar_12 is starting this frame...
            if tar_12.status == NOT_STARTED and tThisFlip >= 1.28-frameTolerance:
                # keep track of start time/frame for later
                tar_12.frameNStart = frameN  # exact frame index
                tar_12.tStart = t  # local t and not account for scr refresh
                tar_12.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_12.status = STARTED
                tar_12.play(when=win)  # sync with win flip
            
            # if tar_12 is stopping this frame...
            if tar_12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_12.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_12.tStop = t  # not accounting for scr refresh
                    tar_12.frameNStop = frameN  # exact frame index
                    # update status
                    tar_12.status = FINISHED
                    tar_12.stop()
            # update tar_12 status according to whether it's playing
            if tar_12.isPlaying:
                tar_12.status = STARTED
            elif tar_12.isFinished:
                tar_12.status = FINISHED
            
            # if tar_13 is starting this frame...
            if tar_13.status == NOT_STARTED and tThisFlip >= 1.34-frameTolerance:
                # keep track of start time/frame for later
                tar_13.frameNStart = frameN  # exact frame index
                tar_13.tStart = t  # local t and not account for scr refresh
                tar_13.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_13.status = STARTED
                tar_13.play(when=win)  # sync with win flip
            
            # if tar_13 is stopping this frame...
            if tar_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_13.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_13.tStop = t  # not accounting for scr refresh
                    tar_13.frameNStop = frameN  # exact frame index
                    # update status
                    tar_13.status = FINISHED
                    tar_13.stop()
            # update tar_13 status according to whether it's playing
            if tar_13.isPlaying:
                tar_13.status = STARTED
            elif tar_13.isFinished:
                tar_13.status = FINISHED
            
            # if tar_14 is starting this frame...
            if tar_14.status == NOT_STARTED and tThisFlip >= 1.4-frameTolerance:
                # keep track of start time/frame for later
                tar_14.frameNStart = frameN  # exact frame index
                tar_14.tStart = t  # local t and not account for scr refresh
                tar_14.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_14.status = STARTED
                tar_14.play(when=win)  # sync with win flip
            
            # if tar_14 is stopping this frame...
            if tar_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_14.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_14.tStop = t  # not accounting for scr refresh
                    tar_14.frameNStop = frameN  # exact frame index
                    # update status
                    tar_14.status = FINISHED
                    tar_14.stop()
            # update tar_14 status according to whether it's playing
            if tar_14.isPlaying:
                tar_14.status = STARTED
            elif tar_14.isFinished:
                tar_14.status = FINISHED
            
            # if tar_15 is starting this frame...
            if tar_15.status == NOT_STARTED and tThisFlip >= 1.46-frameTolerance:
                # keep track of start time/frame for later
                tar_15.frameNStart = frameN  # exact frame index
                tar_15.tStart = t  # local t and not account for scr refresh
                tar_15.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_15.status = STARTED
                tar_15.play(when=win)  # sync with win flip
            
            # if tar_15 is stopping this frame...
            if tar_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_15.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_15.tStop = t  # not accounting for scr refresh
                    tar_15.frameNStop = frameN  # exact frame index
                    # update status
                    tar_15.status = FINISHED
                    tar_15.stop()
            # update tar_15 status according to whether it's playing
            if tar_15.isPlaying:
                tar_15.status = STARTED
            elif tar_15.isFinished:
                tar_15.status = FINISHED
            
            # if tar_16 is starting this frame...
            if tar_16.status == NOT_STARTED and tThisFlip >= 1.52-frameTolerance:
                # keep track of start time/frame for later
                tar_16.frameNStart = frameN  # exact frame index
                tar_16.tStart = t  # local t and not account for scr refresh
                tar_16.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_16.status = STARTED
                tar_16.play(when=win)  # sync with win flip
            
            # if tar_16 is stopping this frame...
            if tar_16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_16.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_16.tStop = t  # not accounting for scr refresh
                    tar_16.frameNStop = frameN  # exact frame index
                    # update status
                    tar_16.status = FINISHED
                    tar_16.stop()
            # update tar_16 status according to whether it's playing
            if tar_16.isPlaying:
                tar_16.status = STARTED
            elif tar_16.isFinished:
                tar_16.status = FINISHED
            
            # if tar_17 is starting this frame...
            if tar_17.status == NOT_STARTED and tThisFlip >= 1.58-frameTolerance:
                # keep track of start time/frame for later
                tar_17.frameNStart = frameN  # exact frame index
                tar_17.tStart = t  # local t and not account for scr refresh
                tar_17.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_17.status = STARTED
                tar_17.play(when=win)  # sync with win flip
            
            # if tar_17 is stopping this frame...
            if tar_17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_17.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_17.tStop = t  # not accounting for scr refresh
                    tar_17.frameNStop = frameN  # exact frame index
                    # update status
                    tar_17.status = FINISHED
                    tar_17.stop()
            # update tar_17 status according to whether it's playing
            if tar_17.isPlaying:
                tar_17.status = STARTED
            elif tar_17.isFinished:
                tar_17.status = FINISHED
            
            # if tar_18 is starting this frame...
            if tar_18.status == NOT_STARTED and tThisFlip >= 1.64-frameTolerance:
                # keep track of start time/frame for later
                tar_18.frameNStart = frameN  # exact frame index
                tar_18.tStart = t  # local t and not account for scr refresh
                tar_18.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_18.status = STARTED
                tar_18.play(when=win)  # sync with win flip
            
            # if tar_18 is stopping this frame...
            if tar_18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_18.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_18.tStop = t  # not accounting for scr refresh
                    tar_18.frameNStop = frameN  # exact frame index
                    # update status
                    tar_18.status = FINISHED
                    tar_18.stop()
            # update tar_18 status according to whether it's playing
            if tar_18.isPlaying:
                tar_18.status = STARTED
            elif tar_18.isFinished:
                tar_18.status = FINISHED
            
            # if tar_19 is starting this frame...
            if tar_19.status == NOT_STARTED and tThisFlip >= 1.7-frameTolerance:
                # keep track of start time/frame for later
                tar_19.frameNStart = frameN  # exact frame index
                tar_19.tStart = t  # local t and not account for scr refresh
                tar_19.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_19.status = STARTED
                tar_19.play(when=win)  # sync with win flip
            
            # if tar_19 is stopping this frame...
            if tar_19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_19.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_19.tStop = t  # not accounting for scr refresh
                    tar_19.frameNStop = frameN  # exact frame index
                    # update status
                    tar_19.status = FINISHED
                    tar_19.stop()
            # update tar_19 status according to whether it's playing
            if tar_19.isPlaying:
                tar_19.status = STARTED
            elif tar_19.isFinished:
                tar_19.status = FINISHED
            
            # if tar_20 is starting this frame...
            if tar_20.status == NOT_STARTED and tThisFlip >= 1.76-frameTolerance:
                # keep track of start time/frame for later
                tar_20.frameNStart = frameN  # exact frame index
                tar_20.tStart = t  # local t and not account for scr refresh
                tar_20.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_20.status = STARTED
                tar_20.play(when=win)  # sync with win flip
            
            # if tar_20 is stopping this frame...
            if tar_20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_20.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_20.tStop = t  # not accounting for scr refresh
                    tar_20.frameNStop = frameN  # exact frame index
                    # update status
                    tar_20.status = FINISHED
                    tar_20.stop()
            # update tar_20 status according to whether it's playing
            if tar_20.isPlaying:
                tar_20.status = STARTED
            elif tar_20.isFinished:
                tar_20.status = FINISHED
            
            # if tar_21 is starting this frame...
            if tar_21.status == NOT_STARTED and tThisFlip >= 1.82-frameTolerance:
                # keep track of start time/frame for later
                tar_21.frameNStart = frameN  # exact frame index
                tar_21.tStart = t  # local t and not account for scr refresh
                tar_21.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_21.status = STARTED
                tar_21.play(when=win)  # sync with win flip
            
            # if tar_21 is stopping this frame...
            if tar_21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_21.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_21.tStop = t  # not accounting for scr refresh
                    tar_21.frameNStop = frameN  # exact frame index
                    # update status
                    tar_21.status = FINISHED
                    tar_21.stop()
            # update tar_21 status according to whether it's playing
            if tar_21.isPlaying:
                tar_21.status = STARTED
            elif tar_21.isFinished:
                tar_21.status = FINISHED
            
            # if tar_22 is starting this frame...
            if tar_22.status == NOT_STARTED and tThisFlip >= 1.88-frameTolerance:
                # keep track of start time/frame for later
                tar_22.frameNStart = frameN  # exact frame index
                tar_22.tStart = t  # local t and not account for scr refresh
                tar_22.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_22.status = STARTED
                tar_22.play(when=win)  # sync with win flip
            
            # if tar_22 is stopping this frame...
            if tar_22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_22.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_22.tStop = t  # not accounting for scr refresh
                    tar_22.frameNStop = frameN  # exact frame index
                    # update status
                    tar_22.status = FINISHED
                    tar_22.stop()
            # update tar_22 status according to whether it's playing
            if tar_22.isPlaying:
                tar_22.status = STARTED
            elif tar_22.isFinished:
                tar_22.status = FINISHED
            
            # if tar_23 is starting this frame...
            if tar_23.status == NOT_STARTED and tThisFlip >= 1.94-frameTolerance:
                # keep track of start time/frame for later
                tar_23.frameNStart = frameN  # exact frame index
                tar_23.tStart = t  # local t and not account for scr refresh
                tar_23.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_23.status = STARTED
                tar_23.play(when=win)  # sync with win flip
            
            # if tar_23 is stopping this frame...
            if tar_23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_23.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_23.tStop = t  # not accounting for scr refresh
                    tar_23.frameNStop = frameN  # exact frame index
                    # update status
                    tar_23.status = FINISHED
                    tar_23.stop()
            # update tar_23 status according to whether it's playing
            if tar_23.isPlaying:
                tar_23.status = STARTED
            elif tar_23.isFinished:
                tar_23.status = FINISHED
            
            # if tar_24 is starting this frame...
            if tar_24.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                tar_24.frameNStart = frameN  # exact frame index
                tar_24.tStart = t  # local t and not account for scr refresh
                tar_24.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_24.status = STARTED
                tar_24.play(when=win)  # sync with win flip
            
            # if tar_24 is stopping this frame...
            if tar_24.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_24.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_24.tStop = t  # not accounting for scr refresh
                    tar_24.frameNStop = frameN  # exact frame index
                    # update status
                    tar_24.status = FINISHED
                    tar_24.stop()
            # update tar_24 status according to whether it's playing
            if tar_24.isPlaying:
                tar_24.status = STARTED
            elif tar_24.isFinished:
                tar_24.status = FINISHED
            
            # if tar_25 is starting this frame...
            if tar_25.status == NOT_STARTED and tThisFlip >= 2.06-frameTolerance:
                # keep track of start time/frame for later
                tar_25.frameNStart = frameN  # exact frame index
                tar_25.tStart = t  # local t and not account for scr refresh
                tar_25.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_25.status = STARTED
                tar_25.play(when=win)  # sync with win flip
            
            # if tar_25 is stopping this frame...
            if tar_25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_25.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_25.tStop = t  # not accounting for scr refresh
                    tar_25.frameNStop = frameN  # exact frame index
                    # update status
                    tar_25.status = FINISHED
                    tar_25.stop()
            # update tar_25 status according to whether it's playing
            if tar_25.isPlaying:
                tar_25.status = STARTED
            elif tar_25.isFinished:
                tar_25.status = FINISHED
            
            # if tar_26 is starting this frame...
            if tar_26.status == NOT_STARTED and tThisFlip >= 2.12-frameTolerance:
                # keep track of start time/frame for later
                tar_26.frameNStart = frameN  # exact frame index
                tar_26.tStart = t  # local t and not account for scr refresh
                tar_26.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_26.status = STARTED
                tar_26.play(when=win)  # sync with win flip
            
            # if tar_26 is stopping this frame...
            if tar_26.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_26.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_26.tStop = t  # not accounting for scr refresh
                    tar_26.frameNStop = frameN  # exact frame index
                    # update status
                    tar_26.status = FINISHED
                    tar_26.stop()
            # update tar_26 status according to whether it's playing
            if tar_26.isPlaying:
                tar_26.status = STARTED
            elif tar_26.isFinished:
                tar_26.status = FINISHED
            
            # if tar_27 is starting this frame...
            if tar_27.status == NOT_STARTED and tThisFlip >= 2.18-frameTolerance:
                # keep track of start time/frame for later
                tar_27.frameNStart = frameN  # exact frame index
                tar_27.tStart = t  # local t and not account for scr refresh
                tar_27.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_27.status = STARTED
                tar_27.play(when=win)  # sync with win flip
            
            # if tar_27 is stopping this frame...
            if tar_27.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_27.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_27.tStop = t  # not accounting for scr refresh
                    tar_27.frameNStop = frameN  # exact frame index
                    # update status
                    tar_27.status = FINISHED
                    tar_27.stop()
            # update tar_27 status according to whether it's playing
            if tar_27.isPlaying:
                tar_27.status = STARTED
            elif tar_27.isFinished:
                tar_27.status = FINISHED
            
            # if tar_28 is starting this frame...
            if tar_28.status == NOT_STARTED and tThisFlip >= 2.24-frameTolerance:
                # keep track of start time/frame for later
                tar_28.frameNStart = frameN  # exact frame index
                tar_28.tStart = t  # local t and not account for scr refresh
                tar_28.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_28.status = STARTED
                tar_28.play(when=win)  # sync with win flip
            
            # if tar_28 is stopping this frame...
            if tar_28.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_28.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_28.tStop = t  # not accounting for scr refresh
                    tar_28.frameNStop = frameN  # exact frame index
                    # update status
                    tar_28.status = FINISHED
                    tar_28.stop()
            # update tar_28 status according to whether it's playing
            if tar_28.isPlaying:
                tar_28.status = STARTED
            elif tar_28.isFinished:
                tar_28.status = FINISHED
            
            # if tar_29 is starting this frame...
            if tar_29.status == NOT_STARTED and tThisFlip >= 2.3-frameTolerance:
                # keep track of start time/frame for later
                tar_29.frameNStart = frameN  # exact frame index
                tar_29.tStart = t  # local t and not account for scr refresh
                tar_29.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_29.status = STARTED
                tar_29.play(when=win)  # sync with win flip
            
            # if tar_29 is stopping this frame...
            if tar_29.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_29.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_29.tStop = t  # not accounting for scr refresh
                    tar_29.frameNStop = frameN  # exact frame index
                    # update status
                    tar_29.status = FINISHED
                    tar_29.stop()
            # update tar_29 status according to whether it's playing
            if tar_29.isPlaying:
                tar_29.status = STARTED
            elif tar_29.isFinished:
                tar_29.status = FINISHED
            
            # if tar_30 is starting this frame...
            if tar_30.status == NOT_STARTED and tThisFlip >= 2.36-frameTolerance:
                # keep track of start time/frame for later
                tar_30.frameNStart = frameN  # exact frame index
                tar_30.tStart = t  # local t and not account for scr refresh
                tar_30.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_30.status = STARTED
                tar_30.play(when=win)  # sync with win flip
            
            # if tar_30 is stopping this frame...
            if tar_30.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_30.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_30.tStop = t  # not accounting for scr refresh
                    tar_30.frameNStop = frameN  # exact frame index
                    # update status
                    tar_30.status = FINISHED
                    tar_30.stop()
            # update tar_30 status according to whether it's playing
            if tar_30.isPlaying:
                tar_30.status = STARTED
            elif tar_30.isFinished:
                tar_30.status = FINISHED
            
            # if tar_31 is starting this frame...
            if tar_31.status == NOT_STARTED and tThisFlip >= 2.42-frameTolerance:
                # keep track of start time/frame for later
                tar_31.frameNStart = frameN  # exact frame index
                tar_31.tStart = t  # local t and not account for scr refresh
                tar_31.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('tar_31.started', tThisFlipGlobal)
                # update status
                tar_31.status = STARTED
                tar_31.play(when=win)  # sync with win flip
            
            # if tar_31 is stopping this frame...
            if tar_31.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_31.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_31.tStop = t  # not accounting for scr refresh
                    tar_31.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'tar_31.stopped')
                    # update status
                    tar_31.status = FINISHED
                    tar_31.stop()
            # update tar_31 status according to whether it's playing
            if tar_31.isPlaying:
                tar_31.status = STARTED
            elif tar_31.isFinished:
                tar_31.status = FINISHED
            
            # if tar_32 is starting this frame...
            if tar_32.status == NOT_STARTED and tThisFlip >= 2.48-frameTolerance:
                # keep track of start time/frame for later
                tar_32.frameNStart = frameN  # exact frame index
                tar_32.tStart = t  # local t and not account for scr refresh
                tar_32.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_32.status = STARTED
                tar_32.play(when=win)  # sync with win flip
            
            # if tar_32 is stopping this frame...
            if tar_32.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_32.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_32.tStop = t  # not accounting for scr refresh
                    tar_32.frameNStop = frameN  # exact frame index
                    # update status
                    tar_32.status = FINISHED
                    tar_32.stop()
            # update tar_32 status according to whether it's playing
            if tar_32.isPlaying:
                tar_32.status = STARTED
            elif tar_32.isFinished:
                tar_32.status = FINISHED
            
            # if tar_33 is starting this frame...
            if tar_33.status == NOT_STARTED and tThisFlip >= 2.54-frameTolerance:
                # keep track of start time/frame for later
                tar_33.frameNStart = frameN  # exact frame index
                tar_33.tStart = t  # local t and not account for scr refresh
                tar_33.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_33.status = STARTED
                tar_33.play(when=win)  # sync with win flip
            
            # if tar_33 is stopping this frame...
            if tar_33.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_33.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_33.tStop = t  # not accounting for scr refresh
                    tar_33.frameNStop = frameN  # exact frame index
                    # update status
                    tar_33.status = FINISHED
                    tar_33.stop()
            # update tar_33 status according to whether it's playing
            if tar_33.isPlaying:
                tar_33.status = STARTED
            elif tar_33.isFinished:
                tar_33.status = FINISHED
            
            # if tar_34 is starting this frame...
            if tar_34.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
                # keep track of start time/frame for later
                tar_34.frameNStart = frameN  # exact frame index
                tar_34.tStart = t  # local t and not account for scr refresh
                tar_34.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_34.status = STARTED
                tar_34.play(when=win)  # sync with win flip
            
            # if tar_34 is stopping this frame...
            if tar_34.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_34.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_34.tStop = t  # not accounting for scr refresh
                    tar_34.frameNStop = frameN  # exact frame index
                    # update status
                    tar_34.status = FINISHED
                    tar_34.stop()
            # update tar_34 status according to whether it's playing
            if tar_34.isPlaying:
                tar_34.status = STARTED
            elif tar_34.isFinished:
                tar_34.status = FINISHED
            
            # if tar_35 is starting this frame...
            if tar_35.status == NOT_STARTED and tThisFlip >= 2.66-frameTolerance:
                # keep track of start time/frame for later
                tar_35.frameNStart = frameN  # exact frame index
                tar_35.tStart = t  # local t and not account for scr refresh
                tar_35.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_35.status = STARTED
                tar_35.play(when=win)  # sync with win flip
            
            # if tar_35 is stopping this frame...
            if tar_35.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_35.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_35.tStop = t  # not accounting for scr refresh
                    tar_35.frameNStop = frameN  # exact frame index
                    # update status
                    tar_35.status = FINISHED
                    tar_35.stop()
            # update tar_35 status according to whether it's playing
            if tar_35.isPlaying:
                tar_35.status = STARTED
            elif tar_35.isFinished:
                tar_35.status = FINISHED
            
            # if tar_36 is starting this frame...
            if tar_36.status == NOT_STARTED and tThisFlip >= 2.72-frameTolerance:
                # keep track of start time/frame for later
                tar_36.frameNStart = frameN  # exact frame index
                tar_36.tStart = t  # local t and not account for scr refresh
                tar_36.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_36.status = STARTED
                tar_36.play(when=win)  # sync with win flip
            
            # if tar_36 is stopping this frame...
            if tar_36.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_36.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_36.tStop = t  # not accounting for scr refresh
                    tar_36.frameNStop = frameN  # exact frame index
                    # update status
                    tar_36.status = FINISHED
                    tar_36.stop()
            # update tar_36 status according to whether it's playing
            if tar_36.isPlaying:
                tar_36.status = STARTED
            elif tar_36.isFinished:
                tar_36.status = FINISHED
            
            # if tar_37 is starting this frame...
            if tar_37.status == NOT_STARTED and tThisFlip >= 2.78-frameTolerance:
                # keep track of start time/frame for later
                tar_37.frameNStart = frameN  # exact frame index
                tar_37.tStart = t  # local t and not account for scr refresh
                tar_37.tStartRefresh = tThisFlipGlobal  # on global time
                # update status
                tar_37.status = STARTED
                tar_37.play(when=win)  # sync with win flip
            
            # if tar_37 is stopping this frame...
            if tar_37.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tar_37.tStartRefresh + 0.06-frameTolerance:
                    # keep track of stop time/frame for later
                    tar_37.tStop = t  # not accounting for scr refresh
                    tar_37.frameNStop = frameN  # exact frame index
                    # update status
                    tar_37.status = FINISHED
                    tar_37.stop()
            # update tar_37 status according to whether it's playing
            if tar_37.isPlaying:
                tar_37.status = STARTED
            elif tar_37.isFinished:
                tar_37.status = FINISHED
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.started')
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                pass
            
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
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        tar.pause()  # ensure sound has stopped at end of Routine
        sound1.pause()  # ensure sound has stopped at end of Routine
        sound1_2.pause()  # ensure sound has stopped at end of Routine
        sound1_3.pause()  # ensure sound has stopped at end of Routine
        sound1_4.pause()  # ensure sound has stopped at end of Routine
        sound1_5.pause()  # ensure sound has stopped at end of Routine
        sound1_6.pause()  # ensure sound has stopped at end of Routine
        sound1_7.pause()  # ensure sound has stopped at end of Routine
        sound1_8.pause()  # ensure sound has stopped at end of Routine
        sound2.pause()  # ensure sound has stopped at end of Routine
        sound2_2.pause()  # ensure sound has stopped at end of Routine
        sound2_3.pause()  # ensure sound has stopped at end of Routine
        sound2_4.pause()  # ensure sound has stopped at end of Routine
        sound2_5.pause()  # ensure sound has stopped at end of Routine
        sound2_6.pause()  # ensure sound has stopped at end of Routine
        sound2_7.pause()  # ensure sound has stopped at end of Routine
        sound2_8.pause()  # ensure sound has stopped at end of Routine
        sound3.pause()  # ensure sound has stopped at end of Routine
        sound3_2.pause()  # ensure sound has stopped at end of Routine
        sound3_3.pause()  # ensure sound has stopped at end of Routine
        sound3_4.pause()  # ensure sound has stopped at end of Routine
        sound3_5.pause()  # ensure sound has stopped at end of Routine
        sound3_6.pause()  # ensure sound has stopped at end of Routine
        sound3_7.pause()  # ensure sound has stopped at end of Routine
        sound3_8.pause()  # ensure sound has stopped at end of Routine
        sound4.pause()  # ensure sound has stopped at end of Routine
        sound4_2.pause()  # ensure sound has stopped at end of Routine
        sound4_3.pause()  # ensure sound has stopped at end of Routine
        sound4_4.pause()  # ensure sound has stopped at end of Routine
        sound4_5.pause()  # ensure sound has stopped at end of Routine
        sound4_6.pause()  # ensure sound has stopped at end of Routine
        sound4_7.pause()  # ensure sound has stopped at end of Routine
        sound4_8.pause()  # ensure sound has stopped at end of Routine
        sound5.pause()  # ensure sound has stopped at end of Routine
        sound5_2.pause()  # ensure sound has stopped at end of Routine
        sound5_3.pause()  # ensure sound has stopped at end of Routine
        sound5_4.pause()  # ensure sound has stopped at end of Routine
        sound5_5.pause()  # ensure sound has stopped at end of Routine
        sound5_6.pause()  # ensure sound has stopped at end of Routine
        sound5_7.pause()  # ensure sound has stopped at end of Routine
        sound5_8.pause()  # ensure sound has stopped at end of Routine
        sound6.pause()  # ensure sound has stopped at end of Routine
        sound6_2.pause()  # ensure sound has stopped at end of Routine
        sound6_3.pause()  # ensure sound has stopped at end of Routine
        sound6_4.pause()  # ensure sound has stopped at end of Routine
        sound6_5.pause()  # ensure sound has stopped at end of Routine
        sound6_6.pause()  # ensure sound has stopped at end of Routine
        sound6_7.pause()  # ensure sound has stopped at end of Routine
        sound6_8.pause()  # ensure sound has stopped at end of Routine
        sound7.pause()  # ensure sound has stopped at end of Routine
        sound7_2.pause()  # ensure sound has stopped at end of Routine
        sound7_3.pause()  # ensure sound has stopped at end of Routine
        sound7_4.pause()  # ensure sound has stopped at end of Routine
        sound7_5.pause()  # ensure sound has stopped at end of Routine
        sound7_6.pause()  # ensure sound has stopped at end of Routine
        sound7_7.pause()  # ensure sound has stopped at end of Routine
        sound7_8.pause()  # ensure sound has stopped at end of Routine
        sound8.pause()  # ensure sound has stopped at end of Routine
        sound8_2.pause()  # ensure sound has stopped at end of Routine
        sound8_3.pause()  # ensure sound has stopped at end of Routine
        sound8_4.pause()  # ensure sound has stopped at end of Routine
        sound8_5.pause()  # ensure sound has stopped at end of Routine
        sound8_6.pause()  # ensure sound has stopped at end of Routine
        sound8_7.pause()  # ensure sound has stopped at end of Routine
        sound8_8.pause()  # ensure sound has stopped at end of Routine
        sound9.pause()  # ensure sound has stopped at end of Routine
        sound9_2.pause()  # ensure sound has stopped at end of Routine
        sound9_3.pause()  # ensure sound has stopped at end of Routine
        sound9_4.pause()  # ensure sound has stopped at end of Routine
        sound9_5.pause()  # ensure sound has stopped at end of Routine
        sound9_6.pause()  # ensure sound has stopped at end of Routine
        sound9_7.pause()  # ensure sound has stopped at end of Routine
        sound9_8.pause()  # ensure sound has stopped at end of Routine
        sound10.pause()  # ensure sound has stopped at end of Routine
        sound10_2.pause()  # ensure sound has stopped at end of Routine
        sound10_3.pause()  # ensure sound has stopped at end of Routine
        sound10_4.pause()  # ensure sound has stopped at end of Routine
        sound10_5.pause()  # ensure sound has stopped at end of Routine
        sound10_6.pause()  # ensure sound has stopped at end of Routine
        sound10_7.pause()  # ensure sound has stopped at end of Routine
        sound10_8.pause()  # ensure sound has stopped at end of Routine
        sound11.pause()  # ensure sound has stopped at end of Routine
        sound11_2.pause()  # ensure sound has stopped at end of Routine
        sound11_3.pause()  # ensure sound has stopped at end of Routine
        sound11_4.pause()  # ensure sound has stopped at end of Routine
        sound11_5.pause()  # ensure sound has stopped at end of Routine
        sound11_6.pause()  # ensure sound has stopped at end of Routine
        sound11_7.pause()  # ensure sound has stopped at end of Routine
        sound11_8.pause()  # ensure sound has stopped at end of Routine
        sound12.pause()  # ensure sound has stopped at end of Routine
        sound12_2.pause()  # ensure sound has stopped at end of Routine
        sound12_3.pause()  # ensure sound has stopped at end of Routine
        sound12_4.pause()  # ensure sound has stopped at end of Routine
        sound12_5.pause()  # ensure sound has stopped at end of Routine
        sound12_6.pause()  # ensure sound has stopped at end of Routine
        sound12_7.pause()  # ensure sound has stopped at end of Routine
        sound12_8.pause()  # ensure sound has stopped at end of Routine
        sound13.pause()  # ensure sound has stopped at end of Routine
        sound13_2.pause()  # ensure sound has stopped at end of Routine
        sound13_3.pause()  # ensure sound has stopped at end of Routine
        sound13_4.pause()  # ensure sound has stopped at end of Routine
        sound13_5.pause()  # ensure sound has stopped at end of Routine
        sound13_6.pause()  # ensure sound has stopped at end of Routine
        sound13_7.pause()  # ensure sound has stopped at end of Routine
        sound13_8.pause()  # ensure sound has stopped at end of Routine
        sound14.pause()  # ensure sound has stopped at end of Routine
        sound14_2.pause()  # ensure sound has stopped at end of Routine
        sound14_3.pause()  # ensure sound has stopped at end of Routine
        sound14_4.pause()  # ensure sound has stopped at end of Routine
        sound14_5.pause()  # ensure sound has stopped at end of Routine
        sound14_6.pause()  # ensure sound has stopped at end of Routine
        sound14_7.pause()  # ensure sound has stopped at end of Routine
        sound14_8.pause()  # ensure sound has stopped at end of Routine
        sound15.pause()  # ensure sound has stopped at end of Routine
        sound15_2.pause()  # ensure sound has stopped at end of Routine
        sound15_3.pause()  # ensure sound has stopped at end of Routine
        sound15_4.pause()  # ensure sound has stopped at end of Routine
        sound15_5.pause()  # ensure sound has stopped at end of Routine
        sound15_6.pause()  # ensure sound has stopped at end of Routine
        sound15_7.pause()  # ensure sound has stopped at end of Routine
        sound15_8.pause()  # ensure sound has stopped at end of Routine
        spund16.pause()  # ensure sound has stopped at end of Routine
        spund16_2.pause()  # ensure sound has stopped at end of Routine
        spund16_3.pause()  # ensure sound has stopped at end of Routine
        spund16_4.pause()  # ensure sound has stopped at end of Routine
        spund16_5.pause()  # ensure sound has stopped at end of Routine
        spund16_6.pause()  # ensure sound has stopped at end of Routine
        spund16_7.pause()  # ensure sound has stopped at end of Routine
        spund16_8.pause()  # ensure sound has stopped at end of Routine
        sound17.pause()  # ensure sound has stopped at end of Routine
        sound17_2.pause()  # ensure sound has stopped at end of Routine
        sound17_3.pause()  # ensure sound has stopped at end of Routine
        sound17_4.pause()  # ensure sound has stopped at end of Routine
        sound17_5.pause()  # ensure sound has stopped at end of Routine
        sound17_6.pause()  # ensure sound has stopped at end of Routine
        sound17_7.pause()  # ensure sound has stopped at end of Routine
        sound17_8.pause()  # ensure sound has stopped at end of Routine
        sound18.pause()  # ensure sound has stopped at end of Routine
        sound18_2.pause()  # ensure sound has stopped at end of Routine
        sound18_3.pause()  # ensure sound has stopped at end of Routine
        sound18_4.pause()  # ensure sound has stopped at end of Routine
        sound18_5.pause()  # ensure sound has stopped at end of Routine
        sound18_6.pause()  # ensure sound has stopped at end of Routine
        sound18_7.pause()  # ensure sound has stopped at end of Routine
        sound18_8.pause()  # ensure sound has stopped at end of Routine
        sound19.pause()  # ensure sound has stopped at end of Routine
        sound19_2.pause()  # ensure sound has stopped at end of Routine
        sound19_3.pause()  # ensure sound has stopped at end of Routine
        sound19_4.pause()  # ensure sound has stopped at end of Routine
        sound19_5.pause()  # ensure sound has stopped at end of Routine
        sound19_6.pause()  # ensure sound has stopped at end of Routine
        sound19_7.pause()  # ensure sound has stopped at end of Routine
        sound19_8.pause()  # ensure sound has stopped at end of Routine
        sound20.pause()  # ensure sound has stopped at end of Routine
        sound20_2.pause()  # ensure sound has stopped at end of Routine
        sound20_3.pause()  # ensure sound has stopped at end of Routine
        sound20_4.pause()  # ensure sound has stopped at end of Routine
        sound20_5.pause()  # ensure sound has stopped at end of Routine
        sound20_6.pause()  # ensure sound has stopped at end of Routine
        sound20_7.pause()  # ensure sound has stopped at end of Routine
        sound20_8.pause()  # ensure sound has stopped at end of Routine
        sound21.pause()  # ensure sound has stopped at end of Routine
        sound21_2.pause()  # ensure sound has stopped at end of Routine
        sound21_3.pause()  # ensure sound has stopped at end of Routine
        sound21_4.pause()  # ensure sound has stopped at end of Routine
        sound21_5.pause()  # ensure sound has stopped at end of Routine
        sound21_6.pause()  # ensure sound has stopped at end of Routine
        sound21_7.pause()  # ensure sound has stopped at end of Routine
        sound21_8.pause()  # ensure sound has stopped at end of Routine
        sound22.pause()  # ensure sound has stopped at end of Routine
        sound22_2.pause()  # ensure sound has stopped at end of Routine
        sound22_3.pause()  # ensure sound has stopped at end of Routine
        sound22_4.pause()  # ensure sound has stopped at end of Routine
        sound22_5.pause()  # ensure sound has stopped at end of Routine
        sound22_6.pause()  # ensure sound has stopped at end of Routine
        sound22_7.pause()  # ensure sound has stopped at end of Routine
        sound22_8.pause()  # ensure sound has stopped at end of Routine
        sound23.pause()  # ensure sound has stopped at end of Routine
        sound23_2.pause()  # ensure sound has stopped at end of Routine
        sound23_3.pause()  # ensure sound has stopped at end of Routine
        sound23_4.pause()  # ensure sound has stopped at end of Routine
        sound23_5.pause()  # ensure sound has stopped at end of Routine
        sound23_6.pause()  # ensure sound has stopped at end of Routine
        sound23_7.pause()  # ensure sound has stopped at end of Routine
        sound23_8.pause()  # ensure sound has stopped at end of Routine
        sound24.pause()  # ensure sound has stopped at end of Routine
        sound24_2.pause()  # ensure sound has stopped at end of Routine
        sound24_3.pause()  # ensure sound has stopped at end of Routine
        sound24_4.pause()  # ensure sound has stopped at end of Routine
        sound24_5.pause()  # ensure sound has stopped at end of Routine
        sound24_6.pause()  # ensure sound has stopped at end of Routine
        sound24_7.pause()  # ensure sound has stopped at end of Routine
        sound24_8.pause()  # ensure sound has stopped at end of Routine
        sound25.pause()  # ensure sound has stopped at end of Routine
        sound25_2.pause()  # ensure sound has stopped at end of Routine
        sound25_3.pause()  # ensure sound has stopped at end of Routine
        sound25_4.pause()  # ensure sound has stopped at end of Routine
        sound25_5.pause()  # ensure sound has stopped at end of Routine
        sound25_6.pause()  # ensure sound has stopped at end of Routine
        sound25_7.pause()  # ensure sound has stopped at end of Routine
        sound25_8.pause()  # ensure sound has stopped at end of Routine
        sound26.pause()  # ensure sound has stopped at end of Routine
        sound26_2.pause()  # ensure sound has stopped at end of Routine
        sound26_3.pause()  # ensure sound has stopped at end of Routine
        sound26_4.pause()  # ensure sound has stopped at end of Routine
        sound26_5.pause()  # ensure sound has stopped at end of Routine
        sound26_6.pause()  # ensure sound has stopped at end of Routine
        sound26_7.pause()  # ensure sound has stopped at end of Routine
        sound26_8.pause()  # ensure sound has stopped at end of Routine
        sound27.pause()  # ensure sound has stopped at end of Routine
        sound27_2.pause()  # ensure sound has stopped at end of Routine
        sound27_3.pause()  # ensure sound has stopped at end of Routine
        sound27_4.pause()  # ensure sound has stopped at end of Routine
        sound27_5.pause()  # ensure sound has stopped at end of Routine
        sound27_6.pause()  # ensure sound has stopped at end of Routine
        sound27_7.pause()  # ensure sound has stopped at end of Routine
        sound27_8.pause()  # ensure sound has stopped at end of Routine
        sound28.pause()  # ensure sound has stopped at end of Routine
        sound28_2.pause()  # ensure sound has stopped at end of Routine
        sound28_3.pause()  # ensure sound has stopped at end of Routine
        sound28_4.pause()  # ensure sound has stopped at end of Routine
        sound28_5.pause()  # ensure sound has stopped at end of Routine
        sound28_6.pause()  # ensure sound has stopped at end of Routine
        sound28_7.pause()  # ensure sound has stopped at end of Routine
        sound28_8.pause()  # ensure sound has stopped at end of Routine
        sound29.pause()  # ensure sound has stopped at end of Routine
        sound29_2.pause()  # ensure sound has stopped at end of Routine
        sound29_3.pause()  # ensure sound has stopped at end of Routine
        sound29_4.pause()  # ensure sound has stopped at end of Routine
        sound29_5.pause()  # ensure sound has stopped at end of Routine
        sound29_6.pause()  # ensure sound has stopped at end of Routine
        sound29_7.pause()  # ensure sound has stopped at end of Routine
        sound29_8.pause()  # ensure sound has stopped at end of Routine
        sound30.pause()  # ensure sound has stopped at end of Routine
        sound30_2.pause()  # ensure sound has stopped at end of Routine
        sound30_3.pause()  # ensure sound has stopped at end of Routine
        sound30_4.pause()  # ensure sound has stopped at end of Routine
        sound30_5.pause()  # ensure sound has stopped at end of Routine
        sound30_6.pause()  # ensure sound has stopped at end of Routine
        sound30_7.pause()  # ensure sound has stopped at end of Routine
        sound30_8.pause()  # ensure sound has stopped at end of Routine
        sound31.pause()  # ensure sound has stopped at end of Routine
        sound31_2.pause()  # ensure sound has stopped at end of Routine
        sound31_3.pause()  # ensure sound has stopped at end of Routine
        sound31_4.pause()  # ensure sound has stopped at end of Routine
        sound31_5.pause()  # ensure sound has stopped at end of Routine
        sound31_6.pause()  # ensure sound has stopped at end of Routine
        sound31_7.pause()  # ensure sound has stopped at end of Routine
        sound31_8.pause()  # ensure sound has stopped at end of Routine
        sound32.pause()  # ensure sound has stopped at end of Routine
        sound32_2.pause()  # ensure sound has stopped at end of Routine
        sound32_3.pause()  # ensure sound has stopped at end of Routine
        sound32_4.pause()  # ensure sound has stopped at end of Routine
        sound32_5.pause()  # ensure sound has stopped at end of Routine
        sound32_6.pause()  # ensure sound has stopped at end of Routine
        sound32_7.pause()  # ensure sound has stopped at end of Routine
        sound32_8.pause()  # ensure sound has stopped at end of Routine
        sound33.pause()  # ensure sound has stopped at end of Routine
        sound33_2.pause()  # ensure sound has stopped at end of Routine
        sound33_3.pause()  # ensure sound has stopped at end of Routine
        sound33_4.pause()  # ensure sound has stopped at end of Routine
        sound33_5.pause()  # ensure sound has stopped at end of Routine
        sound33_6.pause()  # ensure sound has stopped at end of Routine
        sound33_7.pause()  # ensure sound has stopped at end of Routine
        sound33_8.pause()  # ensure sound has stopped at end of Routine
        sound34.pause()  # ensure sound has stopped at end of Routine
        sound34_2.pause()  # ensure sound has stopped at end of Routine
        sound34_3.pause()  # ensure sound has stopped at end of Routine
        sound34_4.pause()  # ensure sound has stopped at end of Routine
        sound34_5.pause()  # ensure sound has stopped at end of Routine
        sound34_6.pause()  # ensure sound has stopped at end of Routine
        sound34_7.pause()  # ensure sound has stopped at end of Routine
        sound34_8.pause()  # ensure sound has stopped at end of Routine
        sound35.pause()  # ensure sound has stopped at end of Routine
        sound35_2.pause()  # ensure sound has stopped at end of Routine
        sound35_3.pause()  # ensure sound has stopped at end of Routine
        sound35_4.pause()  # ensure sound has stopped at end of Routine
        sound35_5.pause()  # ensure sound has stopped at end of Routine
        sound35_6.pause()  # ensure sound has stopped at end of Routine
        sound35_7.pause()  # ensure sound has stopped at end of Routine
        sound35_8.pause()  # ensure sound has stopped at end of Routine
        sound36.pause()  # ensure sound has stopped at end of Routine
        sound36_2.pause()  # ensure sound has stopped at end of Routine
        sound36_3.pause()  # ensure sound has stopped at end of Routine
        sound36_4.pause()  # ensure sound has stopped at end of Routine
        sound36_5.pause()  # ensure sound has stopped at end of Routine
        sound36_6.pause()  # ensure sound has stopped at end of Routine
        sound36_7.pause()  # ensure sound has stopped at end of Routine
        sound36_8.pause()  # ensure sound has stopped at end of Routine
        sound37.pause()  # ensure sound has stopped at end of Routine
        sound37_2.pause()  # ensure sound has stopped at end of Routine
        sound37_3.pause()  # ensure sound has stopped at end of Routine
        sound37_4.pause()  # ensure sound has stopped at end of Routine
        sound37_5.pause()  # ensure sound has stopped at end of Routine
        sound37_6.pause()  # ensure sound has stopped at end of Routine
        sound37_7.pause()  # ensure sound has stopped at end of Routine
        sound37_8.pause()  # ensure sound has stopped at end of Routine
        sound38.pause()  # ensure sound has stopped at end of Routine
        sound38_2.pause()  # ensure sound has stopped at end of Routine
        sound38_3.pause()  # ensure sound has stopped at end of Routine
        sound38_4.pause()  # ensure sound has stopped at end of Routine
        sound38_5.pause()  # ensure sound has stopped at end of Routine
        sound38_6.pause()  # ensure sound has stopped at end of Routine
        sound38_7.pause()  # ensure sound has stopped at end of Routine
        sound38_8.pause()  # ensure sound has stopped at end of Routine
        sound39.pause()  # ensure sound has stopped at end of Routine
        sound39_2.pause()  # ensure sound has stopped at end of Routine
        sound39_3.pause()  # ensure sound has stopped at end of Routine
        sound39_4.pause()  # ensure sound has stopped at end of Routine
        sound39_5.pause()  # ensure sound has stopped at end of Routine
        sound39_6.pause()  # ensure sound has stopped at end of Routine
        sound39_7.pause()  # ensure sound has stopped at end of Routine
        sound39_8.pause()  # ensure sound has stopped at end of Routine
        sound40.pause()  # ensure sound has stopped at end of Routine
        sound40_2.pause()  # ensure sound has stopped at end of Routine
        sound40_3.pause()  # ensure sound has stopped at end of Routine
        sound40_4.pause()  # ensure sound has stopped at end of Routine
        sound40_5.pause()  # ensure sound has stopped at end of Routine
        sound40_6.pause()  # ensure sound has stopped at end of Routine
        sound40_7.pause()  # ensure sound has stopped at end of Routine
        sound40_8.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
            # was no response the correct answer?!
            if str(correct).lower() == 'none':
               key_resp_3.corr = 1;  # correct non-response
            else:
               key_resp_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('key_resp_3.keys',key_resp_3.keys)
        trials_3.addData('key_resp_3.corr', key_resp_3.corr)
        if key_resp_3.keys != None:  # we had a response
            trials_3.addData('key_resp_3.rt', key_resp_3.rt)
            trials_3.addData('key_resp_3.duration', key_resp_3.duration)
        tar_2.pause()  # ensure sound has stopped at end of Routine
        tar_3.pause()  # ensure sound has stopped at end of Routine
        tar_4.pause()  # ensure sound has stopped at end of Routine
        tar_5.pause()  # ensure sound has stopped at end of Routine
        tar_6.pause()  # ensure sound has stopped at end of Routine
        tar_7.pause()  # ensure sound has stopped at end of Routine
        tar_8.pause()  # ensure sound has stopped at end of Routine
        tar_9.pause()  # ensure sound has stopped at end of Routine
        tar_10.pause()  # ensure sound has stopped at end of Routine
        tar_11.pause()  # ensure sound has stopped at end of Routine
        tar_12.pause()  # ensure sound has stopped at end of Routine
        tar_13.pause()  # ensure sound has stopped at end of Routine
        tar_14.pause()  # ensure sound has stopped at end of Routine
        tar_15.pause()  # ensure sound has stopped at end of Routine
        tar_16.pause()  # ensure sound has stopped at end of Routine
        tar_17.pause()  # ensure sound has stopped at end of Routine
        tar_18.pause()  # ensure sound has stopped at end of Routine
        tar_19.pause()  # ensure sound has stopped at end of Routine
        tar_20.pause()  # ensure sound has stopped at end of Routine
        tar_21.pause()  # ensure sound has stopped at end of Routine
        tar_22.pause()  # ensure sound has stopped at end of Routine
        tar_23.pause()  # ensure sound has stopped at end of Routine
        tar_24.pause()  # ensure sound has stopped at end of Routine
        tar_25.pause()  # ensure sound has stopped at end of Routine
        tar_26.pause()  # ensure sound has stopped at end of Routine
        tar_27.pause()  # ensure sound has stopped at end of Routine
        tar_28.pause()  # ensure sound has stopped at end of Routine
        tar_29.pause()  # ensure sound has stopped at end of Routine
        tar_30.pause()  # ensure sound has stopped at end of Routine
        tar_31.pause()  # ensure sound has stopped at end of Routine
        tar_32.pause()  # ensure sound has stopped at end of Routine
        tar_33.pause()  # ensure sound has stopped at end of Routine
        tar_34.pause()  # ensure sound has stopped at end of Routine
        tar_35.pause()  # ensure sound has stopped at end of Routine
        tar_36.pause()  # ensure sound has stopped at end of Routine
        tar_37.pause()  # ensure sound has stopped at end of Routine
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pra_feed" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pra_feed.started', globalClock.getTime())
        # Run 'Begin Routine' code from code_8
        if key_resp_3.corr==1:
            message='correct'
        elif key_resp_3.corr==0:
            message='incorrect'
        
        for i in range(40):
            condition_list[0][i][0][0]
            condition_list[0][i][0][1]
            condition_list[0][i][0][2]
            condition_list[0][i][0][3]
            condition_list[0][i][1][0]
            condition_list[0][i][1][1]
            condition_list[0][i][1][2]
            condition_list[0][i][1][3]
            chord_list.append(condition_list[0][i][0][0])
            chord_list.append(condition_list[0][i][0][1])
            chord_list.append(condition_list[0][i][0][2])
            chord_list.append(condition_list[0][i][0][3])
            chord_list.append(condition_list[0][i][1][0])
            chord_list.append(condition_list[0][i][1][1])
            chord_list.append(condition_list[0][i][1][2])
            chord_list.append(condition_list[0][i][1][3])
        
        
        thisExp.addData("chord_list", chord_list)
        text_11.setText(message)
        # keep track of which components have finished
        pra_feedComponents = [text_11]
        for thisComponent in pra_feedComponents:
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
        
        # --- Run Routine "pra_feed" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            
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
            for thisComponent in pra_feedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pra_feed" ---
        for thisComponent in pra_feedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pra_feed.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_8
        if target== "wav\C7.wav":
            c_upper.append("wav\C7.wav")
            f_upper.append("wav\C7.wav")
            a_upper.append("wav\C7.wav")
            c_upper2.append("wav\C7.wav")
            f_upper2.append("wav\C7.wav")
            a_upper2.append("wav\C7.wav")
            c_upper3.append("wav\C7.wav")
            f_upper3.append("wav\C7.wav")
            a_upper3.append("wav\C7.wav")
            c_upper4.append("wav\C7.wav")
            f_upper4.append("wav\C7.wav")
            a_upper4.append("wav\C7.wav")
            c_upper5.append("wav\C7.wav")
            f_upper5.append("wav\C7.wav")
            a_upper5.append("wav\C7.wav")
            c_upper6.append("wav\C7.wav")
            f_upper6.append("wav\C7.wav")
            a_upper6.append("wav\C7.wav")
            disone_upper.append("wav\C7.wav")
            disone_upper2.append("wav\C7.wav")
            disone_upper3.append("wav\C7.wav")
            disone_upper4.append("wav\C7.wav")
            disone_upper5.append("wav\C7.wav")
            disone_upper6.append("wav\C7.wav")
            disone_upper7.append("wav\C7.wav")
            disone_upper8.append("wav\C7.wav")
            disone_upper9.append("wav\C7.wav")
            disone_upper10.append("wav\C7.wav")
            disone_upper11.append("wav\C7.wav")
            disone_upper12.append("wav\C7.wav")
            disone_upper13.append("wav\C7.wav")
            disone_upper14.append("wav\C7.wav")
            disone_upper15.append("wav\C7.wav")
            disone_upper16.append("wav\C7.wav")
            disone_upper17.append("wav\C7.wav")
            disone_upper18.append("wav\C7.wav")
            disone_upper19.append("wav\C7.wav")
            disone_upper20.append("wav\C7.wav")
            disone_upper21.append("wav\C7.wav")
            disone_upper22.append("wav\C7.wav")
            disone_upper23.append("wav\C7.wav")
            disone_upper24.append("wav\C7.wav")
            disone_upper25.append("wav\C7.wav")
            disone_upper26.append("wav\C7.wav")
            disone_upper27.append("wav\C7.wav")
            disone_upper28.append("wav\C7.wav")
            disone_upper29.append("wav\C7.wav")
            disone_upper30.append("wav\C7.wav")
            disone_upper31.append("wav\C7.wav")
            disone_upper32.append("wav\C7.wav")
            disone_upper33.append("wav\C7.wav")
            disone_upper34.append("wav\C7.wav")
            disone_upper35.append("wav\C7.wav")
            disone_upper36.append("wav\C7.wav")
            disone_upper37.append("wav\C7.wav")
            disone_upper38.append("wav\C7.wav")
            disone_upper39.append("wav\C7.wav")
            disone_upper40.append("wav\C7.wav")
        elif target== "wav\D7.wav":
            g_lower.append(g_upper[-1])
            g_upper.remove(g_upper[-1])
            g_upper.append("wav\D7.wav")
            b_lower.append(b_upper[-1])
            b_upper.remove(b_upper[-1])
            b_upper.append("wav\D7.wav")
            disone_upper.append("wav\D7.wav")
            g_lower2.append(g_upper2[-1])
            g_upper2.remove(g_upper2[-1])
            g_upper2.append("wav\D7.wav")
            b_lower2.append(b_upper2[-1])
            b_upper2.remove(b_upper2[-1])
            b_upper2.append("wav\D7.wav")
            disone_upper2.append("wav\D7.wav")
            g_lower3.append(g_upper3[-1])
            g_upper3.remove(g_upper3[-1])
            g_upper3.append("wav\D7.wav")
            b_lower3.append(b_upper3[-1])
            b_upper3.remove(b_upper3[-1])
            b_upper3.append("wav\D7.wav")
            disone_upper3.append("wav\D7.wav")
            g_lower4.append(g_upper4[-1])
            g_upper4.remove(g_upper4[-1])
            g_upper4.append("wav\D7.wav")
            b_lower4.append(b_upper4[-1])
            b_upper4.remove(b_upper4[-1])
            b_upper4.append("wav\D7.wav")
            disone_upper4.append("wav\D7.wav")
            g_lower5.append(g_upper5[-1])
            g_upper5.remove(g_upper5[-1])
            g_upper5.append("wav\D7.wav")
            b_lower5.append(b_upper5[-1])
            b_upper5.remove(b_upper5[-1])
            b_upper5.append("wav\D7.wav")
            disone_upper5.append("wav\D7.wav")
            g_lower6.append(g_upper6[-1])
            g_upper6.remove(g_upper6[-1])
            g_upper6.append("wav\D7.wav")
            b_lower6.append(b_upper6[-1])
            b_upper6.remove(b_upper6[-1])
            b_upper6.append("wav\D7.wav")
            disone_upper6.append("wav\D7.wav")
            disone_upper7.append("wav\D7.wav")
            disone_upper8.append("wav\D7.wav")
            disone_upper9.append("wav\D7.wav")
            disone_upper10.append("wav\D7.wav")
            disone_upper11.append("wav\D7.wav")
            disone_upper12.append("wav\D7.wav")
            disone_upper13.append("wav\D7.wav")
            disone_upper14.append("wav\D7.wav")
            disone_upper15.append("wav\D7.wav")
            disone_upper16.append("wav\D7.wav")
            disone_upper17.append("wav\D7.wav")
            disone_upper18.append("wav\D7.wav")
            disone_upper19.append("wav\D7.wav")
            disone_upper20.append("wav\D7.wav") 
            disone_upper21.append("wav\D7.wav")
            disone_upper22.append("wav\D7.wav")
            disone_upper23.append("wav\D7.wav")
            disone_upper24.append("wav\D7.wav")
            disone_upper25.append("wav\D7.wav")
            disone_upper26.append("wav\D7.wav")
            disone_upper27.append("wav\D7.wav")
            disone_upper28.append("wav\D7.wav")
            disone_upper29.append("wav\D7.wav")
            disone_upper30.append("wav\D7.wav")
            disone_upper31.append("wav\D7.wav")
            disone_upper32.append("wav\D7.wav")
            disone_upper33.append("wav\D7.wav")
            disone_upper34.append("wav\D7.wav")
            disone_upper35.append("wav\D7.wav")
            disone_upper36.append("wav\D7.wav")
            disone_upper37.append("wav\D7.wav")
            disone_upper38.append("wav\D7.wav")
            disone_upper39.append("wav\D7.wav")
            disone_upper40.append("wav\D7.wav")
            d_upper.append("wav\D7.wav")
            d_upper2.append("wav\D7.wav")
            d_upper3.append("wav\D7.wav")
            d_upper4.append("wav\D7.wav")
            d_upper5.append("wav\D7.wav")
            d_upper6.append("wav\D7.wav")
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials_3'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    # keep track of which components have finished
    endComponents = [text_6]
    for thisComponent in endComponents:
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
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        
        # if text_6 is stopping this frame...
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                # update status
                text_6.status = FINISHED
                text_6.setAutoDraw(False)
        
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
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
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
