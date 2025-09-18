#version 1.2

#imports everything from the math module
import json
from math import *
#sets the work variable to false which is used by the main gui to determine if the history / export button should be enabled
works = False
#sets the quest and awnser variable as global
global quest
global awnser
#makes the awnser variable a list so that it can have stuff added to it easily
awnser=[]

#this is where all function for the calculator are contained
class calculation():
    #main converter that converts certain letters into stuff python understands
    def convert(quest):
        #sets ques as a global and makes it equal to quest, it is used to add the equation to the result if the user want both in their export
        global ques
        ques = quest
        #converts x into * as x is often used as the multiplier symbol
        if "x" in quest:
            quest = quest.replace("x", "*")
        #converts ^ into ** so python can process it
        if "^" in quest:
            quest = quest.replace("^", "**")
        #converts g into the gravity of earth which is approximatley 9.81m per second
        if "g" in quest:
            quest = quest.replace("g","9.81")
        #replaces c with the speed of light and assigns the result to quest 1 which is set to global
        if "c" in quest:
            global quest1
            quest1 = quest.replace("c", "3*10**8")
       #sets quest 1 to the same as quest quest
        else:  
            quest1 = quest
    #this runs the processed question to get an awnser
    # apparently eval is unsafe as it allows the user execute code which can be a security risk
    # im going to ignore it because it works 
    def calculate(self):
        #opens the settings.json file and saves the contents as a list called settings_list
        with open("settings.json") as j:
            y = json.loads(j.read())
            global settings_list
            settings_list = y
        j.close()
        global works
        try:
            global result
            result = eval(quest1)
            #adds the result to a list and if the the thrid item in the settings_list is true adds the equation before the awnser
            if settings_list[2] == True:
                awnser.append(str(ques)+"="+str(result)+"\n")
            else:
                awnser.append(str(result)+"\n")
            #sets the works variable to true (this is used to enable the history export button)
            works = True
        #if the program is unable to process the equarion it sets the result variable to ERROR
        except:
            result = "ERROR"
#this just runs the functions for the calculator
def process(qu):
    global awnser
    calculation.convert(qu) 
    calculation.calculate(quest1)






