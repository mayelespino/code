#!/usr/local/bin/python3
from random import randint

random_number_list = []

for idx in range(300):
    random_number_list.append(randint(0,1000))

print(random_number_list)


def mSort(list):
    if len(list) == 1:
        return(list)

    half = int(len(list)/2)
    part_a = list[:half]
    part_b = list[half:]
    part_one = mSort(part_a)
    part_two = mSort(part_b)

    merged_list = []
    while (len(part_one) > 0 ) and (len(part_two) > 0 ):
        if part_one[0] > part_two[0] :
            merged_list.append(part_one[0])
            part_one.pop(0)
        else:
            merged_list.append(part_two[0])
            part_two.pop(0)
    merged_list += part_one
    merged_list += part_two
    return(merged_list)

print("\nSorted list:\n")
print(mSort(random_number_list))
