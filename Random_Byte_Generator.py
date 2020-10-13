
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#    This is my first py program, it's terrible, has spaghetti code, I only posted it here so I can see how  I improve... 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import random
import time
# __________________________________________
base = "__asm _emit ";
zero_to_nine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'B', 'c', 'd', 'E', 'f', 'G', 'H', 'i', 'J', 'K', 'l', 'M', 'N', 'o', 'P', 'q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z']
#unnecessary but it's too late now...



#__________________fix this________________________|
'''
def setrandomnumbers():
    global random_number, two_random_number, three_random_number, four_random_number, five_random_number, six_random_number, seven_random_number, eight_random_number, nine_random_number, ten_random_number


def setrandomalphabet():
    global random_alphabet, two_random_alphabet, three_random_alphabet, four_random_alphabet, five_random_alphabet, six_random_alphabet, seven_random_alphabet, eight_random_alphabet, nine_random_alphabet, ten_random_alphabet

def setcombinations():
    global first_combination, two_first_combination, three_first_combination, four_first_combination, five_first_combination, six_first_combination, seven_first_combination, eight_first_combination, nine_first_combination, ten_first_combination


def setallvariables():
    global random_number, two_random_number, three_random_number, four_random_number, five_random_number, six_random_number, seven_random_number, eight_random_number, nine_random_number, ten_random_number
    global random_alphabet, two_random_alphabet, three_random_alphabet, four_random_alphabet, five_random_alphabet, six_random_alphabet, seven_random_alphabet, eight_random_alphabet, nine_random_alphabet, ten_random_alphabet
    global first_combination, two_first_combination, three_first_combination, four_first_combination, five_first_combination, six_first_combination, seven_first_combination, eight_first_combination, nine_first_combination, ten_first_combination
'''

#_________________________________________________________|
def GetRandomNumbers():
    #setrandomnumbers()
    global random_number, two_random_number, three_random_number, four_random_number, five_random_number, six_random_number, seven_random_number, eight_random_number, nine_random_number, ten_random_number
    random_number = random.choice(zero_to_nine)
    two_random_number = random.choice(zero_to_nine)
    three_random_number = random.choice(zero_to_nine)
    four_random_number = random.choice(zero_to_nine)
    five_random_number = random.choice(zero_to_nine)
    six_random_number = random.choice(zero_to_nine)
    seven_random_number = random.choice(zero_to_nine)
    eight_random_number = random.choice(zero_to_nine)
    nine_random_number = random.choice(zero_to_nine)
    ten_random_number = random.choice(zero_to_nine)

    #___________________|

def GetRandomLetters():
        #setrandomalphabet()
        global random_alphabet, two_random_alphabet, three_random_alphabet, four_random_alphabet, five_random_alphabet, six_random_alphabet, seven_random_alphabet, eight_random_alphabet, nine_random_alphabet, ten_random_alphabet
        random_alphabet = random.choice(alphabet)
        two_random_alphabet = random.choice(alphabet)
        three_random_alphabet = random.choice(alphabet)
        four_random_alphabet = random.choice(alphabet)
        five_random_alphabet = random.choice(alphabet)
        six_random_alphabet = random.choice(alphabet)
        seven_random_alphabet = random.choice(alphabet)
        eight_random_alphabet = random.choice(alphabet)
        nine_random_alphabet = random.choice(alphabet)
        ten_random_alphabet = random.choice(alphabet)


#___________________|


def SettingVariables():
    #setallvariables()
    global random_number, two_random_number, three_random_number, four_random_number, five_random_number, six_random_number, seven_random_number, eight_random_number, nine_random_number, ten_random_number
    global random_alphabet, two_random_alphabet, three_random_alphabet, four_random_alphabet, five_random_alphabet, six_random_alphabet, seven_random_alphabet, eight_random_alphabet, nine_random_alphabet, ten_random_alphabet
    global first_combination, two_first_combination, three_first_combination, four_first_combination, five_first_combination, six_first_combination, seven_first_combination, eight_first_combination, nine_first_combination, ten_first_combination
    first_combination = (base + "0" + "x" + random_number + random_alphabet + " " + "/")
    two_first_combination = (base + "0" + "x" + two_random_alphabet + two_random_number + " " + "/")
    three_first_combination = (base + "0" + "x" + three_random_number + three_random_alphabet + " " + "/")
    four_first_combination = (base + "0" + "x" + four_random_alphabet + four_random_number + " " + "/")
    five_first_combination = (base + "0" + "x" + five_random_number + five_random_alphabet + " " + "/")
    six_first_combination = (base + "0" + "x" + six_random_alphabet + six_random_number + " " + "/")
    seven_first_combination = (base + "0" + "x" + seven_random_number + seven_random_alphabet + " " + "/")
    eight_first_combination = (base + "0" + "x" + eight_random_alphabet + eight_random_number + " " + "/")
    nine_first_combination = (base + "0" + "x" + nine_random_number + nine_random_alphabet + " " + "/")
    ten_first_combination = (base + "0" + "x" + ten_random_alphabet + ten_random_number + " " + "/")

    #___________________|

def PrintVariables():
    #setcombinations()
    global first_combination, two_first_combination, three_first_combination, four_first_combination, five_first_combination, six_first_combination, seven_first_combination, eight_first_combination, nine_first_combination, ten_first_combination
    print (first_combination)
    print (two_first_combination)
    print (three_first_combination)
    print (four_first_combination)
    print (five_first_combination)
    print (six_first_combination)
    print (seven_first_combination)
    print (eight_first_combination)
    print (nine_first_combination)

    #___________________|

def ResetVariables():
    #setcombinations()
    global first_combination, two_first_combination, three_first_combination, four_first_combination, five_first_combination, six_first_combination, seven_first_combination, eight_first_combination, nine_first_combination, ten_first_combination
    del first_combination
    del two_first_combination
    del three_first_combination
    del four_first_combination
    del five_first_combination
    del six_first_combination
    del seven_first_combination
    del eight_first_combination
    del nine_first_combination


def FinalProduct():
   GetRandomNumbers()
   GetRandomLetters()
   SettingVariables()
   PrintVariables()
   ResetVariables()


#_________________________________________________________|

FinalProduct()
FinalProduct()
FinalProduct()
FinalProduct()
FinalProduct()






