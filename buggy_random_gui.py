import tkinter as tk
import random

class RandomNumberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Run/Stop Random Numbers")

        self.running = False
        self.label = tk.Label(root, text="", font=("Arial", 24))
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Run", font=("Arial", 18), width=10, command=self.toggle)
        self.button.pack(pady=10)

        self.button_clicked = False

    def toggle(self):
        if self.running:
            self.running = False
            self.button.config(text="Run")
        else:
            self.running = True
            self.button.config(text="Stop")
            if self.button_clicked:
                self.update_numbers()
            self.button_clicked = True

    def update_numbers(self):
        if self.running:
            num = random.randint(1, 1000)
            self.label.config(text=str(num))
            self.root.after(500, self.update_numbers)

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberApp(root)
    root.mainloop()
