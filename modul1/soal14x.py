def formatRupiah(angka):
    hasil = "Rp. {:,.0f}".format(angka).replace(',','.')
    return hasil

print(formatRupiah(1576000))