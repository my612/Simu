import time

class NOT:
    def __init__(self, inpName, outName, delay=0, gname=""):
        self.gate_name = gname
        self.input = 0
        self.input_name = inpName
        self.output_name = outName
        self.delay = delay
    def value(self):
        time.sleep(self.delay)
        return not self.input
    def setInput(self, input):
        self.input = input
        

class AND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.input1 = 0
        self.input2 = 0
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 and self.input2
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2

class OR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.input1 = 0
        self.input2 = 0
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 or self.input2
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        
class NAND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.input1 = 0
        self.input2 = 0
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return not(self.input1 and self.input2)
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        
class NOR:
    def __init__(self, inpName1, inpName2, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.input1 = 0
        self.input2 = 0
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return not(self.input1 or self.input2)
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
    
class XOR:  
    def __init__(self, inpName1, inpName2, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.input1 = 0
        self.input2 = 0
        self.input_name1 = inpName1
        self.input_name2 = inpName2
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input1 ^ self.input2
    def setInputs(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
    
class buffer:
    def __init__(self, inpName, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.input = 0
        self.input_name = inpName
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay)
        return self.input   
    def setInput(self, input):
        self.input = input

class change:
    def __init__(self, inputName, inputValue):
        self.input_name = inputName
        self.input_value = inputValue
def parseVerilog(filePath):
    
    inputs = []
    outputs = []
    wires = []
    gates = {}
    ins = dict()
    with open(filePath, 'r') as f:
        for line in f:
            line = line.replace(";", "")
            line = line.split()
            if(line):
                if(line[0] == "input"):
                    inputs.append(line[1])
                    ins[line[1]] = []
                if(line[0] == "output"):
                    outputs.append(line[1])
                if(line[0] == "wire"):
                    wires.append(line[1])
                    ins[line[1]] = []
                if(line[0] == "not"):
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = NOT(parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                if(line[0] == "and"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = AND(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])
                if(line[0] == "or"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = OR(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])
                if(line[0] == "nand"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = NAND(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])
                if(line[0] == "xor"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = XOR(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])
                if(line[0] == "NOR"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = NOR(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])

        return inputs, outputs, gates, ins

def printPath(start: str, inputs : dict, outputs: list, gates : dict):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if(nextWire in outputs):
            print(nextWire, "->>", gate.gate_name)
            print(gate.value())
        else:
            print(start, "->>", gate.gate_name, end=" ")
            printPath(nextWire, inputs, outputs, gates)
    

            
# and #(5) g0 (w,a,b);
        
# not #(2) g1 (n,a);
        
# or #(9) g2 (y,n,c);
        
# nand #(7) g3 (z,y,w);
        

ins, outs, gates, inputs = parseVerilog("./tests/circ1.v")
printPath('sel0', inputs, outs, gates)