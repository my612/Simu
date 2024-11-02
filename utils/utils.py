import time
from .structures import Change
from .structures import Timer


def simulatePath(
    inputs: dict,
    outputs: list,
    gates: dict,
    change: Change,
    changed_wires: list,
    cumulative_delay: int = 0,
):
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
                if nextWire in [wire for wire, _, _ in changed_wires]:
                    for i in range(len(changed_wires)):
                        if changed_wires[i][0] == nextWire:
                            if changed_wires[i][1] == outValue:
                                changed_wires[i] = (nextWire, outValue, total_delay)
                            else:
                                if i < len(changed_wires):
                                    changed_wires.pop(i)
                            break
                        else:
                            continue
                else:
                    changed_wires.append((nextWire, outValue, total_delay))
        else:
            gate.setInputs(change)
            outValue = gate.value()
            input_name = gate.output_name
            if outValue is None:
                outValue = 0
            input_value = int(outValue)
            if input_name in [wire for wire, _, _ in changed_wires]:
                for i in range(len(changed_wires)):
                    if changed_wires[i][0] == input_name:
                        if changed_wires[i][1] == input_value:
                            changed_wires[i] = (input_name, input_value, total_delay)
                        else:
                            if i < len(changed_wires):
                                changed_wires.pop(i)
                        break
                    else:
                        continue
            else:
                changed_wires.append((input_name, input_value, total_delay))
            simulatePath(
                inputs,
                outputs,
                gates,
                Change(input_name, input_value),
                changed_wires,
                total_delay,
            )


def simulate(
    instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str
):
    timestamp = 0
    previous_state = {output: None for output in outputs}
    with open(output_file_path, "w") as file:
        for instruction in instructions:
            delay, input_name, new_input_value = instruction
            change = Change(input_name, new_input_value)
            changed_wires = []
            simulatePath(inputs, outputs, gates, change, changed_wires)
            time.sleep(delay / 1000000)
            timestamp += delay
            changed_wires = [
                (wire, value, wire_delay)
                for wire, value, wire_delay in changed_wires
                if previous_state.get(wire) != value
            ]  # Filter out wires that did not change
            for (
                wire,
                value,
                _,
            ) in changed_wires:  # Update the previous state of the wires that changed
                previous_state[wire] = value
            input_wire_str = "\n".join(
                [f"{timestamp}: {input_name} = {new_input_value}"]
            )
            file.write(f"{input_wire_str}\n")
            print(f"{input_wire_str}")
            if changed_wires:
                changed_wires_str = "\n".join(
                    [
                        f"{timestamp + wire_delay}: {wire}: {value}"
                        for wire, value, wire_delay in changed_wires
                    ]
                )
                file.write(f"{changed_wires_str}\n")
                print(f"{changed_wires_str}")
            # print the output wires after each input change
            # output_str = '\n'.join([f"{timestamp}: {output}: {value}" for output, value in outputs.items()])
            # print(f"{output_str}")


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
        changed_wires = [
            (wire, value, wire_delay)
            for wire, value, wire_delay in changed_wires
            if previous_state.get(wire) != value
        ]
        # Update the previous state
        for wire, value, _ in changed_wires:
            previous_state[wire] = value
        input_wire_str = f"{timestamp}: {input_name} = {new_input_value}"
        results.append(input_wire_str)
        if changed_wires:
            changed_wires_str = "\n".join(
                [
                    f"{timestamp + wire_delay}: {wire}: {value}"
                    for wire, value, wire_delay in changed_wires
                ]
            )
            results.append(changed_wires_str)

    return results


def simulateChangeBFS(inputs: dict, prevState: dict, gates: dict, changes: dict):
    queue = []
    outs = {}
    for start in changes.keys():
        queue = queue + inputs[start]
    while queue:
        current = gates[queue.pop(0)]
        inputNames = current.inputs.keys()
        # print(changes)
        for i in inputNames:
            if i in changes:
                delay = changes[i][1] + current.delay
                current.setInputs(Change(i, changes[i][0]))
        outValue = current.value()
        if current.output_name in prevState:
            outs[current.output_name] = outValue
            if prevState[current.output_name] != outs[current.output_name]:
                changes[current.output_name] = (outValue, delay)

        else:
            queue = queue + inputs[current.output_name]
            changes[current.output_name] = (outValue, delay)

    return outs, changes


def simulateBFS(
    instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str
):
    timestamp = 0
    previous_state = {output: None for output in outputs}
    results = []
    with open(output_file_path, "w") as file:
        for instruction in instructions:
            delay, input_name, new_input_value = instruction
            timestamp += delay
            change = {input_name: (new_input_value, timestamp)}
            previous_state, changes = simulateChangeBFS(
                inputs, previous_state, gates, change
            )

            if changes:
                changed_wires_str = "\n".join(
                    [
                        f"{time}: {wire}: {value}"
                        for wire, (value, time) in changes.items()
                    ]
                )
                file.write(f"{changed_wires_str}\n")
                print(f"{changed_wires_str}")
                results.append(changed_wires_str)
    return results
