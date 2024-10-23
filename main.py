from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulate
from utils.reading import parsestimuli


def main():
    ins, outs, gates, inputs = parseVerilog("./tests/circ1.v")
    simulate('in0', inputs, outs, gates, Change('in0', 1))
    ins, outs, gates, inputs = parseVerilog("./tests/circ1.v")
    simulate('in0', inputs, outs, gates, Change('in0', 1))
    timess, inputNamess, inputValuess, ins = parsestimuli("./utils/file.stim")
    print("Times:", timess)
    print("Input Names:", inputNamess)
    print("Input Values:", inputValuess)    
    print("Instructions", ins)
    
if __name__ == "__main__":
    main()



