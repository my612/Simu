import time

from utils.structures import Change

class NOT:
    def __init__(self, inpName, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName: 0}
        self.output_name = outName
        self.delay = delay
    def value(self):
        time.sleep(self.delay /1000)
        return not self.input
    def setInput(self, change:Change):
        self.inputs[change.input_name] = change.input_value
       
class AND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return self.input1 and self.input2
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value


class OR:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return self.input1 or self.input2
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value
        
class NAND:
    def __init__(self, inpName1, inpName2, outName, delay=0, gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return not(self.input1 and self.input2)
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value
        
class NOR:
    def __init__(self, inpName1, inpName2, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return not(self.input1 or self.input2)
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value
    
class XOR:  
    def __init__(self, inpName1, inpName2, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.inputs = {inpName1: 0, inpName2: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return self.input1 ^ self.input2
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value
    
class buffer:
    def __init__(self, inpName, outName, delay=0 , gname=""):
        self.gate_name = gname
        self.inputs = {inpName: 0}
        self.output_name = outName
        self.delay = delay

    def value(self):
        time.sleep(self.delay /1000)
        return self.input   
    def setInputs(self, change:Change):
        self.inputs[change.input_name] = change.input_value
