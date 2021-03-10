#buat bilangan 1 sampai 100
#gunakan shuffle dari random
import random
bilangan = random.randint(0,100)
print("PERMAINAN TEBAK ANGKA")
print('Saya menyimpan sebuah angka bulat antara 1 sampai 100 coba tebak hayolo uwiui')
percobaan=1
while True:
    if percobaan < 8:
        tebak = int(input('Masukan tebakan ke-{} : '.format(percobaan)))
        percobaan+=1
        if tebak < bilangan:
            print('Itu terlalu kecil, coba lagi')
        elif tebak > bilangan:
            print('Itu terlalu besar, coba lagi')
        else:
            print('Ya, anda benar')
            break
    else:
        print('Kesempatanmu habis coba lagi yaaa!!!')
        break