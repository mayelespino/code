#!/usr/bin/python

original_string = "Hello, my name is inigo montoya"
print(original_string)
#
# By concatenation
#
reversed_string = ""
for letter in original_string:
    reversed_string = letter + reversed_string

print(reversed_string)

#
# Reversed transversal
#
reversed_string = original_string[::-1]
print(reversed_string)


#
#
#
reversed_string = reversed(original_string)
print("".join(reversed_string))

#
# Queue operations
#
reversed_string = ""
copy_string =  list(original_string)
while len(copy_string):
    reversed_string += copy_string.pop(-1)
print(reversed_string)

#
# Introspection
#

reversed_string = [original_string[index] for index in range((len(original_string)-1), -1, -1)]
print("".join(reversed_string))