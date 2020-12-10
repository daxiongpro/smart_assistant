__package__ = "Main"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import cv2
import threading
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from .MainUI import Ui_MainWindow
from .Product import Product
from .Thread import Thread_video


class Display:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd

        # 信号槽设置
        # ui.pushButton_open.clicked.connect(self.Play)
        # ui.pushButton_close.clicked.connect(self.Close)
        ui.pushButton_pause.clicked.connect(self.Pause)
        ui.pushButton_restart.clicked.connect(self.Restart)

        ui.pushButton_last.clicked.connect(self.Last)
        ui.pushButton_next.clicked.connect(self.Next)

        # 创建一个关闭事件并设为未触发
        self.thread_video = Thread_video()
        self.stopEvent = threading.Event()
        self.stopEvent.clear()
        self.product = Product(1, '产品一', 5)
        self.now_step = 0

    def Pause(self):
        self.thread_video.pause()

    def Restart(self):
        self.thread_video.restart()

    def Next(self):
        self.now_step += 1
        if self.now_step <= self.product.total_steps:
            if self.product.step[self.now_step] == 0:
                # 播放语音提示
                print("播放语音提示")
            else:
                self.Play()
                print('播放视频教学')
        else:
            print('已教学完！')

    def Last(self):
        pass

    def Play(self):
        '''
        创建视频线程，并播放
        :return:
        '''
        if self.thread_video.is_alive():
            self.thread_video.pause()
        # file_name, file_type = QFileDialog.getOpenFileName(self.mainWnd, 'Choose file', '', '*.mp4')
        file_name, file_type = 'C:/Users/91066/Videos/eat.mp4', '*.mp4'
        # print(file_name, file_type)
        if file_type != '' and file_name != '':
            self.cap = cv2.VideoCapture(file_name)
            self.frameRate = self.cap.get(cv2.CAP_PROP_FPS)
            # 创建视频显示线程
            self.thread_video = Thread_video(cap=self.cap, ui=self.ui, frameRate=self.frameRate)
            self.thread_video.start()

    def Close(self):
        # 关闭事件设为触发，关闭视频播放
        # self.stopEvent.set()
        self.thread_video.stop()

    # def Display(self):
    #     # self.ui.pushButton_open.setEnabled(False)
    #     # self.ui.pushButton_close.setEnabled(True)
    #
    #     while self.cap.isOpened():
    #         success, frame = self.cap.read()
    #         # RGB转BGR
    #         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #         img = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
    #         self.ui.label_video.setPixmap(QPixmap.fromImage(img))
    #         cv2.waitKey(int(1000 / self.frameRate))
    #
    #         # 判断关闭事件是否已触发
    #         if self.stopEvent.is_set() == True:
    #             # 关闭事件置为未触发，清空显示label
    #             self.stopEvent.clear()
    #             self.ui.label_video.clear()
    #             # self.ui.pushButton_close.setEnabled(False)
    #             # self.ui.pushButton_open.setEnabled(True)
    #             break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = QMainWindow()
    ui = Ui_MainWindow()
    # 可以理解成将创建的 ui 绑定到新建的 mainWnd 上
    ui.setupUi(mainWnd)
    display = Display(ui, mainWnd)
    mainWnd.show()
    sys.exit(app.exec_())
