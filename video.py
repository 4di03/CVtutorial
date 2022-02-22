import numpy as np
import cv2


def video(imgFunc = None):

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        frame = cv2.resize(frame,(0, 0), fx= 0.6, fy = 0.6)

        # #returns width property of video capture
        # width = int(cap.get(3))


        # #returns height property of video capture
        # height = int(cap.get(4))



        # # for pasting image (passing shape of frame to get same 3d array)
        # image = np.zeros(frame.shape, np.uint8)
        

        # smaller_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)

        # # pastes smaller_frame in 4 quadrants of black image (image)
        # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
        # image[height//2:, :width//2] = smaller_frame
        # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
        # image[height//2 : , width//2:] = smaller_frame

        if imgFunc == None:
            cv2.imshow('frame', frame)
        else:
            cv2.imshow('frame', imgFunc(frame))

        # waitKey returns ordinal value of key pressed
        # checking for keypress = q to break and break the loop to display video
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

