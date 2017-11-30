import sys

def fibonacci(n):
	if n < 2:
			return n
	else:
		return(fibonacci(n-1)+fibonacci(n-2))

if len(sys.argv) < 2:
	print("Please provide a number.")
	exit()

target = int(sys.argv[1])
print(target)
print (fibonacci(target))
