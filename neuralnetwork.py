from neuron import Neuron
import numpy as np

if __name__ == '__main__':
    x = np.array([[2, 7, 1], [8, 1, 1], [7, 5, 1], [6, 3, 1],[7, 8, 1],[5, 9, 1],[4, 5,1],[4, 2, 1],[-1, -1,1],[1, 3,1], [3, -2,1], [5, 3.25,1], [2, 4,1],[7, 1, 1]])
    # y = np.array([1, 1, 1, 1, 1, 1, 1,-1, -1, -1, -1, -1, -1,-1])
    # p = Perceptron(x,y)
    # #p.plotBoundary()
    # #p.trainRelaxation(0.005,1)
    # p.plotBoundary()
    n =  Neuron(x)
    print n.out_value()
