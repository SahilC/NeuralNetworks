import numpy as np
class InputProcessor:
    def __init__(self,file_name):
        self.file_name = file_name

    def process_output(self,val):
        binary = [int(x) for x in bin(val)[2:]]
        binary = [0 for _ in xrange(2-len(binary))] + binary

        return binary

    def read_processed_input(self):
        with open(self.file_name) as f:
            digits = []
            out_value = []
            while True:
                lines = f.readlines(8192)
                if not lines:
                    break

                for line in lines:
                    line = line.strip()
                    temp = map(int,line.split(','))
                    #print temp[:-1]
                    if temp[-1] < 3:
                        out_value.append(self.process_output(temp[-1]))

                        #normalize the input from 0 to 1
                        temp = [(x/16) for x in temp[:-1]]
                        temp.append(1)
                        digits.append(temp)

        #print np.array(out_value)
        return {'input':np.array(digits),'output':np.array(out_value)}

    def read_input(self):
        with open(self.file_name) as f:
            digits = []
            out_value = []
            digit = []
            while True:
                lines = f.readlines(8192)
                if not lines:
                    break

                for line in lines:
                    line = line.strip()
                    l = len(line)
                    if l == 32:
                        digit.append(map(int,list(line)))
                    elif l == 1:
                        tmp = []
                        for i in xrange(0,len(digit),4):
                            for j in xrange(0,len(digit[i]),4):
                                val = 0
                                for k in xrange(0,4):
                                    if (i+k) < len(digit):
                                        val += sum(digit[i+k][j:j+4])
                                tmp.append(val)
                        digit = []
                        if int(line) < 3:
                            digits.append(tmp)
                            out_value.append(self.process_output(int(line)))
            #print digits
            return {'input':np.array(digits),'output':np.array(out_value)}
