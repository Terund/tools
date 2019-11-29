"""
theading.local()
"""
import threading
# 创建全局ThreadLocal对象:
local_var = threading.local()
def process_student():
    print(local_var.a)
def process_thread(v):
    # 绑定ThreadLocal的student:
    local_var.a = v
    process_student()
t1 = threading.Thread(target= process_thread, args=('123',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('456',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()