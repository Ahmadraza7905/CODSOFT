import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        # Characters to include
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        # Show password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

# GUI Window
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x300")
root.configure(bg="#1e1e1e")  # dark background

# Heading
heading = tk.Label(root, text="PASSWORD GENERATOR", 
                   font=("Arial Black", 16, "bold"), 
                   fg="cyan", bg="#1e1e1e")
heading.pack(pady=10)

# Length input
length_label = tk.Label(root, text="Enter password length:", 
                        font=("Arial", 12), fg="white", bg="#1e1e1e")
length_label.pack(pady=5)

length_entry = tk.Entry(root, font=("Arial", 12), justify="center", width=10, bg="#333", fg="white")
length_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", 
                         font=("Arial", 12, "bold"), 
                         bg="blue", fg="white", activebackground="green", activeforeground="white",
                         relief="raised", bd=3, command=generate_password)
generate_btn.pack(pady=10)

# Output field
password_entry = tk.Entry(root, font=("Arial", 14, "bold"), justify="center", width=25, bg="#222", fg="yellow")
password_entry.pack(pady=10)

# Copy button
copy_btn = tk.Button(root, text="Copy", font=("Arial", 12, "bold"), 
                     bg="red", fg="white", relief="raised", bd=3,
                     command=lambda: root.clipboard_append(password_entry.get()))
copy_btn.pack(pady=5)

root.mainloop()
