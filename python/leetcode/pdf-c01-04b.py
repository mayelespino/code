# 4. Valid Palindrome
# Code it now: https://oj.leetcode.com/problems/valid-palindrome/ Difficulty: Easy, Frequency: Medium
# Question:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.

import string

def isValidPalindrome(_phrase):
    if _phrase == "":
        return(True)

    valid_characters = string.ascii_lowercase + "1234567890"

    _phrase = list(_phrase.lower())
    while len(_phrase) > 1:
        b_char = _phrase.pop()
        while b_char not in valid_characters and len(_phrase) > 1:
            b_char = _phrase.pop()

        f_char = _phrase.pop(0)
        while f_char not in valid_characters and len(_phrase) > 1:
            f_char = _phrase.pop(0)

        if len(_phrase) == 0:
            return(True)

        if b_char != f_char :
            return(False)
    return(True)


def main():
    phrase = "A man, a plan, a canal: Panama"
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == True)

    phrase = "abc"
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == False)

    phrase = ""
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == True)

    phrase = "abccba"
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == True)


if __name__ == "__main__": main()