import numpy as np
import cv2
import threading
from rift import PyRift


class Buffer(object):
    def __init__(self):
        ret, self.right = cam1.read()
        ret, self.left = cam2.read()


def update_left(buffer):
    while True:
        ret, left_frame = cam1.read()
        left_frame = left_frame[0:1080, 480:1440]
        buffer.left = left_frame


def update_right(buffer):
    while True:
        ret, right_frame = cam2.read()
        # Crop from x, y, w, h -> 100, 200, 300, 400
        right_frame = right_frame[0:1080, 480:1440]
        buffer.right = right_frame


if __name__ == '__main__':

    cam1 = cv2.VideoCapture(0)
    cam2 = cv2.VideoCapture(1)

    cv2.namedWindow('view', cv2.WND_PROP_FULLSCREEN)

    frame_buffer = Buffer()

    left_thread = threading.Thread(target=update_left, args=(frame_buffer,))
    right_thread = threading.Thread(target=update_right, args=(frame_buffer,))

    right_thread.setDaemon(True)
    left_thread.setDaemon(True)

    left_thread.start()
    right_thread.start()

    while True:
        frame = np.concatenate((frame_buffer.left, frame_buffer.right), axis=1)
        frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_CUBIC)

        # Display the resulting frame
        cv2.imshow('view', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cam1.release()
    cam2.release()
    cv2.destroyAllWindows()
