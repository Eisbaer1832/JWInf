from SCons.Tool.MSCommon.vc import component_id
from german_compound_splitter import comp_split
from loguru import logger
from trimesh.bounds import contains
import pandas as pd

dict = comp_split.read_dictionary_from_file( './dicts/german.dic')
german = pd.read_csv("./dicts/german.dic", header=None, names=["word"], encoding="utf-8")
english = pd.read_csv("./dicts/english.dic", header=None, names=["word"], encoding="utf-8")


def check_for_comp(compound):
    pass_compound = compound.strip(",").strip()
    result = compound

    schIndex = pass_compound.rfind("sch")
    try:
        if schIndex >= 1:
            schIndex = schIndex + 3
            if isConsonant(pass_compound[schIndex]):
                pass_compound = pass_compound[0:schIndex] + " " + pass_compound[schIndex: len(pass_compound)]
                result = " " + pass_compound
    except:
        pass

    chIndex = pass_compound.rfind("ch")
    try:
        if chIndex >= 1:
            chIndex = chIndex + 2
            if not isConsonant(pass_compound[chIndex - 3]) and isConsonant(pass_compound[chIndex]) and not isFirstOrLastChar(pass_compound[chIndex + 1]):
                pass_compound = pass_compound[0:chIndex] + " " + pass_compound[chIndex: len(pass_compound)]
                result = " " + pass_compound
    except:
        pass

    # check for prefix
    prefix = ["be", "ent", "ver"]
    for e in prefix:
        if pass_compound.startswith(e):
            pass_compound = " " + pass_compound[0:len(e)] + " " + pass_compound[len(e):len(pass_compound)]
            result = pass_compound

    try:
        dissection = comp_split.dissect(pass_compound, dict)

        if len(dissection) > 1:
            #logger.info(dissection)
            for i in range(len(dissection) - 1):
                index = result.lower().rfind(dissection[i + 1].lower())
                result = result[0:index] + " " + result[index:len(result)]
                index += 1
            #logger.debug(result)
        return result
    except:
        return compound

def is_english(word):
    return
    #print("german[word]")

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
    elif c[1] == "i" and c[2] == "e":
        return True
    elif c[1] == "h" and c[2] == "r":
        return True
    elif c[1] == "s" and c[2] == "c" and c[3] == "h":
        return True
    else:
        return False

def check_for_sillable(c):
    state = False
    skip_next = False

    # 3 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]) and isConsonant(c[3]) and not cant_seperate(c):
        if c[2] == c[3]:
            state = False
        else:
            state = True

    # 2 Konsonanten
    if isConsonant(c[1]) and isConsonant(c[2]):
        state = True

    # "lich"-Fix -> "-liche"-Trennung / "-lich"-keine Trennung
    if c[2] == "c" and c[3] == "h":
        if not isConsonant(c[1]) and isFirstOrLastChar(c[4]):
            state = False
        elif not isConsonant(c[4]):
            state = True

    if c[1] == c[2]:
        if c[3] == "h":
            state = False
        elif isConsonant(c[3]) and isFirstOrLastChar(c[4]):
            state = False
        else:
            state = True

    # 1 Vokal und keine 2 Konsonanten
    if isConsonant(c[1]) == False and ((isConsonant(c[2]) == False and isConsonant(c[3])) or (isConsonant(c[2]) and isConsonant(c[3]) == False)):
        state = True

    # Der Sauerkraut Fix: 3 Vokale
    if isConsonant(c[1]) == False and isConsonant(c[2]) == False and isConsonant(c[3]) == False:
        state = True

    # "lisch"-Fix -> "-lische"-Trennung / "-lisch"-keine Trennung
    if c[2] == "s" and c[3] == "c" and c[4] == "h":
        if  isFirstOrLastChar(c[5]):
            state = False
        elif not isConsonant(c[1]) and not isConsonant(c[5]):
            state = True


    if isFirstOrLastChar(c[0]) and isConsonant(c[1]) or isFirstOrLastChar(c[3]):
        state = False

    # zwei aufeinanderfolgende Vokale werden getrennt
    if not isConsonant(c[1]) and not isConsonant(c[2]):
        state = True


    if c[1] == "r" and c[2] == "n" and isConsonant(c[3]):
        state = False

    # h ist nach einem Vokal stumm und wird dann nicht getrennt ig?
    if isConsonant(c[1]) == False and c[2] == "h":
        state = False

    # Letztes Zeichen des Worts
    if isFirstOrLastChar(c[2]):
        state = False

    # Verhindert, dass Leerzeichen Silbentrennung kriegen
    if c[1] == " ":
        state = False

    #"sch" und voranstehender Konsonant werden nicht getrennt
    if isConsonant(c[1]) and cant_seperate(c):
        state = False

    if c[0] == "c" and c[1] == "h" and isConsonant(c[2]):
        state = False


    if cant_seperate(c):
        state = False

    is_english(c)


    if c[1] == "y" and c[2] == "t" and c[3] == "e":
        state = False

    if c[0] == "g" and c[1] == "e" and c[2] == "t":
        state = True



    return state, skip_next

def doSeperation(text):
    i = 1
    text = " " + text

    word_start_i = 0
    for j in range(len(text)):
        if text[j] in " ?.,:!" or text[j] == "":
            word = text[word_start_i: j]
            if not word in " ?.,:!":
                text = text.replace(word, check_for_comp(word))
                word_start_i = j

    while i < len(text) - 4:
        (state,skipNext) = check_for_sillable(text[i - 1] + text[i] + text[i + 1] + text[i + 2] + text[i + 3]+ text[i + 4])
        if state: 
            text = text[:i+1] + " " + text[i+1:] # Silbentrennung einfügen
            if (skipNext):
                i = i + 1
            i = i + 2
        else:
            i = i + 1
    return text + " "

