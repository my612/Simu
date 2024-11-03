import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox, scrolledtext
from utils.reading import parseVerilog, parseStimuli
from utils.utils import simulateBFS
from utils.waveform import waveform


class simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Circuit Simulator")
        self.root.geometry("1000x600")

        # intializing the variables
        self.gates = {}
        self.inputs = {}
        self.outputs = {}
        self.instructions = []
        self.ins = {}
        self.circuit_file = None
        self.stimuli_file = None

        #Adding the GUI components
        tk.Label(root, text="Logic Circuit Simulator", font=("Helvetica", 16)).pack(
            pady=10
        ) 
        Verilog_button = tk.Button(
            root, text="Add Verilog file", command=self.open_file_dialog_V
        ).pack(pady=10) #Adding the button to add the verilog file
        Stim_button = tk.Button(
            root, text="Add Stimuli file", command=self.open_file_dialog_S
        ).pack(pady=10) #Adding the button to add the stimuli file
        start_button = tk.Button(
            root, text="Start Simulation", command=self.start_simulation
        ).pack(pady=10) #Adding the button to start the simulation
        waveform_button = tk.Button(
            root, text="Show Waveform", command=self.show_waveform
        ).pack(pady=10) #Adding the button to show the waveform

        tk.Label(root, text="Simulation Terminal:").pack(pady=5)
        self.output_box = scrolledtext.ScrolledText(
            root, width=100, height=15, state="disabled"
        ) #Adding the output box
        self.output_box.pack()

    def open_file_dialog_V(self): #Function to open the file dialog for the verilog file
        file_path = filedialog.askopenfilename(filetypes=[("Verilog Files", "*.v")])
        if file_path:
            self.circuit_file = file_path
            self.inputs, self.outputs, self.gates, self.ins = parseVerilog(file_path)
            print("parsed v", self.inputs, self.outputs, self.gates, self.ins)

    def open_file_dialog_S(self): #Function to open the file dialog for the stimuli file
        file_path = filedialog.askopenfilename(filetypes=[("Stimuli Files", "*.stim")])
        if file_path:
            self.stimuli_file = file_path
            self.instructions = parseStimuli(file_path)
            print("parsed s", self.instructions)

    def start_simulation(self): #Function to start the simulation calling the simulateBFS function 
        if not self.circuit_file or not self.stimuli_file:
            messagebox.showwarning( #If the files are not added, show a warning
                "Warning", "Add circuit and stimuli files and try again."
            )
            return
        # Clear the output box before showing the results of the simulation
        self.output_box.config(state="normal")
        self.output_box.delete(1.0, tk.END)

        print("\nstarting simulation\n")
        simfile = "./simulations/sim_g.sim"

        try:
            # results =  simulate_g(self.instructions, self.ins, self.outputs, self.gates)
            # simulate(self.instructions, self.ins, self.outputs, self.gates, simfile)
            results = simulateBFS( #Calling the simulateBFS function
                self.instructions, self.ins, self.outputs, self.gates, simfile
            )
        except Exception as e: #If there is an error, print the error
            print("\n\nerror", e)
            return

        for result in results: #Print the results in the output box
            self.output_box.insert(tk.END, result + "\n")
        self.output_box.insert(tk.END, "Simulation done!") #Print simulation done in the output box after exisiting the for loop
        self.output_box.config(state="disabled")
        print("\n\nsimulation done\n\n")
    
    
    
    def show_waveform(self): #Function to show the waveform calling the waveform function
        if not self.circuit_file or not self.stimuli_file:
            messagebox.showwarning( #If the files are not added, show a warning
                "Warning", "Add circuit and stimuli files and try again."
            )
            return
        simfile = "./simulations/sim_g.sim" 
        waveform(simfile, self.inputs, self.outputs) 
