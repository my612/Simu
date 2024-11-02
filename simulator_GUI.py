import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog , Canvas
from utils.reading import parseVerilog, parseStimuli
from utils.utils import simulate_g, simulate
from utils.structures import Change


class simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Circuit Simulator")
        self.root.geometry("1000x1200")
        #intializing the variables
        self.gates = {}
        self.inputs = {}
        self.outputs = {}
        self.instructions = []
        self.ins = {}
        self.circuit_file = None
        self.stimuli_file = None

       #
        tk.Label(root, text="Logic Circuit Simulator", font=("Helvetica", 16)).pack(pady=10)
        Verilog_button = tk.Button(root, text="Add Verilog file", command=self.open_file_dialog_V).pack(pady=10)
        Stim_button = tk.Button(root, text="Add Stimuli file", command=self.open_file_dialog_S).pack(pady=10)
        start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation).pack(pady=10)

        
        tk.Label(root, text="Simulation Terminal:").pack(pady=5)
        self.output_box = scrolledtext.ScrolledText(root, width=100, height=10, state='disabled')
        self.output_box.pack()


       
     

    def open_file_dialog_V(self):
        file_path = filedialog.askopenfilename(filetypes=[("Verilog Files", "*.v")])
        if file_path:
            self.circuit_file = file_path
            self.inputs, self.outputs, self.gates, self.ins = parseVerilog(file_path)
            print("parsed v",self.inputs, self.outputs, self.gates, self.ins)
           

    def open_file_dialog_S(self):
        file_path = filedialog.askopenfilename(filetypes=[("Stimuli Files", "*.stim")])
        if file_path:
            self.stimuli_file = file_path
            self.instructions = parseStimuli(file_path)
            print("parsed s",self.instructions)
            

    def start_simulation(self):
        if not self.circuit_file or not self.stimuli_file:
            messagebox.showwarning("Warning", "Add circuit and stimuli files and try again.")
            return
        
        self.output_box.config(state='normal')
        self.output_box.delete(1.0, tk.END)

        print("\nstarting simulation\n")
        simfile = "./utils/simulations/sim_g.sim"
        try: 
            results =  simulate_g(self.instructions, self.ins, self.outputs, self.gates)
            simulate(self.instructions, self.ins, self.outputs, self.gates, simfile)
        except Exception as e:
            print("\n\nerror", e)
            return
        
        for result in results:
            self.output_box.insert(tk.END, result + "\n")

        self.output_box.insert(tk.END, "Simulation done!")
        self.output_box.config(state='disabled')
        print("\n\nsimulation done\n\n")
        


# parsing : parsed v ['in0', 'in1', 'en'] {'o0': None, 'o1': None, 'o2': None, 'o3': None} 
# {'g1': <utils.gates.NOT object at 0x000001AD6FBAEE40>, 'g2': <utils.gates.NOT object at 0x000001AD717D07D0>,
#  'g3': <utils.gates.AND object at 0x000001AD6FBAEF90>, 'g4': <utils.gates.AND object at 0x000001AD717D0910>, 
# 'g5': <utils.gates.AND object at 0x000001AD717D0A50>, 'g6': <utils.gates.AND object at 0x000001AD6FC2C510>, 
# 'g7': <utils.gates.AND object at 0x000001AD6FC2D220>, 'g8': <utils.gates.AND object at 0x000001AD6F849370>, 
# 'g9': <utils.gates.AND object at 0x000001AD6FC149E0>, 'g10': <utils.gates.AND object at 0x000001AD6FC15E10>}
#  {'in0': ['g1', 'g5', 'g9'], 'in1': ['g2', 'g7', 'g9'], 'en': ['g4', 'g6', 'g8', 'g10'], 'w0': ['g3', 'g7'], 
# 'w1': ['g3', 'g5'], 'w2': ['g4'], 'w3': ['g6'], 'w4': ['g8'], 'w5': ['g10']}
 
 
root = tk.Tk()
app = simulator_GUI(root)
root.mainloop()
    #0ther features
    #canvas for circuit display
    #create a terminal (or something similar)
    #

