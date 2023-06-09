
def gridTraveler(m, n, memo = {}):
    key = f'{m},{n}'
    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1
    memo[key] = (gridTraveler(m - 1, n) + gridTraveler(m, n - 1))
    return(memo[key])

if __name__ == "__main__":
    print(gridTraveler(1,1))
    print(gridTraveler(3,3))
    print(gridTraveler(3,2))
    print(gridTraveler(2,3))
    print(gridTraveler(18, 18))