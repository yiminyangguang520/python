from numpy import *
from sklearn.svm import *
x = array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = array([0, 1, 1, 0])
svc = SVC()
svc.fit(x, y)
print svc.predict([[0, 0], [0, 1], [1, 0], [1, 1]])
print svc.predict([[0.1, 0.2], [0.3, 0.5], [0.6, 0.4], [0.7, 0.8]])