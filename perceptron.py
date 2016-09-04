import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self,x,y):
        self.ntrain = x.shape[0]
        self.dim = x.shape[1]
        self.x = x
        self.y = y
        self.w = np.random.random((self.dim,1))

    def plotBoundary(self):
        a = self.x[:,0]
        b = self.x[:,1]
        vals = {1:'+',-1:'<'}
        for i in xrange(len(x)):
            plt.scatter(self.x[i][0],self.x[i][1],marker=vals[self.y[i]])
        plt.show()

    def train(self):
        pass


if __name__ == '__main__':
    x = np.array([[2, 7], [8, 1], [7, 5], [6, 3],[7, 8],[5, 9],[4, 5],[4, 2],[-1, -1],[1, 3], [3, -2], [5, 3.25], [2, 4],[7, 1]])
    y = np.array([1, 1, 1, 1, 1, 1, 1,-1, -1, -1, -1, -1, -1,-1])
    p = Perceptron(x,y)
    p.plotBoundary()
