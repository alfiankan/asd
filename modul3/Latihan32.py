B = [[0 for x in range(3)] for y in range(3)]
print(B)

# membuat kuadrat

K = [x**x for x in range(5)]
print(K)

# list tuple pasangan
T = [(i,i**2) for i in range(6)]
print(T)

# kuadrat genap

KG = [x**2 for x in range(15) if x%2==0]
print(KG)

# membuat list 5 elemen

LL = [3 for x in range(5)]
print(LL)

# membuat list 3 elemen berisi list 3 data 0

L3 = [[0 for i in range(3)] for y in range(3)]
print(L3)

# membuat matrix identitas 3 x 3
# expected = [
# [1,0,0],
# [0,1,0],
# [0,0,1]
# ]
matrix = [[1 if i==y else 0 for i in range(3)] for y in range(3)]
print(matrix)

# list berisi huruf vokal suatu string
# expected = [’o’,’a’,’a’,’a’,’a’,’u’,’a’,’a’,’a’]
# input d="YogyakartadanSurakarta."
d="YogyakartadanSurakarta."
vokal = [x for x in d if x in 'AIUEOaiueo']
print(vokal)

# Membuatlistbilanganprimaadari20sampai50
# expected = [23,29,31,37,41,43,47]
from math import sqrt as sq

def apakahPrima(n):
    n = int(n) #convert ke integer untuk menghilangkan pecahan
    assert n>0 # mengambil hanya bilangan positif
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    sta = 1
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            print(i)
            if n % i == 0:
                return False
        return True

primania = [x for x in range(20,50) if apakahPrima(x)]
print(primania)

