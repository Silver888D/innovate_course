from operator import index
import random

# # testing commment
# print ("this is my current file")

# # strings are for representing chracters
# print("hello my name is")
# print("1234")

# #this is an integer - a whole number
# print(1234)

# # this is a floating point - anything with a decimal point
# print(1234.5)

# #booleans - true or false, yes or no, 0 or 1 - needs to start with capital
# print(True)
# print(False)

# # none -  a blank or null type - needs to start with capital
# print(None)
# # len is length of string but won't show without telling to print
# print(len("hello"))
# # index position starts count at 0
# print("hello"[1])
# # .notation is a way of accessing methods- can specifiy within the end brackets after the .notation
# print("hello".upper())
# # generating random numbers, random - floating point, uniform - floating point, randint - only whole numbers
# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))

# my_name = "Seb"
# my_age = 28
# print(f"my name is {my_name} and I am {my_age}.")

# #other methods
# print("hello my name is",my_name)
# print("hello my name is "+ my_name)#-- doesn't work with numbers only string
# print("hello my name is {} and I am {} years old".format(my_name,my_age))

# #Maths
# print(1+2)
# print(2-1)
# print(2*3)
# print(3**3)
# print(15/3)
# print(15%3)
# print(15%4)

# balance = 100
# amount = 50
# print(balance-amount)
# #balance = balance-amount
# balance -=amount # see above
# print(balance)


# #input allows us to prompt the user to input a response
# char_name = input("what is your name?  >    ")
# print (f"Welcome, {char_name}")
# #if/else/elif
# music = "classical"
# if music == "classical":
#     print("oh no, it's classical again")
# elif music == "no music":
#     print("ahh peace and quiet")
# else:
#     print("nice and noisy")

# num1 = 10
# num2 = 20

# if num1 > num2:
#     print("number 1 is the bigger number")
# elif num1 < num2:
#     print("number 2 is the bigger number")
# else:
#     print("number 1 and 2 are the same")
# # has to be in logical order otherwise will print first correct statement
# num = 21
# if num%7==0 and num%3==0:
#     print("fizzbuzz")
# elif num%7==0:
#     print("buzz")
# elif num%3==0:
#     print("fizz")
# else:
#     print(num)

# # with 'and' both situations have to be true for the statement to be true
# # with 'or' only one situation has to be true for the statement to be true
# bank_holiday = True
# day = "Sunday"
# if day == "Saturday" or day == "Sunday" or bank_holiday == True:
#     print("Yay it's a day off")
# else:
#     print("Time to go to CodeNation")

# # Making Functions

# def light_switch():
#     print("Who turned out the lights")
# light_switch() # have to call a function through it's definition name

# #functions with parameter - required information to call function i.e amount/accnum

# def cash_withdrawal(amount,accnum):
#     print(f"Withdrawing £{amount} from account {accnum}")
# cash_withdrawal(300,50449921)
# # returns - allows us to set value to come back with, otherwise will come back with none

# def add_up(num1,num2):
#     return num1+num2

# print(add_up(5,2))

# fav_films=["jurassic park","lost world","jurassic world"]
# # runs through it until list loop is finished, doesn't have to be 'i' anything between 'for' and 'in' will work
# for i in fav_films:
#     print(i)
# for i in range (10):# stops at number prior '9'
#     print(i)

# num4 = 5

# while num4 > 40:
#     print("right on")
#     print (num4)
# while num4 <=40:
#     print("Rookie numbers")
#     num4+=0.25
#     print (num4)


# activity 1
# welcome = "welcome to Code Nation"
# welcomelength = len(welcome)

# def check():
#     if welcomelength%2 == 0:
#         print (welcome, welcomelength,"Even Number")
#     else:
#         print(welcome, welcomelength, "an odd number")
# check()
#activity 2

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in alphabet:
    print (i)

rand_num = (int)(input("pick a number...."))

def rand_letter():
    print(alphabet[rand_num])
rand_letter()


