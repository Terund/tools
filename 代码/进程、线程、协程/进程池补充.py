"""
1.创建multiprocessing.Pool
2.添加任务
    applay()
        顺序执行
    applay_async()
        交替执行
3.进程池的关闭
    close()
4.阻塞
    join()
    让主进程等着进程池中所有的子任务执行完毕之后，再结束

获取当前进程
current_process()

查看进程id
pid

"""
from  multiprocessing import current_process
from  multiprocessing import Pool
import random
import time
def download(name):
    print(f'下载任务:{current_process().pid}')
    for i in range(1,11):
        print(f'{name}下载进行到{i*10}%')
        time.sleep(random.random())
    return name
def alert(name):
    print(f'{name}下载完成')

list1 = [f'西部世界第{i}集' for i in range(1,13)]
# print(list1)
if __name__ == '__main__':
    print(f'当前进程:{current_process().pid}')

    # 创建进程池
    pool = Pool(2)
    for s in list1:
        #循环将任务存储到进程池中
        # pool.apply(func=download,args=(s,))
        pool.apply_async(func=download,args=(s,),callback=alert)
    pool.close()
    # 阻塞主进程，让主进程等待所有子进程任务执行完毕之后才结束
    pool.join()





