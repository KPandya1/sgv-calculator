import tkinter as tk
from tkinter import messagebox
from main import players, calculate_sgv

def get_score():
    name = entry.get()
    if name in players:
        player_data = players[name]
        score = calculate_sgv(players[name])
        commentary = player_data.get("commentary", "No commentary available.")
        result_label.config(text=f"{name}'s SGV: {score}")
        commentary_label.config(text=f"{commentary}")
    else:
        messagebox.showerror("Error", "Player not found!")
        commentary_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("SGV Calculator")

tk.Label(root, text="Enter Player Name:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate", command=get_score).pack()
result_label = tk.Label(root, text="")
result_label.pack()
commentary_label = tk.Label(root, text="", wraplength=400, justify="left")
commentary_label.pack(pady=5)

root.mainloop()