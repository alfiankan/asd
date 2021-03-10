#kelipatan ex : 3 6 9 12 15 18 21 24 27 29 32
def cetak(n):
    for x in range(1,n+1):
        
        if x%3 == 0:
            print('Python')
        elif x%5 == 0:
            print('UMS')
        elif x%3 == 0 and x%5 == 0:
            print('Python UMS')
        else:
            print(x)
cetak(100)