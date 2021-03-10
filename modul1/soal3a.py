# Buatlah sebuah fungsi yang menerima sebuah string dan mengembalikan sebuah list
# yang terdiri dari dua integer. Dua integer kembalian ini adalah: jumlah huruf di
# string itu dan jumlah huruf vokal (huruf vokal adalah huruf hidup) di string itu.
# Contoh pemanggilan:
# >>> k = jumlahHurufVokal(’Surakarta’)
# >>> k
# (9, 4) # Sembilan huruf, dan empat di antaranya huruf vokal
#expected  => (jumlahhuruf,jumlahvokal)

def jumlahHurufVokal(kata):
    abjadTotal=0
    vokalTotal=0
    abjad_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vokal_ = 'AIUEO'
    for a in kata:
        if a.upper() in abjad_:
            abjadTotal+=1
        if a.upper() in vokal_:
            vokalTotal+=1
    return (abjadTotal,vokalTotal)

print(jumlahHurufVokal('Surakarta'))
