## Nama : Alfian Nur Fathoni
## NIM. : L2001900002
## class untuk membuat sngle node
class Node(object):
    """
    membuat node
    """
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#buat linkedin list dengan head 'linke'
a = Node(35)
b = Node(40)
c = Node(33)
d = Node(13)
e = Node(43)

linke = a
linke.next = b
b.next = c
c.next = d
d.next = e

print(linke.next.data)

## cetak linkedlist
def cetak(head):
    headnya = head
    while headnya is not None:
        print(headnya.data)
        headnya = headnya.next
        

## cari(head,yangdicari)
def cari(head,yangdicari):
    headnya = head
    node = 1
    while headnya is not None:
        if headnya.data == yangdicari:
            return str(headnya.data) + " Pada Node Ke : "+str(node)
            break
        else:
            headnya = headnya.next
            node+=1
        
    
print()
print(cari(linke,13))

## tambahDepan(head)
def tambahDepan(head):
    """Menambah node pada awal/depan list dengan membuat node baru lalu menyimpan linked list sebelumnya yang berada di head ke temp variabel
        setelah itu linked list yang bead di temp variabel dimasukan kedalam head baru yang berasal dari node baru"""
    nodelama = head
    nodebaru = Node(0)
    nodebaru.next = nodelama
    return nodebaru

linkeDepan = tambahDepan(linke)
cetak(linkeDepan)
## tambahAkhir(head)
def tambahAkhir(head,isi=0):
    """Menambah node di akhir list dengan membuat node baru ke next pointer dari node paling terakhir list sekarang"""
    #iterasi jika none maka tambahkan satu data baru tersewbut lalu break
    headnya = head
    while headnya is not None:
        print(headnya.data)
        if headnya.next is None:
            if isi == 0:
                headnya.next = Node(0)
            else:
                headnya.next = Node(isi)
            return headnya
            break
        headnya = headnya.next

print()
cetak(tambahAkhir(linkeDepan))
## tambah(head,posisi) menyisipkan node setelah posisi node yang disebutkan
def tambah(head,posisi):
    headnya = head
    jml = 1
    while headnya is not None:
        print(headnya.data)
        if posisi-1 == jml:
            headnya = headnya.next.next
            jml+=1
        else:
            headnya = headnya.next
            jml+=1

print("SISIPKAN")
cetak(linke)
print()
cetak(tambah(linke,3))

## hapus(posisi)
print("MENGHAPUS")
def hapus(head, posisi):
        prev = None
        curr = head
        while curr:
            if curr.getData() == posisi:
                if prev:
                    prev.setNextNode(curr.getNextNode())
                else:
                    self.head = curr.getNextNode()
                return True
                    
            prev = curr
            curr = curr.getNextNode()
            
        return False
cetak(linke)

print("HAPUS LIST")
print()
hapus(linke,3)