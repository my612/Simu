from utils.structures import Change
def printPath(start: str, inputs : dict, outputs: list, gates : dict):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if(nextWire in outputs):
            print(nextWire, "->>", gate.gate_name)
            print(gate.value())
        else:
            print(start, "->>", gate.gate_name, end=",")
            print("output is", gate.value(), end=" ")
            printPath(nextWire, inputs, outputs, gates)
def simulate(start:str, inputs:dict, outputs: list, gates: dict, change:Change):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if(nextWire in outputs):
            print(nextWire, "->>", gate.gate_name)
            print(gate.value())
            outValue = gate.setInputs(change.input_value)
        else:
            print(start, "->>", gate.gate_name, end=",")
            print("output is", gate.value(), end=" ")
            
            printPath(nextWire, inputs, outputs, gates)
            