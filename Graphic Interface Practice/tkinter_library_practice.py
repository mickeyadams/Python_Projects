import tkinter as tk

root = tk.Tk()

root.geometry("600x400")
root.title("MY FIRST GUI")


label = tk.Label(root, text="GRAPHIC USER INTERFACE", font=('Arial', 12))
label.pack(padx=30, pady=30)

button = tk.Button(root, text="CLICK ME :)", font=('Arial', 12))
button.pack()


root.mainloop()