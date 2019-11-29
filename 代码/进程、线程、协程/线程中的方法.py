"""
join()
t.join()
优先执行线程t，执行完毕后，其他任务才会继续执行

setDaemon()
将某个线程设置为守护线程(主线程结束，不管子线程中的任务是否执完都直接结束)
注意：一定要在开启之前设置

threading模块的方法：
threading.currentThread()
获取当前线程
threading.enumerate()
返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程
theading.activeCount()
返回正在运行的线程的数量

"""
import threading
import time
# def download1(name,):
#     for i in range(3):
#         print('{}进行到{}'.format(name,i))
#         time.sleep(1)
# def download2(name):
#     for i in range(3):
#         print('{}进行到{}'.format(name,i))
#         time.sleep(1)
#
# t1 = threading.Thread(target=download1,args=('线程1',))
# t2 = threading.Thread(target=download2,args=('线程2',))
# t1.start()
# #阻塞其他线程，直到当前线程执行完，其他线程才会执行
# # t1.join()
# t2.start()


def download1():
    # print(f'任务{threading.currentThread()}')
    for i in range(3):
        print('下载任务1进行到{}'.format(i))
        time.sleep(1)
t1 = threading.Thread(target=download1,daemon=False)
#将当前线程设置为守护线程(主线程结束，子线程立即结束)
# t1.setDaemon(True)
t1.start()
# 获取当前线程
# print(threading.currentThread())
# print(threading.enumerate())
print(f'活动的线程数:{threading.active_count()}')
print('主线程结束')