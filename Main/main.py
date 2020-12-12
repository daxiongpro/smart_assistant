__package__ = "Main"

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import cv2
import threading
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap

from Main.video_play import Video
from .MainUI import Ui_MainWindow
from .Product import Product
from .Thread import Thread_video


class Main:
    def __init__(self, ui, mainWnd):
        self.ui = ui
        self.mainWnd = mainWnd

        # 按钮注册
        self.add_listener()
        # 开始一系列步骤
        self.start()

    def add_listener(self):
        # 事件监听
        self.ui.pushButton_pause.clicked.connect(Video.pause)
        self.ui.pushButton_restart.clicked.connect(Video.restart)
        self.ui.pushButton_last.clicked.connect(self.Last)
        self.ui.pushButton_next.clicked.connect(self.Next)

    def start(self):
        self.product = Product(1, '产品一')

    def Stop(self):
        Video.stop()


    def Next(self):
        self.product.now_step += 1
        if self.product.now_step <= len(self.product.steps) - 1:
            if self.product.steps[self.product.now_step] == 0:
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
        if Video.started:
            Video.stop()
        video = Video(self.ui)
        video.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWnd = QMainWindow()
    ui = Ui_MainWindow()
    # 可以理解成将创建的 ui 绑定到新建的 mainWnd 上
    ui.setupUi(mainWnd)
    display = Main(ui, mainWnd)
    mainWnd.show()
    sys.exit(app.exec_())
