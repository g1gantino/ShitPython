import random
# /////////////////////////////////
#    This is my first py program, it's terrible, has spaghetti code, I only posted it here so I can see how  I improve... 
# /////////////////////////////////

# __asm _emit 0x00 \
# ___________________________________________________
base = "__asm _emit ";
alphabet = ['a', 'B', 'c', 'd', 'E', 'f', 'G', 'H', 'i', 'j', 'K', 'l', 'M', 'n', 'o', 'P', 'q', 'r', 'S', 't', 'u', 'v', 'W', 'x', 'y', 'z']
zero_to_nine = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#unnecessary but whatever...
zero = ("0")
x =("x")
#spaghetti begins...
#first
random_number = random.choice(zero_to_nine)
r_alphabet = random.choice(alphabet)
#two
two_random_number = random.choice(zero_to_nine)
two_r_alphabet = random.choice(alphabet)
#three
three_random_number = random.choice(zero_to_nine)
three_r_alphabet = random.choice(alphabet)
#four
four_random_number = random.choice(zero_to_nine)
four_r_alphabet = random.choice(alphabet)
#five
five_random_number = random.choice(zero_to_nine)
five_r_alphabet = random.choice(alphabet)
#six
six_random_number = random.choice(zero_to_nine)
six_r_alphabet = random.choice(alphabet)
#seven
seven_random_number = random.choice(zero_to_nine)
seven_r_alphabet = random.choice(alphabet)
#eight
eight_random_number = random.choice(zero_to_nine)
eight_r_alphabet = random.choice(alphabet)
#nine
nine_random_number = random.choice(zero_to_nine)
nine_r_alphabet = random.choice(alphabet)
#ten
ten_random_number = random.choice(zero_to_nine)
ten_r_alphabet = random.choice(alphabet)

# _________IMPORTANT_____________________
#first
first_combination = ("__asm _emit " + zero + ("x") + r_alphabet + random_number + " " + "/")
second_combination = ("__asm _emit " + zero + ("x") + random_number + r_alphabet + " " + "/")
#two
two_first_combination = ("__asm _emit " + zero + ("x") + two_r_alphabet + two_random_number + " " + "/")
two_second_combination = ("__asm _emit " + zero + ("x") + two_random_number + two_r_alphabet + " " + "/")
#three
three_first_combination = ("__asm _emit " + zero + ("x") + three_r_alphabet + three_random_number + " " + "/")
three_second_combination = ("__asm _emit " + zero + ("x") + three_random_number + three_r_alphabet + " " + "/")
#four
four_first_combination = ("__asm _emit " + zero + ("x") + four_r_alphabet + four_random_number + " " + "/")
four_second_combination = ("__asm _emit " + zero + ("x") + four_random_number + four_r_alphabet + " " + "/")
#five
five_first_combination = ("__asm _emit " + zero + ("x") + five_r_alphabet + five_random_number + " " + "/")
five_second_combination = ("__asm _emit " + zero + ("x") + five_random_number + five_r_alphabet + " " + "/")
#six
six_first_combination = ("__asm _emit " + zero + ("x") + six_r_alphabet + six_random_number + " " + "/")
six_second_combination = ("__asm _emit " + zero + ("x") + six_random_number + six_r_alphabet + " " + "/")
#seven
seven_first_combination = ("__asm _emit " + zero + ("x") + seven_r_alphabet + seven_random_number + " " + "/")
seven_second_combination = ("__asm _emit " + zero + ("x") + seven_random_number + seven_r_alphabet + " " + "/")
#eight
eight_first_combination = ("__asm _emit " + zero + ("x") + eight_r_alphabet + eight_random_number + " " + "/")
eight_second_combination = ("__asm _emit " + zero + ("x") + eight_random_number + eight_r_alphabet + " " + "/")
#nine
nine_first_combination = ("__asm _emit " + zero + ("x") + nine_r_alphabet + nine_random_number + " " + "/")
nine_second_combination = ("__asm _emit " + zero + ("x") + nine_random_number + nine_r_alphabet + " " + "/")
#ten
ten_first_combination = ("__asm _emit " + zero + ("x") + ten_r_alphabet + ten_random_number + " " + "/")
ten_second_combination = ("__asm _emit " + zero + ("x") + ten_random_number + ten_r_alphabet + " " + "/")
# __________________________
times = input("EfefefaadfsdfasDFSdf")
if times: 1
print (first_combination)
if times: 2
print (two_first_combination)
print (three_second_combination)
if times: 3
print (three_first_combination)
print (four_second_combination)
print (first_combination)
if times: 4
print (four_first_combination)
print (five_second_combination)
print (nine_first_combination)
print (ten_second_combination)
if times: 5
print (five_first_combination)
print (six_second_combination)
print (two_first_combination)
print (three_second_combination)
print (ten_first_combination)
if times: 6
print (six_first_combination)
print (nine_second_combination)
print (seven_first_combination)
print (ten_second_combination)
print (eight_first_combination)
print (second_combination)
if times: 7
print (seven_first_combination)
print (second_combination)
print (six_first_combination)
print (two_second_combination)
print (ten_first_combination)
print (first_combination)
print (three_second_combination)
if times: 8
print (eight_first_combination)
print (two_second_combination)
print (nine_first_combination)
print (three_first_combination)
print (ten_second_combination)
print (first_combination)
print (four_second_combination)
print (five_first_combination)
if times: 9
print (eight_first_combination)
print (two_second_combination)
print (nine_first_combination)
print (four_first_combination)
print (ten_second_combination)
print (first_combination)
print (seven_second_combination)
print (three_first_combination)
print (six_second_combination)
if times: 10
print (first_combination)
print (two_second_combination)
print (three_first_combination)
print (four_second_combination)
print (five_first_combination)
print (six_second_combination)
print (seven_first_combination)
print (eight_second_combination)
print (nine_first_combination)
print (ten_second_combination)




# ("__asm _emit " + zero + ("x") + r_alphabet + random_number)
# ("__asm _emit " + zero + ("x") + random_number + r_alphabet)




'''import random
a = ['off', 'it', 'on', 'not']
random.choice(a)
=> 'on' # just an example, it's a random outpu
'''