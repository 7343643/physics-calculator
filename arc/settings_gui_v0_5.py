#version 0.5

#imports the module i am using to create the gui
from tkinter import *
import json
class settings():

    #this is the function that contains the gui
    def __init__(self):
        self.sett_frame = Frame(padx=10, pady=10)
        self.sett_frame.grid()
        #makes a function that destroys the gui
        def back():
            r = json.dumps(settings_list)
            with open("settings.json","w") as t:
                t.write(r)
            root.destroy()
            
        #this is the back button that is used to return to the main page
        self.back_button = Button(self.sett_frame,
                                  text="back", bg="#808080",
                                  fg="#FFFFFF", font=("Arial", "12", "bold"),
                                  width=10, command=back)
        
        self.back_button.grid(sticky="w",padx=10, pady=10)
        
        #this adds text at the top of the window
        self.sett_title = Label(self.sett_frame,
                                text="Settings", font=("Arial", "16", "bold"))
        
        self.sett_title.grid(column=0, row=0, padx=10, pady=5)

        #this is the frame for all the settings buttons
        self.button_frame = Frame(self.sett_frame)
        self.button_frame.grid(row=2, column=0)
        
        #this list holds the colors used by the buttons green is 0 red is 1
        shared_button_colors = ["#32CD32", "#FF0000" ]
        #holds the default state for the settings order is as follows
        # sf , blind
        
        default_settings_list = [False,False
        ]

        def clrchg(numb):
            
            if settings_list[numb] == True:
               
               self.button_ref_list[numb].config(bg=shared_button_colors[0])
            
            elif settings_list[numb] == False:
               self.button_ref_list[numb].config(bg=shared_button_colors[1])
        
        def sf():
            if settings_list[0] == True:
                settings_list[0] = False
        
            elif settings_list[0] == False:
                
                settings_list[0] = True
            clrchg(0)
        def blind():
            if settings_list[1] == True:
                settings_list[1] = False
        
            elif settings_list[1] == False:
                
                settings_list[1] = True
            clrchg(1)

         #this holds the rest of the buttons infomation
        #it is formatted as Text|Color|Command|Row
        button_detail_list = [  
            ["Round to correct number of significant figures", 1, sf, 0],
            ["colorblind mode", 1, blind, 1]
        ]
        debug_settings_list = [
            ["Delete calc_cache on exit", 1, "", 2],
            ["Delete exports on exit", 1,"",3]
        ]
        #list to hold the buttons once they are made
        self.button_ref_list = []
        
        for item in button_detail_list:
            temp = item[1]

            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=shared_button_colors[temp],
                                      fg="#000000", font=("Arial", "12", "bold"),
                                      width=40, command=item[2])
            self.make_button.grid(row=item[3], padx=50, pady=5)
            
            self.button_ref_list.append(self.make_button)
        #disable the round to correct number of sf button as it isn't usable currently
        self.sf_button = self.button_ref_list[0].config(state=DISABLED)
        try:
            with open("settings.json") as j:
                y = json.loads(j.read())
                print(y)
                settings_list = y
                if settings_list[1] == True:
                    shared_button_colors = ["#FBFF00", "#001AFF" ]
                clrchg(0)
                clrchg(1)
        except:
            print("error")
#makes a function that runs the gui when called      
def run_set(test):
    global debug
    debug = test
    global root
    root = Tk()
    root.title("Physics Calc Settings")
    settings()
    root.mainloop()
