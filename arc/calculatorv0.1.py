from math import *

quest = input("question")
class calculation():
    #def verify(self):
        #valid = ("1","x", "/", "+", "-", ")", "(","2","3","4","5","6","7","8","9","0")
        #print(quest)
        #for letter in quest:
            #if letter not in valid:
                #print("2")
    #currently unused
    def check(self):
        alphabet = "abcdefghijklmnopqrstuvwyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        full = alphabet + uppercase
        for letter in quest:
            if letter in full:
                
                raise Exception("question is not allowed to contain letters unless representing a symbol")

    #currently unsused       
    def convert_check(self):
        print(quest)
        symbols = "x"
        #convert = False
        for letter in quest:
            if letter in symbols:
                #convert = True
                print("run converter")

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
        
    def calculate(self):
        try:
            print(eval(quest3))
        except:
            print("b")

calculation.convert(quest) 
calculation.calculate(quest3)






