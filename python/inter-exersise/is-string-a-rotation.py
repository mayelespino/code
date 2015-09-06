#!
# instead of if inStringOne == inStringTwo: ...
#
# inStringOne[index] == instringTwo[index]
#
# indexOne = inStringOne[0] in inStringTwo

def istringRotated(inStringOne, inStringTwo):
    charToFind = inStringOne[0]
    index = inStringTwo.find(charToFind)

    if inStringOne == inStringTwo:
        return True
    if len(inStringOne) != len(inStringTwo):
        return False

    partOne = inStringTwo[index:]
    partTwo = inStringTwo[0:index]

    stringThree = partOne+partTwo

    if inStringOne == stringThree:
        return True
    else:
        return False



S1 = "abcdefghijkl"
S2 = "fghijklabcde"
print "S1[",S1,"]S2[",S2,"], isStringRotated: ",istringRotated(S1,S2)

S1 = "adcx"
S2 = "xadc"
print "S1[",S1,"]S2[",S2,"], isStringRotated: ",istringRotated(S1,S2)

S1 = "qwerty"
S2 = "qwerty"
print "S1[",S1,"]S2[",S2,"], isStringRotated: ",istringRotated(S1,S2)

S1 = "qwertyuiop"
S2 = "asdfghjklz"
print "S1[",S1,"]S2[",S2,"], isStringRotated: ",istringRotated(S1,S2)

S1 = "asd"
S2 = "a"
print "S1[",S1,"]S2[",S2,"], isStringRotated: ",istringRotated(S1,S2)
