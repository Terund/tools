"""
多任务:
    提高效率
进程
    Process
    Pool
线程
    Thread
    子类(Thread)

Python中的多线程
伪多线程(课下查资料)
GIL（全局解释器锁），导致Python中即使开启多线程处理，也无法发挥多核优势

任务分类：
1.CPU密集型
    计算
    多进程
2.IO密集型
    阻塞
    多线程


"""
import time
import threading
import multiprocessing
def task1():
    start_time = time.time()
    j = 0
    for i in range(10000000):
        j += 1
    end_time = time.time()
    print('耗时:{}秒'.format(end_time-start_time))

def task2(threadName):
    j = 0
    start_time = time.time()
    for i in range(5000000):
        j += 1
    end_time = time.time()
    print('耗时:{}'.format(end_time - start_time))
# 单线程操作
# task1()

# 多线程操作
# for i in range(1,3):
#     t = threading.Thread(target=task2,args=('线程{}'.format(i),))
#     t.start()

# 多进程操作
# if __name__ == '__main__':
#     p = multiprocessing.Pool(2)
#     for i in range(1,3):
#         p.apply_async(task2, args=('进程{}'.format(i),))
#     p.close()
#     p.join()


def download1():
    for i in range(1,11):
        print(f'任务1下载进行{i*10}%')
        time.sleep(0.2)
def download2():
    for i in range(1,11):
        print(f'任务2下载进行{i*10}%')
        time.sleep(0.2)

# download1()
# download2()

# t1 = threading.Thread(target=download1)
# t2 = threading.Thread(target=download2)
# t1.start()
# t2.start()

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=download1)
    p2 = multiprocessing.Process(target=download2)
    p1.start()
    p2.start()