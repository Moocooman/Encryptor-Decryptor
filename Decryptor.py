## Functions to convert from letters to numbers and reverse
def getLetterIndex(let):
    if let == " ":
        return 0
    elif let == "a":
        return 1
    elif let == "b":
        return 2
    elif let == "c":
        return 3
    elif let == "d":
        return 4
    elif let == "e":
        return 5
    elif let == "f":
        return 6
    elif let == "g":
        return 7
    elif let == "h":
        return 8
    elif let == "i":
        return 9
    elif let == "j":
        return 10
    elif let == "k":
        return 11
    elif let == "l":
        return 12
    elif let == "m":
        return 13
    elif let == "n":
        return 14
    elif let == "o":
        return 15
    elif let == "p":
        return 16
    elif let == "q":
        return 17
    elif let == "r":
        return 18
    elif let == "s":
        return 19
    elif let == "t":
        return 20
    elif let == "u":
        return 21
    elif let == "v":
        return 22
    elif let == "w":
        return 23
    elif let == "x":
        return 24
    elif let == "y":
        return 25
    elif let == "z":
        return 26
    elif let == "A":
        return 27
    elif let == "B":
        return 28
    elif let == "C":
        return 29
    elif let == "D":
        return 30
    elif let == "E":
        return 31
    elif let == "F":
        return 32
    elif let == "G":
        return 33
    elif let == "H":
        return 34
    elif let == "I":
        return 35
    elif let == "J":
        return 36
    elif let == "K":
        return 37
    elif let == "L":
        return 38
    elif let == "M":
        return 39
    elif let == "N":
        return 40
    elif let == "O":
        return 41
    elif let == "P":
        return 42
    elif let == "Q":
        return 43
    elif let == "R":
        return 44
    elif let == "S":
        return 45
    elif let == "T":
        return 46
    elif let == "U":
        return 47
    elif let == "V":
        return 48
    elif let == "W":
        return 49
    elif let == "X":
        return 50
    elif let == "Y":
        return 51
    elif let == "Z":
        return 52
    elif let == ".":
        return 53
    elif let == ",":
        return 54
    elif let == "!":
        return 55
    elif let == "?":
        return 56
    elif let == "\"":
        return 57
    elif let == "(":
        return 58
    elif let == ")":
        return 59
    elif let == "&":
        return 60
    elif let == "-":
        return 61
    elif let == "0":
        return 62
    elif let == "1":
        return 63
    elif let == "2":
        return 64
    elif let == "3":
        return 65
    elif let == "4":
        return 66
    elif let == "5":
        return 67
    elif let == "6":
        return 68
    elif let == "7":
        return 69
    elif let == "8":
        return 70
    elif let == "9":
        return 71
    else:
        return "Invalid Letter"
def getIndexLetter(num):
    if num == 0:
        return " "
    elif num == 1:
        return "a"
    elif num == 2:
        return "b"
    elif num == 3:
        return "c"
    elif num == 4:
        return "d"
    elif num == 5:
        return "e"
    elif num == 6:
        return "f"
    elif num == 7:
        return "g"
    elif num == 8:
        return "h"
    elif num == 9:
        return "i"
    elif num == 10:
        return "j"
    elif num == 11:
        return "k"
    elif num == 12:
        return "l"
    elif num == 13:
        return "m"
    elif num == 14:
        return "n"
    elif num == 15:
        return "o"
    elif num == 16:
        return "p"
    elif num == 17:
        return "q"
    elif num == 18:
        return "r"
    elif num == 19:
        return "s"
    elif num == 20:
        return "t"
    elif num == 21:
        return "u"
    elif num == 22:
        return "v"
    elif num == 23:
        return "w"
    elif num == 24:
        return "x"
    elif num == 25:
        return "y"
    elif num == 26:
        return "z"
    elif num == 27:
        return "A"
    elif num == 28:
        return "B"
    elif num == 29:
        return "C"
    elif num == 30:
        return "D"
    elif num == 31:
        return "E"
    elif num == 32:
        return "F"
    elif num == 33:
        return "G"
    elif num == 34:
        return "H"
    elif num == 35:
        return "I"
    elif num == 36:
        return "J"
    elif num == 37:
        return "K"
    elif num == 38:
        return "L"
    elif num == 39:
        return "M"
    elif num == 40:
        return "N"
    elif num == 41:
        return "O"
    elif num == 42:
        return "P"
    elif num == 43:
        return "Q"
    elif num == 44:
        return "R"
    elif num == 45:
        return "S"
    elif num == 46:
        return "T"
    elif num == 47:
        return "U"
    elif num == 48:
        return "V"
    elif num == 49:
        return "W"
    elif num == 50:
        return "X"
    elif num == 51:
        return "Y"
    elif num == 52:
        return "Z"
    elif num == 53:
        return "."
    elif num == 54:
        return ","
    elif num == 55:
        return "!"
    elif num == 56:
        return "?"
    elif num == 57:
        return "\""
    elif num == 58:
        return "("
    elif num == 59:
        return ")"
    elif num == 60:
        return "&"
    elif num == 61:
        return "-"
    elif num == 62:
        return "0"
    elif num == 63:
        return "1"
    elif num == 64:
        return "2"
    elif num == 65:
        return "3"
    elif num == 66:
        return "4"
    elif num == 67:
        return "5"
    elif num == 68:
        return "6"
    elif num == 69:
        return "7"
    elif num == 70:
        return "8"
    elif num == 71:
        return "9"
    else:
        return "Invalid ID"

## User input
encryptedText = input("Decrypt: ")
key = input("Key: ")
## Variable setup
newKey = []
decryptedText = ""

if len(encryptedText) == len(key):
    ## Covert key to numbers
    for letter in key:
        newKey.append(getLetterIndex(letter))

    for letter in encryptedText:
        ## Convert letter to number
        letterID = getLetterIndex(letter)

        ## Offset letter using key
        letterID -= newKey[0]  # Error here usually means a character from encryptedText or key isn't supported by getLetterIndex()
        if letterID < 0:
            letterID += 72

        ## Remove used key letter
        newKey.remove(newKey[0])

        ## Convert back to text and add to output variable
        decryptedText += getIndexLetter(letterID)
else:
    ## Error message
    decryptedText = "ERROR\nDecrypt and Key must be same length\nCheck for space as first or last character"

## Output decrypted message
print(decryptedText)
input("[ENTER] to exit")
