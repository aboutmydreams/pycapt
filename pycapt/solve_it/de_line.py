from PIL import Image
from collections import Counter

import numpy as np

# 保证所有数据能够显示，而不是用省略号表示
np.set_printoptions(threshold = np.inf) 

# 将图片转化为数组 这里会预先灰度化
def get_modes(img):
    img = img.convert('L')
    mode = np.array(img)
    mode = np.where(mode < 100, 0, 1)
    return mode

# 左平移 D为正，右平移，D为负
def pan(line,D):
    if D == 0:
        return line
    else:
        line = line[D:] + line[:D]
    return line


# N 干扰线纵向像素点个数
def clear_line(image, N, pans=None):
    mode = get_modes(image)
    new_mode = []
    for line in mode.T:
        new_column = is_three0(line,N)
        new_mode.append(new_column)

    new_mode = eval(str(new_mode).replace('1','255').replace('0','0'))
    
    array_mode = np.array(new_mode).T.astype('uint8')
    if pans:
        new_mode = []
        for k,line in enumerate(array_mode.tolist()):
            line = pan(line,pans[k])
            new_mode.append(line)
        array_mode = np.array(new_mode).astype('uint8')
    image = Image.fromarray(array_mode).convert('RGB')
    return image



# 判断列表中连续的三个位置是否是0,且相邻位置是1，替换掉这3个0
def is_three0(column, N):
    column_str = ''.join(map(str,column))
    zero_site_list = [i for i,v in enumerate(column) if v==0]

    for i in  zero_site_list[-N:]:
        if i > len(column)-N-1:
            zero_site_list.remove(i)

    for i in zero_site_list:
        if i > 0 and column_str[i:i+N] == '0' * N and column_str[i+N] == '1' and column_str[i-1] == '1':
            column_str = column_str[:i] + '1' * N + column_str[i+N:]
    column = list(map(int,column_str))
    return column

# 处理真实图片
def clear_my_line(img):
    panD_list = [18, 18, 18, 18, 17, 17, 17, 16, 16, 16, 15, 15, 15, 15, 14, 14, 14, 14, 13, 13, 10, 10, 10, 9, 9, 8, 7, 6, 5, 5, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0]
    img2 = clear_line(img,4)
    img2 = clear_line(img2,3,panD_list)
    img2 = clear_line(img2,4)
    img2 = clear_line(img2,3)
    img2 = clear_line(img2,2)
    img2 = clear_line(img2,1)
    return img2


# 清理训练集
def clear_my_train_img(img):
    # panD_list = [18, 18, 18, 18, 17, 17, 17, 16, 16, 16, 15, 15, 15, 15, 14, 14, 14, 14, 13, 13, 10, 10, 10, 9, 9, 8, 7, 6, 5, 5, 4, 4, 4, 4, 4, 3, 1, 0, 0, 0]
    img2 = clear_line(img,4)
    img2 = clear_line(img2,3)
    img2 = clear_line(img2,2)
    img2 = clear_line(img2,1)
    return img2