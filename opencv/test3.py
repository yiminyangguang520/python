# coding: utf-8

import cv2
import cv2.cv as cv
import PIL.Image as Image
import StringIO
import socket

capture = cv2.VideoCapture(-1)
capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = capture.read()   # 从摄像头读取图片
    image = Image.fromarray(img)    # 将图片转为Image对象
    buf = StringIO.StringIO()   # 生成StringIO对象
    image.save(buf, format="JPEG")  # 将图片以JPEG格式写入StringIO
    jpeg = buf.getvalue()   # 获取JPEG图片内容
    buf.close()     # 关闭StringIO
    print len(jpeg)
    cv2.imshow('Video', img)
    key = cv2.waitKey(30)
    if key == 32:
        break

capture.release()
