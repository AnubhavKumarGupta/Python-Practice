class node:
    def __init__(self, data):
        self.data = data
        self.next = None


n1 = node(10)
n2 = node(20)
n3 = node(30)

n1.next = n2
n2.next = n3
n3.next = None

print(n1.data)
print(n1.next.data)
print(n2.next.data)
print(n3.next)
