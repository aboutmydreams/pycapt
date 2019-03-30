from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import random,time

from pycaptcha import make_captcha



# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
# width = 60 * 4
# height = 60

def get_captcha(width,height,num_of_str,gray_value=255):
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Font对象:
    font = ImageFont.truetype('ヒラギノ角ゴシック W8.ttc', 31) # '/Library/Fonts/Bodoni 72.ttc'

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



def get_modes(img,Threshold=100):
    img = img.convert('L')
    mode = np.array(img)
    mode = np.where(mode < Threshold, 0, 1)
    return mode

def mode_to_img(mode,background=None):
    if background:
        mode = np.where(mode < 1, 0, background)
    array_mode = np.array(mode).astype('uint8')
    image = Image.fromarray(array_mode).convert('RGB')
    return image


# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def img_pan(mode,width_x,height_y):
    new_mode = mode.copy()
    if width_x != 0:
        new_mode[:,:width_x] = mode[:,-width_x:]
        new_mode[:,width_x:] = mode[:,:-width_x]
    if height_y != 0:
        new_mode[:height_y,:] = mode[-height_y:,:]
        new_mode[height_y:,:] = mode[:-height_y,:]
    return new_mode
    




# 生成训练集图片
def train_img():
    char_list,image = get_captcha(30,32,num_of_str=1,gray_value=255)
    file_name = char_list[0] + '-' + str(time.time())[-10:-3].replace('.',str(random.random())[2:4])
    # image.show()
    # 在这里增加难度与异动
    mode = get_modes(image,100)
    # 偏移
    mode = img_pan(mode,random.randint(-3,3),random.randint(-2,2))
    # 添加噪点
    image = make_captcha.noise.more_noise(mode,N=0.3,Z=2,to_img='to_img')
    # 旋转
    image = image.rotate(random.randint(-15,15),fillcolor=255) 
    # print(image.size)
    # image.save('train_imgs/{}.png'.format(file_name))
    return file_name,image