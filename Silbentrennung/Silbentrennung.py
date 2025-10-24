from german_compound_splitter import comp_split


def check_for_comp(compound):
    input_file = '/dicts/german.dic'
    ahocs = comp_split.read_dictionary_from_file(input_file)

    dissection = comp_split.dissect(compound, ahocs, make_singular=True)
    print('SPLIT WORDS (plain):', dissection)
    print('SPLIT WORDS (post-merge):', comp_split.merge_fractions(dissection))


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
    c = c.lower()
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
    elif c[1] == "a" and c[2] == "i":
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
        if c[2] == c[3]:
            state = False
        else:
            skip_next = True
            state = True

    # 1 Vokal und keine 2 Konsonanten
    if isConsonant(c[1]) == False and ((isConsonant(c[2]) == False and isConsonant(c[3])) or (isConsonant(c[2]) and isConsonant(c[3]) == False)):
        state = True


    # Der Sauerkraut Fix: 3 Vokale
    if isConsonant(c[1]) == False and isConsonant(c[2]) == False and isConsonant(c[3]) == False:
        state = True

    if isFirstOrLastChar(c[0]) and isConsonant(c[1]) or isFirstOrLastChar(c[3]):
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
    if "sch" in c:
        state = False

    if c[0] == "c" and c[1] == "h" and isConsonant(c[2]):
        state = False

    if cant_seperate(c):
        state = False

    if c[1] == c[2] and c[3] == "h":
        state = False

    return state, skip_next



def doSeperation(text):
    i = 1
    text = " " + text
    word_start_i = 0
    while i < len(text) - 3:
        if(text[i] in " ?.,:!"):
            print(text[word_start_i: i])
        (state,skipNext) = check_for_sillable(text[i - 1] + text[i] + text[i + 1] + text[i + 2] + text[i + 3])
        if state: 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennung einfügen
            if (skipNext): i = i + 1
            i = i + 2
        else:
            i = i + 1
    return text

