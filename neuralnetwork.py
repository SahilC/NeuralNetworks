from neuron import Neuron
import numpy as np

if __name__ == '__main__':
    input_val = np.array([[2, 7], [8, 1], [7, 5], [6, 3],[7, 8],[5, 9],[4, 5],[4, 2],[-1, -1],[1, 3], [3, -2], [5, 3.25], [2, 4],[7, 1]])
    output_val = np.array([1,1,1,1,1,1,1,0,0,0,0,0,0,0])
    num_hidden = 2
    num_out = 1
    hidden_layer = [Neuron(input_val.shape[1]) for i in xrange(num_hidden)]
    output_layer = [Neuron(num_hidden) for i in xrange(num_out)]

    i = 0
    for val in input_val:
        hidden_layer_out = []
        for neuron in hidden_layer:
            hidden_layer_out.append(neuron.out_value(val))

        output_layer_out = []
        for neuron in output_layer:
            output_layer_out.append(neuron.out_value(hidden_layer_out))
            



        #print output_layer_out

        #print hidden_layer_out
