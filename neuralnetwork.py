from neuron import Neuron
from inputprocessor import InputProcessor
import numpy as np

class NeuralNetwork:
    def __init__(self,num_dim,num_hidden,num_out):
        self.num_hidden = num_hidden
        self.num_out = num_out
        self.hidden_layer = [Neuron(num_dim) for i in xrange(num_hidden)]
        self.output_layer = [Neuron(num_hidden) for i in xrange(num_out)]

    def feed_forward(self,x):
        hidden_layer_out = []
        total_error = 0
        for neuron in self.hidden_layer:
            hidden_layer_out.append(neuron.out_value(x))

        output_layer_out = []
        hidden_layer_out.append(1)
        for neuron in self.output_layer:
            h = neuron.out_value(hidden_layer_out)
            output_layer_out.append(h)

        print output_layer_out

    def train(self,input_val,output_val):
        i = 0
        iter = 0
        while iter < 10000:
            iter += 1
            #print iter
            for k in xrange(len(input_val)):
                hidden_layer_out = []
                total_error = 0
                for neuron in self.hidden_layer:
                    #print 'Hidden'+str(iter)
                    hidden_layer_out.append(neuron.out_value(input_val[k]))

                output_layer_out = []
                hidden_layer_out.append(1)
                for neuron in self.output_layer:
                    h = neuron.out_value(hidden_layer_out)
                    output_layer_out.append(h)
                    total_error += neuron.calculate_error(output_val[k])

                print total_error
                delta_k = []
                for neuron in self.output_layer:
                    delta_k.append(neuron.update_weight_hidden(hidden_layer_out,output_val[k]))

                for n in xrange(len(self.hidden_layer)):
                    self.hidden_layer[n].update_weight_input(input_val[k],self.hidden_layer,n,self.output_layer,delta_k)


if __name__ == '__main__':
    ip = InputProcessor('data/optdigits.tra')
    #ip.read_input()
    dataset = ip.read_processed_input()

    #print dataset['input'].shape[1]
    #print np.unique(dataset['output']).shape[0]
    #Credits for this heuristic for number of hidden layer neurons http://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw
    alpha = 2
    nh = dataset['input'].shape[0]/(alpha*(dataset['input'].shape[1]+np.unique(dataset['output']).shape[0]))
    #print (alpha*(dataset['input'].shape[1]+np.unique(dataset['output']).shape[0]))
    #print dataset['input'].shape[0]
    n  = NeuralNetwork(dataset['input'].shape[1]-1, nh ,np.unique(dataset['output']).shape[0])
    # input_val = np.array([[-5],[-1],[1],[6]])
    # output_val = np.array([0,1,1,0])
    #input_val = np.array([[2, 7,1], [8, 1,1], [7, 5,1], [6, 3,1],[7, 8,1],[5, 9,1],[4, 5,1],[4, 2,1],[-1, -1,1],[1, 3,1], [3, -2,1], [5, 3.25,1], [2, 4,1],[7, 1,1]])
    #output_val = np.array([1,1,0,0,1,1,1,1,0,1,1,1,0,1])
    #input_val = np.array([[7,1], [1, 1], [-5,1], [-3,1],[3,1],[-8,1],[5,1],[2,1],[-1,1],[3,1], [-9,1], [3.25,1], [-4,1],[0,1]])
    #input_val = np.array([[1,1,1],[1,0,1],[0,1,1],[0,0,1]])
    #output_val = np.array([0,1,1,0])
    n.train(dataset['input'],dataset['output'])
    #n.feed_forward([0,1,1])
    #n.feed_forward([3,1])
    #n.feed_forward([-2,1])
    #n.feed_forward([7,1])
    #n.feed_forward([5,1])
    #n.feed_forward([-1,1])
    #n.feed_forward([-6,1])

        #print output_layer_out

        #print hidden_layer_out
