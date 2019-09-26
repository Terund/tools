# 随机生成指定位数的验证码
import random


def random_code(len):
    string = "0123456789"
    result = "".join([random.choice(string) for i in range(len)])
    return result