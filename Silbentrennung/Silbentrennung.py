import sys
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
    if (c[1] == "c"  and c[2] == "h"):
        return True
    elif (c[1] == "e"  and c[2] == "u"):
        return True
    elif (c[1] == "m"  and c[2] == "m"):
        return True
    elif (c[1] == "e" and c[2] == "i"):
        return True
    elif (c[1] == "a" and c[2] == "u"):
        return True
    elif (c[1] == "c" and c[2] == "k"):
        return True
    else:
        return False


def checkForSillable(c):
    state = False
    skipNext = False
    logger.debug("-------------------")
    logger.debug(c)
    
    # 2 Konsonanten
    if (isConsonant(c[1]) and isConsonant(c[2])):
        logger.debug("2 Konsonanten: True")
        state = True
    else:
        logger.debug("2 Konsonanten: False")

    # h ist nach einem Voakl Stumm und wird dann nicht getrennt ig?
    if (isConsonant(c[1]) == False and c[2] == "h"):
        logger.debug("Stummer Vokal: True")
        state = False
    else:
        logger.debug("Stummer Vokal: False")

    # 3 Konsonanten
    if (isConsonant(c[1]) and isConsonant(c[2]) and isConsonant(c[3])):
        logger.debug("3 Konsonanten: True")
        skipNext = True # nur der Erste darf ne " " kriegen
        state = True
    else:
        logger.debug("3 Konsonanten: False")

    # 1 Vokal und keine 2 Konsonanten
    if (isConsonant(c[1]) == False and ((isConsonant(c[2]) == False and isConsonant(c[3])) or (isConsonant(c[2]) and isConsonant(c[3]) == False))):
        logger.debug("1 Vokal und keine 2 Konsonanten: True")
        state = True
    else:
        logger.debug("1 Vokal und keine 2 Konsonanten: False")


    # Der Sauerkraut Fix: 3 Vokale
    #if (isConsonant(c[1]) == False and isConsonant(c[2]) == False and isConsonant(c[3]) == False):
    #    state = True
    # hier muss iwi nach dem 2. getrennt werden, da müssen wir uns nochmal angucken

    # ch darf man glaub ich nicht trennen hoffe ich
    if (cantSeperate(c)):
        logger.debug("ch Trennung: True")
        state = False
    else:
        logger.debug("ch Trennung: False")
    
    # Letztes Zeichen des Worts
    if (isFirstOrLastChar(c[2])):
        logger.debug("Letztes Zeichen des Worts: True")
        state = False
    else:
        logger.debug("Letztes Zeichen des Worts: False")

    # Verhindert, dass Leerzeichen Silbentrennugnkriegne
    if (c[1] == " "):
        logger.debug("Leerzeichen: True")
        state = False
    else:
        logger.debug("Leerzeichen werden getrennt: False")

    #"sch" und anschließender Konsonant werden getrennt
    if(c[0] == "s" and c[1] == "c" and c[2] == "h" and isConsonant(c[3])):
        logger.debug("sch: True")
        state = False
    else:
        logger.debug("sch: False")
        
    firstLetter = False
    
    # ebenfalls Fix
    logger.critical(c[1])
    if (c[1] == ""):
        logger.critical("first letter detected")
        firstLetter = True
    else: 
        firstLetter = False

    if(firstLetter and not isConsonant(c[1]) and isConsonant(c[2])):
        logger.debug("Vokal zu Beginn: True")
        state = True
    else:
        logger.debug("Vokal zu Beginn: False")

    logger.critical ("Trennung:" + str(state))
    
    return (state, skipNext)


    
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

    logger.debug(text)
    return text


doSeperation(sys.argv[1])
