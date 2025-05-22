#imports the module i am using to create the gui
from tkinter import *

class settings():

    #this is the function that contains the gui
    def __init__(self):
        self.sett_frame = Frame(padx=10, pady=10)
        self.sett_frame.grid()

        #this is the back button that is used to return to the main page
        self.back_button = Button(self.sett_frame,
                                  text="back", bg="#808080",
                                  fg="#FFFFFF", font=("Arial", "12", "bold"),
                                  width=10, command="")
        
        self.back_button.grid(row=0, column=0, padx=10, pady=10)
        
        #this adds text at the top of the window
        self.sett_title = Label(self.sett_frame,
                                text="Settings", font=("Arial", "16", "bold"))
        
        self.sett_title.grid(column=1, row=0, padx=10, pady=5)

        #this is the frame for all the settings buttons
        self.button_frame = Frame(self.sett_frame)
        self.button_frame.grid(row=2)
        
        #this list holds the colors used by the buttons green is 0 red is 1
        shared_button_colors = ["#32CD32", "#FF0000" ]
        #this holds the rest of the buttons infomation
        #it is formatted as Text|Color|Command|Row
        button_detail_list = [
            ["show uncertainties in history", 0, "", 0],
            ["show calculations in history", 0, "", 1],
            ["Round to correct number of significant figures", 1, "", 2],
            ["colorblind mode", 1, "", 3]
        ]
        #list to hold the buttons once they are made
        self.button_ref_list = []
        for item in button_detail_list:
            temp = item[1]

            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=shared_button_colors[temp],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=20, command=item[2])
            self.make_button.grid(row=item[3], padx=50, pady=5)





if __name__ == "__main__":
    root = Tk()
    root.title("Physics Calc Settings")
    settings()
    root.mainloop()