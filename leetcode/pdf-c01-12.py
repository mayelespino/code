# Question:
# Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
# For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
import random

def generate_array_with_gaps():
    array = [ i for i in range(100)]
    for index in range(50):
        gap = random.randint(0,99)
        if gap in array:
            array.remove(gap)
    return(array)


def find_missing_ranges(list):
    result_list = []
    if list[0] == 1:
        result_list.append("0")
    elif list[0] >= 2:
        result_list.append("0->{}".format(list[idx] - 1))

    for idx in range(1,len(list)):
        if (list[idx] - list[idx-1]) > 2:
            result_list.append("{}->{}".format(list[idx-1] + 1, list[idx] - 1))
        elif (list[idx] - list[idx-1]) == 2:
            result_list.append("{}".format(list[idx] - 1))
            
    if list[-1] == 98:
        result_list.append("99")
    elif list[-1] < 98:
        result_list.append("{}->99".format(list[-1] + 1))
    print(result_list)


def main():
    original_list = generate_array_with_gaps()
    print(original_list)
    find_missing_ranges(original_list)

if __name__ == "__main__": main()