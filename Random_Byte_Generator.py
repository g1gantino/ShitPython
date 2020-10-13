# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#    This is my first py program, it's terrible, has spaghetti code, I only posted it here so I can see how  I improve... 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
import random
import time
# __________________________________________
base = "__asm _emit ";
zero_to_nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'B', 'c', 'd', 'E', 'f', 'G', 'H', 'i', 'J', 'K', 'l', 'M', 'N', 'o', 'P', 'q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z']
#_________________________________________________________|
def GetRandomNumbers():
    global random_number1, random_number2, random_number3, random_number4, random_number5, random_number6, random_number7, random_number8, random_number9
    random_number1 = random.choice(zero_to_nine)
    random_number2 = random.choice(zero_to_nine)
    random_number3 = random.choice(zero_to_nine)
    random_number4 = random.choice(zero_to_nine)
    random_number5 = random.choice(zero_to_nine)
    random_number6 = random.choice(zero_to_nine)
    random_number7 = random.choice(zero_to_nine)
    random_number8 = random.choice(zero_to_nine)
    random_number9 = random.choice(zero_to_nine)
    #___________________
def GetRandomLetters():
        global random_alphabet1, random_alphabet2, random_alphabet3, random_alphabet4, random_alphabet5, random_alphabet6, random_alphabet7, random_alphabet8, random_alphabet9
        random_alphabet1 = random.choice(alphabet)
        random_alphabet1 = random.choice(alphabet)
        random_alphabet2 = random.choice(alphabet)
        random_alphabet3 = random.choice(alphabet)
        random_alphabet4 = random.choice(alphabet)
        random_alphabet5 = random.choice(alphabet)
        random_alphabet6 = random.choice(alphabet)
        random_alphabet7 = random.choice(alphabet)
        random_alphabet8 = random.choice(alphabet)
        random_alphabet9 = random.choice(alphabet)
#___________________
def SettingVariables():
    global random_number1, random_number2, random_number3, random_number4, random_number5, random_number6, random_number7, random_number8, random_number9
    global random_alphabet1, random_alphabet2, random_alphabet3, random_alphabet4, random_alphabet5, random_alphabet6, random_alphabet7, random_alphabet8, random_alphabet9
    global combination1, combination2, combination3, combination4, combination5, combination6, combination7, combination8, combination9
    combination1 = (base + "0" + "x" + random_number1 + random_alphabet1 + " " + "/")
    combination2 = (base + "0" + "x" + random_alphabet2 + random_number1 + " " + "/")
    combination3 = (base + "0" + "x" + random_number3 + random_alphabet3 + " " + "/")
    combination4 = (base + "0" + "x" + random_alphabet4 + random_number4 + " " + "/")
    combination5 = (base + "0" + "x" + random_number5 + random_alphabet5 + " " + "/")
    combination6 = (base + "0" + "x" + random_alphabet6 + random_number6 + " " + "/")
    combination7 = (base + "0" + "x" + random_number7 + random_alphabet7 + " " + "/")
    combination8 = (base + "0" + "x" + random_alphabet8 + random_number8 + " " + "/")
    combination9 = (base + "0" + "x" + random_number9 + random_alphabet9 + " " + "/")
    #
    combinations = [combination1]
    #combination2, combination3, combination4, combination5, combination6, combination7, combination8, combination9
    #___________________
def PrintVariables():
    global combination1, combination2, combination3, combination4, combination5, combination6, combination7, combination8, combination9
    print (combination1)
   #print (combination2)
   #print (combination3)
   #print (combination4)
    #print (combination5)
    #print (combination6)
    #print (combination7)
    #print (combination8)
    #print (combination9)
    #___________________
def ResetVariables():
    global combination1, combination2, combination3, combination4, combination5, combination6, combination7, combination8, combination9
    global random_number1, random_number2, random_number3, random_number4, random_number5, random_number6, random_number7, random_number8, random_number9
    global random_alphabet1, random_alphabet2, random_alphabet3, random_alphabet4, random_alphabet5, random_alphabet6, random_alphabet7, random_alphabet8, random_alphabet9
    #del
    del combination1, combination2, combination3, combination4, combination5, combination6, combination7, combination8, combination9
    del random_number1, random_number2, random_number3, random_number4, random_number5, random_number6, random_number7, random_number8, random_number9
    del random_alphabet1, random_alphabet2, random_alphabet3, random_alphabet4, random_alphabet5, random_alphabet6, random_alphabet7, random_alphabet8, random_alphabet9
    #___________________
def FinalProduct():
   GetRandomNumbers()
   GetRandomLetters()
   SettingVariables()
   PrintVariables()
   ResetVariables()
#_________________________________________________________|

user_input = input("Please enter how many bytes you want to generate. (1-10):")
#optimize this.
if user_input == '1':
    FinalProduct()
if user_input == '2':
    FinalProduct()
    FinalProduct()
if user_input == '3':
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '4':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '5':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '6':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '7':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '8':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if user_input == '10':
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()


