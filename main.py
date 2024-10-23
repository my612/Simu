from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulate


def main():
    ins, outs, gates, inputs = parseVerilog("/media/nicolas/New Volume/DD1 Project 1/DD1-project1/tests/circ1.v")
    simulate('in0', inputs, outs, gates, Change('in0', 1))
    simulate('sel0', inputs, outs, gates, Change('sel0', 0))
    simulate('sel1', inputs, outs, gates, Change('sel1', 0))
    # printPath('sel1', inputs, outs, gates)
    print(gates['g13'].value())
    # print(outs[0])
if __name__ == "__main__":
    main()
