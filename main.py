from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import simulatePath, simulate
from utils.reading import parseStimuli
from utils.waveform import waveform


#TODO adjust for the case when there's a space between the parameters.
#TODO Find a way to pass the output into another gate
#TODO CLEAN THE CODE (Unwanted comments, print statements, etc)
def main():
    ins, outs, gates, inputs = parseVerilog(
        "./tests/circ3.v"   
    )
    waveform("./utils/simulations/sim3.sim", ins, list(outs.keys()))
if __name__ == "__main__":
    main()

