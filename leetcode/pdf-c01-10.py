# Question:
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for “abcabcbb” is “abc”,
# which the length is 3. For “bbbbb” the longest substring is “b”, with the length of 1.
def find_no_repeat_substr(input_string):
    sub_string = ""
    for char in input_string:
        sub_string += char
        if  input_string.count(sub_string) == len(input_string):
            break
        elif input_string.count(sub_string) == 1:
            break

    return(sub_string)


def main():
    print("abcabcbb")
    print(find_no_repeat_substr("abcabcbb"))
    print("bbbbb")
    print(find_no_repeat_substr("bbbbb"))
    print("abcdcedf")
    print(find_no_repeat_substr("abcdcedf"))
    print("eceba")
    print(find_no_repeat_substr("eceba"))

if __name__ == "__main__": main()