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


def simulatePath(inputs: dict, outputs: list, gates: dict, change: Change, changed_wires: list, cumulative_delay: int = 0):
    start = change.input_name

    
     
    for g in inputs[start]:
        gate = gates[g]
        nextWire = gate.output_name
        gate_delay = gate.delay
        total_delay = cumulative_delay + gate_delay
        if nextWire in outputs:
            gate.setInputs(change)
            outValue = int(gate.value())
            if outputs[nextWire] != outValue:
                outputs[nextWire] = outValue
                changed_wires.append((nextWire, outValue, total_delay))
        else:
            gate.setInputs(change)
            outValue = gate.value()
            input_name = gate.output_name
            input_value = int(outValue)
            if input_name not in [wire for wire, _, _ in changed_wires]:
                changed_wires.append((input_name, input_value, total_delay))
            simulatePath(inputs, outputs, gates, Change(input_name, input_value), changed_wires, total_delay)

def OutputGatesValues(outputs: list, gates: dict):
    output_values = []
    for output in outputs:
        for gate_name, gate in gates.items():
            if gate.output_name == output:
                output_values.append(gate.value())
    return output_values


def simulate(instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str):
    timestamp = 0
    previous_state = {output: None for output in outputs}
    with open(output_file_path, 'w') as file:
        for instruction in instructions:
            delay, input_name, new_input_value = instruction
            change = Change(input_name, new_input_value)
            changed_wires = []
            simulatePath(inputs, outputs, gates, change, changed_wires)
            time.sleep(delay / 1000000)
            timestamp += delay
            # Filter out wires that did not change
            changed_wires = [(wire, value, wire_delay) for wire, value, wire_delay in changed_wires if previous_state.get(wire) != value]
            # Update the previous state
            for wire, value, _ in changed_wires:
                previous_state[wire] = value
            if changed_wires:
                changed_wires_str = '\n'.join([f"{timestamp + wire_delay}: {wire}: {value}" for wire, value, wire_delay in changed_wires])
                input_change_str = f"{input_name} = {new_input_value}"
                file.write(f"{timestamp}: {input_change_str}\n{changed_wires_str}\n")
                print(f"{timestamp}: {input_change_str}\n{changed_wires_str}")
            
        
def simulate_g(instructions: list, inputs: dict, outputs: list, gates: dict):
    timestamp = 0
    previous_state = {output: None for output in outputs}
    results = []
    
    for instruction in instructions:
        delay, input_name, new_input_value = instruction
        change = Change(input_name, new_input_value)
        changed_wires = []
        simulatePath(inputs, outputs, gates, change, changed_wires)
        time.sleep(delay / 1000000)
        timestamp += delay
        # Filter out wires that did not change
        changed_wires = [(wire, value, wire_delay) for wire, value, wire_delay in changed_wires if previous_state.get(wire) != value]
        # Update the previous state
        for wire, value, _ in changed_wires:
            previous_state[wire] = value
        if changed_wires:
            changed_wires_str = '\n'.join([f"{timestamp + wire_delay}: {wire}: {value}" for wire, value, wire_delay in changed_wires])
            input_change_str = f"{input_name} = {new_input_value}"
            result_str = f"{timestamp}: {input_change_str}\n{changed_wires_str}\n"
            results.append(result_str)
            
    
    return results
                    