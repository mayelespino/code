# 6. Reverse Words in a String
# Code it now: https://oj.leetcode.com/problems/reverse-words-in-a-string/ Difficulty: Medium, Frequency: High Question:
# Given an input string s, reverse the string word by word.
# For example, given s = "the sky is blue", return "blue is sky the".

def reverse_words(sentence):
    words =  sentence.split()
    reverse_sensece = " ".join(reversed(words))
    return(reverse_sensece)

def main():
    print("the sky is blue")
    print(reverse_words("the sky is blue"))

if __name__ == "__main__": main()