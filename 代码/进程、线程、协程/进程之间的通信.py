"""
进程之间的通信
队列：
    multiprocessing.Queue
工作机制：
    先进先出
创建：
    multiprocessing.Queue(maxsize = n)
入队：
    put()
        如果对满，会导致阻塞
出队：
    get()
        如果队空，会导致阻塞
是否队满：
    full()
是否队空：
    empty()
获取队长:
    qsize()

"""
import multiprocessing

# def task1(list1):
#     for i in range(3):
#         list1.append(i)
#     print(id(list1))
#     print(list1)
# def task2(list1):
#     for i in range(5,8):
#         list1.append(i)
#     print(id(list1))
#     print(list1)
#
# if __name__ == '__main__':
#     list1 = []
#     print(id(list1))
#     p1 = multiprocessing.Process(target=task1,args=(list1,))
#     p2 = multiprocessing.Process(target=task2,args=(list1,))
#     p1.start()
#     p2.start()

#创建队列：
# q = multiprocessing.Queue(maxsize=3)
# q.put('a')
# print(f'队列长度为:{q.qsize()}')
# q.put('b')
# print(f'队列长度为:{q.qsize()}')
# q.put('c')
# print(f'队列长度为:{q.qsize()}')
# print(f'是否队满{q.full()}')
# v = q.get()
# print(v)
# v = q.get()
# print(v)
# v = q.get()
# print(v)
# print(f'是否队空{q.empty()}')
# # v = q.get()
# # 如果队列中没有数据，会导致异常
# # v = q.get_nowait()
# print(v)
# q.put('d')


def getData(q):
    for i in range(5):
        q.put(i)
        print('put')
    print('爬取完毕')
def process_data(q):
    for i in range(5):
        r = q.get()
        print('get')
    print('处理完毕')
if __name__ == '__main__':
    q = multiprocessing.Queue(2)
    p1 = multiprocessing.Process(target=getData, args=(q,))
    p2 = multiprocessing.Process(target=process_data, args=(q,))
    p1.start()
    p2.start()

