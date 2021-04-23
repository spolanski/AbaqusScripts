#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Slawomir Polanski
"""
#===========================================================================
# IMPORT STATEMENTS
#===========================================================================
#import numpy as np
#import matplotlib.pyplot as plt

from abaqus import *
from abaqusConstants import *
from caeModules import *
import os, shutil
from subprocess import Popen, PIPE


# import xyPlot
# import displayGroupOdbToolset as dgo
# from collections import OrderedDict

#import odbAccess
#odbAccess.openOdb(path='myOdb.odb')                                # Abq/Vie
#session.openOdb(name='myOdb', path='stress.odb', readOnly=True)    # Abq/Cae

from textRepr import prettyPrint as pr 
    # odb = session.openOdb('odb_path')

def create_video_viewport(odb):
    if 'video' in session.viewports.keys():
        vprt = session.viewports['video']
    else:
        # linkedin 372 x 400 -> 135.0 x 152.1
        vprt = session.Viewport(name='video', width=135.0, height=152.1)
    
    vprt.setValues(displayedObject=odb)
    vprt.makeCurrent()
    return vprt

def print_pictures(vprt, odb):
    try:
        os.mkdir(os.getcwd() + '\\images')
    except WindowsError:
        shutil.rmtree(os.getcwd() + '\\images')
        os.mkdir(os.getcwd() + '\\images')
    session.printOptions.setValues(reduceColors=False)
    session.printOptions.setValues(vpDecorations=OFF)
 
    numOfFrames = len(odb.steps.values()[0].frames)
    for f in range(numOfFrames):
        vprt.odbDisplay.setFrame(step=0, frame=f )
        fileName = 'img-' + str(f).zfill(3)
        session.printToFile(fileName=os.getcwd()+'\\images\\'+fileName,
                            format=PNG, canvasObjects=(vprt, ))

if __name__ == '__main__':
    video_name = 'LiHeatMap'
    
    curr_vprt = session.viewports[session.currentViewportName]
    mod_path = curr_vprt.displayedObject.path
    odb = session.openOdb(name='myOdb', path=mod_path, readOnly=True)    # Abq/Cae
    viewport = create_video_viewport(odb=odb)
    print_pictures(vprt=viewport, odb=odb)
    path = '/'.join(mod_path.split('/')[:-1])
    print('make_video.bat {} {}'.format(path, video_name))
    p = Popen(['make_video.bat', path, video_name], stdout=PIPE, stderr=PIPE)
    output, errors = p.communicate()
    p.wait() # wait for process to terminate