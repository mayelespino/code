#
# Leetcode Chapter 1: Array/String - Solition B, sorted array
#
import random

def generate_array(length):
    int_list = [0]
    for idx in range(length):
        number = random.randint(1,length)
        if number not in int_list:
            int_list.append(number)
    int_list.sort()
    return(int_list)

def bin_search(list, target):
    start = 1
    end = len(list)
    location = int(end/2)

    for turn in range(location):
        if list[location] == target:
            break
        elif list[location] > target:
            end = location
            location = start + int((end - start)/2)
        elif list[location] < target:
            start =  location
            location = start + int((end - start)/2)
    if list[location] != target:
        return (0)
    else:
         return(location)

def two_sum(int_list, target, start=1):
    index1, index2, complement = 0, 0, 0
    for idx in range(start,len(int_list)):
        if int_list[idx] < target:
            index1 = idx
            complement = target - int_list[idx]
            break

    index2 = bin_search(int_list, complement)
    if index2 != 0:
      return (index1, index2)
    else:
        start += 1
        two_sum(int_list, target, start)

def main():
    int_list = generate_array(100)
    print(int_list)
    target = 55
    index1, index2 = two_sum(int_list, target)
    print("map[{}] + map[{}] = {}".format(index1, index2, target))
    print("{} + {} = {}".format(int_list[index1], int_list[index2], target))
    assert(index1 < index2), "index1 < index2"
    assert(int_list[index1] + int_list[index2] == target), "two numbers selected do not equate to target"

if __name__ == '__main__': main()