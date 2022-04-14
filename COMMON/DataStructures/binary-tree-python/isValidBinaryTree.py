#
# This determines if a given array describes a valid binary tree. It does this by
# starting with the length of a given array and calculate the previous number in
# the series until it arrives at 3.

def isValidBinaryTree(numberOfNodes):
	if numberOfNodes in [0,2] : return False
	if numberOfNodes in [1,3] : return True
	while numberOfNodes > 3:
		if numberOfNodes % 2 == 0: break
		numberOfNodes = int((numberOfNodes - 1 )/2)

	if numberOfNodes == 3:
		return True
	else:
		return False


if __name__ == "__main__":
	for n in [1, 3, 7, 15, 31, 63,127]:
		print(n, isValidBinaryTree(n))
	print("\n","-"*10)
	for n in [2,4,6,8,10,20,128,2002]:
		print(n, isValidBinaryTree(n))