import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

class Neuron:
    def __init__(self, x):
        self.ntrain = x.shape[0]
        self.dim = x.shape[1]
        self.x = x
        self.w = np.random.random((self.dim))

    def sum_value(self):
        print np.sum(self.w*self.x,axis=1)
        return np.sum(self.w*self.x,axis=1)

    def out_value(self):
        return sigmoid(self.sum_value())
