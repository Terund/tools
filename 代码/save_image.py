import requests


# 保存图片到本地
def get_image(url):
    """
    :param url: 图片链接参数
    :return: 无返回值，直接保存一张图片
    """
    response = requests.get(url)
    with open("price.png", "wb") as fp:
        for data in response.iter_content(128):
            fp.write(data)
