import numpy as np
import cv2
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    # waitKey returns ordinal value of key pressed
    # checking for keypress = q to break and break the loop to display video
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()