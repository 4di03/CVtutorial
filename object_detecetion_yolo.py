import numpy as np
import cv2
from video import video

# objects to detect
classesFile = 'assets/coco.names'
classNames = []
with open(classesFile, 'r') as f:
    classNames = f.read().rstrip('\n').split('\n')

print(classNames)
print(len(classNames))

# def objectDetect(img):


# # video(objectDetect)