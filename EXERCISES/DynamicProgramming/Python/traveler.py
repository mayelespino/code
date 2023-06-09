# 
# The rules to travel: You can go one row down, and/or one colum right.
#

def gridTraveler(m, n, memo):
    key = f"{m},{n}"
    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1 

    memo[key] = (gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo))
    return(memo[key])

#memo = {}
print(gridTraveler(1, 1, {}))
#memo = {}
print(gridTraveler(2, 3, {}))
#memo = {}
print(gridTraveler(3, 2, {}))
#memo = {}
print(gridTraveler(3, 3, {}))
memo = {}
print(gridTraveler(18, 18, memo))