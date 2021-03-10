def ucapkanSalam():
    print('Assalamualaikum')

def sapa(nama):
    ucapkanSalam()
    print('Halo',nama)
    print('Selamay Belajar')

def kuadratkan(b):
    h=b*b
    return h

ucapkanSalam()
sapa('Alfian')
b = kuadratkan(9)
k = 9
print('Bilanganya',k,'kalau dipangkatkan dua jadinya',kuadratkan(k))