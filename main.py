class NOT:
    def __init__(self, inpName, input, outName):
        self.input = input
        self.input_name = inpName
        self.output_name = outName
    def value():
        return not input
    
        

class AND:
    def __init__(self, inpName1, inpName2, input1, input2, outName):
        self.input1 = input1
        self.input2 = input2
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName

    def value():
        return input1 and input2


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
