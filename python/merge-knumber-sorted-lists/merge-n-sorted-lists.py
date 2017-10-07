#!/usr/local/bin/python3

def merge_two_lists(list_a, list_b):
    """
    :param list_a:
    :param list_b:
    :return: result_list
    """
    result_list = []

    while len(list_a) > 0 and len(list_b) > 0:
        if list_a[0] < list_b[0] :
            result_list.append(list_a[0])
            list_a.pop(0)
        else:
            result_list.append(list_b[0])
            list_b.pop(0)

    result_list += list_a
    result_list += list_b

    return(result_list)

def merge_k_lists(list_a, list_b, *kLists):
    """
    :param list_a: first required list
    :param list_b: second required list
    :param kLists: valiable number of lists
    :return:
    """
    result_list = merge_two_lists(list_a, list_b)
    for list in kLists:
        result_list = merge_two_lists(result_list, list)

    return(result_list)


def main():
    print(merge_k_lists([1,2,3,4],[10,11,12,13,14], [5,6,7,8,9], [100,101,110,115]))

if __name__ == "__main__" : main()