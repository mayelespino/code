#
#
#
def howSumTab(target, numbers):
    table = [None] * (target + 1)
    table[0] = []

    for index, spot in enumerate(table):
        if spot is None:
            continue
        for number in numbers:
            if (index + number) <= target:
                newSpot = spot.copy()
                newSpot.append(number)
                table[(index + number)] = newSpot

    return table[target]


if __name__ == "__main__":
    print(howSumTab(7, [2, 3])) # 3,2,2
    print(howSumTab(7, [5, 3, 4, 7])) # 4,3
    print(howSumTab(7, [2, 4])) # None
    print(howSumTab(8, [2, 3, 5])) # 2,2,2,2
    print(howSumTab(300, [7, 14])) # #None