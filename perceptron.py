import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self,x,y):
        self.ntrain = x.shape[0]
        self.dim = x.shape[1]
        self.x = x
        self.y = y
        #self.w = np.random.random((self.dim,1))
        #print self.w.shape
        self.w = np.random.random((self.dim))
        #self.w = np.array([1,1,1])

    def plotBoundary(self):
        a = self.x[:,0]
        b = self.x[:,1]
        vals = {1:'+',-1:'<'}
        for i in xrange(len(self.x)):
            #print str(self.x[i][0])+ ' ' + str(self.x[i][1])
            plt.scatter(self.x[i][0],self.x[i][1],marker=vals[self.y[i]])
        x = np.linspace(-10, 10, 10)
        y = -1*(self.w[0]/self.w[1])*x - (1/self.w[1])
        #print y
        plt.plot(x,y,c='r')
        plt.show()

    def train(self):
        # out =  np.abs(np.sign(np.sum(self.w.transpose()*self.x,axis=1)) - self.y)
        # val = np.sum(out)
        # #print self.w
        # k = 0
        # while val > 0:
        #     for i in xrange(len(out)):
        #         #self.w = (self.w.transpose() + self.x[i]).transpose()
        #         if out[i] > 0:
        #             self.w[0] += self.x[i,0]
        #             self.w[1] += self.x[i,1]
        #             self.w[2] += self.x[i,2]
        #     #print self.w
        #     #print np.sign(np.sum(self.w.transpose()*self.x,axis=1))
        #     print out
        #     out =  np.abs(np.sign(np.sum(self.w.transpose()*self.x,axis=1)) - self.y)
        #     val = np.sum(out)
        # self.plotBoundary()
        e = 1
        k = 0
        while e > 0:
            e = 0
            k += 1
            for i in xrange(len(self.x)):
                val = np.sum(self.w*self.x[i])
                if val < 0:
                    self.w[0] += self.x[i,0]
                    self.w[1] += self.x[i,1]
                    self.w[2] += self.x[i,2]
                    e += 1
        print k
        self.plotBoundary()

if __name__ == '__main__':
    x = np.array([[2, 7, 1], [8, 1, 1], [7, 5, 1], [6, 3, 1],[7, 8, 1],[5, 9, 1],[4, 5,1],[-4, -2, -1],[1, 1,-1],[-1, -3,-1], [-3, 2,-1], [-5, -3.25,-1], [-2, -4,-1],[-7, -1, -1]])
    y = np.array([1, 1, 1, 1, 1, 1, 1,-1, -1, -1, -1, -1, -1,-1])
    p = Perceptron(x,y)
    #p.plotBoundary()
    p.train()
