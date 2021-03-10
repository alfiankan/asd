## w = panjang
## h = tinggi
## max num row print semua
## first num row print semua
# Buatlah sebuah fungsi yang menerima dua integer positif, yang akan menggambar bentuk
# persegi empat. Contoh pemanggilan:
# >>> gambarlahPersegiEmpat(4,5) #tombol <enter> dipencet
# @@@@@
# @ @
# @ @
# @@@@@
def gambarlahPerseiEmpat(h,w):
    for x in range(h):
        if(x==0 or x==(h-1)):
            print('@'*w)
        else:
            for y in range(w):
                if(y==0 or y==(w-1)):
                    print('@',end='')
                else:
                    print(' ',end='')
            print()
gambarlahPerseiEmpat(20,20)