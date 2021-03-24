from LatOOP3 import Manusia
class Mahasiswa(Manusia):
    """
    Class mahasiswa extend class manusia
    """
    def __init__(self,nama,NIM,kota,us):
        """ovverida dari class manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__(self):
        s = self.nama+' NIM '+str(self.NIM)\
            + ' Tinggal di : '+self.kotaTinggal\
            + ' Uang saku Rp. '+self.uangSaku\
            + 'tiap bulanya'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """
        method ini ovveride dari cuper class
        """
        print('saya baru saja makan ',s,'sambil belajar')
        self.keadaan='kenyang'