from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random,time

import make_captcha.noise


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 随机自定义字符
def my_random_str(my_str_list):


def get_captcha(width,height,num_of_str,gray_value=255):
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象:
    font = ImageFont.truetype('ヒラギノ角ゴシック W8.ttc', 31) # '/Library/Fonts/Bodoni 72.ttc'  'ヒラギノ角ゴシック W8.ttc'

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            # draw.point((x, y), fill=rndColor())
            draw.point((x, y), fill=(255,255,255))

    # 输出文字:
    char_list = [rndChar() for i in range(num_of_str)]

    for t in range(num_of_str):
        # rndColor2()
        draw.text((height * t, 1), char_list[t], font=font, fill=(0,0,0))

    # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    # image.save('train_imgs/1.png', 'jpeg');
    return char_list,image