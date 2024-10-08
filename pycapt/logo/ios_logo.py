import os
from pycapt.basic.resize_img import resize_and_save_image


def generate_ios_icon_assets(
    image_path, output_path="Assets.xcassets/AppIcon.appiconset"
):
    # 定义所需的图片尺寸和文件名
    icon_sizes = {
        "100.png": (100, 100),
        "102.png": (102, 102),
        "1024.png": (1024, 1024),
        "114.png": (114, 114),
        "120.png": (120, 120),
        "128.png": (128, 128),
        "144.png": (144, 144),
        "152.png": (152, 152),
        "16.png": (16, 16),
        "167.png": (167, 167),
        "172.png": (172, 172),
        "180.png": (180, 180),
        "196.png": (196, 196),
        "20.png": (20, 20),
        "216.png": (216, 216),
        "256.png": (256, 256),
        "29.png": (29, 29),
        "32.png": (32, 32),
        "40.png": (40, 40),
        "48.png": (48, 48),
        "50.png": (50, 50),
        "512.png": (512, 512),
        "55.png": (55, 55),
        "57.png": (57, 57),
        "58.png": (58, 58),
        "60.png": (60, 60),
        "64.png": (64, 64),
        "66.png": (66, 66),
        "72.png": (72, 72),
        "76.png": (76, 76),
        "80.png": (80, 80),
        "87.png": (87, 87),
        "88.png": (88, 88),
        "92.png": (92, 92),
    }

    # 创建输出目录
    os.makedirs(output_path, exist_ok=True)

    # 生成每个图标
    for filename, size in icon_sizes.items():
        resized_image_path = os.path.join(output_path, filename)

        resize_and_save_image(
            image_path=image_path, size=size, output_path=resized_image_path
        )
        # resized_image = generate_resized_image(image_path, size)
        # resized_image_path = os.path.join(output_path, filename)
        # resized_image.save(resized_image_path)
        # print(f"Saved resized image to: {resized_image_path}")

    # 创建 Contents.json
    create_contents_json(output_path)


