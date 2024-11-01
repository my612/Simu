from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulatePath, simulate
from utils.reading import parseStimuli
from utils.structures import Change
from utils.utils import printPath, simulatePath
from utils.reading import parseVerilog, parseStimuli
#TODO adjust for the case when there's a space between the parameters.
#TODO handle the case when the input is not in the dictionary input of each gate
def main():
    ins, outs, gates, inputs = parseVerilog(
        "./tests/circ7.v"   
    )
    instructions = parseStimuli("./stims/circ3.stim")
    simfile = "./utils/simulations/sim6.sim"
    simulate(instructions, inputs, outs, gates, simfile)
    

if __name__ == "__main__":
    main()




