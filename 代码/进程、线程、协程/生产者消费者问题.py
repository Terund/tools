"""
生产者消费者模式：
进程队列：
    multiprocessing.Queue
线程队列：
    queue.Queue(先进先出队列)
    实现了锁的队列，线程安全的
    入队：
        put()
    出队:
        get()
    队长：
        qsize()

"""
from threading import Thread
from queue import Queue
import time
q = Queue(maxsize=10)
class Produce(Thread):
    count = 1
    def __init__(self,name):
        super(Produce, self).__init__()
        self.name = name
    def run(self):
        while True:
            result = '{0}生产的第{1}个包子'.format(self.name,Produce.count)
            q.put(result)
            print(result)
            Produce.count += 1
            time.sleep(1)
class Custom(Thread):
    def __init__(self,name):
        super(Custom, self).__init__()
        self.name = name
    def run(self):
        while True:
            if q.qsize() > 0:
                r = q.get()
                print('{0}吃了{1}'.format(self.name, r))
            time.sleep(1)
if __name__ == "__main__":
    t1 = Produce('张三')
    t2 = Custom('李四')
    t3 = Custom('王五')
    t1.start()
    t2.start()
    t3.start()