def katakan(n):
    ucapan = ['','satu','dua','tiga','empat','lima','enam','tujuh','delapan','sembilan','sepuluh','sebelas']
    if n <= 1000000000:
        hasil=''
        if n >= 0 and n <= 11:
            hasil = ucapan[n]
        elif n <20:
            hasil = ucapan[n-10] + ' belas'
        #puluhhan (30,40m50 dst)
        elif n < 100:
            hasil = katakan(int(n/10)) + " puluh " + ucapan[n%10]
        elif n < 200:
            hasil = 'seratus ' + katakan(int(n-100))
        elif n < 1000:
            hasil = katakan(int(n/100)) + ' ratus '+ katakan(int(n%100))
        elif n < 2000:
            hasil = 'Seribu '+katakan(n-1000)
        elif n < 1000000:
            hasil = katakan(int(n/1000)) + ' ribu ' + katakan(int(n%1000))
        elif n < 1000000000:
            hasil = katakan(int(n/1000000)) + ' juta '+ katakan(int(n%1000000))
        elif n == 1000000000:
            hasil = "satu milyar"
        
        return str(hasil)

    else:
        return "Jumlah tidak boleh lebih dari 1 milyar"

print(katakan(1000000000))
print(katakan(999999999))
print(katakan(1000000001))

