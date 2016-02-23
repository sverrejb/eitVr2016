import numpy as np
import cv2
import scipy.ndimage

cam1 = cv2.VideoCapture(1)

cam1.set(3,320)
cam1.set(4,120)


while(True):
    # Capture frame-by-frame
    ret1, frame1 = cam1.read()

    print frame1.shape[:2]


    #frame1 = cv2.resize(frame1, (0,0), fx=0.5, fy=0.5) 

    # Our operations on the frame come here

    cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)          
    #cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

    #frame1 = cv2.resize(frame1,(1920, 1080), interpolation = cv2.INTER_CUBIC)

    # Display the resulting frame
    cv2.imshow('frame', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cap1.release()
cv2.destroyAllWindows()