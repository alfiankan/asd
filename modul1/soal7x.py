# Buatlah suatu program 
# yang menerima bilangan bulat positif 
# dan memberikan faktorisasiprima-nya. 
# Faktorisasi prima adalah pemfaktoran suatu 
# bilangan bulat ke dalam bilanganbilangan prima 
# yang menjadi konstituennya
# >>> faktorPrima(10)
# (2, 5)
# >>> faktorPrima(120)
# (2, 2, 2, 3, 5)
# >>> faktorPrima(19)
# (19,)
def faktorPrima(n):
    i = 2
    faktor = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            faktor.append(i)
    if n > 1:
        faktor.append(n)
    return faktor

    

print(faktorPrima(120))
print(faktorPrima(19))
