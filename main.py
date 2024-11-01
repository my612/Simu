from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulatePath, simulate
from utils.reading import parseStimuli


#TODO adjust for the case when there's a space between the parameters.
#TODO Find a way to pass the output into another gate
#TODO CLEAN THE CODE (Unwanted comments, print statements, etc)
def main():
    ins, outs, gates, inputs = parseVerilog(
        "./tests/circ2.v"   
    )
    instructions = parseStimuli("./stims/circ2.stim")
    simfile = "./utils/simulations/sim2.sim"
    simulate(instructions, inputs, outs, gates, simfile)
    

if __name__ == "__main__":
    main()




