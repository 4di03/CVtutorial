import numpy as np
import cv2
from video import video

def drawCorners(img):

    #converts image to grayscale , put in seperate variable so as to not tamper with original
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Shi-Tomasi corner detector for image
    #2nd param is number of corners to return
    #3rd param is quality of corners (0 - 1) (good to start low)
    #4th param is minimum euclidan distance between two corners (for rounded corners) 
    # (chooses corners with distances > than that length)

    corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 100)
    # corners are in floats

    #converts floats to ints
    corners = np.int0(corners)


    for corner in corners:
        #ravel flattens the array returns the values in numpy array [[1,2], [2, 1]] -> [1, 2, 2, 1]
        x, y = corner.ravel()
        cv2.circle(img, (x, y), 5, (255, 0 ,0), -1)

    for i in range(len(corners)):
        for j in range(i+1, len(corners)):
            corner1 = tuple(corners[i][0])  #becuase corners[i] is in shape [[2, 2]]
            corner2 = tuple(corners[j][0])

            # returns a list of 3 64bit ints within the range randomly
            # numpy needs 8bit ints
            # lambda is like racket lamdbas
            color = tuple(map(lambda x: int(x) ,np.random.randint(0, 255, size = 3)))

            cv2.line(img, corner1, corner2, color, 1)

    return img

video(drawCorners)