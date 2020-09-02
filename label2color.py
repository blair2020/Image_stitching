from PIL import Image
import numpy as np
from glob import glob
import os

def colorize_mask(mask, palette):
    zero_pad = 256 * 3 - len(palette)
    for i in range(zero_pad):
        palette.append(0)
    new_mask = Image.fromarray(mask.astype(np.uint8)).convert('P')
    new_mask.putpalette(palette)
    return new_mask


# tif2 = np.asarray(Image.open('2.tif'), dtype=np.int32) - 2
LLX_palette = [0, 0, 0, 120, 120, 120, 180, 120, 120, 6, 230, 230, 80, 50, 50, 4, 200,
               3, 120, 120, 80, 140, 140, 140, 204, 5, 255, 230, 230, 230, 4, 250, 7, 224,
               5, 255, 235, 255, 7, 150, 5, 61, 120, 120, 70, 8, 255, 51, 255, 6, 82, 143,
               255, 140, 204, 255, 4, 255, 51, 7, 204, 70, 3, 0, 102, 200, 61, 230, 250, 255,
               6, 51, 11, 102, 255, 255, 7, 71, 255, 9, 224, 9, 7, 230, 220, 220, 220, 255, 9,
               92, 112, 9, 255, 8, 255, 214, 7, 255, 224, 255, 184, 6, 10, 255, 71, 255, 41,
               10, 7, 255, 255, 224, 255, 8, 102, 8, 255, 255, 61, 6, 255, 194, 7]
# colorized_mask = colorize_mask(tif2, LLX_palette)
# colorized_mask.save('2.png')

path = 'G:\\llx_dataset3\\annotations\\training\\'
save_path = 'G:\\llx_test2\\'
image_files = sorted(glob(save_path + '*.tif'))
# image_files = sorted(glob(path + '59_*.tif'))
print(len(image_files))
# print(image_files[1])
# print(os.path.basename(image_files[1])) # 59_101.tif

for sat in image_files:
    # print(sat)
    mask = path + os.path.basename(sat)
    # print(mask)
    new_mask = np.asarray(Image.open(mask), dtype=np.int32) - 1
    colorized_mask = colorize_mask(new_mask, LLX_palette)
    colorized_mask.save(save_path + os.path.basename(mask).split('.')[0] + '_.png')
    print(mask + '_____done!')