# while loop 
count = 0 
while (count < 3): 
  count = count + 1 
  print("Hello Geek") 


# Single statement while block (can be written in one line)
count = 0 
#while (count == 0): print("Hello Geek") 
#it is an infinite loop so we write it as:
while (count == 0): print("Hello Geek") ;count+=1



#for in loop
#syntax
#for iterator_var in sequence:
# -->Examples 
# 1-Iterating over a list
print("List Iteration") 
l = ["geeks", "for", "geeks"] 
for i in l: 
   print(i)

# 2-Iterating over a tuple (immutable) 
print("\nTuple Iteration") 
t = ("geeks", "for", "geeks") 
for i in t: 
  print(i)

# 3-Iterating over a String 
print("\nString Iteration") 
s = "Geeks" 
for i in s : 
  print(i)    # Directly accesses each element

#Python program to illustrate 

# 4-Iterating by index 
list = ["geeks", "for", "geeks"] 
for index in range(len(list)): 
  print ( list[index] )   # Accesses elements using an index 
# this method is usually used when we need both indexes and value...


#Continue Statement: 
# Prints all letters except 'e' and 's' 
for letter in 'geeksforgeeks': 
 if letter == 'e' or letter == 's': 
    continue 
 print ('Current Letter :', letter )


#Break Statement: 
# break the loop as soon it sees 'e' 
# or 's'
for letter in 'geeksforgeeks':  
  if letter == 'e' or letter == 's': 
    break 
  print ('Current Letter :', letter)


#functions in python

#Creating a Function
#def keyword is used 
def my_function(): 
  print("Hello from a function") 

#Calling that Function 
#function_name()
my_function()


#Parameters 
# single parameter
def my_function(fname): 
 print(fname + " Refsnes") 

#Calling that Function
my_function("Emil") 
my_function("Tobias") 
my_function("Linus") 



#Default Parameter Value
def my_function(country = "Norway"): 
  print("I am from " + country) 

#Calling that Function
my_function("Sweden")  
my_function("India")  
my_function()       #in that case it uses default value of parameter country i.e:Norway 
my_function("Brazil")



#Passing a List as a Parameter 
def my_function(food): 
  for x in food: 
   print(x) 
#Calling that Function 
fruits = ["apple", "banana", "cherry"] 
my_function(fruits)


# Return Values 
def my_function(x): 
  return 5 * x 

#Calling that Function
print(my_function(3)) 
print(my_function(5)) 
x=my_function(9)
print(x) 

# Keyword Arguments
def my_function(child3, child2, child1): 
  print("The youngest child is " + child3) 
#Calling that Function
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Create a Class
# keyword class is used
class MyClass: 
  x = 5

# Create Object of that class
p1 = MyClass() 
print(p1.x) 


# The _init_() Function/just like constructor
class Person: 
  def __init__(self, name, age):
    self.name = name 
    self.age = age 

# Create Object of that class
p1 = Person("John", 36) 
print(p1.name) 
print(p1.age)


# Object Methods /Functions
class human: 
  def __init__(self, name, age): 
     self.name = name 
     self.age = age 
  def myfunc(self): 
    print("Hello my name is " + self.name)

# Create Object of that class
p1 = human("John", 36)
p1.myfunc()
