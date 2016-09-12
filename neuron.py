import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

class Neuron:
    def __init__(self, dim, learning_rate = 0.01):
        self.w = np.random.random((dim))
        self.learning_rate = learning_rate

    def sum_value(self, x):
        # print self.w
        # print x
        # print self.w*x
        # print np.sum(self.w*x)
        # print '-------------'
        return np.sum(self.w*x)

    def out_value(self,x):
        return sigmoid(self.sum_value(x))

    def update_weight_hidden(self,x,t,y ):
        for i in xrange(len(self.w)):
            self.w[i] = self.w[i] - self.learning_rate*(y - t)*y*(1 - y)*x[i]

    def update_weight_input(self,x,t,y,h,neurons_hidden):
        for i in xrange(len(self.w)):
            #self.w[i] = self.w[i] - self.learning_rate*(y - t)*y*(1 - y)*x[i]
            joint_contribution = 0
            for j in xrange(len(t)):
                joint_contribution += (y[j] - t[j])*y[j]*h[i]*(1-h[i])*x[i]
