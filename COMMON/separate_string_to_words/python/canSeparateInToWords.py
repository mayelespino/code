

def canSeparateInToWords(sString, wDict):
    word = ""
    foundWord = False
    for c in sString:
        word += c
        foundWord = False
        if word in wDict:
            word = ""
            foundWord = True
    return foundWord

def separateInToWords(sString, wDict):
    word = ""
    wordsArray = []
    foundWord = False
    for c in sString:
        word += c
        foundWord = False
        if word in wDict:
            wordsArray.append(word)
            word = ""
            foundWord = True

    if foundWord:
        return wordsArray
    else:
        return None

if __name__ == "__main__":
    sourceString = "applecartbla"
    words = ["apple", "cart"]
    print(sourceString, "<-->", words)
    print(canSeparateInToWords(sourceString, words))
    print(separateInToWords(sourceString, words))
    print("\n-----\n")
    sourceString = "applecart"
    words = ["apple", "cart"]
    print(sourceString, "<-->", words)
    print(canSeparateInToWords(sourceString, words))
    print(separateInToWords(sourceString, words))
    print("\n-----\n")
    sourceString = "blaapplecart"
    words = ["apple", "cart"]
    print(sourceString, "<-->", words)
    print(canSeparateInToWords(sourceString, words))
    print(separateInToWords(sourceString, words))
