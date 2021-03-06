#!/usr/bin/python
# coding=utf-8
__author__ = 'yangpeiwen'

from pylab import *
from sklearn import svm

from svm.yzm_my import *


testyzm0 = (
    0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 0, 1, 1, 1, 0,
    0, 0, 1, 1, 0, 0, 0, 1, 1, 1,
    0, 1, 1, 0, 0, 0, 0, 0, 1, 1,
    0, 1, 1, 0, 0, 0, 0, 0, 1, 1,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
    0, 1, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 0, 0, 0, 0, 1, 0, 0, 1, 1,
    0, 1, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 0, 0, 0, 0, 1, 1,
    0, 0, 1, 1, 0, 0, 0, 1, 1, 0,
    0, 0, 1, 1, 0, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
)

testyzm1 = (
    0, 0, 0, 1, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 0, 1, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 0, 1, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 1, 0, 1, 0,
)
testyzm2 = (
    0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
)

testyzm3 = (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 0, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
)

testyzmdata = (testyzm0, testyzm1, testyzm2, testyzm3, yzm4, yzm5, yzm6, yzm7, yzm8, yzm9)

classifier = svm.SVC(gamma=0.00001)
classifier.fit(yzmdata, yzmnumber)
predicted = classifier.predict(testyzmdata)
print classifier
gray()


def out():
    print "测试输出:"
    i = 0
    for testim in testyzmdata:
        subplot(2, 5, i + 1)
        axis('off')
        imshow(array(testim).reshape(13, 10), cmap=plt.cm.gray_r, interpolation='nearest')
        title(predicted[i])
        print i, predicted[i]
        i += 1
    show()


out()