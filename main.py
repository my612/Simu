from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import printPath, simulatePath


def main():
    ins, outs, gates, inputs = parseVerilog(
        "/media/nicolas/New Volume/DD1 Project 1/DD1-project1/tests/circ6.v"
    )
    simulatePath(inputs, outs, gates, Change("C", 1))
    print(gates["g2"].value())


if __name__ == "__main__":
    main()
