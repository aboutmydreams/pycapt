from PIL import Image, ImageDraw
from collections import Counter
import numpy as np
import random



# 将np数组转化成01 dic 后面会废弃
def mode_to_dic(mode):
    dic = {}
    for line in range(0,mode.shape[1]):
        for i in range(0,mode.shape[0]):
            dic[(i, line)] = mode[i,line]
    return dic

# 将01 np数组转化为黑白图片
def mode_to_draw(mode):
    image = Image.new("1", (mode.shape[1],mode.shape[0]))
    draw = ImageDraw.Draw(image)
    for x in range(0, mode.shape[0]):
        for y in range(0, mode.shape[1]):
            draw.point((y, x), int(mode[x,y]))
    return image




# 根据一个点A的RGB值，与周围的8个点的RBG值比较，周围有大于1个不同的，那么考虑一定概率增加噪点
# G: Integer 图像二值化阀值
# N: Integer 加噪率 0 < N < 1
# Z: Integer 加噪次数


def more_noise(mode, N, Z, to_img=None):
    # 0和1互相转换
    def one_zero(num):
        if num == 1:
            return 0
        else:
            return 1
    

    # 二值数组
    img_dic = mode_to_dic(mode)

    for i in range(0, Z):
        img_dic[(0, 0)] = 1
        img_dic[(mode.shape[0] - 1, mode.shape[1] - 1)] = 1
        for x in range(1, mode.shape[0] - 1):
            for y in range(1, mode.shape[1] - 1):
                random_num = random.random()
                # 0或1
                L = img_dic[(x, y)]
                # 统计临近8个点是0还是1
                near8 = [img_dic[(x - 1, y - 1)], img_dic[(x - 1, y)],\
                img_dic[(x - 1, y + 1)], img_dic[(x, y - 1)], img_dic[(x, y + 1)], \
                img_dic[(x + 1, y - 1)], img_dic[(x + 1, y)], img_dic[(x + 1, y + 1)]]
                # data 计算0黑点数与 1白点数
                data = Counter(near8)
                # 一样的点小于8
                if (data[L] < 8) and random_num < N:
                    # img_dic[(x, y)] = one_zero(L)
                    # mode[x,y] = one_zero(L)
                    mode[x,y] = 0
    # print(mode.shape)
    if to_img:
        image = mode_to_draw(mode)
        # print(image.size)
        return image
    else:
        return mode




