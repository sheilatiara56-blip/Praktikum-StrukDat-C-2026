thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#access item
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)     #access set tidak dapat menggunakan indeks

#add set items
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.add("orange")
thisset.update(tropical)
print(thisset)
print(thisset)

#remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("banana")
print(thisset)
print(thisset)

#loop item
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) 
print(set3)

''''Metode union() dan update() menggabungkan semua item dari kedua himpunan
Metode intersection() hanya menyimpan item duplikat.
Metode difference() menyimpan item dari himpunan pertama yang 
tidak ada di himpunan lainnya.
Metode symmetric_difference() menyimpan semua item KECUALI item duplikat.'''

#frozenset tidak dapat diubah
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
