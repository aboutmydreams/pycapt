from pycapt.make_captcha.noise import mode_to_draw, more_noise
from pycapt.make_captcha.make_capt import get_modes, img_pan, train_img
from pycapt.make_captcha.my_any_img import mk_captcha


# 图像转化为01 np数组 Threshold为阀值
def get_mode(img, Threshold=100):
    mode = get_modes(img, Threshold)
    return mode


# 将01 np数组转化为黑白图片
def mode_to_img(mode):
    img = mode_to_draw(mode)
    return img


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回数组
def show_noise_mode(mode, N, Z):
    new_mode = more_noise(mode, N, Z)
    return new_mode


# 将np数组噪点处理，mode 数组，N是加噪率（边缘存在1个以上的黑点那么这个点有一点概率变黑） Z 加噪次数 返回图片
def show_noise_img(mode, N, Z):
    new_img = more_noise(mode, N, Z, to_img="toimg")
    return new_img


# 偏移 传入np数组，横向偏移(默认右移)，纵向偏移，传出新的mode
def mode_pan(mode, width_x, height_y):
    new_mode = img_pan(mode, width_x, height_y)
    return new_mode


# 生成验证码 长宽 字符串个数 背景颜色 一般要上线用的话看源码改一改就好了
def make_capt_img(
    my_str_list,
    width,
    height,
    num_of_str,
    gray_value=255,
    font_family="ヒラギノ角ゴシック W8.ttc",
):
    str_list, image = mk_captcha(
        my_str_list, width, height, num_of_str, gray_value, font_family
    )
    return str_list, image


# 生成简单的大写字母训练集图片
def get_train_img(
    width, height, num_of_str=1, xpan=3, ypan=2, rotate=15, gray_value=255
):
    file_name, image = train_img(
        width, height, num_of_str, xpan, ypan, rotate, gray_value
    )
    return file_name, image


def auto_more_noise(img, N=0.3, Z=2):
    """添加更多边缘噪点，返回处理后的图片。"""
    return show_noise_img(img, N, Z)


def do_captcha(
    my_str_list,
    width,
    height,
    num_of_str,
    font=30,
    gray_value=255,
    font_family="ヒラギノ角ゴシック W8.ttc",
):
    """生成验证码。"""
    return mk_captcha(
        my_str_list, width, height, num_of_str, font, gray_value, font_family
    )


# 自定义生成训练图片
# def my_train_img():
