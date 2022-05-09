# print (int(round(5.8)))
# print (int("54"))
# print (float(5.8))
# print (float("54"))
# #casting
# print (type(str(54)))
# print (type(str(5.4)))

# #Truthy and Falsy
# name=input("What is your name?")
# if name:
#     print(f"Hello {name}")
# else:
#     print("you did not provide name")

#'Not' operator swaps the truthy and falsy

# print(not True)
# print(not False)

# bool = False
# if not bool:
#     print(False)
# else:
#     print(True)

# # Try/Except - like if/else, 

# def add_up():
#     num1=(input("what 1? \n"))
#     num2=(input("what 2? \n"))
#     try:
#         print(f"{int(num1) + int(num2)}")
#     except:
#         print("\n ERROR: please only input numbers")
#         add_up()
# add_up()

# #Scope--

# light = False

# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True
# light_switch()
# light_switch()

# balance=100

# def cash_withdraw(amount):
#     global balance
#     print(f"Your balance is {balance}")
#     print(f"You are withdrawing {amount}")
#     balance -= amount
#     print(f"Your new balance is {balance}")

# cash_withdraw(int(input("amount")))
# #Lists and Tuples
# list1 = ["item1","item2"]

# tuple1 = ("item1","item2")

# evennum = ["2" ,"4","6","8","10"]

# oddnum = ("1","3","5","7","9")

# # evennum.append(12)
# # evennum.insert(0,0)
# # for i in evennum:
# #     print(i)

# # oddnum.remove(1)
# # oddnum.pop()
# # print(oddnum)
# # oddnum +=("11","13","15")
# # print(oddnum)


# ##Slices- where to start and end list- last one is steps
# print(evennum[0:5:2])

# num = 0

# while num < 10:
#     print(num)
#     num += 1

# while some_variable:
#     print("the user has spoken")
#     if "5" in evennum:
#         print("yay")
#         break
#     else:
#         print("Please add fruit")
#         nums = input



# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# print (alphabet)


#     rand_num = (input("pick a number.... to pick a letter...."))
#     rand_num == int
#     if rand_num <26:
#         print(alphabet[rand_num])
#     elif rand_num >= 26:
#         print("Number too high")
#     else:
#         print("not a number, try again")


# ## activity 1
nums = [1,2,3,4,5,6,7,8,9,10]
answer1 = input("pick a number....")
def gen_num():
    global answer1
    try:
        if int(answer1) in nums:
            print(f"this number {answer1} is in the list")
        elif int(answer1) not in nums:
            print("Not in list, try again")
            answer1 = input("pick a number....")
            gen_num()
    except:
        print("Not a number")
        answer1 = input("pick a number....")
        gen_num()
gen_num()