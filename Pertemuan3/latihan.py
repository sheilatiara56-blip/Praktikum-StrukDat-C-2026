class Minuman:
    def __init__(self,nama,rasa,rating):
      self.nama = nama
      self.rasa = rasa
      self.rating = rating

    def deskripsi_minuman(self):
      print(f"minuman favorit ku:{self.nama},asal dari{self.rasa},rating{self.rating}")

    def change_minuman(self,new_nama):
      self.nama = new_nama
      print ("favorit baru : {new.nama}")
minum1 = Minuman("SUSU","Manis",8)
minum2 = Minuman ("matcha","pahit",6)
minum3 = Minuman ("frappe","seger",9)
print(minum1.nama)
print(minum2.nama)
print(minum3.nama)

minum1.change_minuman("latte")





