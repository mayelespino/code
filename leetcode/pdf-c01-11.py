# Question:
# Given a string S, find the length of the longest substring T that contains at most two distinct characters.
# For example,
# Given S = “eceba”,
# T is "ece" which its length is 3.

def longest_with_two_chars(input_string):
    substring = ""
    for char in input_string:
        substring += char
        if substring.count(char) == 2:
            break
    return(substring)

def main():
    print("eceba")
    print(longest_with_two_chars("eceba"))

if __name__ == "__main__" : main()
