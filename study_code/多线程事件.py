import threading
import time


class spider(threading.Thread):
    def __init__(self, n, event):
        super().__init__()
        self.n = n
        self.event = event

    def run(self):
        print(f'第{self.n}号爬虫已就位！')
        self.event.wait()
        print(f'信号标记变为True！！第{self.n}号爬虫开始运行')


eve = threading.Event()
for num in range(10):
    crawler = spider(num, eve)
    crawler.start()
input('按下回车键，启动所有爬虫！')
eve.set()
time.sleep(1)
