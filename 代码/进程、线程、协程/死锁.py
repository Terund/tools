"""
死锁：
    死锁的形成:
        1.多线程处理
        2.互斥锁的使用
    解决方案:
        if lock2.acquire(blocking=False):
        if lock2.acquire(timeout=2):
"""
import threading
import time
#创建全局的互斥锁对象
lock1 = threading.Lock()
lock2 = threading.Lock()
def task1():
    print('task1开始执行')
    if lock1.acquire():
        print('task1-获取lock1成功')
        time.sleep(1)
        # 我要获取lock2这个资源，如果获取不到，那就算了
        # if lock2.acquire(blocking=False):
        if lock2.acquire(timeout=2):
        # if lock2.acquire():
            print('task1-获取lock2成功')
            lock2.release()
            print('task1-释放lock2成功')
        lock1.release()
        print('task1-释放lock1成功')
def task2():
    print('task2开始执行')
    if lock2.acquire():
        print('task2-获取lock2成功')
        time.sleep(1)
        if lock1.acquire():
            print('task2-获取lock1成功')
            lock1.release()
            print('task2-释放lock1成功')
        lock2.release()
        print('task2-释放lock2成功')
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start()
t2.start()