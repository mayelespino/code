#
# tabular version of bestSum.py
#
def bestSumTab(target, numbers):
    table = [False] * (target + 1)
    table[0] = []

    for index, spot in enumerate(table):
        if spot is False:
            continue
        for number in numbers:
            if (index + number) > target: continue
            
            table[(index + number)] = True

    return table[target]


if __name__ == "__main__":
    print(bestSumTab(7, [2, 3])) # T
    print(bestSumTab(7, [5, 3, 4, 7]))  # T
    print(bestSumTab(7, [2, 4]))  # F
    print(bestSumTab(8, [2, 3, 5]))  # T
    print(bestSumTab(300, [7, 14]))  # F
