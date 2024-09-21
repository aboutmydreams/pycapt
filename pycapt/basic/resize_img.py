from PIL import Image
import os


def resize_and_save_image(image_path, size, output_path):
    """根据给定的尺寸调整图片大小并保存到指定路径。"""
    try:
        original_image = Image.open(image_path)
        resized_image = original_image.resize(size, Image.LANCZOS)

        # 确保输出路径存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        resized_image.save(output_path)
        print(f"Saved resized image to: {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")


# 示例调用
if __name__ == "__main__":
    # 输入的图片路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = f"{current_dir}/appstore.png"  # 请替换为你的图片路径
    size = (100, 100)  # 目标尺寸
    output_path = f"{current_dir}/resized_image.png"  # 输出路径

    resize_and_save_image(image_path, size, output_path)
