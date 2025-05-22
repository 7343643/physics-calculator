#imports the module i use for gui
from tkinter import *

class processor():
    #this function contains all the infomation on how the program is to draw the gui
    def __init__(self):
        self.proc_frame = Frame(padx=10, pady=10)
        self.proc_frame.grid()

        #this is what makes the settings button]
        self.set_button = Button(self.proc_frame, text="Settings",
                                 bg="#808080",fg="#FFFFFF", 
                                 font=("Arial", "12", "bold"),
                                  width=10, command="")
        
        self.set_button.grid(sticky="w")
        #this is what sets the title on the gui
        self.proc_heading = Label(self.proc_frame,
                                  text="uncertainties processor",
                                  font=("Arial", "16", "bold"))
        self.proc_heading.grid(padx=150, pady=5)
        #the following variable contains the instructions displayed on the gui
        instructions = ("please input the uncertaintie you want processed in the box below"
                        "then press the button that has the method you want to use to process it"
                        "or if you want to calculate eqautions presss the back button")
        
        self.proc_instructions = Label(self.proc_frame, text=instructions,
                                       wraplength=250, width=40, 
                                       justify="left"
                                       )
        self.proc_instructions.grid(row=2)

        #this makes the box where the user inputs their uncertainties
        self.proc_entry = Entry(self.proc_frame, font=("Arial", "14"))
        self.proc_entry.grid(row=3, padx=10, pady=10)

        #this makes the error message that appears below the box
        error = "please insert the uncertaintie you want processed"
        self.proc_error = Label(self.proc_frame, text=error,
                                fg="#9c0000")
        self.proc_error.grid(row=4, padx=5, pady=5)
        #this creates the frame that the buttons to process uncertainties will be placed on
        self.button_frame = Frame(self.proc_frame)
        self.button_frame.grid(row=5)
        #button list that holds the infomation for the buttons
        #(button text| command| row| column)
        button_details_list = [
            ["square relationship", "", 0, 0],
            ["square root relationship", "", 0, 1],
            ["inverse relationship", "", 1, 0],
            ["inverse square relationship", "", 1, 1]
        ]
        #list to hold buttons once they have been made
        self.button_ref_list = []

        #this is what makes the buttons
        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg="#0000FF",
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=22, command=item[1],                                                                     
                                      )
            self.make_button.grid(row=item[2], column=item[3], padx=5, pady=5)
        
            self.button_ref_list.append(self.make_button)
        #this makes the back button
        self.back_button = Button(self.proc_frame,
                                  text="Back", fg="#FFFFFF",
                                   bg="#006400",command="",
                                    font=("Arial", "16", "bold"),
                                    width=15)
        self.back_button.grid(row=6)




if __name__ == "__main__":
    root = Tk()
    root.title("uncertainies processor")
    processor()
    root.mainloop()
