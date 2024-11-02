from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import simulatePath, simulate
from utils.reading import parseStimuli
from utils.utils import simulateChangeBFS, simulateBFS

#TODO adjust for the case when there's a space between the parameters.
#TODO Find a way to pass the output into another gate
#TODO CLEAN THE CODE (Unwanted comments, print statements, etc)
def main():
    ins, outs, gates, inputs = parseVerilog(
        "./tests/circ3.v"   
    )
    # instructions = parseStimuli("./stims/circ2.stim")
    # simfile = "./utils/simulations/sim2.sim"
    # simulate(instructions, inputs, outs, gates, simfile)
    # waveform(simfile, ins, outs)
    # print(inputs)
    # g = [(gate.gate_name, gate.output_name) for gate in gates.values()]
    # print(g)
    # print(outs)
    instructions = parseStimuli("./stims/circ3.stim")
    # changes = {'in1': (0, 0), 'in0': (1, 10), 'en': (1, 10)}
    # o, oo = simulateChangeBFS(inputs, outs, gates, changes)
    # print(oo)
    simulateBFS(instructions, inputs, outs, gates, "./utils/simulations/sim3.sim")
if __name__ == "__main__":
    main()

