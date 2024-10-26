import tkinter as tk
import tkinter.ttk as ttk
from utils.utils import simulate

root = tk.Tk() 
root.title("Logic Circuit Simulator")

frame = ttk.Frame(root, padding="30") 
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  
 

Label_A = tk.Label(frame, text="Input A:")
Label_A.grid(row=0, column=0)
Entry_A = tk.Entry(frame)
Entry_A.grid(row=0, column=1)
 


Label_B = tk.Label(frame, text="Input B:")
Label_B.grid(row=1, column=0)
Entry_B = tk.Entry(frame)
Entry_B.grid(row=1, column=1)


Label_C = tk.Label(frame, text="Input C:")
Label_C.grid(row=2, column=0)
Entry_C = tk.Entry(frame)
Entry_C.grid(row=2, column=1)

#work on the function simulate to fix the parameters issue
start_button = tk.Button(frame, text="Start Simulation", command=simulate)
start_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
