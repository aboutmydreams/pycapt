name = "pycapt"

# 从 pycapt 中导入相关模块和函数
from .solve_it.easy_solve import (  # noqa: E402
    get_modes as get_modes,
    mode_img as mode_img,
    two_value as two_value,
    mode_white_img as mode_white_img,
    dele_noise as dele_noise,
    dele_line as dele_line,
    clear_train_img as clear_train_img,
    clear_lib_line as clear_lib_line,
    cut_img_to_mode_list as cut_img_to_mode_list,
    cut_img_to_img_list as cut_img_to_img_list,
    rectify_img as rectify_img,
    rectify_mode as rectify_mode,
    tran_90 as tran_90,
    get_small_img as get_small_img,
)

from .make_captcha.easy_mode import (  # noqa: E402
    show_noise_mode as show_noise_mode,
    show_noise_img as show_noise_img,
    mode_pan as mode_pan,
    easy_train_img as easy_train_img,
    get_train_img as get_train_img,
    img_pan as img_pan,
    train_img as train_img,
    do_captcha as do_captcha,
    more_noise as more_noise,
    get_mode as get_mode,
)

from .logo.android_logo import (  # noqa: E402
    generate_android_icon_assets as generate_android_icon_assets,
)


from .logo.ios_logo import (  # noqa: E402
    generate_ios_icon_assets as generate_ios_icon_assets,
)

from .basic.resize_img import resize_and_save_image as resize_and_save_image  # noqa: E402
