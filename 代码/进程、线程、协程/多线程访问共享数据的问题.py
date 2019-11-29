"""
多线程访问共享数据的问题：
1.哪些问题
    数据混乱问题

2.如何解决
    用锁（互斥锁）threading.Lock
    获取锁(上锁)
    lock.acquire()
    释放锁（解锁）
    locl.release()

    获取锁与释放锁的次数要对应

好处：
    保护数据安全，实现数据同步，不会混乱

弊端：
    效率降低
    容易导致死锁

"""
import time
import threading

#模拟的总票数
tickets = 1000
lock = threading.Lock()
def sale(name):
    global tickets
    while tickets > 0:
       if lock.acquire():
            if tickets > 0:
                tickets -= 1
                time.sleep(0.01)
                print('{}售出1张票，剩余{}张'.format(name, tickets))
            lock.release()
t1 = threading.Thread(target=sale,args=('窗口1',))
t2 = threading.Thread(target=sale,args=('窗口2',))
t1.start()
t2.start()