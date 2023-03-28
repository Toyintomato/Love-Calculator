print("Welcome to love calculator!!!\n")
name1 = input("What is your name? \n").lower()
name2 = input("What is your lover's name? \n").lower()
combine_name = name1 + name2

#count true
t = combine_name.count("t")
r = combine_name.count("r")
u = combine_name.count("u")
e = combine_name.count("e")
true = t + r + u + e

#count love
l = combine_name.count("l")
o = combine_name.count("o")
v = combine_name.count("v")
e = combine_name.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
int_lovescore = int(love_score)

if int_lovescore < 10 or int_lovescore > 90:
    print(f"Your love score is {love_score}, you two go together like coke and mentos")
elif int_lovescore >= 40 and int_lovescore <= 50:
    print(f"Your love score is {love_score}, you two are alright together")
else:
    print(f"Your love score is {love_score}")

 
