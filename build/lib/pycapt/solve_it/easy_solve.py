from pycapt.solve_it.cut_img import get_modes, mode_to_img, cut_img, get_small_modes
from pycapt.solve_it.de_line import clear_line, clear_my_line, clear_my_train_img
from pycapt.solve_it.de_point import clear_noise


def mode_img(mode, background=None):
    img = mode_to_img(mode, background)
    return img


# 将01数组转化为黑白图片
def mode_white_img(mode):
    img = mode_img(mode, background=255)
    return img


# 二值化图片，变为黑白
def two_value(img, Threshold=100):
    mode = get_modes(img, Threshold)
    return mode_img(mode, background=255)


def dele_noise(image, N, Z):
    img = clear_noise(image, N, Z)
    return img


def dele_line(image, N, pans=None):
    if pans:
        img = clear_line(image, N, pans)
        return img
    else:
        img = clear_line(image, N, pans=None)
        return img


def clear_train_img(image):
    img = clear_my_train_img(image)
    return img


def clear_lib_line(image):
    img = clear_my_line(image)
    return img


def rectify_mode(mode, pans):
    return rectify_mode(mode, pans)


def cut_img_to_mode_list(image, max_width):
    img_mode_list = cut_img(image, max_width)
    return img_mode_list


def get_small_img(img, box=(10, 4, 150, 36), background=None):
    if background:
        return get_small_modes(img, box, background)
    else:
        return get_small_modes(img, box, background=None)


def cut_img_to_img_list(image, max_width, background=None):
    if background:
        mode_list = cut_img(image, max_width)
        img_list = map(mode_white_img, mode_list)
        return img_list
    else:
        img_mode_list = cut_img(image, max_width)
        return map(mode_img, img_mode_list)


def tran_90(img):
    """图片翻转并旋转90度。"""
    mode = get_modes(img)
    return mode_img(mode.T, 255)
