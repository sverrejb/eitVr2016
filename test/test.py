import numpy as np
import cv2
import scipy.ndimage

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    frame1 = cv2.resize(frame1, (0,0), fx=0.5, fy=0.5) 
    frame2 = cv2.resize(frame2, (0,0), fx=0.5, fy=0.5) 

    # Our operations on the frame come here
    vis = np.concatenate((frame1, frame2), axis=1)


    # Display the resulting frame
    cv2.imshow('frame', vis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cap1.release()
cv2.destroyAllWindows()