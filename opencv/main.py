import cv2
import numpy as np

fn = "./resource/123.jpg"
# 读取图像
img = cv2.imread(fn)
# 图像属性
print("彩色图片的属性：")
print(f"(垂直像素={img.shape[0]},水平像素={img.shape[1]},通道数={img.shape[2]})")
print(f"像素个数={img.size}")
print(f"彩色像素的数据类型={img.dtype}")
# gray = cv2.imread(fn, 0)
# print("灰色图片的属性：")
# print(f"(垂直像素={gray.shape[0]},水平像素={gray.shape[1]})")
# print(f"像素个数={gray.size}")
# print(f"彩色像素的数据类型={gray.dtype}")
px = img[49, 69]
print(f"(B={px[0]},G={px[1]},R={px[2]})")
# 修改(588,400)->(616,428)
for i in range(400, 428):
    for j in range(588, 616):
        img[j, i] = [0, 0, 0]

width = 200  # 宽
height = 400  # 高
# arr = np.zeros((width, height), np.uint8)  # 全黑
# arr = np.ones((width, height), np.uint8) * 255  # 全白
arr = np.random.randint(255, size=(height, width, 3), dtype=np.uint8)  # 随机值
print(arr)

# 水平数组拼接
h = np.hstack((img, img))
# 垂直数组拼接
v = np.vstack((img, img))

# 显示图像
cv2.imshow("invoice", arr)
cv2.imshow("img_h", h)
cv2.imshow("img_v", v)
# 等待按下任意键盘
cv2.waitKey()
# 销毁所有窗口
cv2.destroyAllWindows()
# 保存图片
# cv2.imwrite("new.jpg", img)
