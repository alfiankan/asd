# hitung rata rata

def rerata(b):
    """ menggunakan sum untuk mempersingkat """
    return sum(b)/len(b)

# def rerata(b):
#     jumlahNilai = 0
#     for x in b:
#         jumlahNilai+=x
#     return jumlahNilai/len(b)

def stdev(b):
    """ setiap nilai dikurangi rata rata dipangkat 2 """
    ratarata = rerata(b)
    hasil=0
    for x in b:
        hasil+=(x-ratarata) ** 2
    return hasil

def variance(b):
    """ Jumlah deviasi dibagi jumlah data """
    deviasi = stdev(b)
    return deviasi/len(b)

print("Rata-rata : ",rerata([1,2,3,4,5]))
g = [2,4,5,4,3,4,5,2,2,10,11,23]
print("Rata-rata : ",rerata(g))

print("Deviasi : ",stdev(g))
print("Varian : ",variance(g))

