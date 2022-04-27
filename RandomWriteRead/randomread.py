from pathlib import Path

#randomread

#Returns a list of numbers read from file, assuming each line contains one number
#Prints error if file does not exist
def read_random_numbers(file):
    #Check that file exists
    if Path(file).is_file():
        f = open(file, "r")

        #Read integers from file
        a = (f.readlines())

        f.close()

        return a
    else:
        #Indicate file error
        print('''"''' + file + '''" does not exist.''')

#Prints numbers found in file and total amount of numbers printed
def display(file):
    #Print header
    print("List of random numbers in " + '''"''' + file + '''":''')

    #Read numbers from file, find total
    a = read_random_numbers(file)
    count = len(a)
    
    #Print each value
    for x in range(count):
        print(str(a[x]), end = "")

    #Print total
    print("\nRandom number count: " + str(count))
    
def main():
    display("randomnum.txt")
main()
