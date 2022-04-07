#
# tabular version of bestSum.py
# return the shortest combination that results in the target.
#
def bestSumTab(target, numbers):
    table = [None] * (target + 1)
    table[0] = []

    for index, spot in enumerate(table):
        if spot is None:
            continue

        for number in numbers:
            if (index + number) > target: continue
            newList = spot.copy()
            newList.append(number)
            if table[(index + number)] == None or len(table[(index + number)] ) < len(newList):
                table[(index + number)] = newList

    return table[target]


if __name__ == "__main__":
    print(bestSumTab(7, [2, 3])) # T
    print(bestSumTab(7, [5, 3, 4, 7]))  # T
    print(bestSumTab(7, [2, 4]))  # F
    print(bestSumTab(8, [2, 3, 5]))  # T
    print(bestSumTab(300, [7, 14]))  # F
