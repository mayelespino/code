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

def find_target_factors(int_map, target):
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
    print(find_target_factors(int_map, 10))


if __name__ == '__main__': main()