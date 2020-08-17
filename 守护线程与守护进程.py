from threading import Thread
from multiprocessing import Process
import time


def func1():
    while True:
        print(666)
        time.sleep(0.5)


def func2():
    print('hello')
    time.sleep(3)


if __name__ == '__main__':
    # t = Thread(target=func1, )
    # t.daemon = True  # 主线程结束，守护线程随之结束
    # # t.setDaemon(True) #两种方式，和上面设置守护线程是一样的
    # t.start()
    # t2 = Thread(target=func2, )
    # '''
    # 这个子线程要执行3秒，主线程的代码虽然执行完了，但是一直等着子线程的任务执行完毕，主线程才算完毕，因为通过结果你会发现我主线程虽然代码执行完毕了，\
    # 但是主线程的的守护线程t1还在执行，说明什么，说明我的主线程还没有完毕，只不过是代码执行完了，一直等着子线程t2执行完毕，我主线程的守护线程才停止，说明子线程执行完毕之后，我的主线程才执行完毕
    # '''
    # t2.start()
    # print('主线程代码执行完啦！')


    p = Process(target=func1, )
    p.daemon = True
    p.start()

    p2 = Process(target=func2, )
    p2.start()
    time.sleep(1)  # 让主进程等1秒，为了能看到func1的打印效果
    print('主进程代码执行完啦！')
    # 通过结果你会发现，如果主进程的代码运行完毕了，那么主进程就结束了，因为主进程的守护进程p随着主进程的代码结束而结束了，守护进程被回收了，这和线程是不一样的，主线程的代码完了并不代表主线程运行完毕了，需要等着所有其他的非守护的子线程执行完毕才算完毕
