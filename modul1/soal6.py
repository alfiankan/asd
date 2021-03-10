##program menampilkan bilangan prima dari
## prima(mulai,akhir)
from math import sqrt as sq
def prima(m,a):
    #angak sample
    iniprima = []
    for x in range(m,a+1):
        #print('angka',x)
        #cek apakah prima jika ya print
        prima = True
        for i in range(2,int(sq(x))+1):
            #print(i,end=' - ')
            if x % i == 0:
                prima = False
        if prima:
            iniprima.append(x)
    return iniprima

def prima2(m,a):
    prima = []
    iniprima = []
    for i in range(m, a+1):
        if i not in prima:
            iniprima.append(i)
            for j in range(i*i, a+1, i):
                prima.append(j)
    return iniprima

print(prima(2,30))
print(prima2(2,30))