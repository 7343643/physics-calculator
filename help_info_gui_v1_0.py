#imports the module used for the gui
from tkinter import *
#this defines help as a class, this class is used to contain all the info for the gui
class help():
    def __init__(self):
        #this sets the bak variable to global an makes it false
        global bak
        bak = False
        #this sets bak to true and destroys the gui when it is called
        def back_but():
            global bak
            bak = True
            root.destroy()
        self.help_frame = Frame(padx=10, pady=10)
        self.help_frame.grid()
        #this makes the back button that calls the back_but function when pressed
        self.top_button = Button(self.help_frame, text="back",
                                 bg="#808080",fg="#FFFFFF", 
                                 font=("Arial", "12", "bold"),
                                  width=10, command=back_but)
        self.top_button.grid(sticky="w")
        #this is a variable with the words that are to be displayed on the gui
        words = "formatting: if you want to do square roots you need to write them as sqrt(6) " \
        "and replace 6 with the number you want to get the square root of, "
        #this makes a title for the gui
        self.help_heading = Label(self.help_frame,
                                 text=("help/info"),
                                 font=("Arial", "16", "bold"))
        self.help_heading.grid(row=0,column=0,padx=250,pady=5)
        #this is what adds the main text which is contained within the words variables
        self.help_info = Label(self.help_frame,
                               text=(words),
                               font=("Arial","10"))
        self.help_info.grid(row=1)

       
#this makes a function that when run starts the gui     
def run_help():
    global root
    root = Tk()
    root.title("help Name")
    help()
    root.mainloop()
