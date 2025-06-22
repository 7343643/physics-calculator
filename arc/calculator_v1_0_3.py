#version 1.0.3

#imports everything from the math module
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
        if "x" in quest:
            print(quest)
            quest0 = quest.replace("x", "*")
        else:
            quest0 = quest
        #converts ^ into ** so python can process it
        if "^" in quest0:
            quest1 = quest0.replace("^", "**")
        else:
            quest1 = quest0
        #converts g into the gravity of earth which is approximatley 9.81m per second
        if "g" in quest1:
            quest2 = quest1.replace("g","9.81")
        else:
            quest2 = quest1
        #replaces c with the speed of light
        if "c" in quest2:
            global quest3
            quest3 = quest2.replace("c", "3*10**8")
        else:
            
            quest3 = quest2
    #this runs the processed question to get an awnser
    # apparently eval is unsafe as it allows the user execute code which can be a security risk
    # im going to ignore it for now but will need to address this later 
    def calculate(self):
        global works
        try:
            print(eval(quest3))
            global result
            result = eval(quest3)
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
    calculation.calculate(quest3)






