# countries = {"UK":"London","France":"Paris","Germany":"Berlin","Spain":"Madrid","Italy":"Rome"}
# print(countries)
# countries.setdefault("USA", "Washington")
# countries.setdefault("Australia","Canberra")
# print (countries.items)

fav_songs = [{"song title":"Whiskey", "song artist":"Hippie Sabotage","Album":"Red Moon Rising","Release date":"08.09.2020"},
{"song title":"Freefall","song artist":"Rainbow Kitten Surprise","Album":"How to:Friend, Love, Freefall","Release date":"06.04.2018"},
{"song title":"The Hardest Button to Button","song artist":"The White Stripes","Album":"Elephant","Release date":"11.08.2003"}]

print (fav_songs)

for each_dict in fav_songs:
    print("\n")
    for dict_value in each_dict.values():
        print(dict_value)