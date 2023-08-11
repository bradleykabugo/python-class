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
