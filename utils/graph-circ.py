import re
import tkinter as tk
from utils.reading import parseVerilog

def draw_circuit(inputs, outputs, gates, ins):
    root = tk.Tk()
    root.title("Logic Circuit")
    root.geometry("1000x600")
    
    canvas = tk.Canvas(root, width=1000, height=600)
    canvas.pack()
    
    # Draw the inputs
    for i, inp in enumerate(inputs):
        canvas.create_oval(50, 50 + 50*i, 100, 100 + 50*i, fill="white")
        canvas.create_text(75, 75 + 50*i, text=inp)
        canvas.create_line(100, 75 + 50*i, 150, 75 + 50*i)  # Line coming out of the input
    
    # Draw the outputs
    for i, out in enumerate(outputs):
        canvas.create_oval(900, 50 + 50*i, 950, 100 + 50*i, fill="white")
        canvas.create_text(925, 75 + 50*i, text=out)
    
    # Draw the gates
    for i, (gate_name, gate) in enumerate(gates.items()):
        canvas.create_rectangle(200, 50 + 50*i, 250, 100 + 50*i, fill="white")
        canvas.create_text(225, 75 + 50*i, text=gate_name)
    
    # Draw the connections
    for wire, connected_gates in ins.items():
        for g in connected_gates:
            gate = gates[g]
            if gate.output_name == wire:
                # Draw a line from the output of the gate to the input of the wire
                canvas.create_line(250, 75 + 50*list(gates.keys()).index(g), 300, 75 + 50*list(inputs.keys()).index(wire))
    
    root.mainloop()

# Parse the Verilog file and draw the circuit
inputs, outputs, gates, ins = parseVerilog("./tests/circ3.v")

draw_circuit(inputs, outputs, gates, ins)