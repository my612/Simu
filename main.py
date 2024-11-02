from utils.reading import parseVerilog
from utils.structures import Change
from utils.utils import simulatePath, simulate
from utils.reading import parseStimuli
from utils.waveform import waveform
import utils.simulator_GUI as simulator_GUI
import tkinter as tk


from utils.simulator_GUI import simulator_GUI
import tkinter as tk
def main():
    root = tk.Tk()
    app = simulator_GUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()

