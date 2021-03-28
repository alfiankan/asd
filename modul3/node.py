class Node(object):
    def __init__(self,data,next=None):
        self.dataval = data
        self.next = next
    
    def tambahDepan(self,data):
        newnode = Node(data)
        newnode.next = self.dataval

        self.dataval = newnode.dataval


a = Node(60)
print(a.dataval)
a.next = Node(98)
print(a.next.dataval)


a.tambahDepan(76)
print()
print()
print(a.dataval)