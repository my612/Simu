import time

class NOT:
    def __init__(self, inpName, input, outName, delay=0):
        self.input = input
        self.input_name = inpName
        self.output_name = outName
        self.delay = delay
    def value(self):
        time.sleep(self.delay)
        return not self.input
    
        

class AND:
    def __init__(self, inpName1, inpName2, input1, input2, outName, delay=0):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 and self.input2

class OR:
    def __init__(self, inpName1, inpName2, input1, input2, outName, delay=0):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 or self.input2
    
class NAND:
    def __init__(self, inpName1, inpName2, input1, input2, outName, delay=0):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return not(self.input1 and self.input2)

class NOR:
    def __init__(self, inpName1, inpName2, input1, input2, outName, delay=0):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return not(self.input1 or self.input2)
    
class XOR:  
    def __init__(self, inpName1, inpName2, input1, input2, outName, delay=0):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 ^ self.input2
    
class buffer:
    def __init__(self, inpName, input, outName, delay=0):
        self.input = input
        self.input_name = inpName
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input   


def parseVerilog(filePath):
    
    f = open(filePath, "r")
    inputs = []
    outputs = []
    wires = []
    
    for x in f:
        line = f.split()
        if(line[0] == "input"):
            inputs.append(line[1])
        if(line[0] == "output"):
            outputs.append(line[1])
        

    
parseVerilog("test.v")
