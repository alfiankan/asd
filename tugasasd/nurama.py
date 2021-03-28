#Nomor 1
class Perang(object):
    def __init__(self,n):
        self.nama = n[0]
        self.tahun = n[1]
        self.tempat = n[2]
        self.pihak1 = n[3]
        self.pihak2 = n[4]
        self.korban = n[5]
        
    def __str__(self):
        s = str(self.nama) + " - "+ str(self.tempat)
        return s
t = ("Badar",624, "Arabia","Muslim","Quraisy",84)
p = Perang(t)
print(p)