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


