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
        #self.w = np.random.random((self.dim))
        self.w = np.array([1.0,1.0,1.0])

    def plotBoundary(self):
        a = self.x[:,0]
        b = self.x[:,1]
        vals = {1:'+',-1:'<'}
        for i in xrange(len(self.x)):
            #print str(self.x[i][0])+ ' ' + str(self.x[i][1])
            plt.scatter(self.x[i][0],self.x[i][1],marker=vals[self.y[i]])
        x = np.linspace(0, 10, 10)
        y = -1*(self.w[0]/self.w[1])*x - (self.w[2]/self.w[1])
        #print y
        plt.plot(x,y,'r--')
        plt.show()

    def processInput(self):
        self.x[self.y < 0] = -1*self.x[self.y < 0]

    #Train a single perceptron with single sample training
    def train(self,a = 1, b = 0):
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
        self.processInput()
        e = 1
        k = 0
        while e > 0:
            e = 0
            k += 1
            for i in xrange(len(self.x)):
                val = np.sum(self.w*self.x[i])
                if val < b:
                    self.w[0] += a*self.x[i,0]
                    self.w[1] += a*self.x[i,1]
                    self.w[2] += a*self.x[i,2]
                    e += 1
        #print k
        self.processInput()
        self.plotBoundary()

    #Train a single perceptron with relaxation
    def trainRelaxation(self,a = 1, b = 0 ):
        self.processInput()
        e = 1
        k = 0
        while e > 0:
            k += 1
            e = 0
            for i in xrange(len(self.x)):
                val = np.sum(self.w*self.x[i])
                #self.plotBoundary()
                #print val
                if val < b:
                    sumVal = np.sum(self.x[i]**2)
                    update = (b - val)/sumVal
                    #print update
                    self.w[0] += a*self.x[i,0]
                    self.w[1] += a*self.x[i,1]
                    self.w[2] += a*self.x[i,2]
                    e += 1
        print k
        self.processInput()
        self.plotBoundary()

    def trainLMS(self,a = 1,b = 0):
        self.processInput()
        e = 1
        k = 0
        eta = a
        while k < 1000:
            k += 1
            for i in xrange(len(self.x)):
                val = np.sum(self.w*self.x[i])
                if ((b - val) < 0.5):
                    update = 0
                else:
                    update = 1
                self.w += eta*update*self.x[i]
        self.processInput()
        print self.w
        self.plotBoundary()
        return

if __name__ == '__main__':
    x = np.array([[2, 7, 1], [8, 1, 1], [7, 5, 1], [6, 3, 1],[7, 8, 1],[5, 9, 1],[4, 5,1],[4, 2, 1],[-1, -1,1],[1, 3,1], [3, -2,1], [5, 3.25,1], [2, 4,1],[7, 1, 1]])
    y = np.array([1, 1, 1, 1, 1, 1, 1,-1, -1, -1, -1, -1, -1,-1])
    p = Perceptron(x,y)
    #p.plotBoundary()
    #p.trainRelaxation(0.005,1)
    p.trainLMS(0.1,1)
