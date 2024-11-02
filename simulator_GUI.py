import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog , Canvas
from utils.reading import parseVerilog, parseStimuli
from utils.utils import simulate_g
from utils.structures import Change


class simulator_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Circuit Simulator")
        self.root.geometry("1000x800")

        self.gates = {}
        self.inputs = {}
        self.outputs = {}
        self.instructions = []
        self.ins = {}
        self.circuit_file = None
        self.stimuli_file = None


         # Frame for control buttons and output box
        control_frame = tk.Frame(root)
        control_frame.pack(fill=tk.BOTH, expand=True)


        Verilog_button = tk.Button(root, text="Add Verilog file", command=self.open_file_dialog_V).pack(pady=10)
        #Verilog_button.grid(row=0, column=2, columnspan=2)
        Stim_button = tk.Button(root, text="Add Stimuli file", command=self.open_file_dialog_S).pack(pady=10)
        #Stim_button.grid(row=1, column=2, columnspan=2)
        start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation).pack(pady=10)
        #start_button.grid(row=2, column=2, columnspan=2)


        tk.Label(root, text="Simulation Terminal:").pack(pady=5)
        self.output_box = scrolledtext.ScrolledText(root, width=100, height=10, state='disabled')
        self.output_box.pack()

        self.canvas = tk.Canvas(root, width=800, height=300, bg="white")
        self.canvas.pack(pady=10, fill=tk.BOTH, expand=True) 
        self.canvas.bind("<Button-1>", self.on_canvas_click)



    def open_file_dialog_V(self):
        file_path = filedialog.askopenfilename(filetypes=[("Verilog Files", "*.v")])
        if file_path:
            self.circuit_file = file_path
            self.inputs, self.outputs, self.gates, self.ins = parseVerilog(file_path)
            print("parsed v",self.inputs, self.outputs, self.gates, self.ins)
            self.display_circuit()
            

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

        print("\n\nstarting simulation\n\n")
        simfile = "./utils/simulations/sim3.sim"
        try: 
            results =  simulate_g(self.instructions, self.ins, self.outputs, self.gates)
        except Exception as e:
            print("\n\nerror", e)
            return
        
        for result in results:
            self.output_box.insert(tk.END, result + "\n")

        self.output_box.config(state='disabled')
        print("\n\nsimulation done\n\n")



    def display_circuit(self):
        # Clear the canvas
        self.canvas.delete("all")
        
        element_positions = {}  # Stores positions of each input, gate, and output

        # Step 1: Arrange inputs vertically on the left
        x, y = 50, 50
        input_positions = {}
        for input_name in self.inputs:
            self.canvas.create_oval(x, y, x + 20, y + 20, fill="blue", tags=input_name)
            self.canvas.create_text(x + 10, y + 35, text=input_name)
            element_positions[input_name] = (x + 10, y + 10)
            input_positions[input_name] = y  # Save y-position for layout reference
            y += 70  # Space inputs vertically

        # Step 2: Arrange gates in vertical columns based on their dependencies
        x = 200  # Starting x-position for gates
        gate_layer_positions = {}  # Track vertical layers for gates
        for gate_name, gate_instance in self.gates.items():
            gate_type = type(gate_instance).__name__
            
            # Place gate vertically aligned with its inputs
            input_wires = gate_instance.inputs  # Assume this returns list of input wires for the gate
            if input_wires:
                # Position gate based on the y-average of its input wires
                input_y_positions = [input_positions[wire] for wire in input_wires if wire in input_positions]
                if input_y_positions:
                    y = sum(input_y_positions) // len(input_y_positions)  # Center gate vertically on inputs
                else:
                    y += 70  # If no input reference, stack it below last gate
            else:
                y += 70  # Default vertical position if no inputs found

            # Draw the gate rectangle and label it with gate type
            self.canvas.create_rectangle(x, y, x + 50, y + 30, fill="grey", tags=gate_name)
            self.canvas.create_text(x + 25, y + 15, text=gate_type, fill="white")
            element_positions[gate_name] = (x + 25, y + 15)
            
            # Track this gate's y-position in input_positions for downstream connections
            input_positions[gate_name] = y

            # Advance x-position for next gate layer
            if gate_type != "Output":  # Place each output on the next layer
                x += 100

        # Step 3: Arrange outputs on the right side
        x = 500
        y = 50
        for output_name in self.outputs:
            self.canvas.create_oval(x, y, x + 20, y + 20, fill="green", tags=output_name)
            self.canvas.create_text(x + 10, y + 35, text=output_name)
            element_positions[output_name] = (x + 10, y + 10)
            y += 70

        # Step 4: Draw wires based on connections in `ins`
        for wire, connected_gates in self.ins.items():
            # Get starting position (input or intermediate wire position)
            if wire in element_positions:
                start_x, start_y = element_positions[wire]
            else:
                continue  # If the wire has no known starting position, skip it

            # Draw a line to each connected gate
            for gate_name in connected_gates:
                if gate_name in element_positions:
                    end_x, end_y = element_positions[gate_name]
                    # Draw line for the wire with an arrow for direction
                    self.canvas.create_line(start_x, start_y, end_x, end_y, arrow=tk.LAST, fill="black")



    def on_canvas_click(self, event):
        item = self.canvas.find_closest(event.x, event.y)
        item_tags = self.canvas.gettags(item)

        if item_tags:
            component_name = item_tags[0]
            self.edit_component(component_name)

    def get_clicked_component(self, x, y):
        # Placeholder logic to find the clicked component
        # This would use bounds-checking on each drawn element
        # to see if (x, y) falls within any component's area
        return None  # Placeholder, return the clicked component (e.g., gate or wire)

    def edit_component(self, component_name):
        # Check if component is input, gate, or output, and allow modification accordingly
        if component_name in self.inputs:
            new_value = simpledialog.askinteger("Edit Input", f"Set new value for input {component_name}")
            if new_value is not None:
                # Update input in the simulation data
                self.ins[component_name] = new_value
                self.display_circuit()  # Refresh the display if needed

        elif component_name in self.gates:
            new_delay = simpledialog.askinteger("Edit Gate Delay", f"Set new delay for gate {component_name}")
            if new_delay is not None:
                # Update gate delay in the simulation data
                self.gates[component_name].delay = new_delay
                self.display_circuit()  # Refresh the display if needed

        elif component_name in self.outputs:
            messagebox.showinfo("Output", f"Output {component_name} is not editable.")

root = tk.Tk()
app = simulator_GUI(root)
root.mainloop()
    #0ther features
    #canvas for circuit display
    #create a terminal (or something similar)
    #

