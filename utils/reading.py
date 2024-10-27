from utils.gates import AND, OR, NOT, NAND, XOR, NOR


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
    

# 0 A=0;
# 0 B=0;
# 0 C=1;
# 500 A=1;
# 800 B=1;
# 1300 C=1;    

def parseStimuli(filePath):
    instructions = []

    with open(filePath, 'r') as f:
        for line in f:
            line = line.replace(";", "")
            line = line.split()
            if(line):
                instructions.append([int(line[1]), line[2].split("=")[0], int(line[2].split("=")[1])])
    return instructions


