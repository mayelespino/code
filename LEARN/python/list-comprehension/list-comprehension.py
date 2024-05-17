#
# nested comprehension
#
# Nested list comprehension

print("list comprehension 1")
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

print("list comprehension 2")
matrix2 = [(i,j) for i in range(5) for j in ['a','b']]
print(matrix2)

