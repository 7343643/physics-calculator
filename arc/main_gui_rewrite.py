#version 1.1.2

#imports the module i use for gui
from tkinter import *

from tkinter import ttk
from calculator import *
import webbrowser
#defines calculator as a class, this class contains all the info for the gui
class calculator:
    
    #this runs the contained code when the class is called
    def __init__(self,root):
        root.title("Physics Calculator")
        
        #this sets all the runner variable to global
        global setting_run
        global hist_run
        global help_info_run
        #this sets all the runner variable to false so that when the gui is closed by the user another one doesn't open
        hist_run = False
        setting_run = False
        help_info_run = False
        #this grab the input from the box in the gui when called
        question=StringVar()
        #this close the main gui and set the setting_run variable to true when called
        def set_button():
            global setting_run
            setting_run = TRUE
            root.destroy()
        #this close the main gui and set the hist_run variable to true when called
        def hist_button():
            global hist_run
            hist_run = True
            root.destroy()
        #this opens the github page for the project when called
        def open_sauce():
            webbrowser.open('https://github.com/7343643/physics-calculator')
        #this close the main gui and set the help_info_run variable to  true when called
        def help_button():
            global help_info_run
            help_info_run = True
            root.destroy()
        #this proccesses the input the user put in the box and returns an awnser when called
        
        def calc():
            quest = question.get()
            process(quest)
            from calculator import works
            #this checks if the works variable is true and if it is enables the history button
            if works == True:
                self.to_history_button = self.button_ref_list[3].config(state=ACTIVE)
            from calculator import result
            str(result)
            global error
            error = "the awnser is "+str(result)
            self.calc_error.config(text=error)
            question.set("")
        
        
        
        
        content = ttk.Frame(root)
        
        content.grid(column=0, row=0, sticky=(N,S,E,W))
        #content.pack(expand=1,fill=BOTH)
        
        instructions = ("please enter the equation you want solved in the box below "
        "then press calculate, if you need help understanding the program "
        "or are unsure how to format the equations press the help/info button")
        
        self.settings_button = ttk.Button(content,
                                      text="settings", command=set_button,
                                      )
        
        self.settings_button.grid(column=0,row=0,sticky="W")
        
        #self.settings_button.pack(expand=1,anchor=NW)
        #this adds the text physics calculator to the window of the program
        self.calc_heading = ttk.Label(content,
                                   text="Physics Calculator",
                                   font=("Arial",16,"bold"))
       
        self.calc_heading.grid(padx=150,row=0, column=1,sticky=(N))
        #self.calc_heading.pack(expand=1)
        #this is what will be displayed on the window after the tiltle
        
        self.calc_instructions = ttk.Label(content,
                                       text=instructions,wraplength=250,
                                       justify="left",anchor=CENTER)
        self.calc_instructions.grid(row=1,column=1, sticky=(N,S,E,W))
        #self.calc_instructions.pack(expand=1)
        
        #this makes the box where the user will input the equation they want solved
        self.calc_entry = ttk.Entry(content, font=("Arial", "14"),
                                textvariable=question
                                )
        self.calc_entry.grid (row=2,column=1, padx=10, pady=10)
        #self.calc_entry.pack(expand=1)
        #this is the error/ awnser text and what displays it
        error = "please enter an equation"
        self.calc_error = ttk.Label(content, text=error)
        self.calc_error.grid(row=3,column=1)
        #self.calc_error.pack(expand=1)
        #this is for all the buttons on the page except the settings button
        self.button_frame = ttk.Frame(content)
        self.button_frame.grid(row=4,column=1)
        #self.button_frame.pack(expand=1)
        #button list (button text | bg color | command | row | column) this is basically the infomation for the buttons
        button_details_list = [
            ["calculate", "#009900", calc, 0, 0],
            ["github repo", "#87CEEB", open_sauce, 0, 1],
            ["Help / infomation", "#CC6600", help_button, 1, 0],
            ["History / Export", "#800080", hist_button, 1, 1]
        ]

        #list to hold buttons once they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = ttk.Button(self.button_frame,
                                      text=item[0],
                                      width=20, command=item[2],                                                                     
                                      )
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
        
            self.button_ref_list.append(self.make_button)
        
        #this retrieves the history / export button and disables it at startup
        from calculator import works
        if works != True:
          self.to_history_button = self.button_ref_list[3].config(state=DISABLED)
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)
        content.columnconfigure(0,weight=1)
        content.columnconfigure(1,weight=1)
        content.columnconfigure(2,weight=1)
        content.rowconfigure(0,weight=1)
        content.rowconfigure(1,weight=1)
        content.rowconfigure(2,weight=1)
        
        content.rowconfigure(4,weight=1)
#this what runs the gui

root = Tk()
    
    
calculator(root)
root.mainloop()
