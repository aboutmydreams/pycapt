import pycapt
from PIL import Image

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


