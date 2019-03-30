import pycaptcha
from PIL import Image

img = Image.open('1.png')
a = pycaptcha.cut_img_to_img_list(img,30,255)
for i in a:
    i.show()


