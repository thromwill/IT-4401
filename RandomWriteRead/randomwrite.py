import random
from pathlib import Path

#randomwrite

#Takes variable set to prompt, returns variable as integer value input by user
def get_input(var):
    
    while(True):
        try:
            #Take user input for var
            var = int(input(var))
            #Check for positive values
            if var <= 0:
                print("Invalid input. Please enter a positive value.")
                continue
            #Check for integer values
        except ValueError:
                print("Invalid input. Please enter numerical digits.")
        else:
            return var
            break
        
#Writes count number of random integers between floor and ceiling to file.
#If file doesn't exist, prints error.
def write_random_numbers(count, floor, ceiling, file):
    #Check that file exists
    if Path(file).is_file():
        f = open(file, "w")

        #Write random numbers to file
        for x in range(count):
            f.write(str(random.randint(floor, ceiling))+"\n")

        print("The random numbers were written to " + file)

        f.close() 
    else:
        #Indicate file error
        print( '''"''' + file + '''" does not exist.''')

def main():
    #Initialize count to desired prompt
    count = "How many random numbers do you want?\n"
    #Set to user input based on prompt
    count = get_input(count)

    floor = "What is the lowest the random number should be?\n"
    floor = get_input(floor)

    ceiling = "What is the highest the random number should be?\n"
    ceiling = get_input(ceiling)

    write_random_numbers(count, floor, ceiling, "randomnum.txt")

    
    

main()


        
    
