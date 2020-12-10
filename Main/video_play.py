import cv2

from Main.MainUI import Ui_MainWindow
from Main.Thread import Thread_video


class Video(object):
    started = False
    __current_thread = None

    def __init__(self, ui: Ui_MainWindow, file_path: str = 'C:/Users/91066/Videos/birthday.mp4') -> object:
        self.thread_video = None
        # video放在哪个ui组件上播放
        self.ui = ui
        self.file_path = file_path

    def play(self):
        '''
        创建视频线程，并播放
        :return:
        '''

        if not Video.started:
            # 创建播放视频线程
            file_name = self.file_path
            file_type = '*.mp4'
            # print(file_name, file_type)
            if file_type != '' and file_name != '':
                cap = cv2.VideoCapture(file_name)
                frameRate = cap.get(cv2.CAP_PROP_FPS)
                # 创建视频显示线程
                self.thread_video = Thread_video(cap=cap, ui=self.ui, frameRate=frameRate)
                self.thread_video.start()

                Video.started = True
                Video.__current_thread = self.thread_video

    @classmethod
    def stop(cls):
        if Video.__current_thread is not None:
            Video.__current_thread.stop()
        else:
            print('Video.__current_thread is not None:')

    @classmethod
    def pause(cls):
        if Video.__current_thread is not None:
            Video.__current_thread.pause()
        else:
            print('Video.__current_thread is not None:')

    @classmethod
    def restart(cls):
        if Video.__current_thread is not None:
            Video.__current_thread.restart()
        else:
            print('Video.__current_thread is not None:')
