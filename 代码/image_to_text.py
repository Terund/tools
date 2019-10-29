from PIL import Image


# 图像识别获取图片上的所有数字
# img参数为图片路径
def img_discern(img):
    image = Image.open(img)
    text = pytesseract.image_to_string(image)
    return text