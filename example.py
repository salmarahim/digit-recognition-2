# OpenCV is a vast library that helps in providing variuos functions for image and video operations.
# With OpenCV, we can capture a video from the camera. It lets you create a video capture object which
# is helpful to capture videos through webcam and then you may perform desired operations on that video.

#import the opencv library
import cv2
#define a video capture object
vid=cv2.VideoCapture(0)

while(True):
    #capture the video frame by frame
    ret,frame=vid.read()

    #Display the resulting frame
    cv2.imshow('Color frame',frame)

    #the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
#after the loop release the cap object
vid.release()
#destroy all the windows
cv2.destroyAllWindows()

# Decimal=255, Binary=1111 1111 , Hexadecimal=0xff