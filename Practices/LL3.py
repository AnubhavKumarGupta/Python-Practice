class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__ (self):
        return str(self.data)


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)


# Now, you can print the linked list using the printlist function
def printlist(head):
    temp = head
    if temp is None:
        print("Linked List is Empty")
        return

    while temp is not None:
        print(temp, end="-->")
        temp = temp.next
    print("None")

printlist(head)
