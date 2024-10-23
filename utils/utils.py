from .structures import Change


def printPath(start: str, inputs: dict, outputs: list, gates: dict):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if nextWire in outputs:
            
            # print(nextWire, "->>", gate.gate_name)
            # print(gate.value())
            pass
        else:
            if(start != 'sel_not1'):
                print(start, "->>", gate.gate_name, end=",")
                # print("output is", gate.value(), end=" ")
            printPath(nextWire, inputs, outputs, gates)


def simulate(start: str, inputs: dict, outputs: list, gates: dict, change: Change):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if nextWire in outputs:
            # print(nextWire, "->>", gate.gate_name)
            # print(gate.value())
            gate.setInputs(change)
            outValue = int(gate.value())
            # print("The output", gate.output_name, "is", outValue)
        else:
            # print(start, "->>", gate.gate_name, end=",")
            # print("output is", gate.value(), end=" ")
            # print("gate: ", gate.gate_name, "  ", change.input_name, change.input_value)
            gate.setInputs(change)
            outValue = gate.value()
            # print("The wire", gate.output_name, "is", outValue)
            input_name = gate.output_name
            input_value = int(outValue)
            simulate(nextWire, inputs, outputs, gates, Change(input_name, input_value))  
