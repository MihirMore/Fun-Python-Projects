def convertInputString():
    rawinput = input("\n Please enter a word, a phrase or a sentence to check if it's a pallindrome: ")
    rawstring = rawinput.lower()
    rawlist = list(rawstring)
    return rawlist

def dirtyAlphabets(dirtyList):
    dirtyAlphabetics = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for character in dirtyAlphabetics:
        if character in dirtyList:
            dirtyList.remove(character)
            return dirtyAlphabets(dirtyList)
    return dirtyList

def pallindromeCheck(cleanList):
    reversedList = cleanList[::-1]
    if reversedList == cleanList:
        return "The text you entered is a Pallindrome!"
    else:
        return "The text you entered is not a Pallindrome."                

def main():
    print("\nPallindrome Checker")      
    originalList = convertInputString()
    originalList = dirtyAlphabets(originalList)
      