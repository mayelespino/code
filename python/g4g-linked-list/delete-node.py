# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:

    def __init__(self):
        self.head = None

    def deleteNode(self, data):
        temp = self.head

        # if the element to be deleted is at the top
        if (temp.data == data):

            if temp.next is not None:
                temp.data = temp.next.data
                temp.next = temp.next.next
            else:
                print("\nThere is only one node. \
                The list can't be made empty")
            return

        # if not at top then we will search it one by one.
        while (temp.next is not None and temp.next.data != data):
            temp = temp.next

        # if the temp->next is null
        # then element is not present
        if temp.next is None:
            print('\n Given node is not present in Linked List')

        # else element is present and we delete it
        else:
            temp.next = temp.next.next

    # To push a new element in the Linked List
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # To print all the elements of the Linked List
    def PrintList(self):

        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


# Driver Code
llist = LinkedList()
llist.push(3)
llist.push(2)
llist.push(6)
llist.push(5)
llist.push(11)
llist.push(10)
llist.push(15)
llist.push(12)

print("Given Linked List: ", end=' ')
llist.PrintList()
print("\n\nDeleting node 10:")
llist.deleteNode(10)
print("Modified Linked List: ", end=' ')
llist.PrintList()
print("\n\nDeleting first node")
llist.deleteNode(12)
print("Modified Linked List: ", end=' ')
llist.PrintList()

# This code is contributed by Akarsh Somani

