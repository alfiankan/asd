class Manusia(object):
    """
    CLASS manusia dengan inisisasi nama
    """
    keadaan = 'lapar'

    def __init__(self,nama):
        self.nama = nama

    def ucapkansalam(self):
        print("Salam namaku",self.nama)

    def makan(self,s):
        print("Saya baru saja makan")

    def olahraga(self,k):
        print("saya baru saja latihan ",k)
        self.keadaan = 'lapar'

    def mengalikandengandua(self,n):
        return n*2

p1 = Manusia('Fatimah')
p1.ucapkansalam()