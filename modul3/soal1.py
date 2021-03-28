## mengecek ukuran matriks contoh 2 x 2 ; 2 x 3 dll

## inputnya matriks 
## [[1,2],
## [2,3]]

## mengukur matriks

def ukuranMetriks(data):
    for x in data:
        ## cek apakah berupa list
        if type(x) is list:
            ## cek apakah matriks konsisten kolomnya
            if len(x) != len(data[0]):
                return "Matriks tidak konsisten"
                break
            ## cek apakah matrik hanya 2d atau lebih
            for i in x:
                if type(i) is list:
                    return "Matriks tidak konsisten" 
                    break
        else:
            return "Matriks tidak konsisten" 
            break   
    # mengembalikan baris x kolom matriks berupas list [baris,kolom]
    return [len(data),len(data[0])]

#matrik A contoh benar
A = [[1,2],[2,3],[3,3]]
print(ukuranMetriks(A))

#matrik A contoh salah kolom tidak konsisten
A = [[1,2],[2,3],[3,3,4]]
print(ukuranMetriks(A))

#matrik A contoh salah isi list di dalam list
A = [[1,2],[2,3],[3,[3,4]]]
print(ukuranMetriks(A))

#matrik A contoh salah isi berupa integer bukan list
A = [1,2,[2,3],[3,[3,4]]]
print(ukuranMetriks(A))

print()
print()
## untuk menjumlahkan 2 matrix
def jumlahkan(a,b):
    #cek apakah ke 2 matriks sama ukuranya
    if ukuranMetriks(a) == ukuranMetriks(b) and ukuranMetriks(a) != "Matriks tidak konsisten" and ukuranMetriks(a) != "Matriks tidak konsisten":
        #menghitung matriksnya
        hasil=[]
        for x in range(len(a)):
            #print(x)
            newbaris=[]
            for j in range(len(a[x])):
                # cek sequence
                print(a[x][j],b[x][j])
                print(a[x][j]+b[x][j])
                newbaris.append(a[x][j]+b[x][j])
            print("####")
            print(newbaris)
            hasil.append(newbaris)
        
        # prin lebih rapi seperti matriks
        strhasil="Hasil penjumlahan matriks :\n"
        for p in hasil:
            strhasil+=str(p)+'\n'
        strhasil+="\n hasil dalam list : "+str(hasil)
        return strhasil


     

    elif ukuranMetriks(a) == "Matriks tidak konsisten" or ukuranMetriks(a) == "Matriks tidak konsisten":
        return "cek lagi tipe data atau penulisan matriks kamu"
    else:
        return "cek lagi tipe data atau penulisan matriks kamu"
    

##test penjumlahan
b = [
    [5,0],
    [2,6]
    ]

c = [
    [1,0],
    [4,2]
    ]
print(jumlahkan(b,c))

## pekalian matrix
## untuk menjumlahkan 2 matrix
def kalikan(a,b):
    #cek apakah ke 2 matriks sama ukuranya
    if ukuranMetriks(a) == ukuranMetriks(b) and ukuranMetriks(a) != "Matriks tidak konsisten" and ukuranMetriks(a) != "Matriks tidak konsisten":
        #menghitung matriksnya
        hasil = []
        for x in range(0, len(a)):
            newbaris = []
            for y in range(0, len(a[0])):
                total = 0
                for z in range(0, len(a)):
                    total = total + (a[x][z] * b[z][y])
                newbaris.append(total)
            hasil.append(newbaris)
        
        # prin lebih rapi seperti matriks
        strhasil="Hasil perkalian matriks :\n"
        for p in hasil:
            strhasil+=str(p)+'\n'
        strhasil+="\n hasil dalam list : "+str(hasil)
        return strhasil


     

    elif ukuranMetriks(a) == "Matriks tidak konsisten" or ukuranMetriks(a) == "Matriks tidak konsisten":
        return "cek lagi tipe data atau penulisan matriks kamu"
    else:
        return "cek lagi tipe data atau penulisan matriks kamu"

print(kalikan(b,c))


#mencari determinan
def determinant(matrix, mul):

    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        answer = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            answer = answer + mul * determinant(m, sign * matrix[0][i])
    return answer
A = [[-2,2,-3],[-1,1,3],[2,0,-1]]
Det = determinant(A,1)
print(Det)