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