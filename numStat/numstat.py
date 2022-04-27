#numstat

#I had an issue where because of the way I nested the function calls
#gather_data and display would still go through and generate errors
#if the file name was incorrect and the error was printed
#I have yet to find a better way so to temporarily combat this
#I added some if statements and return 0's 


#Takes user input for file name
def get_input():
    return str(input("Enter file name: "))

#Takes file name, reads file and returns file elements as a list
#Prints error and returns 0 on error
def read_file(file):

    try:
        f = open(file, "r")

        a = (f.readlines())

        f.close()

        return a
    except FileNotFoundError:
        print("File " + '''"''' + file + '''" does not exist.''')
        return 0

#Takes file name, reads file and aggregates data
#Returns data variables or 0 on failure
def gather_data(file):
    if read_file(file) != 0:
        
        a = read_file(file)
    
        for i in range(0, len(a)):
            a[i] = int(a[i])
        
        FileName = file
        Sum = sum(a)
        Count = len(a)
        Average = Sum/Count
        Max = max(a)
        Min = min(a)
        Range = Max-Min

        return FileName, Sum, Count, Average, Max, Min, Range
    else:
        return 0
#Takes file, reads file contents, aggregates data, and displays data content
#Returns 0 on failure
def display(file):
    if read_file(file) != 0:

        FileName, Sum, Count, Average, Max, Min, Range = gather_data(file)
        
        print("\nFileName: " + FileName + "\n")

        print("Sum: " + str(Sum) + "\n")

        print("Count: " + str(Count) + "\n")

        print("Average: " + str(Average) + "\n")

        print("Max: " + str(Max) + "\n")

        print("Min: " + str(Min) + "\n")

        print("Range: " + str(Range))
    else:
        return 0

def main():

    #Prompts user to do another calculation if wanted
    do_calculation = True
    while(do_calculation):

        display(get_input())

        another_calculation = input("\nDo you want to perform another calculation? (y/n)")
        if (another_calculation != "y"):
            do_calculation = False
            exit()
    
main()
