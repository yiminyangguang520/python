# coding: utf-8

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import *
import time

last = time.time()
net = buildNetwork(2, 3, 1, bias=True, hiddenclass=TanhLayer)

ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

for inpt, target in ds:
    print inpt,target
trainer = BackpropTrainer(net, ds)
d=1
while d > 1e-5:
    d = trainer.train()
    # print d

print "结果:"
print net.activate([0, 0])
print net.activate([0, 1])
print net.activate([1, 0])
print net.activate([1, 1])

print time.time() - last

