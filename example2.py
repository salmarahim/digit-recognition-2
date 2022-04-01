import numpy as np
import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    #capture frame by frame
    ret,frame=cap.read()
    # if frame is read correctly ret is true

    # our operations on the frame comes here
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    #display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break

#when everything is done, release the capture
cap.release()

cv.destroyAllWindows()