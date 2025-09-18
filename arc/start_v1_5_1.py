#version 1.5.1
#this makes the debug variable global and sets it to false (if this is not a release version then it is true)
global debug
debug = False
#this runs the tester when called
#this defines error as an exception
class error(Exception):
    pass
def First_run():
    import tester
#this function is used to test for issues
def run_test():
    #attempts to open the calc_cache file and if it is unable to it calls the first run function
    try:
        f = open("calc_cache")
        f.close()
    except:
        First_run()
    
    #attempts to open calc_cache and read the first line which should say if there where any issues
    #if there were issues it raises an error and tells the user to check the calc_cache file 
    #if the file is able to be opened but the doesn't have the the expected words on the first line (or it has none) it raises an error
    #if the program is unable to open the file or is unable to find it, it raises an error
    try:
        with open("calc_cache", "r") as file:
            stat = file.readline().rstrip()
        if stat == "no issues found":
           pass
        else:
            if stat == "unable to fufile all dependecies":
                print("an issue was detected the may cause the program to no work" \
                "please look at the calc_cache file and fix what is wrong")
                raise(error("ERROR"))
            else:
                raise(error("ERROR"))
    except:
        raise(error("ERROR"))
    try:
        j = open("settings.json")
        j.close()
    except:
        default_settings_list = [False,False,False,False,False
        ]
        import json
        j = json.dumps(default_settings_list)
        with open("settings.json","w") as t:
            t.write(j)
#this runs the previous function
run_test()
#imports json so settings can be loaded
import json
#imports the files that are needed
from main_gui import *
from settings_gui import *
from history_export_gui import*
from help_info_gui import*
#load settings only does something when debug is true
def load_settings():
    with open("settings.json") as j:
        y = json.loads(j.read())
        global settings_list
        settings_list = y
#makes a function that runs the main gui and when the gui closes checks the runner variables in the main_gui then opens the relevant gui if it necessary
def main_gui():
    run(debug)
    from main_gui import setting_run
    if setting_run == True:
        settings_gui(main_gui)
    from main_gui import hist_run
    if hist_run == True:
        history_export_gui()
    from main_gui import help_info_run
    if help_info_run == True:
        help_info_gui()

#makes a function to run the settings gui with the argument being what gui the user came from and when the settings is closed opens that gui
def settings_gui(gui):
    run_set(debug)
    gui()
#makes a function that runs the history_export gui and when the gui closes checks if the user pressed the back button (to return to the main gui) or setting button then runs the relevant gui if necessary
def history_export_gui():
    from calculator import awnser  
    run_hist(debug,awnser)
    from history_export_gui import back
    if back == True:
        main_gui()
    from history_export_gui import setting_run
    if setting_run == True:
        settings_gui(history_export_gui)
    
#makes a fuction that runs the help_info gui and when the gui closes open the main gui if the user pressed the bak button
def help_info_gui():
    run_help()
    from help_info_gui import bak
    if bak == True:
        main_gui()
#this calls the main_gui function and if python runs into an issue prints that there was an issue

try:
    main_gui()
except:
    print("an error occured within the main program")
#imports the os module
import os
#this checks if the the delete exports setting is true and if it is it checks the files file and deletes all the files listed in it then deletes the file
#in short this deletes files that the program makes when the program closes so i don't have to do it manually
#this is not intended to be used by the end user
load_settings()
if settings_list[4] == True:
    if os.path.exists("files"):
        with open("files") as r:
            for line in r:
                print(line.strip())
        
                os.remove(line.strip())
        os.remove("files")
#checks if the delete calc_cache setting is set to true and if it is deletes the calc_cache
#when the program closes
if settings_list[3] == True:
    os.remove("calc_cache")