#Animals

import random
    
class Animal:
    def __init__(self, animal_type, animal_name):
        self.__animal_type = animal_type
        self.__name = animal_name

        n = random.randint(1,3)
            
        if n == 1:
            self.__mood = "happy"
        elif n == 2:
            self.__mood = "hungry"
        else:
            self.__mood = "sleepy"
                
    def get_animal_type(self):
        return self.__animal_type
    
    def get_name(self):
        return self.__name
    
    def check_mood(self):
        return self.__mood

class Mammal(Animal):
    def __init__(self, animal_type, animal_name, hair_color):
        super().__init__(animal_type, animal_name)
        self.__hair_color = hair_color

    def get_hair_color(self):
        return self.__hair_color
class Bird(Animal):
    def __init__(self, animal_type, animal_name, can_fly):
        super().__init__(animal_type, animal_name)
        self.__can_fly = can_fly

    def get_can_fly(self):
        return self.__can_fly
