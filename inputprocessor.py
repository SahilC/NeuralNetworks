import numpy as np
class InputProcessor:
    def __init__(self,file_name):
        self.file_name = file_name

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
                        val = [int(x) for x in bin(temp[-1])[2:]]
                        val = [0 for _ in xrange(2-len(val))] + val
                        out_value.append(val)
                        temp = temp[:-1]
                        temp.append(1)
                        digits.append(temp)

        #print np.array(out_value)
        return {'input':np.array(digits),'output':np.array(out_value)}

    def read_input(self):
        with open(self.file_name) as f:
            digits = []
            out_value = []
            while True:
                lines = f.readlines(8192)
                if not lines:
                    break

                digit = []
                for line in lines:
                    line = line.strip()
                    l = len(line)
                    if l == 32:
                        digit.append(map(int,list(line)))
                    elif l == 1:
                        digits.append(digit)
                        print line
                        digit = []
                        out_value.append(int(line))
