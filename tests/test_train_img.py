import os
import unittest
from PIL import Image
import pycapt


class TestCaptcha(unittest.TestCase):
    def setUp(self):
        self.image_path = "test_captcha.png"
        self.train_image_path = "train_captcha.png"

    def tearDown(self):
        # Remove any generated images after tests
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        if os.path.exists(self.train_image_path):
            os.remove(self.train_image_path)

    def test_generate_captcha_image(self):
        # Generate a CAPTCHA image
        name, img = pycapt.do_captcha(
            my_str_list=["A", "B", "C", "D", "1", "2", "3"],
            width=160,
            height=40,
            num_of_str=4,
            font=30,
            gray_value=255,
            font_family="ヒラギノ角ゴシック W8.ttc",
        )
        img.save(self.image_path)  # Save the generated image

        # Check if the image file is created
        self.assertTrue(
            os.path.exists(self.image_path),
            "result fail: expected CAPTCHA image not created",
        )

        # Verify the image can be opened
        with Image.open(self.image_path) as opened_img:
            self.assertEqual(
                opened_img.size,
                (160, 40),
                "result fail: expected image size does not match",
            )

    def test_generate_training_image(self):
        # Generate a training CAPTCHA image
        file_name, img = pycapt.easy_train_img(
            my_str_list=["1", "2", "A", "B", "C"],
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
            font_family="ヒラギノ角ゴシック W8.ttc",
        )
        img.save(self.train_image_path)  # Save the generated training image

        # Check if the training image file is created
        self.assertTrue(
            os.path.exists(self.train_image_path),
            "result fail: expected training image not created",
        )

        # Verify the training image can be opened
        with Image.open(self.train_image_path) as opened_img:
            self.assertEqual(
                opened_img.size,
                (30, 32),
                "result fail: expected training image size does not match",
            )


if __name__ == "__main__":
    unittest.main()
