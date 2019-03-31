import pycapt.solve_it.cut_img
import pycapt.solve_it.de_line
import pycapt.solve_it.de_point


def mode_img(mode,background=None):
    img = pycapt.solve_it.cut_img.mode_to_img(mode,background)
    return img

def mode_white_img(mode):
    img = pycapt.solve_it.cut_img.mode_to_img(mode,background=255)
    return img

def dele_noise(image, N, Z):
    img = pycapt.solve_it.de_point.clear_noise(image, N, Z)
    return img

def dele_line(image, N, pans=None):
    if pans:
        img = pycapt.solve_it.de_line.clear_line(image, N, pans)
        return img
    else:
        img = pycapt.solve_it.de_line.clear_line(image, N, pans=None)
        return img

def clear_train_img(image):
    img = pycapt.solve_it.de_line.clear_my_train_img(image)
    return img

def clear_lib_line(image):
    img = pycapt.solve_it.de_line.clear_my_line(image)
    return img

def rectify_img(image, pans):
    return pycapt.solve_it.de_line.rectify_img(image, pans)

def rectify_mode(mode, pans):
    return pycapt.solve_it.de_line.rectify_mode(mode, pans)

def cut_img_to_mode_list(image,max_width):
    img_mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
    return img_mode_list

def get_small_modes(img,box=(10, 4, 150, 36)):
    return pycapt.solve_it.cut_img.get_small_modes(img,box,background=None)

def get_small_img(img,box=(10, 4, 150, 36),background=None):
    if background:
        return pycapt.solve_it.cut_img.get_small_modes(img,box,background)
    else:
        return pycapt.solve_it.cut_img.get_small_modes(img,box,background=None)

def cut_img_to_img_list(image,max_width,background=None):
    if background:
        mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
        img_list = map(mode_white_img,mode_list)
        return img_list
    else:
        img_mode_list = pycapt.solve_it.cut_img.cut_img(image,max_width)
        return map(mode_img,img_mode_list)