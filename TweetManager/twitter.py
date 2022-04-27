#twitter

#This program requires a "Tweets.txt" file to store data

import time
import pickle
from Tweet import Tweet

#--------------------------------------------------------------------------------Helper Functions
    #--------------------------------------------------------------------------------------------

#Returns data read from "Tweets.txt" as a list
def readFile():
    data = []
    f = open("Tweets.txt", "rb")
    while True:
        try: data.append(pickle.load(f))
        except EOFError:
            break
    f.close()

    return data

#Takes Tweet object, stores tweet data on "Tweets.txt"
def writeFile(tweet):
    f = open("Tweets.txt", "ab+")

    tweetList = []
    tweetList.append(tweet.get_author())
    tweetList.append(tweet.get_text())
    tweetList.append(tweet.get_age())
        
    pickle.dump(tweetList, f)

    f.close()
        
    print("\n" + tweetList[0] + ", your tweet has been saved.")
    
#Clears "Tweets.txt" file
def clearFile():
    clear = input("\nAre you sure you want to clear all Tweets? (y/n) ")
    if clear == "y":
        f = open("Tweets.txt", "w")
        f.close()
        print("\nTweets cleared.")
    selection()

#Takes time Tweet was created, returns current Tweet age
def getTime(starttime):
    stoptime = time.time()
    age = stoptime - starttime

    output = ""
    if age < 60:
        output += str((round(age))) + "s"
    elif age < 3600:
        output += str(round((age/60))) + "m"
    else:
        output += str(round((age/3600))) + "h"
        
    return output

#Implements menu Functionality
#Takes user input and calls designated function
def selection():
    print("\nTweet Menu")
    print("----------")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    print("5. Admin - Clear all Tweets")
    
    choice = input("\nWhat would you like to do? ")

    if choice == "1":
        createTweet()
    elif choice == "2":
        displayRecent()
    elif choice == "3":
        search()
    elif choice == "4":
        exitManager()
    elif choice == "5":
        clearFile()
    else:
        choice = -1
        print("\nPlease select a valid option (1, 2, 3, 4, 5)")
        selection()

#--------------------------------------------------------------------------------Four User Functions
    #-----------------------------------------------------------------------------------------------
        
#Creates new tweet object based on user input and stores it on "Tweets.txt"
def createTweet():
    author = input("What is your name? " )
    text = input("What would you like to tweet? ")
    
    while len(text) > 140:
        print("\nTweets must not exceed 140 characters.")
        text = input("\nWhat would you like to tweet? ")
        
    newTweet = Tweet(author, text)
    writeFile(newTweet)

#Displays five most recent Tweets
def displayRecent():
    tweets = readFile()

    if len(tweets) == 0:
        print("\nNo Tweets Available")
        return
    else:
        print("\nRecent Tweets")
        print("----------")
        while len(tweets) < 5:
            temp = ["0"]
            tweets.append(temp)      
        for i in range(1,6):
            if "0" not in tweets[-i]:
                print("\n" + tweets[-i][0] + " - " + getTime(tweets[-i][2]))
                print(tweets[-i][1])
                
#Displays any Tweets whose Author or Text match the user's search criteria     
def search():
    tweets = readFile()
    
    query = input("What would you like to search for? ")
    print("\nSearch results for " + '''"''' + query + '''"''')
    print("----------")
    
    if len(tweets) == 0:
        print("\nNo Tweets Available")
        
    else:
        count = 0
        for i in reversed(tweets):
            if query in i[0] or query in i[1]:
                count += 1
                print("\n" + i[0] + " - " + getTime(i[2]))
                print(i[1])
        if count == 0:
            print('''\n"''' + query + '''"''' + " not found.")

#Exits program
def exitManager():
    end = input("\nAre you sure you want to exit? (y/n) ")
    if end == "y":
        print("\nThank you for using the Tweet Manager!")
        exit()
    selection()
#--------------------------------------------------------------------------------Main Method
    #---------------------------------------------------------------------------------------
def main():
    print("--------------Tweet Manager--------------")
        
    while True:
        selection()
                
main()
    
