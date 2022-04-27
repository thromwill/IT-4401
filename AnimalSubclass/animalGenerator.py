#animalGenerator

from Animals import Animal
from Animals import Mammal
from Animals import Bird

print("Welcome to the animal generator!")
print("This program creates Animal objects.")

def createAnimal():
    
    animalFamily = int(input("\nWould you like to create a mammal or bird?\n1. Mammal\n2. Bird\nWhich would you like to create? "))

    family = 'mammal'
    if animalFamily == 2:
        family = 'bird'
    animalType = str(input("\nWhat type of " + family + " would you like to create? "))

    animalName = str(input("What is the " + family + "'s name? "))
    
    if animalFamily == 1:
        hairColor = str(input("What color is the mammal's hair? "))
        newAnimal = Mammal(animalType, animalName, hairColor)
    if animalFamily == 2:
        canFly = str(input("Can the bird fly? "))
        newAnimal = Bird(animalType, animalName, canFly)

    

    return newAnimal    

def displayAnimals(a):

    print("\nAnimal List: ")
    for i in a:
        print(i)
    
    
def main():

    animals = []
    
    doCalculation = True
    while(doCalculation):
        
        tempAnimal = createAnimal()

        animals.append (str(Animal.get_name(tempAnimal) + " the " + Animal.get_animal_type(tempAnimal) + " is " + Animal.check_mood(tempAnimal)))      
        
        anotherCalculation = input("\nWould you like to add more animals(y/n)? ")
        
        if (anotherCalculation != "y"):
            doCalculation = False
            displayAnimals(animals)
    
main()
