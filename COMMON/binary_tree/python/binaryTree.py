
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if data < self.data:
            if self.left is None:
                self.left = node(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = node(data)
            else:
                self.right.add(data)

    def printPreOrder(self):
        print(self.data)
        if self.right is not None:
            self.right.printPreOrder()
        if self.left is not None:
            self.left.printPreOrder()
    def printLevelOrder(self):
        if self.right is not None:
            self.right.printLevelOrder()
        print(self.data)
        if self.left is not None:
            self.left.printLevelOrder()
    def printPostOrder(self):
        if self.right is not None:
            self.right.printPostOrder()
        if self.left is not None:
            self.left.printPostOrder()
        print(self.data)


root = node(50)
root.add(10)
root.add(60)
root.add(1)
root.add(61)
root.add(99)
print("printPreOrder")
root.printPreOrder()
print("printLevelOrder")
root.printLevelOrder()
print("printPostOrder")
root.printPostOrder()