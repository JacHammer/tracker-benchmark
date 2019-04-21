from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import glob

# TODO: implement a stream to feed images to trackers

# It should take argument like:
# tracker, a batch of images compiled by openCV, and groundtruth

# It should return things like: 
# IOU accuracy, fps, tracker type


# benchmark a tracker
# arguments:
#  -tracker: an OpenCV tracker or your own tracker class, for OpenCV, the 
#       tracker should be created by "cv2.TrackerGNAME_create()"
#       for other tracker, TODO
#  -img_folder__path: the path to a contineous set of images for benchmarking;
#  -groundtruth_path: the path to groundtruth;
#  -dataset_type: so far the benchmarking only supports VTB, more dataset may
#       be added.
def BenchmarkingTracker(tracker, image_path, groundtruth_path, dataset_type):
    
    pass