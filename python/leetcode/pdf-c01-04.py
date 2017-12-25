# 4. Valid Palindrome
# Code it now: https://oj.leetcode.com/problems/valid-palindrome/ Difficulty: Easy, Frequency: Medium
# Question:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.

import string


def isValidPalindrome(_phrase):
    valid_characters = string.ascii_lowercase + "1234567890"
    new_string = ""
    for character in _phrase:
        char = character.lower()
        if char in valid_characters:
            new_string += char
    reverse_string = new_string[::-1]
    if new_string == reverse_string:
        return(True)
    else:
        return(False)

def main():
    phrase = "A man, a plan, a canal: Panama"
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == True)
    phrase = "abc"
    print(phrase)
    print(isValidPalindrome(phrase))
    assert(isValidPalindrome(phrase) == False)

if __name__ == "__main__": main()