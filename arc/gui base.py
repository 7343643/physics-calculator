from tkinter import *

class gui():
    def __init__(self):
        self.gui_frame = Frame(padx=10, pady=10)
        self.gui_frame.grid()

        self.top_button = Button(self.gui_frame, text="Button",
                                 bg="#808080",fg="#FFFFFF", 
                                 font=("Arial", "12", "bold"),
                                  width=10, command="")
        self.top_button.grid(sticky="w")

        self.gui_heading = Label(self.gui_frame,
                                 text=("Title"),
                                 font=("Arial", "16", "bold"))
        self.gui_heading.grid(row=0,column=0,padx=250,pady=5)

        self.button_frame = Frame(self.gui_frame)
        self.button_frame.grid(row=1)

        #button details. text|command|bg code|row|column
        button_detail_list = [
            ["text", "", "#808080", 0, 0],
            ["text", "", "#808080", 0, 1],
            ["text", "", "#808080", 1, 0],
            ["text", "", "#808080", 1, 1]
        ]

        self.button_ref_list = []

        for item in button_detail_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[2],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=15, command=item[1])
            self.make_button.grid(row=item[3],column=item[4],padx=5,pady=5)
            self.button_ref_list.append(self.make_button)

if __name__ == "__main__":
    root = Tk()
    root.title("Gui Name")
    gui()
    root.mainloop()
