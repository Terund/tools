"""
#飞秋发送消息，遵守飞秋自己的协议
#1：默认版本
#123456发送时间，可以任意写
#张无忌:能说的小牛 名称跟简称
#32:发送消息

"""
import socket
import time

# 创建套接字
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送消息

udpSocket.sendto("1:123456:你是弟弟:PC-2019062:32:嘤嘤嘤".encode('gbk'), ('10.10.16.41', 2425))
# 关闭套接字
udpSocket.close()
