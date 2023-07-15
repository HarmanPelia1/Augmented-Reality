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
