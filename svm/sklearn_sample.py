# coding=utf-8
from pylab import *
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))
gray()
for i, (image, label) in enumerate(images_and_labels[:10]):
    subplot(2, 5, i+1)
    imshow(images_and_labels[i][0], cmap=plt.cm.gray_r, interpolation='nearest')
    axis('off')
    title(images_and_labels[i][1])
show()
