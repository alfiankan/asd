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