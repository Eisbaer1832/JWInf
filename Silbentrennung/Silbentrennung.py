from loguru import logger


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

def cantSeperate(c):
    if c[1] == "c"  and c[2] == "h":
        return True
    elif c[1] == "e"  and c[2] == "u":
        return True
    elif c[1] == "m"  and c[2] == "m":
        return True
    elif c[1] == "e" and c[2] == "i":
        return True
    elif c[1] == "a" and c[2] == "u":
        return True
    elif c[1] == "c" and c[2] == "k":
        return True
    else:
        return False


def checkForSillable(c):
    state = False
    skipNext = False

    # 2 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]):
        state = True

    # h ist nach einem Voakl Stumm und wird dann nicht getrennt ig?
    if isConsonant(c[1]) == False and c[2] == "h":
        state = False

    # 3 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]) and isConsonant(c[3]):
        skipNext = True # nur der Erste darf ne " " kriegen
        state = True

    # 1 Vokal und keine 2 Konsonanten
    if isConsonant(c[1]) == False and ((isConsonant(c[2]) == False and isConsonant(c[3])) or (isConsonant(c[2]) and isConsonant(c[3]) == False)):
        state = True


    # Der Sauerkraut Fix: 3 Vokale
    if (isConsonant(c[1]) == False and isConsonant(c[2]) == False and isConsonant(c[3]) == False):
        state = True
    # hier muss iwi nach dem 2. getrennt werden, da müssen wir uns nochmal angucken

    # ch darf man glaub ich nicht trennen hoffe ich
    if cantSeperate(c):
        state = False

    # Letztes Zeichen des Worts
    if isFirstOrLastChar(c[2]):
        state = False

    # Verhindert, dass Leerzeichen Silbentrennugnkriegne
    if c[1] == " ":
        state = False

    #"sch" und anschließender Konsonant werden getrennt
    if c[0] == "s" and c[1] == "c" and c[2] == "h" and isConsonant(c[3]):
        state = False

    firstLetter = False
    
    # ebenfalls Fix
    if c[1] == "" or c[1] == " ":
        firstLetter = True
    else: 
        firstLetter = False

    if firstLetter and not isConsonant(c[1]) and isConsonant(c[2]):
        state = True


    return state, skipNext



def doSeperation(text):
    # ne for loop geht hier nicht, weil er dann unendlich lange immer n " " hinzufügt 😭
    i = 1
    text = " " + text
    while i < len(text) - 2:
        (state,skipNext) = checkForSillable(text[i-1] + text[i] + text[i + 1] + text[i + 2])
        if state: 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennugn einfügen
            if (skipNext): i = i + 1
            i = i + 2
        else:
            i = i + 1

    return text


#doSeperation(sys.argv[1])
