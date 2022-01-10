#
# Return a list of all the possible ways to construct the target word from the word bank.
#

def allConstruct(target, wordBank, memo):
    if target in memo: return memo[target]
    if target == "" : return [[]]

    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffixWays = allConstruct(target[len(word):], wordBank, memo)
            for way in suffixWays:
                way.insert(0,word)
            result.extend(suffixWays)
    memo[target] = result
    return result


print(allConstruct("purple",["purp", "p", "ur", "le", "purpl"], {}))
print(allConstruct("abcdef",["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))
print(allConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "board"], {}))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeee", ["e","ee", "eee", "eeee", "eeeee", "eeeeee"], {}))
