# -*-coding:utf8-*-
"""
本例程实现了一个多线程任务分发的机制，Publisher不断地判断当前系统该处理第几步，一旦有了消息，
Dispatcher类马上得到接收，并检查语音模块、幻灯片模块是否在运行，如果在运行，马上杀掉，按新的
步骤运行。
"""

import threading
import time
import queue as Queue
import random
import ctypes
import inspect
import logging

myLogger = logging.getLogger("my logger")
myLogger.setLevel(logging.DEBUG)

lock = threading.RLock()
q = Queue.Queue()
count = 0
WORKING_STEPS = 20


class Publisher(threading.Thread):

    def __init__(self, Producername):
        threading.Thread.__init__(self)
        self.Producername = Producername

    def Producer(self, name):
        name = self.Producername

        for i in range(1, WORKING_STEPS + 1):
            q.put(f"步骤{i}")
            print('生产者[%s]发出消息[%s]' % (name, i))
            time.sleep(random.randrange(2))  # 主进程等待

    def run(self):
        self.Producer(self.Producername)


class Dispatcher(threading.Thread):
    """负责接收来自于子线程的消息

    """

    def __init__(self, Consumername):
        threading.Thread.__init__(self)
        self.Consumername = Consumername
        self.audio_thread = None

    def checkThread(self, task):
        """
        如果上一个线程还在运行，就马上杀掉
        """
        if self.audio_thread and self.audio_thread.is_alive():
            stop_thread(self.audio_thread)
        # 为什么要新建呢？因为线程只能start一次，所以选用了新建一个线程的方法
        self.audio_thread = StoppableThread("语音模块")
        self.audio_thread.addTask(task)
        self.audio_thread.start()

    def Consumer(self, name):

        name = self.Consumername
        global count

        while count < 20:
            data = q.get()

            print('[%s],收到了来自主进程的消息,要做[%s]' % (name, data))
            count += 1
            self.checkThread(task=data)

    def run(self):
        self.Consumer(self.Consumername)


class StoppableThread(threading.Thread):
    """能够停止的音频线程,可重写或者带参数实例化这个类，构建出语音、视频、投影仪模块"""

    def __init__(self, name, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.name = name
        self.task = None

    def hasTask(self):
        return self.task is not None

    def addTask(self, task):
        self.task = task

    def run(self):
        print("[%s]线程努力做[%s]" % (self.name, self.task))
        time.sleep(4)  # 放大点看看
        print("[%s]活干完了" % (self.task,))


#############停止线程的可复用函数#############
def _async_raise(tid, exctype):
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    print("%s任务还未做完，但马上停止" % thread.task)

    _async_raise(thread.ident, SystemExit)


t1 = Publisher("系统主进程")
t2 = Dispatcher("分配任务者")
t1.start()
t2.start()
