import time

from .structures import Change

# The following classes are the gates that are used in the simulation


class NOT:
    def __init__(
        self, inpName, outName, delay=0, gname=""
    ):  # The constructor of the class
        self.gate_name = gname  # The name of the gate
        self.inputs = {inpName: 0}  # The input of the gate
        self.output_name = outName  # The output of the gate
        self.delay = delay  # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i = list(self.inputs.values())[0] # The input of the gate
        return int(not i) # The output of the gate based on the input and the gate type

    def setInputs(self, change: Change):
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class AND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName1: 0, inpName2: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1, i2 = self.inputs.values() # The inputs of the gate
        return i1 and i2 # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change):
        if change.input_name in self.inputs:
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class OR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName1: 0, inpName2: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay  # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1, i2 = self.inputs.values() # The inputs of the gate
        return i1 or i2     # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change): # The function to set the inputs of the gate based on the change instruction
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class NAND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName1: 0, inpName2: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1, i2 = self.inputs.values() # The inputs of the gate
        return not (i1 and i2) # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change): # The function to set the inputs of the gate based on the change instruction
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class NOR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName1: 0, inpName2: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1, i2 = self.inputs.values() # The inputs of the gate
        return not (i1 or i2) # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change):
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class XOR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName1: 0, inpName2: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1, i2 = self.inputs.values() # The inputs of the gate
        return i1 ^ i2 # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change):
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)


class buffer:
    def __init__(self, inpName, outName, delay=0, gname=""):
        self.gate_name = gname # The name of the gate
        self.inputs = {inpName: 0} # The input of the gate
        self.output_name = outName # The output of the gate
        self.delay = delay # The delay of the gate

    def value(self):
        time.sleep(self.delay / 1000) # The delay of the gate
        i1 = list(self.inputs.values())[0] # The input of the gate
        return i1 # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change):
        time.sleep(self.delay / 1000) # The delay of the gate
        return self.input # The output of the gate based on the inputs and the gate type

    def setInputs(self, change: Change):
        if change.input_name in self.inputs: # If the input is in the dictionary of the gate
            self.inputs[change.input_name] = change.input_value # Set the input of the gate to the input value of the change instruction
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)
