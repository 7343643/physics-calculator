#error list
#error 1 = tester detected 1 or more issues 
#error 2 = tester output missing but calc_cache is present
#error 3 = calc_cache was not made or was unable  to be found(likely an issue with the tester)

#this runs the tester when called
def First_run():
    import tester_v1_0
    
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
                raise(error("ERROR 1"))
            else:
                raise(error("ERROR 2"))
    except:
        raise(error("ERROR3"))
#this runs the previous function
run_test()
#imports the files that are needed
from main_gui_v1_0 import *
from settings_gui_v0_3 import *
from history_export_gui_v0_1 import*
from help_info_gui_v1_0 import*
#makes a function that runs the main gui and when the gui closes checks the runner variables in the main_gui then opens the relevant gui if it necessary
def main_gui():
    run()
    from main_gui_v1_0 import setting_run
    if setting_run == True:
        settings_gui(main_gui)
    from main_gui_v1_0 import hist_run
    if hist_run == True:
        history_export_gui()
    from main_gui_v1_0 import help_info_run
    if help_info_run == True:
        help_info_gui()


#makes a function to run the settings gui with the argument being what gui the user came from and when the settings is closed opens that gui
def settings_gui(gui):
    run_set()
    gui()
#makes a function that runs the history_export gui and when the gui closes checks if the user pressed the back button (to return to the main gui) or setting button then runs the relevant gui if necessary
def history_export_gui():
    run_hist()
    from history_export_gui_v0_1 import setting_run
    if setting_run == True:
        settings_gui(history_export_gui)
    from history_export_gui_v0_1 import back
    if back == True:
        main_gui()
#makes a fuction that runs the help_info gui and when the gui closes open the main gui if the user pressed the bak button
def help_info_gui():
    run_help()
    from help_info_gui_v1_0 import bak
    if bak == True:
        main_gui()
#this calls the main_gui function and if python runs into an issue prints that there was an issue
try:
    main_gui()
except:
    print("an error occured within the main program")