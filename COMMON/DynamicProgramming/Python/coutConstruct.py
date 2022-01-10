#
# Return the number of ways to construct the target word from the word bank.
#

def countConstruct(target, wordBank, memo):
    if (target in memo): return memo[target]
    if (target == ""): return 1

    totalCount = 0

    for word in wordBank:
        if target.find(word) == 0:
            numberOfWays = countConstruct(target[len(word):], wordBank, memo)
            totalCount += numberOfWays
    memo[target] = totalCount
    return totalCount


print(countConstruct("purple",["purp", "p", "ur", "le", "purpl"], {}))
print(countConstruct("abcdef",["ab", "abc", "cd", "def", "abcd"], {}))
print(countConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "board"], {}))
print(countConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee", "eee", "eeee", "eeeee", "eeeeee"], {}))
