#this makes the error variable to global and sets it to false
#the error variable also gets set to true if any of the tests aren't passed
global error 
error = False
#this attempts to import the required python modules and set a variable on whetever it was able to or not
try:
    import platform
    import math 
    import tkinter
    import webbrowser
    py_mod_stat = "able to import required modules\n"
except:
    py_mod_stat = "unable to import one or more python modules\n"
    error = True
#imports the platform module
import platform


#if platform.system() != "Linux" or "Windows":
    #sys = "user is using an unsupported operating system\n"
    #print("g")
    #operate = platform.system()
#else:
    #sys = "user is using a supported operating system\n"
    #operate = platform.system()
    #print(operate)
#this saves the users operating system name as a variable
operate = platform.system()+"\n"
#this retrieves the python version the user is using 
py_ver = platform.python_version()
#this is the version that was used in testing
min_ver = "3.12.3"
#this checks if the user has a version older than the min_ver listed and sets a variable based on whether they do or not
if py_ver < min_ver:
    print("3")
    ver = " python is older then the version required\n"
    error = True
else:
    ver = " python version is supported\n"

#this list contains the names of all the files the program needs (they should all come as one)
files = ["calculator_v1_0","history_export_gui_v0_1","main_gui_v1_0","settings_gui_v0_3","help_info_gui_v1_0"]
#this makes an empty list to store the results of whether the program was able to import the files
file_list = []
global missing_file
#sets the missing files variable to false
missing_file = False
#this checks all the files in the files list and checks if they can be imported then saves the results to the file_list list
for item in files:
    file_name = item
    try:
        __import__(file_name)
    except:
        file_status = (item +".py is missing\n ") 
        missing_file = True
        error = True
    else:
        file_status = (item +".py is present\n")
    file_list.append(file_status)

global missing_files
#checks if there where missing files and saves whether there were or not then saves the result to the same variable
if missing_file == True:
    missing_files = "there are missing files\n"
else:
    missing_files = "all requried files found\n"
#this checks to see if the error variable is true (it should be false unless something is wrong) then saves the result to the same variable
if error == True:
    error = "unable to fufile all dependecies\n"
else:
    error = "no issues found\n"
#this makes a list the contains the results of some of the tests
status = [py_mod_stat, py_ver, ver, missing_files,operate]
#this makes a file called calc_cache and opens it
open("calc_cache","x")
with open("calc_cache", "a") as f:
    #this writes all the results from the tester to the file 
    #whether an error occured or not is written first so it can be accesed by the start program to see if there was an issue
    f.write(error)
    for item in status:
        f.write(item)
    for item in file_list:
        f.write(item)
    f.close
