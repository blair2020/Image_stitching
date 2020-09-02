# 将多个图像排成列合成一幅图

import cv2
import numpy as np
img1_path = 'G:\\llx_test2_\\sat.tif'
img2_path = 'G:\\llx_test2_\\truth.png'
img3_path = 'G:\\llx_test2_\\test.png'
img1 = cv2.imread(img1_path, 1)
img2 = cv2.imread(img2_path, 1)
img3 = cv2.imread(img3_path, 1)
images_column = np.concatenate([img1, img2, img3], 0)  # 0是轴
cv2.imwrite('G:\\llx_test2_\\images_column.png', images_column)

