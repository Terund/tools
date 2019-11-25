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

# 1.创建套接字
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.建立连接
address = ('10.10.16.42', 6666)
tcpsocket.connect(address)
# 客户端要发送给服务器的消息
message = input('请输入给服务器发送的消息:').encode(encoding='utf-8')
# 3.发送  send()
tcpsocket.send(message)
# 4.关闭套接字
tcpsocket.close()
