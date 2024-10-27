from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulatePath, simulate
from utils.reading import parseStimuli
from utils.structures import Change
from utils.utils import printPath, simulatePath
from utils.reading import parseVerilog, parseStimuli


def main():
    ins, outs, gates, inputs = parseVerilog(
        "tests\circ6.v"
    )
    instructions = parseStimuli("./utils/file.stim")
    simulate(instructions, inputs, outs, gates)


if __name__ == "__main__":
    main()



