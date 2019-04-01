import pycapt
from PIL import Image

###处理验证码
'''
img = Image.open('1.png')
img = pycapt.two_value(img,Threshold=100)
img = pycapt.dele_noise(img,N=5,Z=2)
img = pycapt.dele_line(img,4)
img = pycapt.dele_noise(img,N=4,Z=2)
img = pycapt.dele_line(img,3)
img = pycapt.dele_noise(img,N=4,Z=2)
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)


img = pycapt.tran_90(img)
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)
img = pycapt.tran_90(img)

pan = [18, 18, 18, 18, 17, 17, 17,\
        16, 16, 16, 15, 15, 15, 15, 14,\
        14, 14, 14, 13, 13, 10, 10,\
        10, 9, 9, 8, 7, 6, 5, 5, 4, \
        4, 4, 4, 4, 3, 1, 0, 0, 0]
img = pycapt.rectify_img(img,pans=pan)
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)
img.show()

a = pycapt.cut_img_to_img_list(img,30,255)
for i in a:
    i.show()

'''


### 生产验证码训练集
'''

name,img = pycapt.do_captcha(
        my_str_list=['A','B','C','D','1','2','3'],
        width=160,
        height=40,
        num_of_str=4,
        font=30,
        gray_value=255,
        font_family='ヒラギノ角ゴシック W8.ttc')


# pycapt.get_train_img()
img = pycapt.more_noise(img,N=0.5,Z=2)
# img = pycapt.img_pan(img,15,3)
pans = [18, 18, 18, 18, 17, 17, 17,\
        16, 16, 16, 15, 15, 15, 15, 14,\
        14, 14, 14, 13, 13, 10, 10,\
        10, 9, 9, 8, 7, 6, 5, 5, 4, \
        4, 4, 4, 4, 3, 1, 0, 0, 0]

def contrast(num):
    return -num

pan0 = list(map(contrast,pans))
img = pycapt.rectify_img(img,pans=pan0)

img = pycapt.show_noise_img(img,0.1,1)
img = pycapt.dele_noise(img,5,2)
img = pycapt.clear_train_img(img)
img.show()
'''

# 直接生成验证码训练集
file_name,img = pycapt.train_img(
    my_str_list=['1','2','A','B'],
    width=30,
    height=32,
    num_of_str=4,
    font=30,
    xpan=3,
    ypan=2,
    rotate=15,
    noise_N=0.3,
    noise_Z=2,
    gray_value=255,
    font_family='ヒラギノ角ゴシック W8.ttc')

print(file_name)
img.show()