class Segitiga():
   def __init__(self, al, tg):
      self.alas = al
      self.tinggi = tg
 
   def __str__(self):
      return "Segitiga dengan alas {} dan tinggi {}".format(self.alas, self.tinggi)

class Segitigaku(Segitiga):
   def luas(self):
      return 0.5 * self.alas * self.tinggi
 
segitiga_abc = Segitigaku(10, 6)
print(segitiga_abc)
print("memiliki luas")
print(segitiga_abc.luas())