thislist = ["apple", "banana", "cherry"] #list is changeable,ordered,allow duplicate
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #menghitung isi list
print(type(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]                   
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

#access items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#change item value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#add item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.extend(["orange", "mango", "grapes"])
print(thislist)

#remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#list comprehension
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if x != "banana"]
print(newlist)

#sort list
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#sort descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 #Using + operator
print(list3)

list1 = ["a", "b" , "c"] 
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)  #Using append() method
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)  # Using extend() method
print(list1)   

#untuk laporan

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #menghitung isi list

print(type(thislist))
print(thislist[-1]) #access list untuk mengakses list menggunakan indeks

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  #change list, untuk mengubah isi didalam list menjadi variabel baru

thislist.remove("banana") #remove list, untuk menghapus isi didalam list
print(thislist)

thislist.sort() #sort list, untuk mengurutkan isi didalam list
print(thislist)

list1 = ["a", "b", "c"]  #join list, untuk menggabungkan list yg berbeda
list2 = [1, 2, 3]

list3 = list1 + list2 #Using + operator
print(list3)

#list comprehension
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]
print(newlist)
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if x != "banana"]
print(newlist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #copy list, untuk menduplikat isi list kedalam list baru
print(mylist)



