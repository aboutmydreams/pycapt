from PIL import Image
import pycapt.make_captcha.noise
import pycapt.make_captcha.make_capt
import pycapt.make_captcha.my_any_img

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
def make_capt_img(my_str_list,width,height,num_of_str,gray_value=255,font_family='ヒラギノ角ゴシック W8.ttc'):
    str_list,image = pycapt.make_captcha\
    .my_any_img.mk_captcha(my_str_list,width,height,num_of_str,gray_value,font_family)
    return str_list,image


# 生成简单的大写字母训练集图片
def get_train_img(width,height,num_of_str=1,xpan=3,ypan=2,rotate=15,gray_value=255):
    file_name,image = pycapt.make_captcha.make_capt.train_img(width,height,num_of_str,xpan,ypan,rotate,gray_value)
    return file_name,image





# 自定义生成训练图片
# def my_train_img():
