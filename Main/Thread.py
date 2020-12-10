import threading
import cv2
from PyQt5.QtGui import QImage, QPixmap


class Thread_video(threading.Thread):
    id = 0

    def __init__(self, cap, ui, frameRate):
        super().__init__()
        self.cap = cap
        self.ui = ui
        self.frameRate = frameRate

        self.signal = threading.Event()
        self.signal.set()
        self.isStop = False

    def run(self):
        while self.cap.isOpened():
            self.signal.wait()
            if self.isStop:
                break
            success, frame = self.cap.read()
            if str(type(frame)) == "<class 'numpy.ndarray'>":
                #非最后一帧
                # RGB转BGR
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.ui.label_video.setPixmap(QPixmap.fromImage(img))
                cv2.waitKey(int(1000 / self.frameRate))
            else:
                # 最后一帧返回None
                # self.isStop = True
                break

    def stop(self):
        self.isStop = True

    def restart(self):
        self.signal.set()

    def pause(self):
        self.signal.clear()
