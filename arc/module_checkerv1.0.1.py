#this file is not essential to the program and it is only present to ensure dependencies are met
#try:
    #import tkinter   
#except:
    #print("tkinter is not installed")
    #tk_module = False
#else:
    #print("tkinter is installed")
    #tk_module = True
import platform
#this checks the version of python
py_ver = platform.python_version()
#this is the version of python the code was made on
min_ver ="3.12.3"
#this tells the user to upadte python if their version is older than the version listed earlier
if py_ver < min_ver:
    print("please up date python to at least version 3.12.3")
#list of modules used in the program
module_list = [
    ["tkinter"],
    ["math"]
]
#this runs the contained code for each item in the modue list
for item in module_list:
    module = item[0]
    #this try to see if the module can be imported
    try:
        __import__(module)
    #if the module is not instaled it tells the user
    except:
        print(item[0] +" is not installed")
        installed = False
    #if the module is instaled it will tell the user
    else:
        print(item[0] +" is installed")
        installed = True

        
        