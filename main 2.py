#Create a variable outside a function and use it inside the function
x = "awersome"
def myfunc():
    print("Python is " + x)
myfunc()
#Create a variable inside a function with the same name as a global variable
t = "awersome"
def myfunc():
    t = "fantastic"
    print("Python is " + t)
myfunc()
print("Python is " + t)

#Python data types
x = 5
print(type(x))
Y = 5.2
print(type(Y))
Z = 5J
print(type(Z))
A = "Mexico"
print(type(A))

#random Number function
import random
print(random.randrange(1,100))

#Strings

name = "riyadh"
print("blonde hair")
print(name)
city = "istanbul"
print(city)
school = "al danhiwah school"
print(school)
#Get the character at position 1
a = "negara world"
print(a)
print(a[1])
print(a[4])
#String length
print(len(a))
#Check string
txt = "the best things in life are sony!"
print("sony" in txt)
print("carlsen" in txt)
#Use it in an if statement
txt = "the best things in life are expensive"
if "expensive" in txt:
    print("yes 'expensive' is present.")
#Check if not
txt = "the best things in life are cheap"
print("sony" not in txt)
#Get the character from position 2 to position 5
z = "ahlan riyadh!"
print(z[2:9])
#Slice from the start
z = "ahlan jeddah!"
print(z[:7])
#Slice to the end
z = "ahlan islamabad!"
print(z[3:])
#use upper method to print string in upper case
a = "marcus is president"
print(a.upper())
#use lower method to return string in lower case
a = "JONATHAN IS PRIME MINISTER"
print(a.lower())
#remove whitespace
z = "   marcus is rich and jonathan is poor "
print(z)
print(z.strip())
#Replace string
z = "el cofre esta cerrado"
print(z.replace("t", "m"))
#Merge variable y with variable x into variable b
y = "rwanda"
x = "sexy"
b = y + x
print(b)
#To add space between them add "quotations"
b = y + " " + x
print(b)
#concatenate strings with integers
age = 36
txt = "my name is camila, and i am {}"
print(txt.format(age))
quantity = 999
itemno = 786
price = 2
myorder = "i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "i want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))
#boolean
print(14 < 7)
print(128 > 32)
print(44 == 88)

#print a message based on whether the condition is false or true
y = 200
z = 33
if z > y:
    print("z is more than y")
else:
    print("y is more than z")
#evaluate a string and a number
print(bool("sony"))
print(bool(17))
print(bool(0))
print(bool())

#python operators
y = 99
z = 33
#addition
q = y + z
print(q)
#subtraction
q = y - z
print(q)
#multiplication
q = y * z
print(q)
#modulus
q = y % z
print(q)
#create a list
thislist = ["landwind", "carrefour", "walmart"]
print(thislist)

#Print the second item on the list
thislist = ["volvo", "peugeot", "fiat", "citroen", "bmw", "audi", "landwind", "renault"]
print(thislist[1])
#negative indexing
print(thislist[-1])
#range of indexes
print(thislist[2:5])
#range of negative indexes
print(thislist[-6:-1])
#check if item exists
if "landwind" in thislist:
    print("yes, 'landwind' is in the cars list")
#change item value
thislist[3] = "jeep"
print(thislist)
#change a range of item values
thislist[1:3] = ["JVC", "sony"]
print(thislist)
#insert items
thislist.insert(2, "sazgar")
print(thislist)
#append list
thislist.append("subaru")
print(thislist)
#extend list
thislist2 = ["zendaya", "hulu"]
thislist.extend(thislist2)
print(thislist)
#remove list item
thislist.remove("volvo")
print(thislist)
#remove specified index
thislist.pop(9)
print(thislist)
#tuples
thistuple = ("netflix", "peacock", "hulu", "HBO")
print(thistuple)
#tuple length
print(len(thistuple))
#access tuple items
print(thistuple[1])
#negative indexing
print(thistuple[-1])
#index rangee
print(thistuple[2:4])
#negative rangee
print(thistuple[-4:-1])
#update tuple
ql = ("megastar", "europafm", "los40", "melodia")
ch = list(ql)
ch[3] = "cidc"
ql = tuple(ch)
print(ql)
#python sets
thisset = {"nike", "adadias", "vans"}
print(thisset)