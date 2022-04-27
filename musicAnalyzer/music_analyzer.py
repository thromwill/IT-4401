#music_analyzer

#Statistics to be Collected:
#1) Total number of songs in the playlist.
#2) The number of songs that were released each year in the playlist.
#3) The song by Name and Artist for the longest song (based on Time) in the playlist. Display all if there is more than one longest with the same time.
#4) The song by Name and Artist for the shortest song (based on Time) in the playlist. Display all if there is more than one shortest with the same time.
#5) For each genre, provide: the number of songs, the longest song by Name and Artist (list multiple if more than one), the shortest song by Name and Artist (list multiple if more than one).
#6) The number of songs that have been played.
#7) The number of songs that have not been played.

#Import useful tools
import csv
import statistics
from collections import Counter

#--------------------------------------------------------------------------------Helper Functions
    #--------------------------------------------------------------------------------------------

#Takes user input for file name
def getInput():
    
    #Return input file name
    return str(input("\nEnter file name: "))

#Takes file name, returns list filled with file data
def readFile(file):

    #Open file, create list and fill with data
    try:
        f = open(file, "r", encoding = "utf-16")

        data = csv.reader(f, delimiter = "\t")

        dataList = list(data)
      
        f.close()

        #Check that file has some data
        if len(dataList) == 0:
            print("\nNo elements found in " + '''"''' + file + '''"''')

        #Return filled list
        return dataList

    #Check that file name exists
    except FileNotFoundError:
        #Print error message
        print("\nFile " + '''"''' + file + '''" does not exist.''')

        #Provide options to continue
        repeat = input("\nPress " + '''"''' + "y" + '''"''' + " to try again, or any other key to exit: ")
        exitAnalyzer(repeat)
        
def cleanList(dataList):
    
    #Fill empty attributes with string 0
    #Will make integer comparisons easier in some functions
    cleanList = []
    for row in dataList:
            temp = []
            for element in row:
                if element != '':
                    temp.append(element)
                else:
                    temp.append('0')
            cleanList.append(temp)
            
    #Remove header element containing attribute names
    del cleanList[0]

    #Ensure each element has 31 attributes, assumes last attribute is missing if only 30 elements
    for row in cleanList:
        if len(row) == 30:
            row.append('0')
            
    #Return new list
    return cleanList

#Takes list filled from text file, returns organized lists of information segmented by attribute
def stratify(dataList):
    
    #Declare attribute lists
    album = []
    name = []
    artist = []
    composer = []
    album = []
    grouping = []
    work = []
    movementNumber = []
    movementCount = []
    movementName = []
    genre = []
    size = []
    time = []
    discNumber = []
    discCount = []
    trackNumber = []
    trackCount = []
    year = []
    dateModified = []
    dateAdded = []
    bitRate = []
    sampleRate = []
    volumeAdjustment = []
    kind = []
    equalizer = []
    comments = []
    plays = []
    lastPlayed = []
    skips = []
    lastSkipped = []
    myRating = []
    location = []
    
    #Fill lists with corresponding attributes
    for row in dataList:
        name.append(row[0])
        artist.append(row[1])
        composer.append(row[2])
        album.append(row[3])
        grouping.append(row[4])
        work.append(row[5])
        movementNumber.append(row[6])
        movementCount.append(row[7])
        movementName.append(row[8])
        genre.append(row[9])
        size.append(row[10])
        time.append(row[11])
        discNumber.append(row[12])
        discCount.append(row[13])
        trackNumber.append(row[14])
        trackCount.append(row[15])
        year.append(row[16])
        dateModified.append(row[17])
        dateAdded.append(row[18])
        bitRate.append(row[19])
        sampleRate.append(row[20])
        volumeAdjustment.append(row[21])
        kind.append(row[22])
        equalizer.append(row[23])
        comments.append(row[24])
        plays.append(row[25])
        lastPlayed.append(row[26])
        skips.append(row[27])
        lastSkipped.append(row[28])
        myRating.append(row[29])
        location.append(row[30])
        
    #Return lists
    return name, artist, composer, album, grouping, work, movementNumber,movementCount, movementName, genre, size, time, discNumber, discCount,trackNumber, trackCount, year, dateModified, dateAdded, bitRate, sampleRate,volumeAdjustment, kind, equalizer, comments, plays, lastPlayed, skips,lastSkipped, myRating, location

#Takes a text file of music information, displays summary statistics      
def printSummary(dataList):

    #Get lists by attribute
    name, artist, composer, album, grouping, work, movementNumber,movementCount, movementName, genre, size, time, discNumber, discCount,trackNumber, trackCount, year, dateModified, dateAdded, bitRate, sampleRate,volumeAdjustment, kind, equalizer, comments, plays, lastPlayed, skips,lastSkipped, myRating, location = stratify(dataList)

    #Print total number of songs
    print("\n\nTotal Songs: ", getTotalSongs(dataList))

    #Print number of songs by year
    for key, value in getSongsBy(year).items():
        print("\tSongs in", key, ":", value)

    #Print longest, shortest songs
    print("\nLongest Song: ", getLongestSong(time, name, artist))
    print("Shortest Song: ", getShortestSong(time, name, artist))

    print("\n")
    #Print songs by genre
    count, longest, shortest = getSongsByGenre(dataList, genre)
    for key, value in count.items():
        index = list(count).index(key)
        print(key,"songs:", value)
        print("\tLongest", key, "Song:", longest[index])
        print("\tShortest", key, "Song:", shortest[index])
    
    #Print number of songs played, not played
    played, notPlayed = getPlayed(plays)
    print("\nNumber of Songs Played: " , played)
    print("Songs Not Played:", notPlayed)

