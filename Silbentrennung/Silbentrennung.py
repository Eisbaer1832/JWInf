def isConsonant(char):
    if char.lower() in "aeiouäöüy!.,;- ":
        return False
    else:
        return True

def isLastChar(nextChar):
    if (nextChar in " ?.:!"):
        return True
    else:
        return False

def checkForSillable(charA, charB, charC):
    state = False
    
    # 2 Konsonanten
    if (isConsonant(charA) and isConsonant(charB)):
        print(charA + " und " + charB + " sind Konsonanten!")
        state = True
    

    # 3 Konsonanten
    #if (isConsonant(charA) and isConsonant(charB) and isConsonant(charC)):
    #    print(charA + " und " + charB + " sind Konsonanten!")
    #    state = True
    

    # h ist nach einem Voakl Stumm und wird dann nicht getrennt ig?
    if (isConsonant(charA) == False and charB == "h"):
        state = False

    # 1 Vokal und keine 2 Konsonanten
    if (isConsonant(charA) == False and ((isConsonant(charB) == False and isConsonant(charC)) or (isConsonant(charB) and isConsonant(charC) == False))):
        state = True

    # Der Sauerkraut Fix: 3 Vokale
    #if (isConsonant(charA) == False and isConsonant(charB) == False and isConsonant(charC) == False):
    #    state = True
    # hier muss iwi nach dem 2. getrennt werden, da müssen wir uns nochmal angucken

    # ch darf man glaub ich nicht trennen hoffe ich
    if (charA == "c"  and charB == "h" or charB == "c" and charC == "h"):
        state = False
    
    # Letztes Zeichen des Worts
    if (isLastChar(charC)):
        state = False

    return state

    
def doSeperation(text):
    # ne for loop geht hier nicht, weil er dann unendlich lange immer n " " hinzufügt 😭
    i = 0
    while i < len(text) - 2:
        if checkForSillable(text[i], text[i + 1],text[i + 2]): 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennugn einfügen
            i = i + 2
        else:
            i = i + 1
    return text
