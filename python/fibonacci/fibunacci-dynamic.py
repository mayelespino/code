import sys

def fibonacci(n, memory):
	if n < 2:
		return n
	elif memory[n] != 0:
		return memory[n]

	one = fibonacci(n-1, memory)
	two = fibonacci(n-2, memory)
	memory[n] = one + two
	return(one + two)

target= int(sys.argv[1])
memory = [0] * (target + 1)
print(target)
print (fibonacci(target, memory))
#print(memory)
