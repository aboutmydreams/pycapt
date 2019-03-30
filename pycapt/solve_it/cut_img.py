from PIL import Image
import numpy as np
import heapq

# np.set_printoptions(threshold=np.inf)


def get_small_modes(img,background=None):
    img = img.convert('L')
    box1 = (10, 4, 150, 36)
    img1 = img.crop(box1)
    mode = np.array(img1)
    if background:
        mode = np.where(mode < 100, 0, background)
    else:
        mode = np.where(mode < 100, 0, 1)
    return mode

def mode_to_img(mode,background=None):
    if background:
        mode = np.where(mode < 1, 0, background)
    array_mode = np.array(mode).astype('uint8')
    image = Image.fromarray(array_mode).convert('RGB')
    return image

def is_white_column(column):
    # print(column)
    for c in column:
        if c == 0:
            return False
    return True

def cut_from_rect(rect, start, end):
    # print("cut from %s to %s" % (start, end))
    return rect[:, start:end]
# 返回分割后的numpy矩阵
def vertical_cut(rect):
    max_width = 35
    last_position = 0
    # print(rect)
    width = rect.shape[1]

    result = []
    bools = []
    for x in range(width):
        c_position = x
        bools.append(is_white_column(rect[:, x]))
        
        if not bools[c_position] and c_position == 0:
            continue
        
        if not bools[c_position] and bools[c_position - 1]:
            last_position = c_position - 1
            continue
        
        if (bools[c_position] and not bools[c_position - 1]):
            # 开始截取, 从last_position到c_position
            delta = c_position - last_position
            if delta <= 1: # 像这样到肯定有问题，直接跳过
                continue
            
            bit = float(delta)/float(max_width)

            point_right = bit - int(bit)
            if point_right > 0.3:
                npart = int(bit) + 1
                interval = int(delta/npart)
                for i in range(npart):
                    if i == npart - 1:
                        # 考虑到整数运算会有误差，所以到最后一步就直接 last_position + inpart : c_position
                        result.append(cut_from_rect(rect, last_position, c_position))
                        last_position = c_position
                    else:
                        # 取last_position + i*npart : last_position + (i+1)*npart
                        result.append(cut_from_rect(rect, last_position, (last_position+(i+1)*interval)))
                        last_position += interval
                        
                
            
    # for x in range(width):
    #     c_position = x
    #     bools.append(is_white_column(rect[:, x]))        
    #     if bools[-1] and (bools[-2] if bools.__len__() > 2 else True):
    #         last_position = c_position
    #     if bools[-1] and (not bools[-2] if bools.__len__() > 2 else True):
    #         if c_position - last_position >= 35:
    #             x1 = last_position
    #             x2 = int((c_position + last_position)/2)
    #             x3 = c_position
    #             # print(x1, x2, x3)
    #             result.extend([rect[:, x1:x2], rect[:, x2:x3]])
    #         else:
    #             # print(last_position, c_position)
    #             result.append(rect[:, last_position:c_position+1])
    #         last_position = c_position
    # result.pop(0)
    # result.pop(0)
    return result

def cut_mode(mode,max_width,need_num=4):
    ### 获取边缘列（字母边缘 白色）位置的列表 

    # 转置矩阵
    mode = mode.T
    # 第一行和最后一行变1 白
    mode[[0,-1]] = 1
    mode = mode.tolist()
    # 边缘行列表 由数学知识可知道 边缘一定是成双的
    bian_yuan = []
    all_num_list = list(range(len(mode)-1))
    for k,line in enumerate(mode[:-1]):
        is_one_num = list(set(line))
        if is_one_num == [1]:
            all_num_list.remove(k)
            if ((k-1) in all_num_list):
                bian_yuan.append(k)
        if (is_one_num == [0,1]) and ((k-1) not in all_num_list):
            bian_yuan.append(k-1)
    # print('边缘：',bian_yuan)
    ### 边缘列表俩俩组合成新的列表
    black_list = []
    len_list =[]
    for k,i in enumerate(bian_yuan[::2]):
        alpha_list = list(range(i,bian_yuan[(k+1)*2-1]+1))
        # 判断长度大于等于4
        if len(alpha_list) > 3:
            black_list.append(alpha_list)
            len_list.append(len(alpha_list))
    # print(len_list)
    ### 列表长度大于n 删除最小的几个,判断太长的 平均分
    # listTemp 为列表 平分后每份列表的的个数n
    def average_func(m, n):
        f = False
        s = len(m) // n
        lef = len(m) % n
        lop = 0
        stopat = 0
        if lef != 0:
            s += 1
            f = True
        ret = []
        if f:
            for i in range(lef):
                ret.append(m[i*s:(i+1)*s])
                stopat = i*s+1
                lop = i
            s -= 1
            for i in range(1, n-lop):
                ret.append(m[stopat+i*s:stopat+(i+1)*s])
            return ret
        else:
            for i in range(n):
                ret.append(m[i*s:(i+1)*s])
            return ret
        
        
    need_list = []
    if len(black_list) > need_num:
        pass
        max_num_index_list = map(len_list.index, heapq.nlargest(need_num, len_list))
        for i in max_num_index_list:
            need_list.append(black_list[i])
    elif len(black_list) < need_num:
        for k,black in enumerate(black_list):
            if float(max_width)*2.4 > len(black) > float(max_width)*1.25:
                real_list = list(average_func(black,2))
                real_list.reverse()
                black_list.remove(black)
                for i in real_list:
                    black_list.insert(k,i)
            elif float(max_width)*3.4 > len(black) >= float(max_width)*2.4:
                real_list = list(average_func(black,3))
                real_list.reverse()
                black_list.remove(black)
                for i in real_list:
                    black_list.insert(k,i)
            elif len(black) >= float(max_width)*3.4:
                real_list = list(average_func(black,need_num - len(black_list) + 1))
                real_list.reverse()
                black_list.remove(black)
                for i in real_list:
                    black_list.insert(k,i)

    mode_list = []
    # print(black_list)
    for i in black_list:
        new_mode = np.array(mode)[i].T
        mode_list.append(new_mode)
    return mode_list

def cut_img(img,max_width):
    my_mode = get_small_modes(img)

    # img2 = mode_to_img(my_mode,255)
    # img2.show()

    # li = vertical_cut(my_mode)
    li = cut_mode(my_mode,max_width=30)
    for k,i in enumerate(li):
        its_height = np.shape(i)[0]
        its_width = np.shape(i)[1]
        # 当长度超过预计时，切割中间预计的部分
        if its_width > max_width:
            d = its_width - max_width
            li[k] = i[:,int(d/2):-int(d/2)-d%2]
        # 当长度小于预计的时候，两边填充全为1的列
        if its_width < max_width:
            d = max_width - its_width
            if d == 1:
                one_column1 = np.ones(its_height).reshape(its_height,1).astype('uint8')
                li[k] = np.hstack((i,one_column1))
            else:
                one_column = np.ones(its_height*int(d/2))\
                .reshape(its_height,int(d/2)).astype('uint8')
                one_column1 = np.ones(its_height*(int(d/2)+d%2))\
                .reshape(its_height,int(d/2)+d%2).astype('uint8')
                # print(i.shape)
                # print(one_column.shape)
                new_mode = np.hstack((one_column,i))
                li[k] = np.hstack((new_mode,one_column1))
        
        # img = mode_to_img(i,255)
        # img.show()
    return li


### 测试
# import de_point,de_line
# img = Image.open('RHLIN-45884951.png')
# img = de_point.clear_noise(img, N=2, Z=1)
# img = de_line.clear_my_line(img)

# cut_img(img, 30)
# img.show()