import re
import itertools


def extractPriceDiff(note):
    percent = re.findall(r'\d+\.\d+', note)
    if len(percent) < 1:
        return(00.00, ' ')
    direction = 'U' if note.find("higher") > 0 else 'D'
    return (float(percent[0]), direction)


def solution(prices, notes, x):
    totalDiff = 0.0
    for price, note in itertools.zip_longest(prices, notes):
        percent, direction = extractPriceDiff(note)
        if direction == 'D':
            instoreDiff = (price * percent) / (100.00 - percent)
            totalDiff -= instoreDiff
        elif direction == 'U':
            instoreDiff = (price * percent) / (100.00 + percent)
            totalDiff += instoreDiff

    return (True if totalDiff <= x else False)


# prices = [48, 165]
# notes = ["20.00% lower than in-store",
#          "10.00% higher than in-store"]
# X=2

# prices = [110, 95, 70]
# notes = ["10.0% higher than in-store",
#          "5.0% lower than in-store",
#          "Same as in-store"]
# X = 5

prices = [220]
notes = ["120.0000% higher than in-store"]
X = 120

print(solution(prices, notes, X))