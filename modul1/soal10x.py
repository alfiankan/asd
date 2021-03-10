from math import sqrt as akar

def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D >= 0:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1,x2)
    else:
        hasil = ["Determinannyanegatif. Persamaantidakmempunyaiakarreal","Determinannyanegatif. Persamaantidakmempunyaiakarreal"]
    return hasil

k = selesaikanABC(1,-5,6)
h = selesaikanABC(1,2,3)

print(k[0])
print(k[1])

print(h[0])
print(h[1])