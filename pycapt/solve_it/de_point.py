# 去除噪点
from PIL import Image,ImageDraw
from collections import Counter
import numpy as np




# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# G: Integer 图像二值化阀值
# N: Integer 降噪率 0 <N <8
# Z: Integer 降噪次数
# 输出
#  0：降噪成功
#  1：降噪失败

def two_value(image, G):
    # 二值数组
    image = image.convert("L")
    img_dic = {}
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            g = image.getpixel((x, y))
            img_dic[(x, y)] = 1 if g > G else 0
    return img_dic


def get_modes(img,Threshold=100):
    img = img.convert('L')
    mode = np.array(img)
    mode = np.where(mode < Threshold, 0, 1)
    return mode

def mode_to_img(mode,background=None):
    if background:
        mode = np.where(mode < 1, 0, background)
    array_mode = np.array(mode).astype('uint8')
    return Image.fromarray(array_mode).convert('RGB')

def clear_noise(image, N, Z):
    # 0和1互相转换
    def one_zero(num):
        return 0 if num == 1 else 1
    # 二值数组
    image = image.convert("L")
    img_dic = two_value(image,100)
    mode = get_modes(image)
    for i in range(0, Z):
        img_dic[(0, 0)] = 1
        img_dic[(image.size[0] - 1, image.size[1] - 1)] = 1

        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                L = img_dic[(x, y)]# 0或1
                # 统计临近8个点是0还是1
                near8 = [img_dic[(x - 1, y - 1)], img_dic[(x - 1, y)],\
                img_dic[(x - 1, y + 1)], img_dic[(x, y - 1)], img_dic[(x, y + 1)], \
                img_dic[(x + 1, y - 1)], img_dic[(x + 1, y)], img_dic[(x + 1, y + 1)]]
                # data 计算0黑点数与 1白点数
                data = Counter(near8)
                if data[L] < N:
                    # img_dic[(x, y)] = one_zero(L)
                    mode[y,x] = one_zero(L)
    return mode_to_img(mode,255)



def save_img(filename, size, img_dic):
    image = Image.new("1", size)
    draw = ImageDraw.Draw(image)

    for x in range(size[0]):
        for y in range(size[1]):
            draw.point((x, y), img_dic[(x, y)])

    image.save(filename)

# for i in range(1,2):
#     path =  str(i) + ".png"
#     image = Image.open(path).convert("L")
#     img_dic = clear_noise(image, 2, 1)
#     print(img_dic)
#     path1 = str(i) + ".jpeg"
#     save_img(path1, image.size, img_dic)


