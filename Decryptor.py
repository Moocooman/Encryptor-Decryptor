## Functions to convert from letters to numbers and reverse
def getLetterIndex(let):
    try:
        return charSource.index(let)
    except:
        print("Invalid character inserted")

def getIndexLetter(num):
    return charSource[num]

# User input
encryptedText = input("Decrypt: ")
key = input("Key: ")
# Variable setup
newKey = []
decryptedText = ""

try:
    if len(encryptedText) == len(key):
        # Covert key to numbers
        for letter in key:
            newKey.append(getLetterIndex(letter))
    
        for letter in encryptedText:
            # Convert letter to number
            letterID = getLetterIndex(letter)
    
            # Offset letter using key
            letterID -= newKey[0]
            if letterID < 0:
                letterID += 72
    
            # Remove used key letter
            newKey.remove(newKey[0])
    
            # Convert back to text and add to output variable
            decryptedText += getIndexLetter(letterID)
    else:
        # Error message
        decryptedText = "Decrypt and Key must be same length\nCheck for misplaced characters violating this rule"
    
    # Output decrypted message
    print(decryptedText)
    input("Press Enter to exit")
except:
    print("Valid Input Required")