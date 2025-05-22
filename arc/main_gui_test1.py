#imports the module i use for gui
from tkinter import *

class calculator():
    
    #i think this is what starts the gui
    def __init__(self):
        self.calc_frame = Frame(padx=10, pady=10)
        self.calc_frame.grid()

        #this adds the text physics calculator to the window of the program
        self.calc_heading = Label(self.calc_frame,
                                   text="Physics Calculator",
                                   font=("Arial", "16", "bold")
                                   )

        self.calc_heading.grid(row=0)
        #this is what will be displayed on the window after the tiltle
        instructions = ("please enter the equation you want solved in the box below"
        "then press calculate, or if you want to process uncertainties press the"
        "process uncertainties button")

        self.calc_instructions = Label(self.calc_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.calc_instructions.grid(row=1)

        #this makes the box where the user will input the equation they want solved
        self.calc_entry = Entry(self.calc_frame, font=("Arial", "14")
                                )
        self.calc_entry.grid (row=2, padx=10, pady=10)
        
        #this is the error/ awnser text and what displays it
        error = "please enter an equation"
        self.calc_error = Label(self.calc_frame, text=error,
                                fg="#9c0000")
        self.calc_error.grid(row=3)

        #this is for all the buttons on the page except the settings button
        self.button_frame = Frame(self.calc_frame)
        self.button_frame.grid(row=4)

        #this is the uncertainties processor button
        self.to_unc_button = Button(self.button_frame, text="uncertaties processor",
                                 bg="#990099", fg="#ffffff",
                                 font=("Arial", "12", "bold"), width=20)
        
        self.to_unc_button.grid(row=0, column=0, padx=5, pady=5)
        #this is the calculate button
        self.calc_button = Button(self.button_frame, text="calculate",
                                 bg="#009900", fg="#ffffff",
                                 font=("Arial", "12", "bold"), width=20)
        
        self.calc_button.grid(row=0, column=1, padx=5, pady=5)

        #this is the help/info button
        self.to_info_button = Button(self.button_frame, text="Help/information",
                                 bg="#CC6600", fg="#ffffff",
                                 font=("Arial", "12", "bold"), width=20)
        
        self.to_info_button.grid(row=1, column=0, padx=5, pady=5)

        #this is the history/export button
        self.to_history_button = Button(self.button_frame, text="History/export",
                                 bg="#004C99", fg="#ffffff",
                                 font=("Arial", "12", "bold"), width=20)
        
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


#this what runs the gui
if __name__ == "__main__":
    root = Tk()
    root.title("Physics Calculator")
    calculator()
    #think this is what keeps the gui up
    root.mainloop()