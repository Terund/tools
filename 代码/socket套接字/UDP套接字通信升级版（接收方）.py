"""
传输层传输协议：
    UDP

    TCP

套接字通信(socket)

UDP
1.发送方


2.接收方
    1.创建套接字
    2.绑定地址跟端口(发送者发送时候要知道的地址，以及端口)
    3.接收
    4.关闭
"""
import socket
#1.创建套接字
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#2.绑定地址跟端口 127.0.0.1
print('接收方绑定成功')
udpsocket.bind(('10.10.116.107',9999))
print('接收方等待发送方发送消息:')
#3.接收数据
while True:
    message = udpsocket.recvfrom(4096)
    content = message[0].decode(encoding='utf-8')
    print(f'接收到ip地址为{message[1][0]}的用户发送来的消息:{content}')

    # 回复
    backdata = input('请输入要回复的消息:').encode('utf-8')
    udpsocket.sendto(backdata,message[1])

udpsocket.close()