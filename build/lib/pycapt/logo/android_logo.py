import os
from PIL import Image


def generate_android_icon_assets(image_path, output_path="res"):
    # 定义目标文件夹和尺寸
    mipmap_sizes = {
        "mipmap-mdpi": (48, 48),  # 基准
        "mipmap-hdpi": (72, 72),  # 1.5x
        "mipmap-xhdpi": (96, 96),  # 2.0x
        "mipmap-xxhdpi": (144, 144),  # 3.0x
        "mipmap-xxxhdpi": (192, 192),  # 4.0x
        "mipmap-xxxxhdpi": (240, 240),  # 5.0x
        "mipmap-xxxxxhdpi": (384, 384),  # 6.0x
    }

    # 打开原始图片
    try:
        original_image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # 创建基文件夹
    os.makedirs(output_path, exist_ok=True)

    # 生成各个 mipmap 文件夹和缩放图片
    for folder, size in mipmap_sizes.items():
        folder_path = os.path.join(output_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        # 重新调整图片大小
        resized_image = original_image.resize(size, Image.LANCZOS)
        resized_image_path = os.path.join(folder_path, os.path.basename(image_path))

        # 保存调整后的图片
        resized_image.save(resized_image_path)
        print(f"Saved resized image to: {resized_image_path}")


# 示例调用
if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_android_icon_assets(
        f"{current_dir}/appstore.png", f"{current_dir}/output_directory"
    )
