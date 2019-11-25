import time
ADDR = '10.10.116.107'
PORT = 2425
import socket
#创建一个套接字 udp
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpSocket.bind((ADDR,PORT))
while True:
    #接收数据，用户信息
    s,addr = udpSocket.recvfrom(1024)
    print(s.decode(encoding='gbk'))
    print(addr)