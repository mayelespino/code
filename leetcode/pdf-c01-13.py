# 13. Longest Palindromic Substring
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
def is_palindrom_start(in_list, position):
    if in_list[position - 1] == in_list[position]:
        return True
    elif in_list[position - 1] == in_list[position + 1]:
        return True
    else:
        return False

def find_length_of_palindrom(in_list, position):
    left = position
    right = len(in_list) - position -1
    if left == right:
        max_length = left
    elif left > right:
        max_length = right
    else:
        max_length = left
    return(max_length)

def longest_palindrom(in_string):
    max_palindrom = {}
    for idx in range(1,len(in_string)-1):
        is_it = is_palindrom_start(in_string, idx)
        # print("{}:{}".format(idx, is_it))
        if is_it is True:
            length = find_length_of_palindrom(in_string, idx)
            if length ==  1:
                tmp_string = in_string[idx - length : idx + length + 1]
            else:
                pass
            max_palindrom[idx] = tmp_string

    for k,v in max_palindrom.items():
            print("{}:{}".format(k, v))


def main():
    s1 = "abacdgfdcaba"
    longest_palindrom(s1)

if __name__ == "__main__": main()