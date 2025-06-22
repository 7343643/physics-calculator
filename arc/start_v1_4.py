#error list
#error 1 = tester detected 1 or more issues 
#error 2 = tester output missing but calc_cache is present
#error 3 = calc_cache was not made or was unable  to be found(likely an issue with the tester)

#version 1.4

global debug
debug = True
#this runs the tester when called
def First_run():
    import tester
def ignore(code):
    if debug != True:
        raise(error(code))
    else:
        ask = input("a non-fatal error has occured, enter y if you wish to continue\n" \
        "an invalid input will result in the program crashing with the error that occured\n"
        "WARNING CONTINUING MAY RESULT IN CRASHES AND IS NOT RECOMMENDED")
        if ask == "y":
            print("continuing")
            pass
        else:
            raise(error(code))

#this function is used to test for issues
def run_test():
    #attempts to open the calc_cache file and if it is unable to it calls the first run function
    try:
        f = open("calc_cache")
        f.close()
    except:
        First_run()
    #this defines error as an exception
    class error(Exception):
        pass
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
                ignore("ERROR 1")
                raise(error("ERROR 1"))
            else:
                ignore("ERROR 2")
                raise(error("ERROR 2"))
    except:
        ignore("ERROR 3")
        raise(error("ERROR 3"))
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
import json
#imports the files that are needed
from main_gui import *
from settings_gui import *
from history_export_gui import*
from help_info_gui import*
#load settings not used currently
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
import os
try:
    main_gui()
except:
    print("an error occured within the main program")

#this checks if the debug variable is set to true and if it is it checks the files file and deletes all the files listed in it then deletes the file
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
if settings_list[3] == True:
    os.remove("calc_cache")