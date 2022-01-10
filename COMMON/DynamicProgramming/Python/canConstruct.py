#
# The function takes a target word and an array of words that may be used to build the target.
# The function will return True if the target can be constructed from the words in the bank.
#

def canConstruct(target, wordBank, memo):
    if target in memo : return memo[target]
    if target == ""  : return True

    for word in wordBank:
        if target.find(word) == 0:
            newTarget = target[len(word):]
            if canConstruct(newTarget, wordBank, memo) == True: 
                memo[target] = True
                return  True
    memo[target] = False
    return(False)
 

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee", "eee", "eeee", "eeeee", "eeeeee"], {}))