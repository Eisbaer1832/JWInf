def isConsonant(char):
    if char.lower() in "aeiouäöüy!.,;- ":
        return False
    else:
        return True

def isFirstOrLastChar(char):
    if (char in " ?.,:!" or char == ""):
        return True
    else:
        return False
    
    
def checkForSillable(char0, char1, char2, char3):
    state = False
    skipNext = False
    
    # 2 Konsonanten
    if (isConsonant(char1) and isConsonant(char2)):
        print(char1 + " und " + char2 + " sind Konsonanten!")
        state = True
    
    # h ist nach einem Voakl Stumm und wird dann nicht getrennt ig?
    if (isConsonant(char1) == False and char2 == "h"):
        state = False
        
    # 3 Konsonanten
    if (isConsonant(char1) and isConsonant(char2) and isConsonant(char3)):
        skipNext = True # nur der Erste darf ne " " kriegen
        state = True
    



    # 1 Vokal und keine 2 Konsonanten
    if (isConsonant(char1) == False and ((isConsonant(char2) == False and isConsonant(char3)) or (isConsonant(char2) and isConsonant(char3) == False))):
        state = True

    # Der Sauerkraut Fix: 3 Vokale
    #if (isConsonant(char1) == False and isConsonant(char2) == False and isConsonant(char3) == False):
    #    state = True
    # hier muss iwi nach dem 2. getrennt werden, da müssen wir uns nochmal angucken

    # ch darf man glaub ich nicht trennen hoffe ich
    if (char1 == "c"  and char2 == "h" or char2 == "c" and char3 == "h" or char1 == "e"  and char2 == "u" or char1 == "m"  and char2 == "m" or char1 == "l"  and char2 == "l"):
        state = False
    
    # Letztes Zeichen des Worts
    if (isFirstOrLastChar(char3) or isFirstOrLastChar(char0)):
        state = False

    # Verhindert, dass Lehrzeichen Silbentrennugnkriegne
    if (char1 == " "):
        state = False

    return (state, skipNext)

    
def doSeperation(text):
    # ne for loop geht hier nicht, weil er dann unendlich lange immer n " " hinzufügt 😭
    i = 1
    while i < len(text) - 2:
        (state,skipNext) = checkForSillable(text[i-1], text[i], text[i + 1],text[i + 2])
        if state: 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennugn einfügen
            if (skipNext): i = i + 1
            i = i + 2
        else:
            i = i + 1
    return text
