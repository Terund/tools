"""
多线程

进程与线程(关系)

进程是资源分配的最小单位,
线程是 CPU 调度的最小单位（程序真正执行的时候调用的是线程）.
每一个进程中至少有一个线程（主线程）。
一个进程中可以包含多个线程，多个线程共享系统为进程分配的系统资源(内存)


什么是线程？

可以手动多个子线程：
如何创建：
    threading.Thread(target=download1,args=('任务1',),name='子线程1')

    target: 关联的任务
    args: 给关联任务传递的参数
    name: 指定的线程名字
如何开启：
    t.start()
需求：
    使用多线程实现多任务

"""
import time
import threading
def download1(task_name):
    for i in range(1,6):
        print(f'{task_name}下载进行{i*20}%')
        time.sleep(1)
def download2(task_name):
    for i in range(1,6):
        print(f'{task_name}下载进行{i*20}%')
        time.sleep(1)

# download1('任务1')
# download2('任务2')
t1 = threading.Thread(target=download1,args=('任务1',),name='子线程1')
t2 = threading.Thread(target=download2,args=('任务2',),name='子线程2')
t1.start()
t2.start()