import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    """
    Initialize Perceptron with inputs and output pairs. Set Weights to random values
    """
    def __init__(self,x,y):
        self.ntrain = x.shape[0]
        self.dim = x.shape[1]
        self.x = x
        self.y = y
        #self.w = np.random.random((self.dim,1))
        self.w = np.random.random((self.dim))
        #self.w = np.array([1.0,1.0,1.0])

    """
        Function that plots the boundary between datapoints in x. If provided a set of Weights,
        will plot all of them on the same graph with different points provided.
    """
    def plotBoundary(self, w = [], type = 'r--', labels = []):
        a = self.x[:,0]
        b = self.x[:,1]
        vals = {1:'+',-1:'<'}
        for i in xrange(len(self.x)):
            #print str(self.x[i][0])+ ' ' + str(self.x[i][1])
            plt.scatter(self.x[i][0],self.x[i][1],marker=vals[self.y[i]])
        x = np.linspace(0, 10, 10)
        if w == []:
            y = -1*(self.w[0]/self.w[1])*x - (self.w[2]/self.w[1])
            plt.plot(x,y ,type)
        else:
            type = ["r--","b--","g--","b-."]
            for i in xrange(0,len(w)):
                y = -1*(w[i][0]/w[i][1])*x - (w[i][2]/w[i][1])
                plt.plot(x,y ,type[i],label=labels[i])
            plt.legend(bbox_to_anchor=(0.5, 1), loc=2, borderaxespad=0.)
        #print y

        plt.show()

    """
        This method inverts the input points for points belonging to the second class.
    """
    def processInput(self):
        self.x[self.y < 0] = -1*self.x[self.y < 0]

    """
    Train a single perceptron with single sample training with the margin specified.
    """
    def train(self,a = 1, b = 0):
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
        #self.plotBoundary()
        #print self.w
        return self.w

    """
    Train a single perceptron with relaxation
    """
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
        #print k
        self.processInput()
        #self.plotBoundary()
        #print self.w
        return self.w

    """
    LMS procedure implemented for a given learning rate and margin
    """
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
        #print self.w
        return self.w

if __name__ == '__main__':
    x = np.array([[2, 7, 1], [8, 1, 1], [7, 5, 1], [6, 3, 1],[7, 8, 1],[5, 9, 1],[4, 5,1],[4, 2, 1],[-1, -1,1],[1, 3,1], [3, -2,1], [5, 4,1], [2, 4,1],[7, 1, 1]])
    y = np.array([1, 1, 1, 1, 1, 1, 1,-1, -1, -1, -1, -1, -1,-1])
    p = Perceptron(x,y)
    #p.plotBoundary()
    #w = [[ 0.5 ,  0.55, -4.5 ],[  3.2 ,   3.35, -27.9 ],[  2.685  ,   2.68375, -23.15   ],[  2. ,   1.9, -16.7]]
    #labels = ["Single-sample","Single-sample(margin)", "Relaxation(margin)","LMS"]
    #w.append(p.train(0.1,0))
    #w.append(p.train(0.1,1))
    #w.append(p.trainRelaxation(0.005,1))
    #w.append(p.trainLMS(0.1,1))
    p.trainLMS(0.1,1)
    #p.plotBoundary(w,labels=labels)
