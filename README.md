# What is pycapt

[![Auto CI and Build Tools](https://github.com/aboutmydreams/pycapt/actions/workflows/ci-test.yml/badge.svg)](https://github.com/aboutmydreams/pycapt/actions/workflows/ci-test.yml)
[![Auto Publish to PyPI and GitHub Release](https://github.com/aboutmydreams/pycapt/actions/workflows/release.yml/badge.svg)](https://github.com/aboutmydreams/pycapt/actions/workflows/release.yml)
[![label](https://img.shields.io/badge/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3-ZH-brightgreen)](https://github.com/aboutmydreams/pycapt/blob/main/README_ZH.md)
[![label](https://img.shields.io/badge/English-EN-brightgreen)](https://github.com/aboutmydreams/pycapt/blob/main/README.md)
[![Release Version](https://img.shields.io/github/release/aboutmydreams/pycapt.svg)](https://github.com/aboutmydreams/pycapt/releases)
[![Visits](https://komarev.com/ghpvc/?username=aboutmydreams&repo=way3)](https://github.com/aboutmydreams/pycapt)
[![License](https://img.shields.io/github/license/aboutmydreams/pycapt.svg)](https://github.com/aboutmydreams/pycapt/license)
[![Stars](https://img.shields.io/github/stars/aboutmydreams/pycapt.svg)](https://github.com/aboutmydreams/pycapt/stargazers)
[![Forks](https://img.shields.io/github/forks/aboutmydreams/pycapt.svg)](https://github.com/aboutmydreams/pycapt/network)
[![Downloads](https://pepy.tech/badge/pycapt)](https://pepy.tech/project/pycapt)
[![Contributors](https://img.shields.io/github/contributors/aboutmydreams/pycapt.svg)](https://github.com/aboutmydreams/pycapt/graphs/contributors)

[GitHub Welcome to submit PRs, if there are bugs or new requests please feedback in issues](https://github.com/aboutmydreams/pycapt/issues)

pycapt is a collection of image processing algorithms I created for handling CAPTCHAs. You can use it to denoise images, remove interference lines, and segment CAPTCHAs. pycapt encapsulates methods for manipulating image matrices, such as splitting images into standardized matrices and generating the required training images, which is helpful for using deep learning in image recognition. In 2024, pycapt released a new version that added some logo generation methods to generate Android or iOS logos with one click.

pycapt includes both CAPTCHA processing and generation. Special thanks to my friends [exqlnet](https://github.com/exqlnet) and [ZhouYingSASA](https://github.com/ZhouYingSASA) for their support in releasing pycapt version 1.0.1.


## Dependencies and Installation

```bash
Pillow
numpy
```

```py
pip3 install pycapt
```

### Directory Structure

![frcc0](img/files.png)

## Using pycapt for CAPTCHA Image Processing

### Importing

```py
import pycapt
from PIL import Image
```

### Image Binarization

**two_value**: This method binarizes the image. The required parameter `img` is the image, and the optional parameter `Threshold` is the gray threshold, where you can choose an appropriate value (default is 100). **Returns a newly processed image.**

```py
img = Image.open('./img/frcc0.png')
img = pycapt.two_value(img, Threshold=100)
img.show()
```

![frcc0](img/frcc0.png)

![frcc1](img/frcc1.png)

### Noise Reduction

**dele_noise**: This method removes noise using an eight-neighborhood denoising technique. `N` is the number of neighborhood outliers, and `Z` is the number of processing iterations; more iterations will result in a smoother image.

```py
img = pycapt.dele_noise(img, N=5, Z=2)
img.show()
```

![frcc2](img/frcc2.png)

### Removing Interference Lines

**dele_line**: This method removes interference lines by deleting `N` consecutive vertical pixels. It works best when used in conjunction with the `dele_noise` method.

```py
img = pycapt.dele_line(img, N=4)
img.show()
```

**For better results, you can first transpose the image using the `tran_90(img)` method, then apply the line removal method, and finally transpose it back.**

```py
img = pycapt.tran_90(img)
img.show()
img = pycapt.dele_line(img, 3)
img = pycapt.dele_line(img, 2)
img = pycapt.dele_line(img, 1)
img = pycapt.tran_90(img)
img.show()
```

![frcc2](img/frcc4.png)

### Slant Correction

**The purpose of slant correction is to improve segmentation and recognition.** The principle involves shifting each row left or right by different distances to create a correction effect. The `pans` list contains the shift values, where positive numbers shift left and negative numbers shift right. The number of elements in the `pans` list must equal the image height.

**`rectify_img(img, pans)` returns a new image.**

```py
pan = [18, 18, 18, 18, 17, 17, 17,
        16, 16, 16, 15, 15, 15, 15, 14,
        14, 14, 14, 13, 13, 10, 10,
        10, 9, 9, 8, 7, 6, 5, 5, 4,
        4, 4, 4, 4, 3, 1, 0, 0, 0]
img = pycapt.rectify_img(img, pans=pan)
img.show()
```

![frcc2](img/frcc5.png)

If you find it too unappealing, you can apply correction first and then use `dele_line` and `dele_noise`. Of course, addressing issues later is also acceptable.

```py
img = pycapt.rectify_img(img, pans=pan)
img = pycapt.dele_line(img, 3)
img = pycapt.dele_line(img, 2)
img = pycapt.dele_line(img, 1)
img.show()
```

![frcc2](img/frcc6.png)

### Image Segmentation

**cut_img_to_img_list** sets a suitable length for the single image before cutting, returning the segmented image. The length can be set relatively large, and this method will pad the cut images on both sides. You can use this as a method for standardizing images.

```py
img = Image.open('1.png')
img_list = pycapt.cut_img_to_img_list(img, max_width=30, background=255)
for i in img_list:
    i.show()
```

![frcc2](img/last.png)

When using **deep learning**, you can also use **cut_img_to_mode_list(image, max_width)** to obtain a standardized array.

### Image Cropping

When your image height can be compressed, you can use **small_img(img, box)** to crop the image, reducing the computational load for later learning.

## Using pycapt to Generate CAPTCHA Training Sets

### do_captcha for Generating CAPTCHA Training Sets

`width` is the length of the CAPTCHA image, `height` is the height, `num_of_str` is the number of characters in the CAPTCHA (default is 4), `font` is the font size (default is 30), `gray_value` is the background gray value (default is 255), and `font_family` is the font file. You can choose the thickness, style, etc., but the font must be installed on your computer.

If you're unsure about which fonts are installed on your computer, please click [**here**](https://www.yuque.com/zhiwa/deepin/ahimr7).

```py
name, img = pycapt.do_captcha(
    my_str_list=['A', 'B', 'C', 'D', '1', '2', '3'],
    width=160,
    height=40,
    num_of_str=4,
    font=30,
    gray_value=255,
    font_family='ヒラギノ角ゴシック W8.ttc'
)

print(name)
img.show()

# output: ['C', 'D', '2', 'A']
```

![frcc2](img/do.png)

### Adding Noise

**more_noise**: `N` is the noise rate (0 < N < 1), and `Z` is the number of processing iterations.

```py
img = pycapt.more_noise(img, N=0.5, Z=2)
```

![frcc2](img/do1.png)

### Panning

```py
img = pycapt.img_pan(img, 10, 3)
```

![frcc2](img/do2.png)

### Inclining

As before, use `rectify_img`.

```py
pan = [18, 18, 18, 18, 17, 17, 17,
        16, 16, 16, 15, 15, 15, 15, 14,
        14, 14, 14, 13, 13, 10, 10,
        10, 9, 9, 8, 7, 6, 5, 5, 4,
        4, 4, 4, 4, 3, 1, 0, 0, 0]
img = pycapt.rectify_img(img, pans=pan)
```

![frcc2](img/do3.png)

### Denoising for Smoothness

`clear_train_img` effectively applies `dele_line(line, N)` sequentially for `N=4, 3, 2, 1`, smoothing the image vertically.

```py
img = pycapt.show_noise_img(img, 0.1, 1)
img = pycapt.dele_noise(img, 5, 2)
img = pycapt.clear_train_img(img)
```

![frcc2](img/do4.png)

Here, you can fully utilize pycapt to generate a training set for CAPTCHA with deep learning.

If you want something more convenient, please see below.

### Directly Generating Training Set Method

**easy_train_img** returns training set images. `my_str_list` is your character set list, `width` and `height` are the dimensions, and `num_of_str` is the number of characters displayed in the CAPTCHA image, which will be randomly selected from your `my_str_list`.

```py
filename, img = pycapt.easy_train_img(
    my_str_list=['A', 'B', 'C', 'D', 'E'],
    width=30,
    height=32,
    num_of_str=1,
    font=30,
    xpan=3,
    ypan=2,
    rotate=15,
    noise_N=0.3,
    noise_Z=2,
    gray_value=255,
    font_family='ヒラギノ角ゴシック W8.ttc'
)
```

You just need to write a loop like `img.save('train_img/{}.png'.format(file_name))` to generate thousands of training images

, and you can obtain the label simply as `name = file_name[0]`.

![frcc2](img/train.png)

### 2024 Update: One-click Generation of Android or iOS Logos

```py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Android
pycapt.generate_android_icon_assets(
    f"{current_dir}/appstore.png", f"{current_dir}/output_directory"
)

# iOS
pycapt.generate_ios_icon_assets(
    f"{current_dir}/appstore.png",
    f"{current_dir}/Assets.xcassets/AppIcon.appiconset",
)
```

The second parameter is your icon output directory, which will be created by default if it doesn't exist.

## Conclusion

Theoretically, as long as you use pycapt to process images, call various methods, and use the `easy_train_img` method, you can solve 90% of CAPTCHA processing and generation problems. Feel free to star, PR, and submit issues. If you want to learn more about the underlying principles, click [here](https://www.yuque.com/zhiwa/deepin/og0te8). I look forward to hearing your thoughts or PR.

### Small Donations

If you found this helpful, [buy me a cup of tea](https://www.yuque.com/zhiwa/deepin/hwnhg0)~
