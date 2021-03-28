#No1
class AlatTulis(object):
    """Class alatTulis"""
    def _init_(self,nama,merk,jumlah,harga,nomorRak):
        """.."""
        self.nama = nama
        self.merk = merk
        self.jumlah = jumlah
        self.harga = harga
        self.nomorRak = nomorRak
    def _str_(self):
        s = self.nama + '(' + self.merk + ')'
        return s

#No2
AlatTulis = """Nama;merek;jumlah,hargabeli,nomorrak
Pensil;Staedler;10;2500;10A
Serutan pensil;Joyko;15;2500;12B
Penggaris;Butterfly;20;2000;20A
Buku Tulis;Kyky;30;2500;30C
Karet Penghapus;Joyko;25;2000;5C
Bolpoint;Faster;30;3000;15B
Buku Gambar;Gelatik;30;4500;20C
Spidol;Snowman;25;7000;10B
Tipex;Kenko;20;3500;12C
Stabilo;Boss;15;8000;15A
Map;Diamond;20;3000;10C
Pensil warna;Faber Castel;10;30000;15C
Crayon;Titi;10;35000;17C
Kertas HVS A4 70gram;Sidu;30;37500;1A
Penggaris Busur;Butterfly;15;1000;16B
"""

#No3
## membuat class untuk array custom kita
class Arreha(object):
    ##constructor inisiasi
    def __init__(self,n):
        self._internal = n * [None]

    ## method set untuk indexing
    def __setitem__(self, key, value):
        if key >= len(self._internal):
            kurang = key - len(self._internal) + 1
            li = kurang * [None]
            self._internal.extend(li)
        self._internal[key] = value

    ## method get untuk indexing
    def __getitem__(self, key):
        if 0 <= key < len(self._internal):
            return self._internal[key]
        else:
            raise KeyError("Indeks diluar panjang array")

a = Arreha(8)


# cek semua isi array
print(a._internal)

# mengetest apakah array dinamis dengan menambahkan item
a[9] = 90
print(a[9])

# cek semua isi array
print(a._internal)


#No4 -> ada didalam class Arreha
# input : 
## asumsi membuat object Alat tulis danmemasukan kedalam array
## namun data input berupa string semua jadi begini

print()
print()
print()
# parsing string ke object

#split setiap baris baru \n
itemdata = AlatTulis.split('\n')

listobject = []

for x in itemdata:
    print(x)
    # split setiap colomn ke list dari tanda ;
    kolom = x.split(';')
    listobject.append(kolom)

print()
print(listobject)

# cek panjang data dari list object alat tulis yang sudah dibuat
panjangdata = len(listobject)
print()
print(panjangdata)
print()
# membuat array  sesuai panjang data yang dicek tadi
arrayATK = Arreha(panjangdata)
print(arrayATK._internal)

# memasukan kedalam array (iterasi)