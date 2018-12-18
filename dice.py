import random

min = 1
max = 6 
roll_agin = ("yes")

while roll_agin == ("yes") or roll_agin == ("y"):
    print ("rolling...")
    print ("the numbers are...")
    print (random.randint(min,max))
    print (random.randint(min,max))

    roll_agin = input("roll again?")
    #hey
    #heythere
    #heythereagain
    
    
    
