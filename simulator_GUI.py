import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, scrolledtext
from utils.reading import parseVerilog, parsestimuli
from utils.utils import simulate
from utils.structures import Change


class simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Circuit Simulator")
        self.root.geometry("600x400")


        self.circuit_file = None
        self.stimuli_file = None


        Verilog_button = tk.Button(root, text="Add Verilog fule", command=self.open_file_dialog_V).pack(pady=10)
        #Verilog_button.grid(row=0, column=2, columnspan=2)
        Stim_button = tk.Button(root, text="Add Stimuli file", command=self.open_file_dialog_S).pack(pady=10)
        #Stim_button.grid(row=1, column=2, columnspan=2)
        start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation).pack(pady=10)
        #start_button.grid(row=2, column=2, columnspan=2)


        self.gates = {}
        self.inputs = {}
        self.outputs = []
        self.instructions = []
        self.ins = []

        tk.Label(root, text="Simulation terminal:").pack(pady=5)
        self.output_box = scrolledtext.ScrolledText(root, width=70, height=15, state='disabled')
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
            self.instructions = parsestimuli(file_path)
            print("parsed s",self.instructions)
            

    def start_simulation(self):
        if not self.circuit_file or not self.stimuli_file:
            messagebox.showwarning("Warning", "Add circuit and stimuli files and try again.")
            return
        print("starting simulation")
       
        self.output_box.config(state='normal')
        self.output_box.delete(1.0, tk.END)

        
        results = simulate(self.instructions, self.inputs, self.outputs, self.gates)
        for result in results:
            self.output_box.insert(tk.END, result + "\n")

        self.output_box.config(state='disabled')  # Disable editing of the output box

        # print(self.instructions, "/n", self.inputs, self.outputs, self.gates)
        # simulate(self.instructions, self.inputs, self.outputs, self.gates)
        
        # messagebox.showinfo("final", self.outputs)

root = tk.Tk()
app = simulator_GUI(root)
root.mainloop()
    #0ther features
    #canvas for circuit display
    #create a terminal (or something similar)
    #

