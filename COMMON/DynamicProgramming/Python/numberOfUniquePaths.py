# - start from top to bottom
# - can only go down or right
# - how many ways to get to the bottom right most position of an n x m matrix
# - leetcode 62

def uniquePaths(n, m):
    board = [[1 for i in range(m)] for j in range(n)]
    n -= 1
    m -= 1
    # fill last row wil 1s
    for col in range(m, -1, -1):
        board[n][col] = 1

    # calculate the value in the cell as the sum of the cell to the right and the cell below.
    for row in range(n -1, -1, -1):
        for col in range(m -1, -1, -1):
            board[row][col] = (board[row][col+1] + board[row+1][col])
    return(board)


if __name__ == "__main__":
    print(uniquePaths(2,2))
    print(uniquePaths(2, 3))
    print(uniquePaths(3, 7))
    print(uniquePaths(7, 3))
    print(uniquePaths(5, 4))