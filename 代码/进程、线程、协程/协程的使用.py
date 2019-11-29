"""
多任务处理：
1.进程
2.线程
3.协程
协程的创建:
比线程更小的执行单元
某个函数， 可以在任何地方保存当前函数的一些临时变量等信息，
然后切换到另外一个函数中执行
协程的切换只是单纯的操作CPU的上下文，比线程的切换更快速
1:N 模式。 所谓 1:N 就是一个线程作为一个容器可以放置多个协程
协程的使用方式：yield

传统方式：
    yield
第三方模块：
使用gevent完成协程
1.安装gevent
2.引入gevent
"""
import gevent
def task(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        # 实现休眠一秒
        gevent.sleep(1)
#创建协程操作
g1 = gevent.spawn(task,5)
g2 = gevent.spawn(task,5)
g3 = gevent.spawn(task,5)
gevent.joinall([g1,g2,g3])