#Prompts user to exit program if desired
def exitAnalyzer(repeat):
    if repeat != "y":
            end = input("\nAre you sure you want to exit? (y/n) ")
            if end == "y":
                print("\nGoodbye!")
                exit()
    main(1)

#--------------------------------------------------------------------------------Functions by Statistic
    #--------------------------------------------------------------------------------------------------

#Returns number of songs in the data list
#--------------------------------------------------------------------------------1)
def getTotalSongs(dataList):
    
    return len(dataList)

#Returns number of songs released each year
def getSongsBy(year):
    
    #Remove songs with a blank year attribute
    year = [i for i in year if i != "0"]
    
    #Fill dictionary with year/songs per year pairs
    dictionary = dict(Counter(sorted(year)))
    
    #Return dictionary
    return(dictionary)

#Takes lists containing song times, names, and artists
#Returns the name and artist of the longest song
#--------------------------------------------------------------------------------2)
def getLongestSong(time, name, artist):
    
    #Convert string list to integer list
    time = list(map(int, time))
    
    #Find song with longest time
    maximum = max(time)
    
    #Find name and artist of longest song
    index = time.index(maximum)
    maximumName = name[index]
    maximumArtist = artist[index]

    #Check that the artist is not blank
    #Return clean string to be printed
    returnValue = maximumName
    if maximumArtist != '0':
        returnValue += " by " + maximumArtist
        
    return(returnValue)

#Takes lists containing song times, names, and artists
#Returns the name and artist of the shortest song
#--------------------------------------------------------------------------------3)
def getShortestSong(time, name, artist):
    
    #Convert string list to integer list
    time = list(map(int, time))
    
    #Find shortest song
    minimum = min(time)

    #Find name and artist of shortest song
    index = time.index(minimum)
    minimumName = name[index]
    minimumArtist = artist[index]

    #Return clean string to be printed
    returnValue = minimumName + " by " + minimumArtist
    return(returnValue)

#Takes list of song data and list of song genres
#Returns a dictionary containing number of songs by genre,
#and two lists containing the longest and shortest songs by genre
#--------------------------------------------------------------------------------4)
def getSongsByGenre(dataList, genre):
    
    #Initialize dictionary with genre/songs per genre pairs
    #Uses same method as when getting songs by year
    count = getSongsBy(genre)

    #Initialize clean list to pull data from
    dataList = cleanList(dataList)

    #Declare lists to store data to be returned
    #These will hold the longest and shortest songs in each genre
    longest = []
    shortest = []
    
    #Iterate through each genre
    for key in count:
        #Declare temporary lists to store the time, name, and artist
        #of each song in the current genre
        time = []
        name = []
        artist = []
        #Iterate through the full dataList
        for i in dataList:
            #Find songs matching the current genre
            #Add their time, name, and artist to temporary lists
            if i[9] == key:
                time.append(i[11])
                name.append(i[0])
                artist.append(i[1])
        #Find the longest and shortest song in each genre using the temp lists
        #Add their name and artist to the respective lists to be returned
        longest.append(getLongestSong(time, name, artist))
        shortest.append(getShortestSong(time, name, artist))
      
    return count, longest, shortest
    
#Takes list of plays
#returns number of songs that have/have not been played at least once
#--------------------------------------------------------------------------------5)
#--------------------------------------------------------------------------------6)
def getPlayed(plays):
    
    #Convert string list to integer list
    plays = list(map(int, plays))

    #Initialize count
    played = 0

    #Check if each song has been played at least once
    for i in plays:
        if i > 0:
            played += 1
    #Return number of songs played/not played    
    return(played, len(plays) - played)   
    
#--------------------------------------------------------------------------------Main Method
    #---------------------------------------------------------------------------------------

#Take user input for a file name of music data
#Print summary statistics of the file
def main(args):
    #Print Header
    if args==0:
        print("\n\n---------------------Welcome to Music Analyzer!-------------------")
        print("\t\n  This program provides summary statistics of your music data files!")
        print("\n  We will display:")
        print("\t1) Total number of songs\n\t2) Number of songs released each year")
        print("\t3) Name and artist of the longest and shortest song in the playlist")
        print("\t4) By genre, the longest, shortest, and total number of songs")
        print("\t5) Number of songs that have been played")
        print("\t6) Number of songs that have not been played")
        print("\n----------------Please enter a file name to begin!----------------")
        
    #Parse data and print summary information
    dataList = cleanList(readFile(getInput()))
    printSummary(dataList)

    #Repeat or exit
    repeat = input("\nDo you want to analyze another file? (y/n) ")
    exitAnalyzer(repeat)
    
#Call main method
main(0)
