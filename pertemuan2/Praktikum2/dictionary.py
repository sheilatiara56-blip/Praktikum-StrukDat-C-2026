thisdict = {            #item2 dalam dict itu berurutan, dapat diubah, no duplicate
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#access item
print(thisdict["brand"])
x = thisdict.get("model")
x = thisdict.keys()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change
car["year"] = 2020
print(x) #after the change

#change item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #mengubah isi

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020}) 

#add item
thisdict["color"] = "red" #bisa kayak gini
print(thisdict)

thisdict.update({"color": "red"}) #atau pakai update

#remove items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
thisdict.popitem() #menghapus variabel terakhir.pake pop biar bisa lebih spesifik

del thisdict["year"]
print(thisdict)

#Loop Through a Dictionary
'''Anda dapat melakukan perulangan melalui dict dengan menggunakan perulangan for. 
Saat melakukan perulangan melalui dict, nilai yang dikembalikan
 adalah kunci-kunci dict tersebut,
tetapi ada juga metode untuk mengembalikan nilai-nilainya.'''

#copy item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"]) #untuk mengaksesnya
