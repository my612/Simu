class NOT:
    def __init__(self, inpName, input, outName):
        self.input = input
        self.input_name = inpName
        self.output_name = outName
    def value():
        return not input
    
        


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