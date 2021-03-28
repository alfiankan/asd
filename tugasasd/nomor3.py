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
