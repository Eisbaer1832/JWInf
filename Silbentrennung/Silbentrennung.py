from loguru import logger


def isConsonant(char):
    if char.lower() in "aeiouäöüy!.,;- ":
        return False
    else:
        return True

def isFirstOrLastChar(char):
    if char in " ?.,:!" or char == "":
        return True
    else:
        return False

def cant_seperate(c):
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


def check_for_sillable(c):
    state = False
    skip_next = False


    # 2 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]):
        state = True

    # 3 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]) and isConsonant(c[3]):
        skip_next = True # nur der Erste darf ne " " kriegen
        state = True

    # 1 Vokal und keine 2 Konsonanten
    if isConsonant(c[1]) == False and ((isConsonant(c[2]) == False and isConsonant(c[3])) or (isConsonant(c[2]) and isConsonant(c[3]) == False)):
        state = True


    # Der Sauerkraut Fix: 3 Vokale
    if (isConsonant(c[1]) == False and isConsonant(c[2]) == False and isConsonant(c[3]) == False):
        state = True

    if isFirstOrLastChar(c[0]) or isFirstOrLastChar(c[3]):
        state = False

    # h ist nach einem Voakl Stumm und wird dann nicht getrennt ig?
    if isConsonant(c[1]) == False and c[2] == "h":
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

    if cant_seperate(c):
        state = False

    return state, skip_next



def doSeperation(text):
    i = 1
    text = " " + text
    while i < len(text) - 2:
        (state,skipNext) = check_for_sillable(text[i - 1] + text[i] + text[i + 1] + text[i + 2])
        if state: 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennugn einfügen
            if (skipNext): i = i + 1
            i = i + 2
        else:
            i = i + 1
    return text

