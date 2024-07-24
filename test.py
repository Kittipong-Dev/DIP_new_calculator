import tkinter as tk

class MyCalculator:
    def __init__ (self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title('My Calculator')

        self.label = tk.Label(self.root, text="Hello DIP02", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click here", height=4)
        self.button.place(x=3, y=5)

        self.root.mainloop()

if __name__ == "__main__":
    MyCalculator()