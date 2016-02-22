import numpy as np
import cv2
#import scipy.ndimage
import threading
#from rift import PyRift


class Buffer(object):
    def __init__(self):
        ret, self.right = cam1.read()
        ret, self.left = cam2.read()


def update_left(buffer):
    while True:
        ret, frame = cam1.read()
        frame = frame[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400
        buffer.left = frame


def update_right(buffer):
    while True:
        ret, frame = cam2.read()
        frame = frame[0:1080, 480:1440] # Crop from x, y, w, h -> 100, 200, 300, 400
        buffer.right = frame


cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)

cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)

buffer = Buffer()

left_thread = threading.Thread(target = update_left, args = (buffer,))
right_thread = threading.Thread(target = update_right, args = (buffer,))

left_thread.start()
right_thread.start()

while True:

    frame = np.concatenate((buffer.left, buffer.right), axis=1)

    frame = cv2.resize(frame,(1920, 1080), interpolation = cv2.INTER_CUBIC)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam1.release()
cam2.release()
cv2.destroyAllWindows()
