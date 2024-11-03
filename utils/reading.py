from utils.gates import AND, OR, NOT, NAND, XOR, NOR, buffer


def parseVerilog(filePath): # The function to parse the verilog file

    inputs = [] # The list of inputs of the circuit
    outputs = {}  # The dictionary of outputs of the circuit with the outputs names as keys and the gates objects as values
    wires = [] # The list of wires of the circuit 
    gates = {} # The dictionary of gates of the circuit with the gates objects
    ins = dict() # The dictionary of inputs of the circuit with the corresponding gates
    with open(filePath, "r") as f: # Open the file
        for line in f: # Read the file line by line
            line = line.replace(";", "") # Remove the semicolon from the line
            line = line.split() 
            if line:
                if line[0] == "input": # If the line is an input 
                    inputs.append(line[1]) # Add the input to the list of inputs
                    ins[line[1]] = [] # Add the input to the dictionary of inputs
                if line[0] == "output": # If the line is an output
                    outputs[line[1]] = None # Add the output to the dictionary of outputs
                if line[0] == "wire": # If the line is a wire
                    wires.append(line[1]) # Add the wire to the list of wires
                    ins[line[1]] = [] # Add the wire to the dictionary of inputs
                if line[0] == "not": # If the line is a not gate 
                    parameters = line[3].strip("();").split(",") 
                    gates[line[2]] = NOT(parameters[1], parameters[0], int(line[1].strip("#()")), line[2]) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "and": 
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = AND(
                        parameters[2],
                        parameters[1],
                        parameters[0],
                        int(line[1].strip("#()")),
                        line[2],
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                    ins[parameters[2]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "or":
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = OR(
                        parameters[2],
                        parameters[1],
                        parameters[0],
                        int(line[1].strip("#()")),
                        line[2],
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                    ins[parameters[2]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "nand":
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = NAND(
                        parameters[2],
                        parameters[1],
                        parameters[0],
                        int(line[1].strip("#()")),
                        line[2],
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                    ins[parameters[2]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "xor":
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = XOR(
                        parameters[2],
                        parameters[1],
                        parameters[0],
                        int(line[1].strip("#()")),
                        line[2],
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                    ins[parameters[2]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "nor":
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = NOR(
                        parameters[2],
                        parameters[1],
                        parameters[0],
                        int(line[1].strip("#()")),
                        line[2],
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
                    ins[parameters[2]].append(line[2]) # Add the gate to its corresponding input
                if line[0] == "buf":
                    parameters = line[3].strip("();").split(",")
                    gates[line[2]] = buffer(
                        parameters[1], parameters[0], int(line[1].strip("#()")), line[2]
                    ) # Add the gate to the dictionary of gates with its inputs and output
                    ins[parameters[1]].append(line[2]) # Add the gate to its corresponding input
        return inputs, outputs, gates, ins


def parseStimuli(filePath): # The function to parse the stimuli file
    instructions = []

    with open(filePath, "r") as f:
        for line in f:
            line = line.replace(";", "")
            line = line.split()
            if line:
                instructions.append(
                    [int(line[1]), line[2].split("=")[0], int(line[2].split("=")[1])]
                ) # Add the instruction to the list of instructions
    return instructions # Return the list of instructions


def parseSimFile(filepath, inputs, outputs): # The function to parse the simulation file to draw the waveform
    fn: dict[int, list[tuple]] = {} # The dictionary of the simulation file with the inputs and outputs
    with open(filepath, "r") as f:
        for line in f:
            line = line.replace(":", "").replace("=", "")
            line = line.split()
            if line:
                if line[1] in inputs or line[1] in outputs: # If the input or output is in the line
                    if line[1] not in fn: # If the input or output is not in the dictionary
                        fn[line[1]] = [] # Add the input or output to the dictionary
                    if line[2] == "None": # If the input or output is None
                        fn[line[1]].append((line[0], 0)) # Add the input or output to the dictionary with the value 0
                    fn[line[1]].append((line[0], line[2])) # Add the input or output to the dictionary with the value
    return fn
