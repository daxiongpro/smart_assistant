# -*- coding:utf-8 -*-
import threading
import time
import queue

event = threading.Event()
goods = queue.Queue()
num = 0


class Producer(threading.Thread):
    def run(self):
        global num
        while True:
            if goods.empty():
                event.clear()
                for _ in range(20):
                    goods.put('商品-' + str(num))
                    print('生产了商品-{0}.'.format(str(num)))
                    num += 1
                    time.sleep(0.1)
                event.set()


class Customer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.money = 100

    def run(self):
        while self.money:
            event.wait()
            self.money -= 1
            print('{0} 买了一个{1}.'.format(
                threading.current_thread().name, goods.get()))
            time.sleep(0.1)
        print('{0}没钱了，回家.'.format(threading.current_thread().name))


if __name__ == '__main__':
    p = Producer(daemon=True) #没钱了，主程序退出后，自动干掉生产者
    c1 = Customer(name='Alice')
    c2 = Customer(name='Bob')
    c2.start()
    p.start()
    c1.start()
    c1.join()
    c2.join()
