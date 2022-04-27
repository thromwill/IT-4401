#Rock, Paper, Scissors

import pickle
import random
import os
#--------------------------------------------------------------------------------Helper Functions
    #--------------------------------------------------------------------------------------------

#Takes a player name, creates game file under their name, initializes statistic values and adds it to the list of files
def createFile(name):
    
    f = open(name + ".txt", "x")

    f.write(name + "\n") #name
    f.write("1\n") #round
    f.write("0\n") #wins
    f.write("0\n") #losses
    f.write("0\n") #ratio

    #If you open a file, you had better close it
        # - JimR
    f.close()

    addGame(name)

#Overwrites statistics in the game file corresponding to 'name' with parameter values
def writeFile(name, roundNumber, wins, losses, ratio):
    
    f = open(name + ".txt", "w")

    f.write(name + "\n")
    f.write(str(roundNumber) + "\n")
    f.write(str(wins) + "\n")
    f.write(str(losses) + "\n")
    f.write(str(ratio) + "\n")

    f.close()

#Reads statistics froma a game file corresponding to 'name', returns each statistic   
def readFile(name):
    
    f = open(name + ".txt", "r")
    
    data = f.readlines()

    roundNumber = int(data[1])
    wins = int(data[2])
    losses = int(data[3])
    ratio = float(data[4])

    f.close()

    return roundNumber, wins, losses, ratio

#Implements menu functionality
#Prints menu and performs function calls corresponding to user input
def selection():
    
    print("\nMenu")
    print("----------")
    print("1. Start New Game")
    print("2. Load Game")
    print("3. View Statistics")
    print("4. Exit")
    print("5. Admin - Clear all Games")

    choice = input("\nEnter choice: ")

    if choice == "1":
        createGame("")
    elif choice == "2":
        loadGame("")
    elif choice == "3":
        viewStats("")
    elif choice == "4":
        exitProgram()
    elif choice == "5":
        clearFiles()
    else:
        choice = -1
        print("\nPlease select a valid option (1, 2, 3, 4)")
        selection()

#Takes player name, carries out Rock, Paper, Scissors gameplay
def play(name):
    
    #Read in current statistic values from player's game file
    roundNumber, wins, losses, ratio = readFile(name)
    
    #Print header with current rount number
    print("\nRound " + str(roundNumber) + ":")
    
    #Print game header
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")

    #Take user selection and have computer select random value
    while True:
        player = input("\nWhat will it be? ")
        if player not in ('1', '2', '3'):
            print("\nPlease select a valid option (1, 2, 3)")
        else:
            break
    computer = str(random.randint(1,3))

    #Takes numerical value one through three, returns corresponding Rock, Paper, Scissors selection
    def convert(choice):
        if choice == "1":
            choice = "Rock"
        elif choice == "2":
            choice = "Paper"
        elif choice == "3":
            choice = "Scissors"
        return choice

    #Convert numerical selection to Rock, Paper, or Scissors
    player = convert(player)
    computer = convert(computer)

    #Print outcome of current game
    print("\nYou chose " + player + ". The computer chose " + str(computer) + ". ", end = "")

    #Check if gameplay resulted in a tie, if yes, play another game until a win or loss occurs
    if player == computer:
        print("Tie-Breaker!")
        play(name)

    #Once a win/loss occurs...
    else:
        
        #Increase the round number by one
        roundNumber += 1

        #Combine the player and computer selections to determine the single game result
        outcome = player + computer
        
        #Initialize a dictionary with corresponding outcomes, ties have already been dealt with
        outcomes = {
            "RockScissors" : "win!",
            "PaperRock" : "win!",
            "ScissorsPaper" : "win!",
            "RockPaper" : "lose!",
            "PaperScissors" : "lose!",
            "ScissorsRock" : "lose!"
        }
        #Display the outcome
        print("You " + outcomes[outcome])

        #Update statistics for wins, losses, and win/loss ratio
        if outcomes[outcome] == "win!":
            wins += 1
        else:
            losses += 1

        #Check for 0 before calculating the ratio
        if wins == 0:
            ratio = 0
        elif losses == 0:
            ratio = 1
        else:
            ratio = round(int(wins)/int(losses), 2)

    #Update the game file with new statistics
    writeFile(name, roundNumber, wins, losses, ratio)

    #Allows user to select what to do after a round of gameplay (Play again, View Stats, Quit)
    def end_menu():
        
        #Take user input
        choice = input("\n1. Play again\n2. View Statistics\n3. Quit\n\nWhat would you like to do? ")

        #Make corresponding function call
        if choice == "1":
            play(name)
        elif choice == "2":
            viewStats(name)
        elif choice == "3":
            selection()

        #Ensure viable input
        else:
            print("\nPlease select a valid option. (1, 2, 3)")
            end_menu()

    #Redirect to end menu
    end_menu()

