import time

from .structures import Change


class NOT:
    def __init__(self, inpName, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay / 1000)
        i = list(self.inputs.values())[0]
        return not i

    def setInputs(self, change: Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)

class AND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: None, inpName2: None}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1, i2 = self.inputs.values()
        return i1 and i2
    def setInputs(self, change:Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)

class OR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1, i2 = self.inputs.values()
        return i1 or i2
    def setInputs(self, change:Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)



class NAND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1, i2 = self.inputs.values()
        return not(i1 and i2)
    def setInputs(self, change:Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)



class NOR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1, i2 = self.inputs.values()
        return not(i1 or i2)
    def setInputs(self, change:Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)



class XOR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1, i2 = self.inputs.values()
        return i1 ^ i2
    def setInputs(self, change:Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)



class buffer:
    def __init__(self, inpName, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        i1 = list(self.inputs.values())[0]
        return i1   
    def setInputs(self, change:Change):
        time.sleep(self.delay / 1000)
        return self.input

    def setInputs(self, change: Change):
        if(change.input_name in self.inputs):
            self.inputs[change.input_name] = change.input_value
        else:
            print("Input not found in the dictionary of the gate")
            print("The input is: ", change.input_name)
            print("The gate is: ", self.gate_name)
            exit(1)

