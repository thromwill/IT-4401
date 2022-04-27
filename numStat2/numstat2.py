#numstat2

#Returns input file name as string
def getInput():
    
    return str(input("\nEnter file name: "))

#Takes name of an integer text file
#Returns list filled with integer elements upon success
#If there are no integer elements or the file is not found, returns -1
def readFile(file):

    try:
        f = open(file, "r")

        a = (f.readlines())

        f.close()

        if(len(a)) == 0:
            print("\nThere are no numbers in " + '''"''' + file + '''"''')
            return -1

        return a
    
    except FileNotFoundError:
        print("\nFile " + '''"''' + file + '''" does not exist.''')
        return -1
    
#Takes list of integers, returns median value
def median(a):
    
    a.sort()

    if len(a) == 1:
        return a[0]
    elif len(a) % 2 == 0:
        return (a[int(len(a) / 2)] + a[int(len(a) / 2) - 1]) / 2
    else:
        return a[int(len(a) / 2 )]
    
#Takes list of integers, returns list of mode value(s)
def mode(a):
    
    counts = {}

    for i in a:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    maxCount = counts[a[0]]
    
    for i in counts:
        count = counts[i]
        if count > maxCount:
            maxCount = count

    mode = []
    
    for i in a:
        if counts[i] == maxCount and i not in mode:
            mode.append(i)
            
    mode.sort(reverse = True)
    
    return mode
      
#Takes file name, reads file and aggregates data
#Returns data variables upon success or -1 on failure
def gatherData(file):
    
    if readFile(file) != -1:
        
        a = readFile(file)
    
        for i in range(0, len(a)):
            a[i] = int(a[i])
        
        FileName = file
        Sum = sum(a)
        Count = len(a)
        Average = Sum/Count
        Max = max(a)
        Min = min(a)
        Range = Max-Min
        Median = median(a)
        Mode = mode(a)

        return FileName, Sum, Count, Average, Max, Min, Range, Median, Mode
    
    else:
        return -1
    
#Takes file, reads file contents, aggregates data, and displays data content
#Returns -1 on failure
def display(file):
    
    if readFile(file) != -1:

        FileName, Sum, Count, Average, Max, Min, Range, Median, Mode = gatherData(file)
        
        print("\nFileName: " + FileName + "\n")

        print("Sum: " + str(Sum) + "\n")

        print("Count: " + str(Count) + "\n")

        print("Average: " + str(Average) + "\n")

        print("Max: " + str(Max) + "\n")

        print("Min: " + str(Min) + "\n")

        print("Range: " + str(Range) + "\n")
        
        print("Median: " + str(Median) + "\n")

        print("Mode: " + str(Mode))
        
    else:
        return -1

def main():

    #Prompts user to do another calculation if wanted
    doCalculation = True
    while(doCalculation):

        display(getInput())

        anotherCalculation = input("\nDo you want to perform another calculation? (y/n)")
        
        if (anotherCalculation != "y"):
            doCalculation = False
            exit()
    
main()
