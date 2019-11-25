"""
传输层协议：
    UDP
    TCP(Transmission Control Protocol)
    客户端：
        1.创建套接字
        2.建立连接
        3.发送  send()
        4.关闭套接字

    服务器：
        1.创建套接字
        2.绑定地址跟端口
        3.开启监听 listern()
        4.等待接收accept()
        5.通过连接过来的套接字接收消息
        6.关闭

"""
import socket
import threading

def task(socket,addr):
    print(f'有客户端{addr}接入')
    # 通过客户端的套接字进行接收
    message = socket.recv(4096)
    print("服务器端收到信息为：", message.decode())
    # 关闭服务对象
    socket.close()

#创建socket对象
tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#给服务器端 绑定一个端口号
tcpSocket.bind(('10.10.116.107',6666))
#当服务器满载时，设置客户端最大的等待连接数为 5
tcpSocket.listen(5)
print('开启监听')
while True:
    #等待着客户端 来跟服务器端建立连接 ：在此阻塞
    newSocket,clientAddr = tcpSocket.accept()
    t = threading.Thread(target=task,args=(newSocket,clientAddr))
    t.start()
tcpSocket.close()