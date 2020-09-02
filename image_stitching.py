# 将分割后的小图片拼接成原来的大图
import cv2
from glob import glob
import numpy as np

# 小图片所在文件夹
small_images_path = 'G:\\llx_test2\\'
# 小图片的宽和高
small_image_width = 512
small_image_height = 512
# 大图的宽高各有几个小图
width_num = 6
height_num = 3
# 输出文件夹
output_path = 'G:\\llx_test2_\\test.png'
output_path_ = 'G:\\llx_test2_\\truth.png'

# 创建一个大图大小的零张量
big_image = np.zeros((small_image_height*height_num, small_image_width*width_num, 3), np.uint8)
big_image_ = np.zeros((small_image_height*height_num, small_image_width*width_num, 3), np.uint8)
# 获取小图列表
small_images_list = sorted(glob(small_images_path + '*.png'))
print(small_images_list)
for i, small_image_path in enumerate(small_images_list):
    if i % 2 == 0:  # 测试结果
        row = i // 2 // width_num
        col = i // 2 % width_num
        print(i, row, col, small_image_path)
        small_image = cv2.imread(small_image_path, 1)
        big_image[row * small_image_height:(row + 1) * small_image_height, col * small_image_width:(col + 1) * small_image_width, :] = small_image
    else:  # groundtruth
        row = i // 2 // width_num
        col = i // 2 % width_num
        print(i, row, col, small_image_path)
        small_image = cv2.imread(small_image_path, 1)
        big_image_[row * small_image_height:(row + 1) * small_image_height, col * small_image_width:(col + 1) * small_image_width, :] = small_image
cv2.imwrite(output_path, big_image)
cv2.imwrite(output_path_, big_image_)
