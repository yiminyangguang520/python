#!/usr/bin/python
#coding: utf-8


from pybrain.structure import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet

n = FeedForwardNetwork()
inLayer = LinearLayer(2)
hiddenLayer = TanhLayer(3)
outLayer = LinearLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()

def out():
    print "网络:",n
    print "输入(1,1):",n.activate((1, 1))
    print "输入层:",in_to_hidden.params
    print "隐藏层:",hidden_to_out.params

def test():
    print("测试结果:")
    print n.activate([0,0])
    print n.activate([0,1])
    print n.activate([1,0])
    print n.activate([1,1])


ds = SupervisedDataSet(2, 1)

ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

print ds

trainer = BackpropTrainer(n,ds)
print trainer.trainEpochs(1000)

test()
