# coding=utf-8
import threading
import time

m_lock = threading.RLock()


def h():
    with m_lock:
        g()
        print('h')


def g():
    with m_lock:
        print('g')


h()
g()
