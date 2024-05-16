#
# nested comprehension
#
# Nested list comprehension

print("list comprehension")
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

matrix2 = [(i,j) for i in range(5) for j in ['a','b']]
print(matrix2)

