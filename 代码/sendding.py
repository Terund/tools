import json
import requests
import random


# 随机生成一段验证码
def random_code(len):
    string = "0123456789"
    result = "".join([random.choice(string) for i in range(len)])
    return result

# 钉钉机器人的webhook码，改成自己的钉钉机器人的
url = "https://oapi.dingtalk.com/robot/send?access_token=8382bd4da57657e34b08f4626ac9d060d584251bfd614d06b8b7c8e445614def"


# 发送钉钉消息
def send_dd(send_code):
    headers = {
	# 设置连接类型
        "Content-Type": "application/json",
        "Charset": "utf-8"
    }
    # 设置发送的数据，是否@全体成员
    requests_data = {
        "msgtype": "text",
        "text": {
            "content": send_code
        },
        "at": {
	    # 需要@某些人，这里写上他们的手机号
            "atMobiles": [
            ],
            "isAtAll": False
        }
    }
    sendData = json.dumps(requests_data)
    response = requests.post(url=url, headers=headers, data=sendData)
    content = response.json()
    return content