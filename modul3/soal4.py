class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def tambahBelakang(self, data):
        """menambah node didepan"""
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def tambahDepan(self, data):
        """tambah ke depan head"""
        new_node = Node(data)
        new_node.next = self.tail
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def iterasi(self):
        """iterasi setiap node"""
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

    def iterasibalik(self):
        """iterasi setiap node"""
        
        current = self.balik()
        while current:
            item_val = current.data
            current = current.next
            yield item_val
            
    def cetakkedepan(self):
        """tampilkan data setiap Node kedepan"""
        for node in self.iterasibalik():
            print(node)

    def balik(self):
        """membalik tail (node paling belakang ) menjadi head (node paling depan)"""
        curr = self.head
        prev_node = None
        while curr:
            prev_node = curr.prev
            curr.prev = curr.next
            curr.next = prev_node
            curr = curr.prev
        return prev_node.prev
        
    def cetakkebelakang(self):
        """tampilkan data setiap Node kebelakang"""
        for node in self.iterasi():
            print(node)


items = doubly_linked_list()

# menambah node ke belakang
items.tambahBelakang(34)
items.tambahBelakang(12)
items.tambahBelakang(44)
items.tambahBelakang(87)
items.tambahBelakang(44)


print("Mencetak semua isi Node dari depan")
items.cetakkebelakang()


print("Mencetak semua isi Node dari belakang")

items.cetakkedepan()

# menambah node ke depan head
print("menambah node ke depan head")

items.tambahDepan(55)


items.cetakkebelakang()

