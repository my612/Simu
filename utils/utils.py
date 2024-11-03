import time
from .structures import Change

#in the simulatePath function, the function is called recursively to simulate the path of the circuit by DFS traversal
#the function takes the inputs, outputs, gates, change, changed_wires, and cumulative_delay as arguments
#the function is called recursively to simulate the path of the circuit by traversing the gates and updating the outputs
#the function updates the outputs and changed_wires based on the gate values and inputs and whether the output has changed

def simulatePath(
    inputs: dict, 
    outputs: list,
    gates: dict,
    change: Change,
    changed_wires: list,
    cumulative_delay: int = 0,
):
    start = change.input_name

    for g in inputs[start]: # For each gate connected to the input
        gate = gates[g]
        nextWire = gate.output_name # Handle the first gate output (wire) as the next wire
        gate_delay = gate.delay 
        total_delay = cumulative_delay + gate_delay # The total delay of the wire = the cumulative delay coming from the previous wire (gates) + the delay of the current gate
        if nextWire in outputs:  # If the wire is an output
            gate.setInputs(change) # Set the input of the gate to the input value of the change instruction
            outValue = int(gate.value()) # Get the output value of the gate
            if outputs[nextWire] != outValue: # If the output value has changed
                outputs[nextWire] = outValue # Update the output value
                # the following code block updates and filters the changed wires list with the output value and the total delay
                if nextWire in [wire for wire, _, _ in changed_wires]: # If the wire is in the list of changed wires
                    for i in range(len(changed_wires)): # For each wire in the list of changed wires
                        if changed_wires[i][0] == nextWire: # If the wire is the same as the current wire
                            if changed_wires[i][1] == outValue: # If the wire value is the same as the output value
                                changed_wires[i] = (nextWire, outValue, total_delay) # Update the wire value and the total delay
                            else: # If the wire value is different from the output value then it is equal to its original value and the total delay
                                if i < len(changed_wires): # If the index is less than the length of the changed wires list so it does not go out of range
                                    changed_wires.pop(i) # Remove the wire from the list
                            break
                        else:
                            continue
                else: # If the wire is not in the list of changed wires
                    changed_wires.append((nextWire, outValue, total_delay)) # Add the wire to the list of changed wires
        else:
            gate.setInputs(change)
            outValue = gate.value() # Get the output value of the gate
            input_name = gate.output_name # Get the output name of the gate
            if outValue is None: 
                outValue = 0
            input_value = int(outValue) # Get the output value of the gate as an integer
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
            ) # Recursively call the function with the updated inputs, outputs, gates, change, changed_wires, and cumulative_delay


def simulate(
    instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str
): # The simulate function simulates the circuit based on the instructions, inputs, outputs, gates, and the output file path 
    timestamp = 0 # The timestamp of the simulation
    previous_state = {output: None for output in outputs} 
    with open(output_file_path, "w") as file: # Open the simulation output file
        for instruction in instructions: # For each instruction in the list of instructions
            delay, input_name, new_input_value = instruction
            change = Change(input_name, new_input_value)
            changed_wires = []
            simulatePath(inputs, outputs, gates, change, changed_wires) # Simulate the path of the circuit based on the inputs, outputs, gates, change, and changed_wires
            time.sleep(delay / 1000000)
            timestamp += delay # Update the timestamp to each input change
            changed_wires = [
                (wire, value, wire_delay)
                for wire, value, wire_delay in changed_wires
                if previous_state.get(wire) != value]  # Filter out wires that did not change
            for (
                wire,
                value,
                _,
            ) in changed_wires:  # for each wire, value, and wire delay in the changed wires list
                previous_state[wire] = value 
            input_wire_str = "\n".join(
                [f"{timestamp}: {input_name} = {new_input_value}"]
            )  # Join the timestamp, input name, and new input value
            file.write(f"{input_wire_str}\n") # Write the input wire string to the file
            print(f"{input_wire_str}") # Print the input wire string
            if changed_wires: # If there are changed wires
                changed_wires_str = "\n".join(
                    [
                        f"{timestamp + wire_delay}: {wire}: {value}"
                        for wire, value, wire_delay in changed_wires
                    ]
                ) # Join the changed wires with the timestamp and the wire value
                file.write(f"{changed_wires_str}\n") # Write the changed wires string to the file
                print(f"{changed_wires_str}") # Print the changed wires string

# The simulate_g function simulates the circuit based on the instructions, inputs, outputs, and gates as simultate but returns the results instead of writing them to a file
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

# The simulateChangeBFS function simulates the circuit based on the inputs, previous state, gates, and changes using a Breadth-First Search (BFS) traversal
# The function takes the inputs, previous state, gates, and changes as arguments
# The function simulates the circuit by traversing the gates and updating the outputs based on the changes in a queue
# The function returns the outputs and changes after simulating the circuit
def simulateChangeBFS(inputs: dict, prevState: dict, gates: dict, changes: dict):
    queue = []
    outs = {}
    for start in changes.keys(): # For each start in the changes keys
        queue = queue + inputs[start]
    while queue: # While the queue is not empty
        current = gates[queue.pop(0)] # Get the current gate from the queue and remove it
        inputNames = current.inputs.keys() # Get the input names of the current gate
        # print(changes)
        for i in inputNames: 
            if i in changes: # If the input is in the changes dictionary
                delay = changes[i][1] + current.delay # The delay of the input = the delay of the input in the changes dictionary + the delay of the current gate
                current.setInputs(Change(i, changes[i][0])) # Set the input of the current gate to the input value of the change instruction
        outValue = current.value() # Get the output value of the current gate
        if current.output_name in prevState: # If the output name of the current gate is in the previous state
            outs[current.output_name] = outValue # Update the output value of the current gate
            if prevState[current.output_name] != outs[current.output_name]: # If the output value has changed
                changes[current.output_name] = (outValue, delay) # Update the changes dictionary with the output value and the delay

        else:
            queue = queue + inputs[current.output_name] # Add the output name of the current gate to the queue
            changes[current.output_name] = (outValue, delay) # Update the changes dictionary with the output value and the delay

    return outs, changes


def simulateBFS(
    instructions: list, inputs: dict, outputs: list, gates: dict, output_file_path: str
):
    timestamp = 0 # The timestamp of the simulation
    previous_state = {output: None for output in outputs} # The previous state of the outputs
    results = [] # The results of the simulation
    with open(output_file_path, "w") as file: # Open the simulation output file
        for instruction in instructions: # For each instruction in the list of instructions
            delay, input_name, new_input_value = instruction # Get the delay, input name, and new input value of the instruction
            timestamp += delay # Update the timestamp to each input change
            change = {input_name: (new_input_value, timestamp)} # The change dictionary with the input name and the new input value
            previous_state, changes = simulateChangeBFS( 
                inputs, previous_state, gates, change
            ) # Simulate the circuit based on the inputs, previous state, gates, and changes

            if changes:
                changed_wires_str = "\n".join(
                    [
                        f"{time}: {wire}: {value}"
                        for wire, (value, time) in changes.items()
                    ]
                ) # Join the changed wires with the timestamp and the wire value
                file.write(f"{changed_wires_str}\n") # Write the changed wires string to the file
                print(f"{changed_wires_str}") # Print the changed wires string
                results.append(changed_wires_str) # Add the changed wires string to the results
    return results
