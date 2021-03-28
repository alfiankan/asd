## Nama : Alfian Nur Fathoni
## NIM. : L2001900002
class Node(object):
    """
    membuat node
    """
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# coba membuat beberapa node
a = Node(5)
b = Node(8)
c = Node(2)

## linking
a.next  = b
b.next = c
print(a.data,b.next.data)
print(a.next.next.data)

# mengunjungi setiap atau mencetak node dari head yang ditentuka
def kunjungi(head):
    curNode = head
    while curNode is not None:
        print(curNode.data)
        curNode = curNode.next
print("######################")
kunjungi(c)

# menambah node sebelum head yang sekarang
def tambahDepan(head,data):
    print("Menambah node di awal")
    #node baru
    ndbr = Node(data)
    ndbr.next = head
    return ndbr
a = tambahDepan(a,54)
print(a.next.data)

## menyisipkan node

## cari

## hapus
