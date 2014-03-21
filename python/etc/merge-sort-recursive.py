#!/usr/bin/python
def merge(list1, list2):
  i = 0
  j = 0
  output = []
  len1 = len(list1)
  len2 = len(list2)
  while i < len1 or j < len2:
    # case 1: both lists have data
    if i < len1 and j < len2:
      if list1[i] < list2[j]:
        # list1 has a smaller element.
        output += [list1[i]]
        i = i+1
      else:
        # list2 has a smaller element.
        output += [list2[j]]
        j = j+1
    # case 2: only list1 has data
    elif i < len1:
      output += [list1[i]]
      i = i+1
    # case 3: only list2 has data
    elif j < len2:
      output += [list2[j]]
      j = j+1
  return output

def mergeSort(list):
  length = len(list)
  # base case
  if length <= 1:
    return list
  # recursive case
  else:
    # Divide
    mid = length/2
    left = list[0:mid]
    right = list[mid:]
    # Conquer
    sorted_left = mergeSort(left)
    sorted_right = mergeSort(right)
    # Combine
    return merge(sorted_left, sorted_right)


l = [1, 6, 7, 2, 76, 45, 23, 4, 8, 12, 11]
sortedList = mergeSort(l)
print sortedList
 
