# Making People

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def talk(self):
        print(f"Hello, my name is {self.name}, I am {self.age} and {self.height} inches tall")
    
    def set_hair(self,hair):
        self.hair = hair
    
    def get_hair(self):
        print(self.hair)




