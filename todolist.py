import tkinter as tk
from tkinter import messagebox, font

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

is_dark = True   # change to False for light mode

light_bg = "#ffffff"
dark_bg = "#121212"
bg_color = dark_bg if is_dark else light_bg
fg_color = "#FF0000"  # 🔴 Bold red text for tasks

root.configure(bg=bg_color)

custom_font = font.Font(family="Segoe UI", size=13, weight="bold")

task_listbox = tk.Listbox(root, width=40, height=15, bg=bg_color,
                          fg=fg_color, font=custom_font,
                          selectbackground="#0066FF",   # 🔵 Bright blue highlight
                          selectforeground="white", bd=0, highlightthickness=0)
task_listbox.pack(pady=20)

entry = tk.Entry(root, width=30, font=("Segoe UI", 12, "bold"),
                 bg="#222222" if is_dark else "#eeeeee",
                 fg="#0066FF", insertbackground="#0066FF", relief="flat")  # 🔵 Bold blue input text
entry.pack(pady=10)

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task first!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

btn_style = {"width": 18, "font": ("Segoe UI", 11, "bold"), "relief": "flat", "pady": 5}

add_button = tk.Button(root, text="➕ Add Task", bg="#00C853", fg="white", activebackground="#00E676", activeforeground="black", **btn_style, command=add_task)  
add_button.pack(pady=5)

delete_button = tk.Button(root, text="🗑 Delete Task", bg="#D50000", fg="white", activebackground="#FF1744", activeforeground="black", **btn_style, command=delete_task)  
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="🧹 Clear All", bg="#2962FF", fg="white", activebackground="#448AFF", activeforeground="black", **btn_style, command=clear_tasks)  
clear_button.pack(pady=5)

root.mainloop()
