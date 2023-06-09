# Can take a target sum and an array of numbers
# SHould return a bool, True if can get the target sum using numbers in the array
# you may use a number in the array multiple times.
# assume all input numbers are positive

def canSum(targetSum, numbers, memo):
    if targetSum in memo: return(memo[targetSum])
    if targetSum == 0: return(True)
    if targetSum < 0: return(False)

    for number in numbers:
        remainder =  targetSum - number
        if(canSum(remainder, numbers, memo) == True):
            memo[targetSum] = True;
            return(True)

    memo[targetSum] = False;
    return(False)

print(canSum(7, [2, 3], {}))
print(canSum(7, [5, 3, 4,7], {}))
print(canSum(7, [2, 4], {}))
print(canSum(8, [2, 3, 5], {}))
print(canSum(300, [7, 14], {}))