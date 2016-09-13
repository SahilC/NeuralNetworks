import numpy as np
class InputProcessor:
    def __init__(self,file_name):
        self.file_name = file_name

    def read_processed_input(self):
        with open(self.file_name) as f:
            digits = np.array([])
            out_value = np.array([])
            while True:
                lines = f.readlines(8192)
                if not lines:
                    break

                for line in lines:
                    line = line.strip()
                    temp = map(int,line.split(','))
                    print temp[:-1]
                    digits = np.append(digits,temp[:-1])
                    out_value = np.append(out_value,temp[-1])
        return {'input':digits,'output':out_value}

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
