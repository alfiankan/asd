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

al = AlatTulis("Buku Gambar","Gelatik",30,4500,"20C")
print(al)