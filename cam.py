import numpy as np
import cv2
from utils import WebcamVideoStream
from rift import PyRift


if __name__ == '__main__':
    left = WebcamVideoStream(src=0).start()
    right = WebcamVideoStream(src=1).start()

    cv2.namedWindow('view', cv2.WND_PROP_FULLSCREEN)

    while True:

        left_frame = left.read()
        right_frame = right.read()

        frame = np.concatenate((left_frame, right_frame), axis=1)
        frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_NEAREST)

        # Display the resulting frame
        cv2.imshow('view', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            left.stop()
            right.stop()
            break

    # When everything done, release the capture
    cv2.destroyAllWindows()
