#version 1.1

#imports everything from the math module
import json
from math import *
works = False
#asks for the an input (will be removed later and is only here for testing purposes)
#quest = input("question")
global quest
global awnser
awnser=[]

#this is where all function for the calculator are contained
class calculation():
    #currently unsused 
    #remove?      
    def convert_check(self):
        print(quest)
        symbols = "x"
        #convert = False
        for letter in quest:
            if letter in symbols:
                #convert = True
                print("run converter")
    #main converter that converts certain letters into stuff python understands
    def convert(quest):
        #converts x into * as x is often used as the multiplier symbol
        global ques
        ques = quest
        if "x" in quest:
            print(quest)
            quest = quest.replace("x", "*")
        else:
            quest = quest
        #converts ^ into ** so python can process it
        if "^" in quest:
            quest = quest.replace("^", "**")
        else:
            quest = quest
        #converts g into the gravity of earth which is approximatley 9.81m per second
        if "g" in quest:
            quest = quest.replace("g","9.81")
        else:
            quest = quest
        #replaces c with the speed of light
        if "c" in quest:
            global quest1
            quest1 = quest.replace("c", "3*10**8")
        else:
            
            quest1 = quest
    #this runs the processed question to get an awnser
    # apparently eval is unsafe as it allows the user execute code which can be a security risk
    # im going to ignore it for now but may address this later 
    def calculate(self):
        global works
        try:
            print(eval(quest1))
            global result
            result = eval(quest1)
            #adds the result to a list
            awnser.append(str(result)+"\n")
            #sets the works variable to true (this is used to enable the history export button)
            works = True
        except:
            print("b")
            result = "ERROR"
#this just runs the functions for the calculator
def process(qu):
    global awnser
    calculation.convert(qu) 
    calculation.calculate(quest1)






