mytuple = ("apple", "banana", "cherry") #tuple is unchangeable,ordered,allow duplicate
print(mytuple)

thistuple = ("apple", "banana", "cherry","kiwi","orange")
print(thistuple[1])
print(thistuple[1:4])
print(thistuple[2 :]) #dst..

#check item

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#update tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y) #ubah ke list,ubah,balikin lagi ke tuple
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)  #atau pakai tambah
thistuple += y 
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  #buat remove
y.remove("apple")
thistuple = tuple(y)

'''thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) ''' #this will raise an error because the tuple no longer exists

#unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)  #unpack lah pokoknya :)
print(yellow) 
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#using asterisk
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#loop tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple): 
  print(thistuple[i])
  i = i + 1   

#join tuple 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 2
print(tuple3)
print(tuple4)

#tuple methods
#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found


