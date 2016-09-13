import numpy as np
import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

class Neuron:
    def __init__(self, dim, learning_rate = 0.1):
        self.w = -1+2*np.random.random((dim+1))
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
        # print self.w
        # print x
        #print self.sum_value(x)
        self.y = sigmoid(self.sum_value(x))
        # print self.y
        # print '========'
        return self.y

    def update_weight_hidden(self,x,t):
        delta_k = (self.y - t)*self.y*(1 - self.y)
        for i in xrange(len(self.w)):
            self.w[i] = self.w[i] - self.learning_rate*delta_k*x[i]

        # print 'UPDATED_HIDDEN'
        # print self.y
        # print t
        # print delta_k
        # print self.w
        # print 'xxxxxxxxxxxxxxxx'
        return delta_k

    def calculate_error(self,t):
        return (0.5*(self.y - t)**2)

    def update_weight_input(self,x,neuron_hidden,hidden_idx, neuron_out,delta_k):
        val = 0
        for n in xrange(len(neuron_out)):
            val += delta_k[n]*neuron_out[n].w[hidden_idx]
            # print delta_k[n]
            # print neuron_out[n].w[hidden_idx]
            # print '-----------------------'

        # print 'UPDATE_OUT'
        # print val
        # print '----------------'
        for i in xrange(len(self.w)):
            # print self.y*(1-self.y)*x[i]
            self.w[i] = self.w[i] - self.learning_rate*val*self.y*(1-self.y)*x[i]

        # print self.w
        # print 'yyyyyyyyyyyyyyyyyyyyyy'
