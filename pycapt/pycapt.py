import pycapt.solve_it

from PIL import Image
import pycapt.make_captcha.noise
import pycapt.make_captcha.make_capt

# 图像转化为01 np数组 Threshold为阀值
def get_mode(img,Threshold=100):
    mode = pycapt.make_captcha.make_capt.get_modes(img,Threshold)
    return mode


# 将01 np数组转化为黑白图片
def mode_to_img(mode):
    img = pycapt.make_captcha.noise.mode_to_draw(mode)
    return img


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回数组
def show_noise_mode(mode, N, Z):
    new_mode = pycapt.make_captcha.noise.more_noise(mode, N, Z)
    return new_mode


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回图片
def show_noise_img(mode, N, Z):
    new_img = pycapt.make_captcha.noise.more_noise(mode, N, Z, to_img='toimg')
    return new_img


# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def mode_pan(mode,width_x,height_y):
    new_mode = pycapt.make_captcha.make_capt.img_pan(mode,width_x,height_y)
    return new_mode


# 生成验证码 长宽 字符串个数 背景颜色 一般要上线用的话看源码改一改就好了
def mk_captcha(my_str_list,width,height,num_of_str,gray_value=255,font_family='ヒラギノ角ゴシック W8.ttc'):
    image = pycapt.make_captcha.my_any_img.mk_captcha(my_str_list,width,height,num_of_str,gray_value,font_family)
    return image


# 生成简单的训练集图片
def get_train_img(my_str_list,width,height,num_of_str,font=30,gray_value=255,font_family='ヒラギノ角ゴシック W8.ttc'):
    str_list,image = pycapt.make_captcha\
    .my_any_img.mk_captcha(my_str_list,width,height,num_of_str,font,gray_value,font_family)
    return str_list,image


def mode_img(mode,background=None):
    img = pycapt.solve_it.cut_img.mode_to_img(mode,background=None)
    return img

def mode_white_img(mode):
    img = pycapt.solve_it.cut_img.mode_to_img(mode,background=255)
    return img

def dele_noise(image, N, Z):
    img = pycapt.solve_it.de_point.clear_noise(image, N, Z)
    return img

def dele_line(image, N, pans=None):
    img = pycapt.solve_it.de_line.clear_line(image, N, pans=None)
    return img

def clear_train_img(image):
    img = pycapt.solve_it.de_line.clear_my_train_img(image)
    return img

def clear_lib_line(image):
    img = pycapt.solve_it.de_line.clear_my_line(image)
    return img

def cut_img_to_mode_list(image,max_width):
    img_mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
    return img_mode_list

def cut_img_to_img_list(image,max_width,background=None):
    if background:
        mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
        img_list = map(mode_white_img,mode_list)
        return img_list
    else:
        img_mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
        return map(mode_img,img_mode_list)


def small_img(img,box):
    return pycapt.solve_it.get_small_img(img,box)

def small_mode(mode,box):
    img = mode_img(mode)
    return pycapt.solve_it.get_small_modes(img,box)

def rectify_img(image, pans):
    return pycapt.solve_it.rectify_img(image,pans)

# 返回斜体纠正后的np数组
def rectify_mode(mode, pans):
    return pycapt.solve_it.rectify_mode(mode,pans)


# img = Image.open('1.png')
# print(get_mode(img))