import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))


    #hsv color scheme  hue saturation and lightness/brightness

    #converts bgr img to hsv img
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # BGR_color = np.array((([255,0,0])))

    # does AND operation for pixels in frames with its own pixels(checks if both are blue)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('frame', result)


    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()