import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        simple_interest = (principal * rate * time) / 100

        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        label_result.config(
            text=f"Simple Interest: ${simple_interest:.2f}\nCompound Interest: ${compound_interest:.2f}"
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Principal Amount ($):").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time Period (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

root.mainloop()