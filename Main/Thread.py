import threading
import time

import cv2
from PyQt5.QtGui import QImage, QPixmap


class Thread_video(threading.Thread):
    id = 0

    def __init__(self, id=0, name=None, cap=None, ui=None, frameRate=None):
        super().__init__()
        self.singal = threading.Event()
        self.singal.set()
        self.cap=cap
        self.ui=ui
        self.frameRate=frameRate
        self.stop = False

    def run(self):
        i = 0
        while self.cap.isOpened():

            if self.stop == True:
                break
            self.singal.wait()

            success, frame = self.cap.read()

            if str(type(frame)) == "<class 'numpy.ndarray'>": #最后一帧返回None
                # RGB转BGR
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.ui.label_video.setPixmap(QPixmap.fromImage(img))
                cv2.waitKey(int(1000 / self.frameRate))
            else:
                break


    def stop(self):
        self.stop = True
        # self.ui.label_video.clear()
        # self.singal.clear()

    def restart(self):
        self.singal.set()

    def pause(self):
        self.singal.clear()

