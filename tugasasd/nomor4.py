class AlatTulis(object):
    """Class alatTulis"""
    def __init__(self,nama,merk,jumlah,harga,nomorRak):
        """.."""
        self.nama = nama
        self.merk = merk
        self.jumlah = jumlah
        self.harga = harga
        self.nomorRak = nomorRak
    def __str__(self):
        s = self.nama + '(' + self.merk + ')'
        return s
        
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

    def simpan(self,data):
        # split data kelist setiap ganti baris
        itemdata = data.split('\n')

        listobject = []
        #buang baris pertama sebelum iterasi
        for x in itemdata[1::]:
            # split setiap colomn ke list dari tanda ;
            kolom = x.split(';')
            listobject.append(kolom)

        ## extend panjang arraynya
        tambahan = len(listobject) - len(self._internal)
        self.__setitem__(tambahan,None)
        for x in range(len(self._internal)):
            #buat object alat tulis lalu memasukan kedalam list
            new = AlatTulis(listobject[x][0],listobject[x][1],listobject[x][2],listobject[x][3],listobject[x][4])
            self.__setitem__(x,new)

# data inputan
DataAlatTulis = """Nama;merek;jumlah,hargabeli,nomorrak
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

## asumsi memparsing data string lalu membuatkan setiap baris menjadi object AlatTulis lalu memasukan setiap objek kedalam array

## membuat array panjang 2 karena dinamis nnti bisa diperpanjang sesuai banyaknya data
arrayATK = Arreha(2)

## memanggil method simpan untuk detail bisa dilihat di dalam class Arreha
arrayATK.simpan(DataAlatTulis)

print()
#cetak isi array
print(arrayATK._internal)
#cek panjang array
print(len(arrayATK._internal))

#cek isi array
#coba iterasi semua isi array menjadi rapih total 15
#Nama;merek;jumlah,hargabeli,nomorrak
def buatDaftarHarga():
    for x in range(len(arrayATK._internal)):
        print("##### "+str(x+1)+" ######")
        print("Nama       : ",arrayATK[x].nama)
        print("Merek      : ",arrayATK[x].merk)
        print("Jumlah     : ",arrayATK[x].jumlah)
        print("Harga Beli : ",arrayATK[x].harga)
        print("Nomor Rak  : ",arrayATK[x].nomorRak)
        print("############")
        print()
buatDaftarHarga()
# mencoba merubah harga item ke 15 (terakir)
##### 15 ######
# Nama       :  Penggaris Busur
# Merek      :  Butterfly
# Jumlah     :  15
# Harga Beli :  1000
# Nomor Rak  :  16B
############
# MENJADI
# Nama       :  Penggaris Busur
# Merek      :  Samsung
# Jumlah     :  15
# Harga Beli :  75000
# Nomor Rak  :  16B
############
# data ke 15 index ke 14 (0<)
arrayATK[14].merk = "Samsung"
arrayATK[14].harga = 75000
## cek kembali apakah berubah
buatDaftarHarga()