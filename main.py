from utils.reading import parseVerilog
from utils.utils import printPath

def main():
    ins, outs, gates, inputs = parseVerilog("./tests/circ1.v")
    printPath('sel0', inputs, outs, gates)


if __name__ == "__main__":
    main()