# 13. Longest Palindromic Substring
# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
def is_palindrom_start(in_list, position):
    if in_list[position - 1] == in_list[position]:
        return True
    elif in_list[position - 1] == in_list[position + 1]:
        return True
    else:
        return False

# def find_length_of_palindrom(in_list, position):
#     left = position
#     right = len(in_list) - position -1
#     if left == right:
#         max_length = left
#     elif left > right:
#         max_length = right
#     else:
#         max_length = left
#     return(max_length)


def longest_palindrom(in_string):
    max_palindrom = {}
    for idx in range(1,len(in_string)-1):
        is_it = is_palindrom_start(in_string, idx)
        if is_it is True:
            tmp_string = in_string[idx]
            offset = 1
            while (idx - offset) >= 0 and (idx + offset) < len(in_string):
                if in_string[idx] == in_string[idx - offset]:
                    tmp_string = in_string[idx - offset] + tmp_string
                if in_string[idx] == in_string[idx + offset]:
                    tmp_string = tmp_string + in_string[idx + offset]
                if in_string[idx - 1] == in_string[idx + offset]:
                    tmp_string = in_string[idx - offset] + tmp_string + in_string[idx + offset]
                offset  +=1
            max_palindrom[idx] = tmp_string

    max_len_palindrom = ""
    for k,v in max_palindrom.items():
            #print("{}:{}".format(k, v))
            if len(v) >= len(max_len_palindrom):
                max_len_palindrom = v
    return (max_len_palindrom)

def main():
    s1 = "abacdgfdcaba"
    p1 = longest_palindrom(s1)
    print(p1)
    assert(p1 == "aba")

    s1 = "aacdgfdcaba"
    p1 = longest_palindrom(s1)
    print(p1)
    assert(p1 == "aba")

    s1 = "aacdgfdcaa"
    p1 = longest_palindrom(s1)
    print(p1)
    assert(p1 == "aa")

if __name__ == "__main__": main()