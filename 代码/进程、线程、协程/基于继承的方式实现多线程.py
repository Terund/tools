"""
threading.Thread

t.start()

"""
import threading,time
class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print(f'i = {i}')
            time.sleep(0.1)

t = MyThread()
t.start()

t2 = MyThread()
t2.start()