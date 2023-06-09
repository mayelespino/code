#
#
#
def gridTravel(rows, cols):
    table  = [[0 for i in range(cols+1)] for j in range(rows+1)]
    table[1][1] = 1

    for i in range(rows):
        for j in range(cols):
            table[i][j+1] += table[i][j]
            table[i+1][j] += table[i][j]
        table[i+1][cols] += table[i][cols]
    for j in range(cols):
        table[rows][j+1] += table[rows][j]

    return table[rows][cols]

if __name__ == "__main__":
    print(gridTravel(1, 1)) # 1
    print(gridTravel(3, 2)) # 3
    print(gridTravel(3, 3)) # 6
    print(gridTravel(18, 18)) # 2333606220