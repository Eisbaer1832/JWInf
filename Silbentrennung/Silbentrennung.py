def isConsonant(char):
    if char in "aeiouäöüy!.,;- ":
        return False
    else:
        return True

def checkForSillable(charA, charB):
    state = False
    # 2 Konsonanten
    if (isConsonant(charA) and isConsonant(charB)):
        print(charA + " und " + charB + " sind Konsonanten!")
        state = True
    if (charA == "c"  and charB == "h"):
        state = False
    return state

def doSeperation(text):
    # ne for loop geht hier nicht, weil er dann unendlich lange immer n " " hinzufügt 😭
    i = 0
    while i < len(text) - 1:
        if checkForSillable(text[i], text[i + 1]): 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennugn einfügen
            i = i + 2
        else:
            i = i + 1
    return text
