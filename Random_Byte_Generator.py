
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#    This is my first py program, it's terrible, has spaghetti code, I only posted it here so I can see how  I improve... 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import random
import time


base = "__asm _emit ";
zero_to_nine = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99',]
#unnecessary but whatever...
x =("x")
zero =("0")
#_________________________________________________________|
def GetRandomNumbers():
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


def SettingVariables():
    first_combination = ("__asm _emit " + zero + ("x") + random_number + " " + "/")
    two_first_combination = ("__asm _emit " + zero + ("x") + two_random_number + " " + "/")
    three_first_combination = ("__asm _emit " + zero + ("x") + three_random_number + " " + "/")
    four_first_combination = ("__asm _emit " + zero + ("x") + four_random_number + " " + "/")
    five_first_combination = ("__asm _emit " + zero + ("x") + five_random_number + " " + "/")
    six_first_combination = ("__asm _emit " + zero + ("x") + six_random_number + " " + "/")
    seven_first_combination = ("__asm _emit " + zero + ("x") + seven_random_number + " " + "/")
    eight_first_combination = ("__asm _emit " + zero + ("x") + eight_random_number + " " + "/")
    nine_first_combination = ("__asm _emit " + zero + ("x") + nine_random_number + " " + "/")
    ten_first_combination = ("__asm _emit " + zero + ("x") + ten_random_number + " " + "/")

    #___________________|

def PrintVariables():
    print (first_combination)
    print (two_second_combination)
    print (three_first_combination)
    print (four_second_combination)
    print (five_first_combination)
    print (six_second_combination)
    print (seven_first_combination)
    print (eight_second_combination)
    print (nine_first_combination)

    #___________________|

def ResetVariables():
    del first_combination
    del two_second_combination
    del three_first_combination
    del four_second_combination
    del five_first_combination
    del six_second_combination
    del seven_first_combination
    del eight_second_combination
    del nine_first_combination


def FinalProduct():
   GetRandomNumbers()
   SettingVariables()
   PrintVariables()
   ResetVariables()


#_________________________________________________________|

number_of_bytes = input("Please enter how many strings you want to generate: (1-10)")
if number_of_bytes == 1:
    FinalProduct()
if number_of_bytes == 2:
    FinalProduct()
    FinalProduct()
if number_of_bytes == 3:
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 4:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 5:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 6:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 7:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 8:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 9:
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
    FinalProduct()
if number_of_bytes == 10:
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







# ("__asm _emit " + zero + ("x") + r_alphabet + random_number)
# ("__asm _emit " + zero + ("x") + random_number + r_alphabet)




'''import random
a = ['off', 'it', 'on', 'not']
random.choice(a)
=> 'on' # just an example, it's a random outpu
'''
