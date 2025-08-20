import tkinter as tk
from tkinter import font
import math

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("480x720")
root.configure(bg="#121212")

display_font = font.Font(family="Segoe UI", size=32, weight="bold")
button_font = font.Font(family="Segoe UI", size=18, weight="bold")

btn_colors = {
    "nums": "#424242",
    "ops": "#FF9800",
    "spec": "#4CAF50",
    "sci": "#9C27B0",
}

equation = tk.StringVar()
display = tk.Entry(root, textvariable=equation, font=display_font,
                   bg="#1c1c1c", fg="#FFFFFF", insertbackground="white",
                   justify="right", bd=20, relief="flat")
display.pack(fill="both", ipadx=10, ipady=25, padx=10, pady=20)

def press(key):
    equation.set(equation.get() + str(key))

def clear():
    equation.set("")

def calculate():
    try:
        expr = equation.get()
        
        replacements = {
            '÷': '/',
            '×': '*',
            'π': 'math.pi',
            'e': 'math.e',
            '√': 'math.sqrt',
            'xʸ': '**',
            'log(': 'math.log10(',
            'sin(': 'math.sin(math.radians(',
            'cos(': 'math.cos(math.radians(',
            'tan(': 'math.tan(math.radians('
        }
        
        for key, value in replacements.items():
            expr = expr.replace(key, value)
            
        result = str(eval(expr, {"__builtins__": None}, math.__dict__))
        equation.set(result)
        
    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        equation.set("Error")

button_frame = tk.Frame(root, bg="#121212")
button_frame.pack()

buttons = [
    ("7", "nums"), ("8", "nums"), ("9", "nums"), ("÷", "ops"),
    ("4", "nums"), ("5", "nums"), ("6", "nums"), ("×", "ops"),
    ("1", "nums"), ("2", "nums"), ("3", "nums"), ("-", "ops"),
    ("0", "nums"), (".", "nums"), ("=", "spec"), ("+", "ops"),
    ("(", "ops"), (")", "ops"), ("xʸ", "ops"), ("%", "ops"),
    ("√(", "sci"), ("log(", "sci"), ("sin(", "sci"), ("cos(", "sci"),
    ("tan(", "sci"), ("π", "sci"), ("e", "sci")
]

row, col = 0, 0
for (text, kind) in buttons:
    action = lambda x=text: press(x) if x != "=" else calculate()
    
    btn = tk.Button(button_frame, text=text, command=action,
                    font=button_font, width=5, height=2,
                    bg=btn_colors[kind], fg="white", relief="flat",
                    activebackground="#BDBDBD", activeforeground="black")
    
    btn.grid(row=row, column=col, padx=8, pady=8)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="Clear", command=clear,
                         font=button_font, width=28, height=2,
                         bg="#D32F2F", fg="white", relief="flat",
                         activebackground="#BDBDBD", activeforeground="black")
clear_button.pack(pady=20)

root.mainloop()
