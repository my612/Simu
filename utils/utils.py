import time
from .structures import Change
from .structures import Timer



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


def simulate(instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str):
    timestamp = 0
    previous_state = {output: 0 for output in outputs}
    with open(output_file_path, 'w') as file:
        for instruction in instructions:
            delay, input_name, new_input_value = instruction
            change = Change(input_name, new_input_value)
            changed_wires = []
            simulatePath(inputs, outputs, gates, change, changed_wires)
            time.sleep(delay / 1000000)
            timestamp += delay
            changed_wires = [(wire, value, wire_delay) for wire, value, wire_delay in changed_wires if previous_state.get(wire) != value]  # Filter out wires that did not change
            for wire, value, _ in changed_wires:             # Update the previous state of the wires that changed
                previous_state[wire] = value
            file.write(f"{timestamp}: {input_name} = {new_input_value}\n")
            print(f"{timestamp}: {input_name} = {new_input_value}")
            if changed_wires:
                changed_wires_str = '\n'.join([f"{timestamp + wire_delay}: {wire}: {value}" for wire, value, wire_delay in changed_wires])
                file.write(f"{changed_wires_str}\n")
                print(f"{changed_wires_str}")