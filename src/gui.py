import tkinter as tk
from tkinter import messagebox
from main import players, calculate_sgv

def get_score():
    name = entry.get()
    if name in players:
        score = calculate_sgv(players[name])
        result_label.config(text=f"{name}'s SGV: {score}")
    else:
        messagebox.showerror("Error", "Player not found!")

# GUI Setup
root = tk.Tk()
root.title("SGV Calculator")

tk.Label(root, text="Enter Player Name:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=get_score).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()