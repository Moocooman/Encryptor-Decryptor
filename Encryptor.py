from random import *

# Character source for both functions
charSource = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?"()&-0123456789'

def getLetterIndex(let):
    try:
        return charSource.index(let)
    except:
        print("Invalid character inserted")

def getIndexLetter(num):
    return charSource[num]
    
# User input
plaintext = input("Encrypt: ")
# Variable setup
encryptedText = ""
key = ""

try:
    for letter in plaintext:
        # Convert letter to number
        ID = getLetterIndex(letter)
    
        # Offset number and record as key
        randomKey = randint(0, 72)  # Change this to a non-random to create key DEFAULT=randint(0, 72)
        key += getIndexLetter(randomKey)
        ID += randomKey  # Error here usually means a character from plaintext isn't supported by getLetterIndex()
        if ID >= 72:
            ID = ID - 72
    
        # Convert back to text and add to output variable
        encryptedText += getIndexLetter(ID)
    
    # Output encrypted message
    print(f"Cypher Text: {encryptedText}\nKey: {key}")
    input("Press Any Button to Exit")
except:
    print("Valid input required")

# Keep keys of the same offset (not using randint(0, 72) in line 310) simple