#
# Best Sum
# return the shortest array thar adds up exactly to the target array.
# 

# def bestSum(targetSum, numbers):
#     if targetSum == 0: return []
#     if targetSum < 0 : return None

#     shortest = None

#     for number in numbers:
#         remainder = targetSum - number
#         result = bestSum(remainder, numbers)
#         if result != None:
#             result.append(number)
#             if shortest == None or len(result) < len(shortest): 
#                 shortest = result

#     return shortest

def bestSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum < 0: return None
    if targetSum == 0: return []

    shortest = None

    for number in numbers:
        remainder = targetSum - number
        result = bestSum(remainder, numbers, memo)
        if result != None:
            newResult = list(result).copy()
            newResult.append(number)
            if shortest == None or len(result) < len(shortest): 
                shortest = newResult
    memo[targetSum] = shortest            
    return  shortest

print(bestSum(7, [5, 3, 4, 7], {}))
print(bestSum(8, [2, 3, 5], {}))
print(bestSum(8, [1, 4, 5], {}))
print(bestSum(100, [1, 2, 5, 25], {}))