# After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters.
# The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

# Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

# grid1 = [
# 	['c', 'c', 'x', 't', 'i', 'b'],
# 	['c', 'c', 'a', 't', 'n', 'i'],
# 	['a', 'c', 'n', 'n', 't', 't'],
# 	['t', 'c', 's', 'i', 'p', 't'],
# 	['a', 'o', 'o', 'o', 'a', 'a'],
# 	['o', 'a', 'a', 'a', 'o', 'o'],
# 	['k', 'a', 'i', 'c', 'k', 'i'],
# ]
# word1 = "catnip"
# word2 = "cccc"
# word3 = "s"
# word4 = "bit"
# word5 = "aoi"
# word6 = "ki"
# word7 = "aaa"
# word8 = "ooo"

# grid2 = [['a']]
# word9 = "a"

# find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
# find_word_location(grid1, word2) =>
#        [(0, 1), (1, 1), (2, 1), (3, 1)]
#     OR [(0, 0), (1, 0), (1, 1), (2, 1)]
#     OR [(0, 0), (0, 1), (1, 1), (2, 1)]
#     OR [(1, 0), (1, 1), (2, 1), (3, 1)]
# find_word_location(grid1, word3) => [(3, 2)]
# find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
# find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
# find_word_location(grid1, word6) => [(6, 4), (6, 5)]
# find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
# find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
# find_word_location(grid2, word9) => [(0, 0)]

# Complexity analysis variables:

# r = number of rows
# c = number of columns
# w = length of the word


grid1 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'c', 'a', 't', 'n', 'i'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'c', 's', 'i', 'p', 't'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['o', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'c', 'k', 'i']
]

word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"


def findTheRestOfWord(grid, row, column, word, XLen, YLen, Wlen, result):
    result.append((row, column))
    if len(word) == 0:
        return result

    if column + 1 <= XLen and grid[row][column + 1] == word[0]:
        result = findTheRestOfWord(grid, row, column+1, word[1:], XLen, YLen, Wlen, result)
        if(len(result) == Wlen):
            return (result)
        else:
            result.pop()

    if row + 1 <= YLen and grid[row + 1][column] == word[0]:
        result = findTheRestOfWord(grid, row + 1, column, word[1:], XLen, YLen, Wlen, result)
        if(len(result) == Wlen):
            return (result)
        else:
            result.pop()

    return (result)


def find_word_location(grid, word):
    for row, line in enumerate(grid):
        for column, character in enumerate(line):
            # print(f"[{row}, {column}]{character}  ", end="")
            if character == word[0]:
                result = []
                result = findTheRestOfWord(grid, row, column, word[1:], len(grid[0]) -1 , len(grid) -1, len(word), result)
                if result is not None and len(result) == len(word):
                    return (result)
    return (None)




if __name__ == '__main__':
    print(find_word_location(grid1, "catnip"))
    print(find_word_location(grid1, "cccc"))
    print(find_word_location(grid1, "s"))
    print(find_word_location(grid1, "bit"))
    print(find_word_location(grid1, "aoi"))
    print(find_word_location(grid1, "ki"))
    print(find_word_location(grid1, "aaa"))
    print(find_word_location(grid1, "ooo"))
    print(find_word_location(grid2, "a"))


