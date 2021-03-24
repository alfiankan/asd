class Pesan(object):
    """
    Sebuah class bernama Pesan

    """
    def __init__(self, sebuahstring):
        self.teks = sebuahstring

    def cetakini(self):
        print(self.teks)

    def cetakhurufkapital(self):
        print(str.upper(self.teks))

    def cetakpakaihurufkecil(self):
        print(str.lower(self.teks))

    def jumlahkar(self):
        return len(self.teks)

    def cetakjumlahkarakterku(self):
        print("Kalimatku mempunyai ",len(self.teks))

    def perbarui(self,stringbaru):
        self.teks = stringbaru
    ##tambahan untuk soal
    def apakahTerkandung(self,txt):
        if txt.upper() in self.teks.upper():
            return True
        else:
            return False

    def hitungKonsonan(self):
        konsonan = "bcdfghjklmnpqrstvwxyz"
        total = 0
        for x in self.teks:
            if x.lower() in konsonan:
                total+=1
        return total

    def hitungVokal(self):
        vokal = "aiueo"
        total = 0
        for x in self.teks:
            if x.lower() in vokal:
                total+=1
        return total
