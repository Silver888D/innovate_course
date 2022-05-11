
fav_songs = [{"song title":"Whiskey", "song artist":"Hippie Sabotage","Album":"Red Moon Rising","Release date":"08.09.2020"},
{"song title":"Freefall","song artist":"Rainbow Kitten Surprise","Album":"How to:Friend, Love, Freefall","Release date":"06.04.2018"},
{"song title":"The Hardest Button to Button","song artist":"The White Stripes","Album":"Elephant","Release date":"11.08.2003"}]
empty = []



for i in fav_songs:
    empty.append(list(i.values())[0]) 

def add_to_list(song):
    empty.append(song)

def delete_from_list(song):
    empty.remove(song)