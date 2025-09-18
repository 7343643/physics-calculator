#version 1.1

#imports the module used for the gui
from tkinter import *
import datetime
#makes a class called gui that contains all the infomation for the gui
class gui():
    def __init__(self):
        self.gui_frame = Frame(padx=10, pady=10)
        self.gui_frame.grid()
        #sets two variables to global and makes them false
        global setting_run
        setting_run = False
        global back
        global anwsers
        back = False
        #this variable is used to store how many items there are in the awnsers list
        calc = 0
        #this checks how many items are in the awnsers list
        for item in anwsers:
            calc = calc + 1
        #this makes the shown variable equal the calc variable then checks if it is more than 5
        #if it is more than five it sets the shown variable to to 5 and makes the show list equal
        #to the last 5 calculations made. if the calc variable is less than 5 than show is equal to awnsers 
        #this means that no more than 5 awnsers should ever be displayed at once
        shown = calc
        if shown > 5:
            shown = 5
            show = anwsers[-5:]
            print(show)
        else:
            show = anwsers
        #this makes the tree variable global and adds all the calculations that are to be shown to it
        global tree
        tree = ""
        for item in show:
            
            tree = tree + item
        #makes a function that when called sets the setting_run variable to true and destroys the gui
        def set_button():
            global setting_run
            setting_run = True
            root.destroy()
        #makes a function that when called sets the back variable to true and destroys the gui
        def back_but():
            global back
            back = True
            root.destroy()
        #makes a function that when called grabs the current time, makes a file with the name of the current time
        #then writes all the calculations the user has made to the file 
        def export():
            global anwsers
            time = datetime.datetime.now()
            name = time.strftime("%c")
            open(name,"x")
            with open(name,"a") as f:
                for item in anwsers:
                    f.write(item)
                f.close()
            #this opens the files file which stores the name of all the files made by the export program so they can be easily deleted
            with open("files","a") as t:
                t.write(name+"\n")
        
        #this makes the settings button
        self.top_button = Button(self.gui_frame, text="settings",
                                 bg="#808080",fg="#FFFFFF", 
                                 font=("Arial", "12", "bold"),
                                  width=10, command=set_button)
        self.top_button.grid(sticky="w")
        
        #makes a title and displays it on the gui
        self.gui_heading = Label(self.gui_frame,
                                 text=("History/Export"),
                                 font=("Arial", "16", "bold"))
        self.gui_heading.grid(row=0,column=0,padx=250,pady=5)
        #this variable holds the text that is to be displayed on the gui
        info=(f"below are your recent calculations, showing {shown}/{calc} calcuations"
               " only calculations done this session are avalible")
        #displays the contents of the info variable on the gui
        self.hist_info = Label(self.gui_frame,
                               text=info,font=("Arial","12","bold"),
                               wraplength=250, width=40,
                                       justify="left")
        self.hist_info.grid(row=1)
        #displays the 5 most recent calculations on the gui
        self.hist_anwsers = Label(self.gui_frame,
                                  text=tree,font=("Arial","12","bold"))

        self.hist_anwsers.grid(row=2)


        self.button_frame = Frame(self.gui_frame)
        self.button_frame.grid(row=3)
        #this list contains all the infomation for the buttons
        #button details. text|command|bg code|row|column
        button_detail_list = [
            ["back", back_but, "#808080", 0, 0],
            ["export", export, "#808080", 0, 1]
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
def run_hist(test,hist):
    #sets two variables to global and makes them equal another variable
    global debug
    global anwsers
    anwsers = hist
    debug = test
    global root
    root = Tk()
    root.title("history/export")
    gui()
    root.mainloop()
