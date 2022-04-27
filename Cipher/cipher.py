#Cipher

def encode(message):
    newMessage = ""
    for i in message:
        if i == " ":
            newMessage = newMessage + " "
        if i == "a":
            newMessage = newMessage + "0"
        if i == "b":
            newMessage = newMessage + "1"
        if i == "c":
            newMessage = newMessage + "2"
        if i == "d":
            newMessage = newMessage + "3"
        if i == "e":
            newMessage = newMessage + "4"
        if i == "f":
            newMessage = newMessage + "5"
        if i == "g":
            newMessage = newMessage + "6"
        if i == "h":
            newMessage = newMessage + "7"
        if i == "i":
            newMessage = newMessage + "8"
        if i == "j":
            newMessage = newMessage + "9"
        if i == "k":
            newMessage = newMessage + "!"
        if i == "l":
            newMessage = newMessage + "@"
        if i == "m":
            newMessage = newMessage + "#"
        if i == "n":
            newMessage = newMessage + "$"
        if i == "o":
            newMessage = newMessage + "%"
        if i == "p":
            newMessage = newMessage + "^"
        if i == "q":
            newMessage = newMessage + "&"
        if i == "r":
            newMessage = newMessage + "*"
        if i == "s":
            newMessage = newMessage + "("
        if i == "t":
            newMessage = newMessage + ")"
        if i == "u":
            newMessage = newMessage + "-"
        if i == "v":
            newMessage = newMessage + "+"
        if i == "w":
            newMessage = newMessage + "<"
        if i == "x":
            newMessage = newMessage + ">"
        if i == "y":
            newMessage = newMessage + "?"
        if i == "z":
            newMessage = newMessage + "="
    return newMessage
def decode(message):
    newMessage = ""
    for i in message:
        if i == " ":
            newMessage = newMessage + " "
        if i == "0":
            newMessage = newMessage + "a"
        if i == "1":
            newMessage = newMessage + "b"
        if i == "2":
            newMessage = newMessage + "c"
        if i == "3":
            newMessage = newMessage + "d"
        if i == "4":
            newMessage = newMessage + "e"
        if i == "5":
            newMessage = newMessage + "f"
        if i == "6":
            newMessage = newMessage + "g"
        if i == "7":
            newMessage = newMessage + "h"
        if i == "8":
            newMessage = newMessage + "i"
        if i == "9":
            newMessage = newMessage + "j"
        if i == "!":
            newMessage = newMessage + "k"
        if i == "@":
            newMessage = newMessage + "l"
        if i == "#":
            newMessage = newMessage + "m"
        if i == "$":
            newMessage = newMessage + "n"
        if i == "%":
            newMessage = newMessage + "o"
        if i == "^":
            newMessage = newMessage + "p"
        if i == "&":
            newMessage = newMessage + "q"
        if i == "*":
            newMessage = newMessage + "r"
        if i == "(":
            newMessage = newMessage + "s"
        if i == ")":
            newMessage = newMessage + "t"
        if i == "-":
            newMessage = newMessage + "u"
        if i == "+":
            newMessage = newMessage + "v"
        if i == "=":
            newMessage = newMessage + "w"
        if i == "<":
            newMessage = newMessage + "x"
        if i == ">":
            newMessage = newMessage + "y"
        if i == "?":
            newMessage = newMessage + "z"
    return newMessage
def main():
    prompt = True
    while(prompt):

        print("\nWelcome to he Secret Message Encoder/Decoder")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("\nWhat would you like to do? ")

        if (choice == "1"):
            message = input("\nEnter a message to encode: ")
            print("Encoded message: ", encode(message))
        elif (choice == "2"):
            message = input("\nEnter a message to decode: ")
            print("Decoded message: ", decode(message))
        elif (choice == "3"):
            prompt = False
            exit()
        else:
            print("\nPlease enter 1, 2, or 3.")
main()
