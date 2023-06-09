#
# Permutations
#

def calculatePartial(elements, partialResult):
    if len(elements) == 1:
        partialResult.append(elements[0])
        return

    for element in elements:
        partialResult.append(element)
        newElements = elements
        newElements.remove(element)
        calculatePartial(newElements,partialResult)

def calculatePermutations(elements):
    result = []
    for element in elements:
        newElements = elements.copy()
        newElements.remove(element)
        partialResult = []
        partialResult.append(element)
        calculatePartial(newElements,partialResult)
        result.append(partialResult)
    return result

print(calculatePermutations([1,2,3]))
print(calculatePermutations([0,1]))