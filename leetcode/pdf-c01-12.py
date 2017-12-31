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


    # for idx in range(1, len(missing_list)-1):
    #     if missing_list[idx] != missing_list[idx+1]-1 or missing_list[idx-1] != missing_list[idx]-1:
    #         result_list.append("{}".format(missing_list[idx]))
    #         result_string += ",{}".format(missing_list[idx])
    #     else:
    #         result_list.append("->")
    #         result_string += "->"


def find_missing_ranges(list, size):
    original_set = set(list)
    full_set = set([i for i in range(size)])
    missing_set = full_set - original_set
    missing_list = [i for i in missing_set]
    print(missing_list)
    result_list = []
    result_list.append("{}|".format(missing_list[0]))
    for idx in range(1, len(missing_list)-1):
        left_delta = (missing_list[idx] - missing_list[idx-1])
        right_delta = (missing_list[idx+1] - missing_list[idx])
        if left_delta == 1:
            result_list.append("{}".format(missing_list[idx]))
        elif left_delta > 1:
            result_list.append("{}->{}".format(missing_list[idx]+1, missing_list[idx+1]-1))
    print(result_list)


def main():
    original_list = generate_array_with_gaps()
    #print(original_list)
    find_missing_ranges(original_list, 100)

if __name__ == "__main__": main()