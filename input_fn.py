# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:33:47 2017

@author: lidong
"""

import os

import numpy as np
import tensorflow as tf

from tensorflow.python.platform import flags
from tensorflow.python.platform import gfile
import cv2

import python_pfm
FLAGS=flags.FLAGS

# Original image dimensions
ORIGINAL_WIDTH = 640
ORIGINAL_HEIGHT = 512
COLOR_CHAN = 3

# Default image dimensions.
IMG_WIDTH = 64
IMG_HEIGHT = 64

def get_input(mode=0):
"""creat input data and ground truth data for network
Args:
	the mode is training or prediction
Return:
	three matrix for left images, right images, ground truth images
"""
    olfilenames=gfile.Glob(os.path.join(FLAGS.data_dir,'*','left','*.png'))
    orflilenames=gfile.Glob(os.path.join(FLAGS.data_data,'*','right','*.png'))
    glfilenames=gfile.Glob(os.path.join(FLAGS.data_data,'*','left','*.pfm'))
    grfilenames=gfile.Glob(os.path.join(FLAGS.data_data,'*','right','*.pfm'))
    if not lfilenames or not not lfilenames or not gfilenames:
        raise RuntimeError('No data files found.')
    index=len(lfilenames)
    olimages=tf.train.string_input_producer(olfilenames,shuffle=False)
    orimages=tf.train.string_input_producer(orflilenames,shuffle=False)
    gldisparity=tf.train.string_input_producer(glfilenames,shuffle=False)
    grdisparity=tf.tranin.string_input_producer(grfilenames,shuffle=False)
    reader=tf.WholeFileReader()
    key,limagev=reader.read(olimages)
    limage=tf.image.decode_png(limagev)
    key,rimagev=reader.read(orimages)
    rimage=tf.image.decode_png(rimagev)







    
