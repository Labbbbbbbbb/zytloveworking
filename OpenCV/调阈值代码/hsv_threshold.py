import numpy as np

import cv2

cap = cv2.VideoCapture(1)  
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)   # 设置图像宽度为160
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)  # 设置图像高度为120
cap.set(cv2.CAP_PROP_BRIGHTNESS, 1)     # 设置亮度，范围0-1
cap.set(cv2.CAP_PROP_AUTO_WB, 0)         # 关闭自动白平衡
# 关闭自动曝光（必须关闭才能手动设置）
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)  # 0.25 或 0 表示手动曝光
# 调小曝光值（减少进光量）
cap.set(cv2.CAP_PROP_EXPOSURE, -6)  # 典型范围：-8（最暗）到 -1（较亮），或 0.1~0.001（秒）

# 全局定义段
# 1. 饱和度增强定义
# 调节通道强度
# 线性查找表（保持蓝色通道不变）
lutEqual = np.array([i for i in range(256)]).astype("uint8")

# 增强红色通道的查找表（可调整参数）
lutRaisen_red = np.array([int(50 + 0.8 * i) for i in range(256)]).astype("uint8")  # 增强红色

# 增强绿色通道的查找表（可调整参数）
lutRaisen_green = np.array([int(50 + 0.8 * i) for i in range(256)]).astype("uint8")  # 增强绿色

# 组合成三通道 LUT（R:增强, G:增强, B:不变）
lutSRG = np.dstack((lutRaisen_red, lutRaisen_green, lutEqual))  # 增强红、绿，蓝不变

# 2. 滑动条定义
cv2.namedWindow("TrackBars")


def empty(a):
    pass


cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 0, 255, empty)

#############################
# 运行段
#############################
while cap.isOpened():
    ret, frame = cap.read()
    if ret is True:
        # 图像处理段
        # # 1. 饱和度增强
        hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  # 色彩空间转换, RGB->HSV
        hsv = cv2.LUT(hsv, lutSRG)  # 红绿饱和度增大
        
        # cv2.imshow('hsv', hsv)
        blendSRaisen = cv2.LUT(hsv, lutSRG)             # 饱和度增大
        # 2. 掩膜生成
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(blendSRaisen, lower, upper)
        imgResult = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('result', imgResult)

        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
