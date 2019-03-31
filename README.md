![all](img/all.png)

# 什么是 pycapt

[GitHub 欢迎提 pr，如果有bug或新需求 请反馈 issue]()

pycapt 是我在处理验证码时编写的一系列图像处理的算法包，你可以使用它来为图像去噪点、干扰线 以及分割验证码，pycapt 封装了一些关于图形矩阵的方法，例如将图片分割为标准化的矩阵、生成您所需要的训练集图片等，有助于您使用深度学习来进行图像识别。

pycapt 包括处理验证码和生成验证码两部分，多谢我的好友 [exqlnet](<https://github.com/exqlnet>) [ZhouYingSASA](<https://github.com/ZhouYingSASA>) 的共同帮助 发布 pycapt 0.0.1

### 依赖与安装

```bash
Pillow
numpy
```

```py
pip3 install pycapt
```



## 使用 pycapt 进行验证码图像处理

### 导入

```py
import pycapt
from PIL import Image
```



### 图像二值化

**two_valve : 二值化方法，必选参数img为图片，可选参数 Threshold** 是灰度阀值，这里可以选择适合的值，默认值是100 .  **返回新处理过的图片**

```py
img = Image.open('./img/frcc0.png')
img = pycapt.two_value(img,Threshold=100)
img.show()
```



![frcc0](img/frcc0.png)

![frcc1](img/frcc1.png)

### 处理噪点

**dele_noise ：消除噪点方法，该方法使用的是八领域去噪点法，N是领域异点个数，Z是处理次数，处理次数越多 图形越圆滑**。

```py
img = pycapt.dele_noise(img,N=5,Z=2)
img.show()
```



![frcc2](img/frcc2.png)

### 处理干扰线

**dele_line : 去除干扰线，删除连续的N个竖直像素。配合dele_noise方法使用效果更佳。**

```py
img = pycapt.dele_line(img,N=4)
img.show()
```

**配合dele_noise方法使用效果更佳。**

```py
img = pycapt.dele_line(img,4)
img = pycapt.dele_noise(img,N=4,Z=2)
img = pycapt.dele_line(img,3)
img = pycapt.dele_noise(img,N=4,Z=2)
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)
img.show()
```

![frcc2](img/frcc3.png)

**想要更好的效果，你还可以先使用转置图片的 tran_90(img) 方法 再次使用去除干扰线的方法，最后再转置回来**

```py
img = pycapt.tran_90(img)
img.show()
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)
img = pycapt.tran_90(img)
img.show()
```

![frcc2](img/frcc4.png)

### 斜体矫正

**斜体矫正的目的是为了更好的分割与识别。**原理是平移，将每一行向左或向右平移不同距离，最后形成矫正的效果。pans就是矫正列表，正左负右平移。pans列表的元素个数需要是图片的高度，例子中图片 height 是40.

**rectify_img(img,pans) 返回新的图片。**

```py
pan = [18, 18, 18, 18, 17, 17, 17,\
        16, 16, 16, 15, 15, 15, 15, 14,\
        14, 14, 14, 13, 13, 10, 10,\
        10, 9, 9, 8, 7, 6, 5, 5, 4, \
        4, 4, 4, 4, 3, 1, 0, 0, 0]
img = pycapt.rectify_img(img,pans=pan)
img.show()
```

![frcc2](img/frcc5.png)

如果你觉得太难看了，可以提前使用矫正再使用 dele_line 和 dele_noise, 当然亡羊补牢也不太坏。

```py
img = pycapt.rectify_img(img,pans=pan)
img = pycapt.dele_line(img,3)
img = pycapt.dele_line(img,2)
img = pycapt.dele_line(img,1)
img.show()
```

![frcc2](img/frcc6.png)



### 图形分割

**cut_img_to_img_list** 设置单个图片合适长度后切割，返回该长度的切割图片，该长度可以设置的比较大，该方法会在切割图片的两边补白。你可以将这作为一种标准化图片的方法。

```py
img = Image.open('1.png')
img_list = pycapt.cut_img_to_img_list(img,max_width=30,background=255)
for i in img_list:
    i.show()
```

![frcc2](img/last.png)

当你使用**深度学习**时，还可以使用 **cut_img_to_mode_list(image,max_width) **来获得标准化的数组。

### 图片裁剪

当你的图片 height 可以压缩时，可以使用 **small_img(img,box)** 来裁剪图片，这样可以减少之后学习的计算量。

例如

## 使用 pycapt 生成验证码训练集

如果你不知道自己电脑有哪些字体，请点击 [**这里**](<https://www.yuque.com/zhiwa/deepin/ahimr7>) 。

```py
name,img = pycapt.do_captcha(
        my_str_list=['A','B','C','D','1','2','3'],
        width=160,
        height=40,
        num_of_str=4,
        font=30,
        gray_value=255,
        font_family='ヒラギノ角ゴシック W8.ttc')

print(name)
img.show()
```

![frcc2](img/do.png)

