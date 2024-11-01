import time
from .structures import Change
from .structures import Timer


def printPath(start: str, inputs: dict, outputs: list, gates: dict):
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if nextWire in outputs:

            # print(nextWire, "->>", gate.gate_name)
            # print(gate.value())
            pass
        else:
            if start != "sel_not1":
                print(start, "->>", gate.gate_name, end=",")
                # print("output is", gate.value(), end=" ")
            printPath(nextWire, inputs, outputs, gates)


def simulatePath(inputs: dict, outputs: list, gates: dict, change: Change):
    start = change.input_name
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        if nextWire in outputs:
            gate.setInputs(change)
            outValue = int(gate.value())
            outputs[nextWire] = outValue
        else:
            gate.setInputs(change)
            outValue = gate.value()
            input_name = gate.output_name
            input_value = int(outValue)
            simulatePath(inputs, outputs, gates, Change(input_name, input_value))


def OutputGatesValues(outputs: list, gates: dict):
    output_values = []
    for output in outputs:
        for gate_name, gate in gates.items():
            if gate.output_name == output:
                output_values.append(gate.value())
    return output_values


def simulate(instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str):
    with open(output_file_path, 'w') as file:
        for instruction in instructions:
            delay, input_name, new_input_value = instruction
            change = Change(input_name, new_input_value)
            simulatePath(inputs, outputs, gates, change)
            time.sleep(delay / 1000)
            file.write(f"{delay}:{outputs}\n")
            print(f"{delay}:{outputs}")
            
        