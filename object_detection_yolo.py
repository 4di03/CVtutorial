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

modelConfiguration = 'assets/yolov3.cfg'
modelWeights = 'assets/yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


# def objectDetect(img):


# # video(objectDetect)