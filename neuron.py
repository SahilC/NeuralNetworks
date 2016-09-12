import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

class Neuron:
    def __init__(self, dim, learning_rate = 0.01):
        self.w = np.random.random((dim))
        self.learning_rate = learning_rate
        self.y = 0

    def sum_value(self, x):
        # print self.w
        # print x
        # print self.w*x
        # print np.sum(self.w*x)
        # print '-------------'
        return np.sum(self.w*x)

    def out_value(self,x):
        self.y = sigmoid(self.sum_value(x))
        return self.y

    def update_weight_hidden(self,x,t):
        delta_k = (self.y - t)*self.y*(1 - self.y)
        for i in xrange(len(self.w)):
            self.w[i] = self.w[i] - self.learning_rate*delta_k*x[i]
        return delta_k

    def update_weight_input(self,x, h, neuron_out,delta_k):
        val = 0
        for n in xrange(len(neuron_out)):
            val += np.sum(delta_k[n]*neuron_out[n].w)

        for i in xrange(len(self.w)):
            self.w[i] = self.w[i] - self.learning_rate*delta_k*x[i]
