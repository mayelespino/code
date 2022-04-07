
class BinaryTree:
    value = 0
    left = None
    right = None
    def __init__(self, rootNodeValue):
        self.value = rootNodeValue
    def addNode(self,value):
        if value > self.value and self.right is None:
            self.right = BinaryTree(value)
        elif value > self.value and self.value is not None:
            self.right.addNode(value)
        elif value < self.value and self.left is None:
            self.left = BinaryTree(value)
        else:
            self.left.addNode(value)
    def __str__(self, level = 0):
        if self.right is not None:
            self.right.__str__(level + 1)

        print(f'{" "* level*6} {self.value}\n\n')

        if self.left is not None:
            self.left.__str__(level + 1)
        return('')

    def preOrder(self):
        print(f'{self.value}, ', end='')

        if self.right is not None:
            self.right.preOrder()

        if self.left is not None:
            self.left.preOrder()

    def inOrder(self):
        if self.right is not None:
            self.right.inOrder()

        print(f'{self.value}, ', end='')

        if self.left is not None:
            self.left.inOrder()

    def postOrder(self):
        if self.right is not None:
            self.right.postOrder()

        if self.left is not None:
            self.left.postOrder()

        print(f'{self.value}, ', end='')

    def breadthFirst(self):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            currentNode = stack.pop(0)
            print(f'{currentNode.value}, ', end='')

            if currentNode.left != None:
                stack.append(currentNode.left)
            if currentNode.right != None:
                stack.append(currentNode.right)


if __name__ == "__main__":
    bt = BinaryTree(50)
    bt.addNode(25)
    bt.addNode(75)
    bt.addNode(30)
    bt.addNode(0)
    bt.addNode(100)
    bt.addNode(74)
    print("\n", "-" * 40)
    print("__str__")
    print(bt)
    print("\n", "-" * 40)
    print("preOrder")
    bt.preOrder()
    print("\n", "-" * 40)
    print("inOrder")
    bt.inOrder()
    print("\n", "-" * 40)
    print("postOrder")
    bt.postOrder()
    print("\n", "-" * 40)
    print("breadthFirst")
    bt.breadthFirst()

# Links I consulted:
# https://www.codespeedy.com/how-to-implement-binary-tree-in-python/
# https://www.pythontutorial.net/python-oop/python-__repr__/

