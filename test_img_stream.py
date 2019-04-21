import matplotlib.pyplot as plt
import os
import cv2
import glob

images = [cv2.imread(file) for file in glob.glob('dataset/Basketball/Basketball/img/*jpg')]
