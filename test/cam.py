import numpy as np
import cv2
import scipy.ndimage
#from rift import PyRift

cam1 = cv2.VideoCapture(1)
cam2 = cv2.VideoCapture(1)

cam1.set(3,1920)
cam1.set(4,1080)

cam2.set(3,1920)
cam2.set(4,1080)

cv2.namedWindow('frame',cv2.WND_PROP_FULLSCREEN)

while(True):
    # Capture frame-by-frame
    # to threads?
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam1.read()

    # Our operations on the frame come here

    frame1 = frame1[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400
    frame2 = frame2[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400

    frame = np.concatenate((frame1, frame2), axis=1)

    
    #frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)
    #frame = cv2.resize(frame,(1920, 1080), interpolation = cv2.INTER_CUBIC)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam1.release()
cam2.release()
cv2.destroyAllWindows()