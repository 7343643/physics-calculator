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

py_ver = platform.python_version()
min_ver ="3.12.3"
if py_ver < min_ver:
    print("please up date python to at least version 3.12.3")

module_list = [
    ["tkinter", "mod = tkinter"],
    ["math"]
]

for item in module_list:
    module = item[0]
    try:
        __import__(module)
    except:
        print(item[0] +" is not installed")
        installed = False
    else:
        print(item[0] +" is installed")
        installed = True

        
        