#Python indentations!
#how to use indentations
if 5 > 2:
    print("Five is greater than two!")

#Numbers
x = 3+5j
y = 5
z = -5.877
print(type(x))
print(type(y))
print(type(z))

#specify a type of variable
x = int(1)  # x will be 1
y = float(2.8)  # y will be 2.8
z = str("s1")  # z will be 's1'

#How to declare a variable
a = 100
print (a)

#Re-declare a Variable

# Declare a variable and initialize it
f = 0
print(f)
# re-declaring the variable works
f = 'dav'
print(f)

#Concatenate Variables
a='DT'
b = 99
print (a+str(b))

#Local and Global Variables
# 1. Variable "f" is global in scope and is assigned value 101 which is printed in output
# 2. Variable f is again declared in function and assumes local scope. It is assigned value "I am learning Python." which is printed out as an output. This variable is different from the global variable "f" define earlier
# 3. Once the function call is over, the local variable f is destroyed. When we again, print the value of "f" is it displays the value of global variable f=101

# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)

#learn to use the word global for variable inside a function
f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
    global f
print(f)
f = "changing global variable"
someFunction()
print(f)

# How to delete a variable
f = 11;
print(f)
del f
#Normal to get an error code because f is no longer defined so delete the print command

#string literals
a = "Hello, World!"
print(a[1])

#How to substring
b = "Hello, World!"
print(b[2:5])

#remove white space for the beginning and the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#How to return the length of a string
a = "Hello, World!"
print(len(a))

#Assigment Operators
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print(("Line 1 - Result of + is ", res))

#Python Comparison Operators
x = 4
y = 5
print(('x > y is',x>y))

#python logical operators
a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))

#Python Identity Operators

x = 20
y = 20
if ( x is y ):
    print("x & y SAME identity")
y=30
if ( x is not y ):
    print("x & y have DIFFERENT identity")

#Python Membership Operators
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if ( y not in list ):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

#How to create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#How to access the list items by refering to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#numbers in the index list start at 0 and that's why 1 is the second

#How to change item value in a list (here we changed the second one (1))
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#How to print all items for a list one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#How to check if an item exists in a list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#How to know the lenght of a certain list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#How to add an item to the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Orange is added at the end with this command

#How to add an item, but at a specific position (here, second position because of 1)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#How to remove an item for the list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#How to remove an item in the list by using the index
#when nothing is specified in pop () it is the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#How to remove a specific index () or the whole list
#Specific
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Whole
thislist = ["apple", "banana", "cherry"]
del thislist
#this will cause an error because "thislist" no longer exists. (deleted the line print)

#How to empty a list (deleted the lines)
#error code

#How to construct a list with list() Error code list object is not callable

#Python collections
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ["apple", "banana", "cherry"]
thistuple[1] = "blackcurrant"
print(thistuple)
#Set is a collection which is unordered and unindexed. No duplicate members.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

#How to add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#How to remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
#Error code because thisset is not longer defined (deleted the print command at the end)

#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#accessing items
x = thisdict["model"]
print(x)
#added a print command to check it

x = thisdict.get("model")

#change values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#added a print command to verify that it works
#How to add items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
thisdict["color"] = "red"
print(thisdict)

#How to remove items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
thisdict.popitem()
print(thisdict)
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
del thisdict["model"]
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
del thisdict
#Error code so i removed the print command

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964 }
thisdict.clear()
print(thisdict)

#Python if... else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#Python loops
#While loop (With the while loop we can execute a set of statements as long as a condition is true)
i = 1
while i < 6:
    print(i)
    i += 1

#the break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#The continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Python for Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Looping through a string
for x in "banana":
    print(x)

#The break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#the continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
for x in range(6):
    print(x)

#Else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#Recursion
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)

#Creating a function
def my_function():
    print("Hello from a function")

def my_function():
    print("Hello from a function")

my_function()

#parameters
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Return Values
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#How to create a class
class MyClass:
    x = 5

#Create Object
p1 = MyClass()
print(p1.x)

#The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = name
    def myfunc(self):
        print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#The Self parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#Modify Object Properties
p1.age = 40

#delete Object Properties
del p1.age

#delete object
del p1

#FIle Handling
f = open("demofile.txt", "a")
f = open("demofile.txt", "w")
f = open("demofile.txt", "r")
print(f.read())

#Python file write
# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("""Hello! Welcome to demofile.txt This file is for testing purposes. Good Luck!""")
f = open("demofile.txt", "r")
print(f.read())

#How to read only parts of the file

f = open("demofile.txt", "r")
print(f.read(5))
#Return the 5 first characters of the file

#How to read lines
f = open("demofile.txt", "r")
print(f.readline())

# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
# the "w" method will overwrite the entire file.
f = open("demofile.txt", "r")
print(f.read())
#"w" - Write - will overwrite any existing content

#Python Delete File
# Remove the file "demofile.txt":
#import os
#os.remove("demofile.txt")

# Check if file exist, then delete it:
#import os
#if os.path.exists("demofile.txt"):
    #os.remove("demofile.txt")
#else:
    #print("The file does not exist")

# Remove the folder "myfolder":
#import os
#os.rmdir("myfolder")
