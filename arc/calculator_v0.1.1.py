#imports everything from the math module
from math import *

#asks for the an input (will be removed later and is only here for testing purposes)
quest = input("question")

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
    def convert(self):
        
        if "x" in quest:
            print(quest)
            quest0 = quest.replace("x", "*")
        else:
            quest0 = quest
        
        if "^" in quest0:
            quest1 = quest0.replace("^", "**")
        else:
            quest1 = quest0
        
        if "g" in quest1:
            quest2 = quest1.replace("g","9.81")
        else:
            quest2 = quest1
        if "c" in quest2:
            global quest3
            quest3 = quest2.replace("c", "3*10**8")
        else:
            
            quest3 = quest2
    #this runs the processed question to get an awnser
    # apparently eval is unsafe as it allows the user execute code which can be a security risk
    # im going to ignore it for now but will need to address this later 
    def calculate(self):
        try:
            print(eval(quest3))
        except:
            print("b")
#this just runs the functions for the calc
calculation.convert(quest) 
calculation.calculate(quest3)






