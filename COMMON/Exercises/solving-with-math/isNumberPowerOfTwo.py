#
# This is used to determine if a number is a power of two.
# This is where I got the code from: 
# https://www.quora.com/How-do-you-check-if-a-number-is-a-power-of-2-in-Python
import math

def is_power_of_2(n):
	# check if n is power of 2
	if n == 0: return (True)
	return (math.log(n)/math.log(2)).is_integer()

for n in range(0,10):
	print(n, is_power_of_2(n))
print("-"*10)
for n in [1,3,7,15,31,63]:
	print(n, is_power_of_2(n))

