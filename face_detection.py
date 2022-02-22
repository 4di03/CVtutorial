import numpy as np
import cv2
from video import video

#uses haarcascaade model 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


#frame = img
def detectFace(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #returns (x,y,w,h) of detected faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

        #returns image where face is located
        # y first cause rows and then coloumns
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        #draws rectangle over eyes
        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)
        
    
    return img

    



video(detectFace)