def create_contents_json(output_path):
    """创建 Contents.json 文件。"""
    contents = {
        "images": [
            {
                "size": "60x60",
                "expected-size": "180",
                "filename": "180.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "3x",
            },
            {
                "size": "40x40",
                "expected-size": "80",
                "filename": "80.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "2x",
            },
            {
                "size": "40x40",
                "expected-size": "120",
                "filename": "120.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "3x",
            },
            {
                "size": "60x60",
                "expected-size": "120",
                "filename": "120.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "2x",
            },
            {
                "size": "57x57",
                "expected-size": "57",
                "filename": "57.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "1x",
            },
            {
                "size": "29x29",
                "expected-size": "58",
                "filename": "58.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "2x",
            },
            {
                "size": "29x29",
                "expected-size": "29",
                "filename": "29.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "1x",
            },
            {
                "size": "29x29",
                "expected-size": "87",
                "filename": "87.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "3x",
            },
            {
                "size": "57x57",
                "expected-size": "114",
                "filename": "114.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "2x",
            },
            {
                "size": "20x20",
                "expected-size": "40",
                "filename": "40.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "2x",
            },
            {
                "size": "20x20",
                "expected-size": "60",
                "filename": "60.png",
                "folder": output_path + "/",
                "idiom": "iphone",
                "scale": "3x",
            },
            {
                "size": "1024x1024",
                "filename": "1024.png",
                "expected-size": "1024",
                "idiom": "ios-marketing",
                "folder": output_path + "/",
                "scale": "1x",
            },
            {
                "size": "40x40",
                "expected-size": "80",
                "filename": "80.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "72x72",
                "expected-size": "72",
                "filename": "72.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "76x76",
                "expected-size": "152",
                "filename": "152.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "50x50",
                "expected-size": "100",
                "filename": "100.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "29x29",
                "expected-size": "58",
                "filename": "58.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "76x76",
                "expected-size": "76",
                "filename": "76.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "29x29",
                "expected-size": "29",
                "filename": "29.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "50x50",
                "expected-size": "50",
                "filename": "50.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "72x72",
                "expected-size": "144",
                "filename": "144.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "40x40",
                "expected-size": "40",
                "filename": "40.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "83.5x83.5",
                "expected-size": "167",
                "filename": "167.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "size": "20x20",
                "expected-size": "20",
                "filename": "20.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "1x",
            },
            {
                "size": "20x20",
                "expected-size": "40",
                "filename": "40.png",
                "folder": output_path + "/",
                "idiom": "ipad",
                "scale": "2x",
            },
            {
                "idiom": "watch",
                "filename": "172.png",
                "folder": output_path + "/",
                "subtype": "38mm",
                "scale": "2x",
                "size": "86x86",
                "expected-size": "172",
                "role": "quickLook",
            },
            {
                "idiom": "watch",
                "filename": "80.png",
                "folder": output_path + "/",
                "subtype": "38mm",
                "scale": "2x",
                "size": "40x40",
                "expected-size": "80",
                "role": "appLauncher",
            },
            {
                "idiom": "watch",
                "filename": "88.png",
                "folder": output_path + "/",
                "subtype": "40mm",
                "scale": "2x",
                "size": "44x44",
                "expected-size": "88",
                "role": "appLauncher",
            },
            {
                "idiom": "watch",
                "filename": "102.png",
                "folder": output_path + "/",
                "subtype": "41mm",
                "scale": "2x",
                "size": "45x45",
                "expected-size": "102",
                "role": "appLauncher",
            },
            {
                "idiom": "watch",
                "filename": "92.png",
                "folder": output_path + "/",
                "subtype": "41mm",
                "scale": "2x",
                "size": "46x46",
                "expected-size": "92",
                "role": "appLauncher",
            },
            {
                "idiom": "watch",
                "filename": "100.png",
                "folder": output_path + "/",
                "subtype": "44mm",
                "scale": "2x",
                "size": "50x50",
                "expected-size": "100",
                "role": "appLauncher",
            },
            {
                "idiom": "watch",
                "filename": "196.png",
                "folder": output_path + "/",
                "subtype": "42mm",
                "scale": "2x",
                "size": "98x98",
                "expected-size": "196",
                "role": "quickLook",
            },
            {
                "idiom": "watch",
                "filename": "216.png",
                "folder": output_path + "/",
                "subtype": "44mm",
                "scale": "2x",
                "size": "108x108",
                "expected-size": "216",
                "role": "quickLook",
            },
            {
                "idiom": "watch",
                "filename": "48.png",
                "folder": output_path + "/",
                "subtype": "38mm",
                "scale": "2x",
                "size": "24x24",
                "expected-size": "48",
                "role": "notificationCenter",
            },
            {
                "idiom": "watch",
                "filename": "55.png",
                "folder": output_path + "/",
                "subtype": "42mm",
                "scale": "2x",
                "size": "27.5x27.5",
                "expected-size": "55",
                "role": "notificationCenter",
            },
            {
                "idiom": "watch",
                "filename": "66.png",
                "folder": output_path + "/",
                "subtype": "45mm",
                "scale": "2x",
                "size": "33x33",
                "expected-size": "66",
                "role": "notificationCenter",
            },
            {
                "size": "29x29",
                "expected-size": "87",
                "filename": "87.png",
                "folder": output_path + "/",
                "idiom": "watch",
                "role": "companionSettings",
                "scale": "3x",
            },
            {
                "size": "29x29",
                "expected-size": "58",
                "filename": "58.png",
                "folder": output_path + "/",
                "idiom": "watch",
                "role": "companionSettings",
                "scale": "2x",
            },
            {
                "size": "1024x1024",
                "expected-size": "1024",
                "filename": "1024.png",
                "folder": output_path + "/",
                "idiom": "watch-marketing",
                "scale": "1x",
            },
            {
                "size": "128x128",
                "expected-size": "128",
                "filename": "128.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "1x",
            },
            {
                "size": "256x256",
                "expected-size": "256",
                "filename": "256.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "1x",
            },
            {
                "size": "128x128",
                "expected-size": "256",
                "filename": "256.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "2x",
            },
            {
                "size": "256x256",
                "expected-size": "512",
                "filename": "512.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "2x",
            },
            {
                "size": "32x32",
                "expected-size": "32",
                "filename": "32.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "1x",
            },
            {
                "size": "512x512",
                "expected-size": "512",
                "filename": "512.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "1x",
            },
            {
                "size": "16x16",
                "expected-size": "16",
                "filename": "16.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "1x",
            },
            {
                "size": "16x16",
                "expected-size": "32",
                "filename": "32.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "2x",
            },
            {
                "size": "32x32",
                "expected-size": "64",
                "filename": "64.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "2x",
            },
            {
                "size": "512x512",
                "expected-size": "1024",
                "filename": "1024.png",
                "folder": output_path + "/",
                "idiom": "mac",
                "scale": "2x",
            },
        ]
    }

    # 写入 Contents.json 文件
    json_path = os.path.join(output_path, "Contents.json")
    with open(json_path, "w") as json_file:
        import json

        json.dump(contents, json_file, indent=4)
        print(f"Created Contents.json at: {json_path}")


# 示例调用
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_ios_icon_assets(
        f"{current_dir}/appstore.png",
        f"{current_dir}/Assets.xcassets/AppIcon.appiconset",
    )
