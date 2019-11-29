"""
4个cpu执行3个任务：
并行

4个cpu执行5个任务
并发

多进程控制问题：

执行下载任务：
    非会员： 1个

    会员:  2+
同步与异步（课下查询）：
    同步：
        任务之间顺序执行，必须一个执行完了，另外一个才会执行
    异步：
        多个任务之间互不干涉，各执行各的

进程池：
1.创建进程池
Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])
apply(func[, args[, kwds]])
    同步操作，它会阻塞，直到结果就绪
apply_async(func[, args[, kwds[, callback[, error_callback]]]])
    异步操作，不会阻塞，可以指定回调函数
colse()
join()
对Pool对象调用join()方法会等待所有子进程执行完毕，
调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了


关注点:
    1.同时执行的任务数量
    2.某个任务执行完毕是否自动调用关联的回调函数
    3.子进程关联的函数，调用后的返回值，会自动传给回调函数
"""
from multiprocessing import Pool
import time
def down_load(movie_name):
    for i in range(5):
        print('电影:{},下载进度{}%'.format(movie_name, (i / 4 * 100)))
        time.sleep(1)
    return movie_name
def alert(movie_name):
    print('恭喜{}下载完成了...'.format(movie_name))
if __name__ == '__main__':
    movie_lst = ['魔兽世界', '权利的游戏', '西部世界','碟中谍','战狼','红海行动','唐伯虎点秋香']
    pool = Pool()
    for movie_name in movie_lst:
        # 创建异步任务，放入进程池中
        pool.apply_async(down_load, (movie_name,),
                         callback=alert)
    pool.close()
    pool.join()
