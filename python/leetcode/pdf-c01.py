#
# Leetcode Chapter 1: Array/String
#
import random

def generate_array(length, range_end):
    int_map = {}
    for idx in range(1,length):
        number = random.randint(1,range_end)
        if number not in int_map:
            int_map[number] = idx
    for key, value in int_map.items():
        print("{}:{}".format(value, key))
    return(int_map)

def two_sum(int_map, target):
    number_list = int_map.keys()
    for key,value in int_map.items():
        if key >= target:
            continue
        complement = (target - key)
        if (complement not in number_list) or (complement == target/2):
            continue
        return(value, int_map[complement])

def main():
    int_map = generate_array(100, 9)
    target = 10
    index1, index2 = two_sum(int_map, target)
    print("map[{}] + map[{}] = {}".format(index1, index2, target))
    print("{} + {} = {}".format(int_map[index1], int_map[index2], target))
    assert(index1 < index2), "index1 < index2"
    assert(int_map[index1] + int_map[index2] == target), "two numbers selected do not equate to target"

if __name__ == '__main__': main()