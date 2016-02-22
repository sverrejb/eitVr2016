import numpy as np
import cv2
import scipy.ndimage
import threading
#from rift import PyRift

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

## scaling ###
cam1.set(3,1920)
cam1.set(4,1080)

cam2.set(3,1920)
cam2.set(4,1080)

class Buffer(object):
    def __init__(self):
        ret, self.right = cam1.read() 
        ret, self.left = cam2.read()

cv2.namedWindow('frame',cv2.WND_PROP_FULLSCREEN)

buffer = Buffer()

def update_left(buffer):
    while True:
        ret, buffer.left = cam1.read()


def update_right(buffer):
    while True:
        ret, buffer.right = cam2.read()

left_thread = threading.Thread(target = update_left, args = (buffer,))
right_thread = threading.Thread(target = update_right, args = (buffer,))

left_thread.start()
right_thread.start()

while(True):

    #frame1 = frame1[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400
    #frame2 = frame2[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400

    frame = np.concatenate((buffer.right, buffer.left), axis=1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam1.release()
cam2.release()
cv2.destroyAllWindows()
