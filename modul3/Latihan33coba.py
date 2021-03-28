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

## class untuk list
class LinkedListku(object):
    def __init__(self):
        self.headval = None

    
    def cetakList(self):
        """Mencetak list"""
        data = self.headval
        while data is not None:
            print(data.data,end=' ')
            data = data.next
        print()

    def tambahAwal(self,baru):
        """Menambah node pada awal/depan list dengan membuat node baru lalu menyimpan linked list sebelumnya yang berada di head ke temp variabel
        setelah itu linked list yang bead di temp variabel dimasukan kedalam head baru yang berasal dari node baru"""
        nodelama = self.headval
        nodebaru = Node(baru)
        nodebaru.next = nodelama
        self.headval = nodebaru

    def tambahAkhir(self,baru):
        """Menambah node di akhir list dengan membuat node baru ke next pointer dari node paling terakhir list sekarang"""
        #iterasi jika none maka tambahkan satu data baru tersewbut lalu break
        data = self.headval
        ##hitung jumlah node
        jml=1
        while data is not None:
            jml+=1
            data = data.next
        print("jumlah : ",jml)

        cekdata = self.headval
        for x in range(jml):
            
            if cekdata.next == None:
                
                cekdata.next = Node(baru)
            else:
                cekdata = cekdata.next
       
# membuat inisiasi class list kosong -> listku

listku = LinkedListku()
print("####List awal kosong###")
print(listku.headval)
print("##################")
a = Node(35)
b = Node(40)
c = Node(33)
d = Node(13)
e = Node(43)
#memsaukuan node pertama ke head
listku.headval = a
#memsaukuan node ke next dan seterusnya

listku.headval.next = b
b.next = c
c.next = d
d.next = e

# mencetak isi linked list yang sudah dibuat
listku.cetakList()

# menambahkan node ke depan list dan ngecek lagi

listku.tambahAwal(77)
listku.tambahAwal(90)

listku.cetakList()

## menambah node ke akhir list
print()
print("Menambah node ke akhir list")

listku.tambahAkhir(12)
listku.cetakList()

listku.tambahAkhir(32)
listku.cetakList()
listku.tambahAkhir(39)
listku.cetakList()

## menyisipkan node