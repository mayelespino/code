#
# tabular version of canSum.py
#
def canSumTab(target, numbers):
    table = [False] * (target + 1)
    table[0] = True

    for index, spot in enumerate(table):
        if spot is False:
            continue
        for number in numbers:
            if (index + number) <= target:
                table[(index + number)] = True

    return table[target]


if __name__ == "__main__":
    print(canSumTab(7, [2, 3])) # T
    print(canSumTab(7, [5, 3, 4, 7]))  # T
    print(canSumTab(7, [2, 4]))  # F
    print(canSumTab(8, [2, 3, 5]))  # T
    print(canSumTab(300, [7, 14]))  # F
