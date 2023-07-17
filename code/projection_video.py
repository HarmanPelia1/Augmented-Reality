import cv2
import numpy as np
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video', help='Path to the video to be projected',
                    default='Ronaldo.mp4')            
args = parser.parse_args()

video_path=args.video

stream = cv2.VideoCapture(0)
video = cv2.VideoCapture(video_path)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters_create()

def find_and_warp(fram, source, cornerIds, dictionary,parameters):
    (imgH, imgW) = frame.shape[:2]
    (srcH, srcW) = source.shape[:2]
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)
    if len(markerCorners) != 4:
        markerIds = np.array([])
        