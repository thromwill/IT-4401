#animalGenerator

from Animals import Animal

print("Welcome to the animal generator!")
print("This program creates Animal objects.")

def createAnimal():
    
    animalType = str(input("\nWhat type of animal would you like to create? "))
    animalName = str(input("What is the animal's name? "))

    newAnimal = Animal(animalType, animalName)

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
        
        anotherCalculation = input("\nWould you like to add more animals? (y/n)")
        
        if (anotherCalculation != "y"):
            doCalculation = False
            displayAnimals(animals)
    
main()
