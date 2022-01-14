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
            if (index + number) < target:
                table[(index + number)] = spot.append(number)

    return table[target]


if __name__ == "__main__":
