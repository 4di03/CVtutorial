import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #draws shapes on images (r, g, b)  (x, y) ints are sizes/radii/length

    img = cv2.line(frame, (0,0), (width, height), (255, 210, 12), 20)
    img = cv2.line(img, (width, 0), (0, height), (255, 210, 12), 20)
    img = cv2.rectangle(img, (100, 100), (300, 300), (20,20,20), 10)
    img = cv2.circle(img, (400, 400), 30, (255,255,255) ,5)

    # writest text with a font
    font = cv2.FONT_HERSHEY_COMPLEX
    #coord is bottom left corner of text
    img = cv2.putText(img, "Adithya is Great!", (600, 200), font, 2 , (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()