#imports the module used for the gui
from tkinter import *

#makes a class called gui that contains all the infomation for the gui
class gui():
    def __init__(self):
        self.gui_frame = Frame(padx=10, pady=10)
        self.gui_frame.grid()
        #sets two variables to global and makes them false
        global setting_run
        setting_run = False
        global back
        back = False
        #makes a function that when called sets the setting_run variable to true and destroys the gui
        def set_button():
            global setting_run
            setting_run = TRUE
            root.destroy()
        #makes a function that when called sets the back variable to true and destroys the gui
        def back_but():
            global back
            back = True
            root.destroy()
        #this makes the settings button
        self.top_button = Button(self.gui_frame, text="settings",
                                 bg="#808080",fg="#FFFFFF", 
                                 font=("Arial", "12", "bold"),
                                  width=10, command=set_button)
        self.top_button.grid(sticky="w")
        #disables the settings button as the settings isn't fully implemented
        self.top_button.config(state=DISABLED)
        #makes a title and displays it on the gui
        self.gui_heading = Label(self.gui_frame,
                                 text=("History/Export"),
                                 font=("Arial", "16", "bold"))
        self.gui_heading.grid(row=0,column=0,padx=250,pady=5)
        #this variable holds the text that is to be displayed on the gui
        info=("below are your recent calculations, showing 0/0 calcuations"
              "only calculations done this session are avalible")
        
        self.hist_info = Label(self.gui_frame,
                               text=info,font=("Arial","12","bold"),
                               wraplength=250, width=40,
                                       justify="left")
        self.hist_info.grid(row=1)
                
        self.button_frame = Frame(self.gui_frame)
        self.button_frame.grid(row=2)
        #this list contains all the infomation for the buttons
        #button details. text|command|bg code|row|column
        button_detail_list = [
            ["back", back_but, "#808080", 0, 0],
            ["text", "", "#808080", 0, 1],
            #["text", "", "#808080", 1, 0],
            #["text", "", "#808080", 1, 1]
        ]
        #makes a list the will be used to hold all the buttons (execpt the settings button)
        self.button_ref_list = []
        #makes the buttons from the info in the button_detail_list
        for item in button_detail_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[2],
                                      fg="#FFFFFF", font=("Arial", "12", "bold"),
                                      width=15, command=item[1])
            self.make_button.grid(row=item[3],column=item[4],padx=5,pady=5)
            self.button_ref_list.append(self.make_button)
#makes a function that runs the gui when called
def run_hist():
    global root
    root = Tk()
    root.title("Gui Name")
    gui()
    root.mainloop()
