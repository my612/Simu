from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import simulatePath, simulate
from utils.reading import parseStimuli
from utils.waveform import waveform
import simulator_GUI
import tkinter as tk


#TODO adjust for the case when there's a space between the parameters.
#TODO Find a way to pass the output into another gate
#TODO CLEAN THE CODE (Unwanted comments, print statements, etc)
from simulator_GUI import simulator_GUI
import tkinter as tk
def main():
    
    root = tk.Tk()
    app = simulator_GUI(root)
    root.mainloop()
    # ins, outs, gates, inputs = parseVerilog(
    #     "./tests/circ3.v"   
    # )
    # waveform("./utils/simulations/sim3.sim", ins, list(outs.keys()))
    root = tk.Tk()
    app = simulator_GUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()

