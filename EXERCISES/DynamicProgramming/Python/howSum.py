#
# takes in target sum and an array of numbers
# returns the array of the numbers that add up to the sum (exactly). Any combination is valid, return only one.
# if no combination is found return null or empty array
# 

def howSum(targetSum, numbers, memo):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0 : return None

    for number in numbers:
        remainder = targetSum - number
        result = howSum(remainder, numbers, memo)
        if result != None:
            result.append(number)
            memo[number] = result
            return result
    memo[targetSum] = None
    return None

print(howSum(7, [2, 3], {}))
print(howSum(7, [5, 3, 4, 7], {}))
print(howSum(7, [2, 4], {}))
print(howSum(8, [2, 3, 5], {}))
print(howSum(300, [7, 14], {}))