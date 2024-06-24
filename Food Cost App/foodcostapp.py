import tkinter as tk
from tkinter import Canvas
from tkinter import ttk

def move_window(event):  # Moving the window
    root.geometry(f'+{event.x_root}+{event.y_root}')

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):  # Creating a rounded rectangle
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True, fill="#ecf0f1")

class FoodCostCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.apply_styles()
        self.create_widgets()

    def setup_window(self):
        self.root.title("Food Cost Calculator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg='grey')
        self.root.attributes("-transparentcolor", "grey")
        self.root.overrideredirect(1)
        self.root.bind("<B1-Motion>", move_window)
        self.root.eval('tk::PlaceWindow . center')

    def apply_styles(self):
        style = ttk.Style()
        style.configure("Modern.TLabel", background="#ecf0f1", foreground="#2c3e50", font=("Helvetica", 14, "bold"))
        style.configure("Modern.TButton", background="#3498db", foreground="white", font=("Helvetica", 12, "bold"), padding=10)
        style.map("Modern.TButton", background=[('active', '#2980b9')])

    def create_widgets(self):
        global canvas
        canvas = Canvas(self.root, bg="grey", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=1)

        round_rectangle(0, 0, 400, 300, radius=50)

        frame = tk.Frame(canvas, bg="#ecf0f1")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        label = ttk.Label(frame, text="Welcome to the Food Cost Calculator", style="Modern.TLabel")
        label.pack(pady=10)

        button = ttk.Button(frame, text="Get Started", command=self.root.quit, style="Modern.TButton")
        button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodCostCalculatorApp(root)
    root.mainloop()