#Creates data file on startup if one does not already exist         
def startUp():
    try:
        f = open("RPS_DATA.txt", "x")
        f.close()
    except FileExistsError:
        return
    
#Adds name of game file to data file
def addGame(name):
    try:
        f = open("RPS_DATA.txt", "a")
        f.write(name + ".txt")
        f.close()
    except FileNotFoundError:
        print("\nError adding game: file not found")
    
#--------------------------------------------------------------------------------Five User Functions
    #-----------------------------------------------------------------------------------------------

#Creates new Rock, Paper, Scissors game with a unique userName
def createGame(name):
    
    #Allows user to select what to do if a game already exists under a given userName (Load game, try another name, go back to menu)
    def errorMenu():

        choice = input("\n1. Load game\n2. Try another name\n3. Go back to menu\n\nWhat would you like to do? ")

        if choice == "1":
            loadGame(name)
        elif choice == "2":
            createGame()
        elif choice == "3":
            selection()
        else:
            print("\nPlease select a valid option. (1, 2)")
            errorMenu()
            
    #Check if createGame has already been called with a userName (i.e. after a loadGame error)
        #If the name is blank, take user input for a new userName
    if name == "":    
        name = input("What is your name? " )

    try:
        createFile(name)
        print("\nHello " + name + ". Let's play!")
        play(name)

    except FileExistsError:
        print("\n" + name + ", you already have a game.")
        errorMenu()

#Loads existing game given a particular userName      
def loadGame(name):
    
    #Allows user to select what to do if no games exist under a given userName (Create a new game under that username, try another name, go back to menu)
    def errorMenu():

        choice = input("\n1. Create game for " + name + "\n2. Try another name\n3. Back to menu\n\nWhat would you like to do? ")

        if choice == "1":
            createGame(name)
        elif choice == "2":
            loadGame("")
        elif choice == "3":
            selection()
        else:
            print("\nPlease select a valid option. (1, 2, 3)")
            errorMenu()

    if name == "": 
        name = input("Who's game would you like to load? ")

    try:
        f = open(name + ".txt", "r")
        f.close()
        print("\nHello " + name + ". Let's play!")
        play(name)
    except FileNotFoundError:
        print("\nNo games found for " + '''"''' + name + '''"''')
        errorMenu()

#Displays the statistics in the game file under a given userName
def viewStats(name):
    
    #Allows the user to select what to do after viewing statistics (View another player's statistics, go back to menu)
    def end_menu():

        choice = input("\n1. View another player's stats\n2. Go back to menu\n\nWhat would you like to do? ")

        if choice == "1":
            viewStats("")
        elif choice == "2":
            selection()
        else:
            print("\nPlease select a valid option. (1, 2)")

    #Allows the user to select what to do if no game file exists for a particular userName (Try another name, go back to menu)
    def errorMenu():

        choice = input("\n1. Try another name\n2. Back to menu\n\nWhat would you like to do? ")

        if choice == "1":
            viewStats("")
        elif choice == "2":
            selection()
        else:
            print("\nPlease select a valid option. (1, 2)")
            errorMenu()

    if name == "":
        name = input("Who's statistics would you like to view? ")

    try:
        roundNumber, wins, losses, ratio = readFile(name)
        roundsPlayed = roundNumber-1
        print("\nGame Statistics for " + name + ":")
        print("----------")
        print("Rounds played: " + str(roundsPlayed))
        print("Wins: " + str(wins))
        print("Losses: " + str(losses))
        print("Win/Loss Ratio: " + str(ratio))
        end_menu()
    except FileNotFoundError:
        print("\nNo data found for " + '''"''' + name + '''"''')
        errorMenu()

#Exits Rock, Paper, Scissors 
def exitProgram():
    #Check that exit was intentional before exiting
    end = input("\nAre you sure you want to exit? (y/n) ")
    if end == "y":
        print("\nThanks for playing Rock, Paper, Scissors!")
        exit()

    #If no, redirect to main menu
    selection()

#Clear all game files
def clearFiles():
    clear = input("\nAre you sure you want to remove all games? (y/n) ")
    if clear == "y":
        try:
            f = open("RPS_DATA.txt", "r")
            files = f.readlines()
            f.close()

            #Delete the files
            for i in files:
                os.remove(i)
                
            #Clear data file
            f = open("RPS_DATA.txt", "w")
            f.close()

            print("\nGames cleared.")
            
        except FileNotFoundError:
            print("\nNo data available.")

    selection()
        
#--------------------------------------------------------------------------------Main Method
    #---------------------------------------------------------------------------------------
def main():
    startUp()
    print("--------------Rock, Paper, Scissors--------------")

    while True:
        selection()
        
#Call main             
main()
    
