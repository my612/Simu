from utils.gates import AND, OR, NOT, NAND, XOR, NOR, buffer

def parseVerilog(filePath):
    
    inputs = []
    outputs = {}
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
                    outputs[line[1]] = None
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
                if(line[0] == "nor"):
                    parameters = line[3].strip("();").split(",")                    
                    gates[line[2]] = NOR(parameters[2], parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
                    ins[parameters[2]].append(line[2])
                if(line[0] == "buf"):
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = buffer(parameters[1], parameters[0], int(line[1].strip("#()")), line[2])
                    ins[parameters[1]].append(line[2])
        return inputs, outputs, gates, ins
    
def parseStimuli(filePath):
    instructions = []

    with open(filePath, 'r') as f:
        for line in f:
            line = line.replace(";", "")
            line = line.split()
            if(line):
                instructions.append([int(line[1]), line[2].split("=")[0], int(line[2].split("=")[1])])
    return instructions


def parseSimFile(filepath, inputs, outputs):
    fn : dict[int, list[tuple]] = {}
    inputs = ['A', 'B', 'C_in']
    outputs = ['S', 'C_out']
    with open(filepath, 'r') as f:
        for line in f:
            line = line.replace(":", "").replace("=", "")
            line = line.split()
            if(line):
                print(line[1])                
                if(line[1] in inputs or line[1] in outputs):
                    if(line[1] not in fn):
                        fn[line[1]] = []
                    fn[line[1]].append((line[0], line[2]))
    return fn
