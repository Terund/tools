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

# 创建socket对象
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 给服务器端 绑定一个端口号
tcpSocket.bind(('10.10.16.42', 6666))
# 当服务器满载时，设置客户端最大的等待连接数为 5
tcpSocket.listen(5)
print('开启监听')
# 等待着客户端 来跟服务器端建立连接 ：在此阻塞
newSocket, clientAddr = tcpSocket.accept()
print('有客户端接入')
print(clientAddr)
# 通过客户端的套接字进行接收
message = newSocket.recv(4096)
print("服务器端收到信息为：", message.decode())
# 关闭服务对象
newSocket.close()
tcpSocket.close()
