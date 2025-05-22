#imports the module i use for gui

from tkinter import *
import webbrowser





class calculator():
    
    #i think this is what starts the gui
    def __init__(self):
        global setting_run
        setting_run = False
        
        def set_button():
            global setting_run
            setting_run = TRUE
            root.destroy()
        self.calc_frame = Frame(padx=10, pady=10)
        self.calc_frame.grid()
        def open_sauce():
            webbrowser.open('https://github.com/')
        
        #this is what makes the settings button
        self.settings_button = Button(self.calc_frame,
                                      text="settings", bg="#808080",
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=10, command=set_button)
        self.settings_button.grid(sticky="w")

        #this adds the text physics calculator to the window of the program
        self.calc_heading = Label(self.calc_frame,
                                   text="Physics Calculator",
                                   font=("Arial", "16", "bold")
                                   )

        self.calc_heading.grid(padx=150,row=0, column=0)

        #this is what will be displayed on the window after the tiltle
        instructions = ("please enter the equation you want solved in the box below"
        "then press calculate, if you need help understanding the program"
        "or are unsure how to format the equations press the help/info button")

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

        #button list (button text | bg color | command | row | column) this is basically the infomation for the buttons
        button_details_list = [
            ["calculate", "#009900", "", 0, 0],
            ["github repo", "#87CEEB", open_sauce, 0, 1],
            ["Help / infomation", "#CC6600", "", 1, 0],
            ["History / Export", "#800080", "", 1, 1]
        ]

        #list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=20, command=item[2],                                                                     
                                      )
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
        
            self.button_ref_list.append(self.make_button)
        
        #this retrieves the history / export button and disables it at startup
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)



#this what runs the g
def run():
    #if __name__ == "__main__":
    global root
    root = Tk()
    root.title("Physics Calculator")
    calculator()
    root.mainloop()
