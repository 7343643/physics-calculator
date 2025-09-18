from tkinter import*
from tkinter import ttk

class main:
    def __init__(self,root):     
        root.title("main")

        self.mainframe = ttk.Frame(root)
        self.mainframe.pack

        self.heading = ttk.Label(text="TITLE")
        self.heading.pack



root = Tk()

main(root)
root.mainloop()