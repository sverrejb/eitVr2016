from threading import Thread
import cv2


class WebcamVideoStream:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        thread = Thread(target=self.update, args=())
        thread.daemon = True
        thread.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            try:
                self.grabbed, tmp = self.stream.read()
                self.frame = tmp[0:1080, 480:1440]
            except:
                pass

    def read(self):
        # return the frame most recently read
        return self.frame

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True
