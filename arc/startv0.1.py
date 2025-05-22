#error list
#error 1 = tester detected 1 or more issues 
#error 2 = tester output missing but calc_cache is present
#error 3 = calc_cache was not made or was unable  to be found(likely an issue with the tester)
def First_run():
    import tester
    

def run_test():
    try:
        f = open("calc_cache")
        f.close()
    except:
        First_run()
    class error(Exception):
        pass
    try:
        with open("calc_cache", "r") as file:
            stat = file.readline().rstrip()
        if stat == "no issues found":
           print("a")
        else:
            if stat == "unable to fufile all dependecies":
                print("an issue was detected the may cause the program to no work" \
                "please look at the calc_cache file and fix what is wrong")
                raise(error("ERROR 1"))
            else:
                raise(error("ERROR 2"))
    except:
        raise(error("ERROR3"))
run_test()
from main_gui import *
from settings_gui import *
from history_export_gui import*


def main_gui():
    run()
    from main_gui import setting_run
    if setting_run == True:
        settings_gui(main_gui)
    from main_gui import hist_run
    if hist_run == True:
        history_export_gui()



def settings_gui(gui):
    run_set()
    gui()

def history_export_gui():
    run_hist()
    from history_export_gui import setting_run
    if setting_run == True:
        settings_gui(history_export_gui)
    from history_export_gui import back
    if back == True:
        main_gui()

try:
    main_gui()
except:
    print("an error occured within the main program")