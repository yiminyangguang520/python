#!/usr/bin/python
#  coding=utf-8
from pylab import *
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()
# 获取datasets里的数据

images_and_labels = list(zip(digits.images, digits.target))
# 将数据从两个数组合并为一个数组,每个元素分别为(image,target)

n_samples = len(digits.images)
# 获取数据个数    1797个
data = digits.images.reshape((n_samples, -1))
# 将图片变为一维数组

classifier = svm.SVC(gamma=0.001)
# 创建一个svm

classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])
# 将data的前半部分输入到训练集中进行匹配

expected = digits.target[n_samples / 2:]
# 提取后半部分数据的期望值
predicted = classifier.predict(data[n_samples / 2:])
# 利用svm计算后半部分的预测值

print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
# 输出预测值和实际值之间的误差

images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
# 列出后半部分图片和它们的预测值

gray()
for i, (image, prediction) in enumerate(images_and_predictions[:15]):
    subplot(3, 5, i + 1)
    imshow(image)
    axis('off')
    title(str(prediction))

show()
