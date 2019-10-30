# 密码加密函数
# hashlib是对二进制进行加密的，因此需要通过encode()将字符串转码为二进制
# hashlib主要提供字符加密功能，将md5和sha模块整合到了一起，支持MD5、sha1、sha224、sha256、sha384、sha512等算法
import hashlib


def setPassword(password):
    m = hashlib.md5()
    m.update(password.encode())
    result = m.hexdigest()
    return result
