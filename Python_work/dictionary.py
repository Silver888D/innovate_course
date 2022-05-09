# #list
# my_cat = ["Salem","Black","Sassy"]
# # Dictionary
# my_cat = {"name":"Salem","color":"black","mood":"sassy"}

dict_of_films = {"rain man": 1988,"baby driver": 2017,"hot fuzz": 2007,"spiderman":2021}

list_of_films = ["rain man","baby driver","hot fuzz","spiderman"]

seb_dict ={"tired":True, "hungry": False, "exercise_time_day":20, "homework":"Look at POP888", "chores": "Clean Kitchen"}

# print(list_of_films[1])
# print(dict_of_films["Baby Driver"])
# def pick_film():
#     print(f"Select a film {list_of_films}")
#     try:
#         print (dict_of_films[input()])
#     except:
#         pick_film()

# pick_film()


dict_of_Vinnie = {"species":"Gerbil","name":"Vinnie","color":"white","hungry":False,"thirsty":False,"sleepy":False,"age":3}

print(dict_of_Vinnie)
print("Oh no, Vinnie fell in sand")
dict_of_Vinnie["color"] = "dirty"
color = dict_of_Vinnie.get("color")
print(f"he became {color}")
print(dict_of_Vinnie)
print("Vinnie jumps out the whole and cleans himself")
dict_of_Vinnie["color"] = "white"
dict_of_Vinnie["thirsty"]= True
dict_of_Vinnie["hungry"]= True
print(dict_of_Vinnie)
print("Vinnie runs to his cage for food and water")
dict_of_Vinnie["hungry"] = False
dict_of_Vinnie["thirsty"] = False
dict_of_Vinnie["sleepy"]= True
print(dict_of_Vinnie)
print("Vinnie is feeling tired, so he goes to his bed.... but there is a bear in it O.O..... Vinnie went beserk")
dict_of_Vinnie.setdefault("Beserker","Detroys all with rage")
print(dict_of_Vinnie)