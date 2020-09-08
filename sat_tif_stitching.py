# 将分割后的遥感影像小图片拼接成原来的大图
# 小图是8位三波段的tif图,融合前后都带有地理坐标信息
# 如果小图是16位或者单波段需要修改代码
# 代码参考:https://www.pythonf.cn/read/6926
import os
from glob import glob
from osgeo import gdal

# 小图片所在文件夹
small_images_path = 'G:\\llx_test3\\'
# 小图片的宽和高
small_image_width = 512
small_image_height = 512
# 大图的宽高各有几个小图
width_num = 10
height_num = 10
# 输出文件夹
output_path = 'G:\\llx_test3_\\sat.tif'

# 如果存在同名影像则先删除
if os.path.exists(output_path):
    os.remove(output_path)
# 获取所有的小图路径
in_files = glob(small_images_path + "*.tif")
# print(in_files)

# 新建一幅大图
driver = gdal.GetDriverByName('GTiff')
columns = small_image_width * width_num
rows = small_image_height * height_num
read_information = gdal.Open(in_files[0])  # 读取一张获取信息
information_band = read_information.GetRasterBand(1)
# print(information_band.DataType)
# print(gdal.GDT_Byte, gdal.GDT_UInt16)  # 8位的图和16位的图 1 2
out_tif = driver.Create(output_path, columns, rows, 3, information_band.DataType)
information_geotrans = read_information.GetGeoTransform()  # 图像的坐标和分辨率信息等
information_proj = read_information.GetProjection()  # 图像的投影信息
out_tif.SetProjection(information_proj)  # 给大图设置投影信息
out_tif.SetGeoTransform(information_geotrans)  #

# 定义仿射逆变换
inv_geotrans = gdal.InvGeoTransform(information_geotrans)
for i, small_sat in enumerate(in_files):
    in_ds = gdal.Open(small_sat)
    in_gt = in_ds.GetGeoTransform()
    offset = gdal.ApplyGeoTransform(inv_geotrans, in_gt[0], in_gt[3])
    x, y = map(int, offset)  # x，y是开始写入时左上角像元行列号
    data = in_ds.ReadAsArray()
    # print('data.shape:', data.shape)  # (3, 512, 512)
    for k in range(3):  # 将三个波段依次写入大图对应位置
        out_tif.GetRasterBand(k + 1).WriteArray(data[k], x, y)
    # out_tif.WriteArray(data, x, y)
    print(f'第{i+1}张图完成')
    del in_ds
