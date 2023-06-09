# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

def isAnagram(string1, string2):
    if len(string1) != len(string2):
        return False
    if sorted(string1) != sorted(string2) :
        return False
    return True


# print(isAnagram("","")) # True
# print(isAnagram(""," ")) # Falser
# print(isAnagram("a","a")) # True
# print(isAnagram("abc","abc")) # True
# print(isAnagram("aabbcc","abc")) # False
# print(isAnagram("123","321")) # True
# print(isAnagram("aabbcc","abcabc")) # True


def isAnagramPlus(string1, string2):
    if len(string1) != len(string2):
        return False

    hashTable = {}

    for letter in string1:
        if letter not in hashTable:
            hashTable[letter] = 1
        else:
            hashTable[letter] += 1

    for letter in string2:
        if letter not in hashTable:
            return False
        if (hashTable[letter] - 1) < 0:
            return False

        hashTable[letter] -= 1

    for count in hashTable.values():
        if count != 0:
            return False

    return True 


print(isAnagramPlus("","")) # True
print(isAnagramPlus(""," ")) # Falser
print(isAnagramPlus("a","a")) # True
print(isAnagramPlus("abc","abc")) # True
print(isAnagramPlus("aabbcc","abc")) # False
print(isAnagramPlus("123","321")) # True
print(isAnagramPlus("aabbcc","abcabc")) # True
