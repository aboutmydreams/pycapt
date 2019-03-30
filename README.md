# 什么是 pycapt

pycapt 是我在处理验证码时编写的一系列图像处理的算法包，你可以使用它来为图像去噪点、干扰线 以及分割验证码，pycapt 封装了一些关于图形矩阵的方法，例如将图片分割为标准化的矩阵、生成您所需要的训练集图片等，有助于您使用深度学习来进行图像识别。

pycaptcha 包括处理验证码和生成验证码两部分，多谢我的好友 [exqlnet](<https://github.com/exqlnet>) [ZhouYingSASA](<https://github.com/ZhouYingSASA>) 的共同帮助 发布 pycapt 0.0.1

```bash
依赖
Pillow
numpy
random
time
heapq
```

## 使用 pycapt 进行验证码图像处理

### 导入

```py
import pycapt
from PIL import Image
```



### 图像二值化

```py
img = Image.open('1.png')
```



### 处理噪点



### 处理干扰线



### 斜体矫正



### 图形分割

```py
img = Image.open('1.png')
img_list = pycapt.cut_img_to_img_list(img,max_width=30,background=255)
for i in img_list:
    i.show()
```



## 使用 pycapt 生成验证码

