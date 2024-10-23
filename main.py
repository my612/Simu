from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulate


def main():
    ins, outs, gates, inputs = parseVerilog("./tests/circ1.v")
    simulate('in0', inputs, outs, gates, Change('in0', 1))
    
if __name__ == "__main__":
    main()
