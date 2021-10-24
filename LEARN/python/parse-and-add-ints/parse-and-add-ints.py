#!/usr/local/bin/python3
"""
partse numbers out of a given string and
"""
import re

def parse_and_sum_ints(string):
    numbers = re.split("\D+", string)
    total = 0
    for number in numbers:
        if number == '':
            continue
        total += int(number)
        print(number,)
    print("-----")
    return (total)

def main():
    print("\n")
    print(parse_and_sum_ints(""))
    print("\n")
    print(parse_and_sum_ints("30"))
    print("\n")
    print(parse_and_sum_ints("l30"))
    print("\n")
    print(parse_and_sum_ints("bla20lll100akdfjadsl30"))

if __name__ == "__main__" : main()