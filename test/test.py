__author__ = 'yangpeiwen'
from threading import Thread
from time import sleep

table = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90, 0x88, 0x83, 0xc6, 0xa1, 0x86, 0x8e]

number = '1'


def dis():
    i = 1
    global number
    while True:
        i += 1
        number = str(i)


def asd():
    global number
    while True:
        print number
        sleep(0.01)

t = Thread(target=asd)
t.setDaemon(True)
t.start()
dis()