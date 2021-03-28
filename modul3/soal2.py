def buatNol(m,n=0):
    if n==0:
        # buat matrix bujur sangkat
        return [ [0 for j in range(m)] for i in range(m) ]
    else:
        return [ [0 for j in range(m)] for i in range(n) ]

def buatIdentitas(m):
    return [[1 if j==i else 0 for j in range(3)] for i in range(3)]

print(buatNol(4))
print(buatNol(4,2))
print(buatIdentitas(4))