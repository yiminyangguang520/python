__author__ = 'ypw'

a = """
作品名称：IMU
制作时间:2015年3月
制作意图:可以采集加速度，角速度，磁场强度，GPS信息，以及解算出来的欧拉角等。用于研究人走路的姿态／小车的导航。
开源地址:https://github.com/ypwhs/Acceleration
iOS：https://github.com/ypwhs/Acceleration-iOS
Arduino：https://github.com/ypwhs/arduino/tree/master/mpuarduino
processing:https://github.com/ypwhs/processing/tree/master/serial-box
"""

a = a.replace("：", ":")

c = ""
i = 0
for b in a.split("\n"):

    d = b.find(':')
    if d > 0:
        i += 1
        if b[d + 1:].find("ttp") > 0:
            f = "[" + b[d + 1:] + "]" + "(" + b[d + 1:] + ")"
        else:
            f = b[d + 1:]
        if b.find("作品") >= 0:
            c = c + "###" + b[d + 1:] + "\n\n"
        c += " " + b[0:d] + "\t| " + f + "\n"
    if i == 1:
        c += " ---- | ---- \n"
print c