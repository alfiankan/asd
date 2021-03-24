from LatOOP3 import Manusia

class SiswaSMA(Manusia):
    def __init__(self,nama,kelas,jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan

    def detail(self):
        return 'Nama : '+self.nama+' Kelas : '+str(self.kelas)+' Jurusan : '+self.jurusan
    def pindahKelas(self,akelas):
        self.kelas = akelas
