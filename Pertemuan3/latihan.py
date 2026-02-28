class Minuman:
    def __init__(self,nama,rasa,rating):
      self.nama = nama
      self.rasa = rasa
      self.rating = rating

    def deskripsi_minuman(self):
      print(f"minuman favoritku: {self.nama} dengan rasa {self.rasa}, rating {self.rating}")

    def change_nama(self,new_nama):
      self.nama = new_nama
      print (f"favorit baru : {self.nama}")
minum1 = Minuman("Susu","Manis",8)
minum2 = Minuman ("Matcha","pahit",6)
minum3 = Minuman ("Frappe","seger",9)
print(minum1.nama)
print(minum2.nama)
print(minum3.nama)

minum1.deskripsi_minuman() #penambahan method

minum1.change_nama("latte")




