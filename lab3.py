
# LAB-03

#Question 1:

for i in range(1500,2701):
    if(i%7==0 and i%5==0):
         print (i)



# Question 2

temp=float(input("Enter temperature: "))
unit=input('Enter unit of temperarure: ').lower()

if(unit=='c'):
    temp=(temp*1.8)+32
    print(f'Temperature in fahrenheit is {temp}F')

elif (unit=='f'):
    temp=((temp-32)/1.8)
    print(f'Temperature in calcius is {temp}C')



# Question 3

guess=5
num=int(input('Enter a guess number between 1-9: '))
while(num!=guess):
    print('Wrong guess')
    num=int(input('Enter a guess number again between 1-9: '))

print('Well guessed!')



# Question 4

# # --------------pattern without nested loops----------------- 


# forward loop method: range(start,stop,step)         -stop not includes in range
# by default step is +1 in range 
for i in range(1,6):
    print(i*"* ")          #special functionality in python


# backward loop method: range(start,stop,step)
# range(4,0) does not work because range's step always +1 by default
for i in range(4,0,-1):  
    print(i*"* ")


# --------------pattern with nested loops----------------------- 
row=5
#upper triangle
for i in range(1,row+1):
    for j in range(i):
        print("*", end=" ")   # → prints on same line with a space
    print()                   # → moves to next line
#lower triangle
for i in range(row-1,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()



# Question 5

word=input('Enter a word: ')
reverse_word=word[::-1]   
print("Reversed word is:",reverse_word)


# EXPLAINATION:
# sequence[start:stop:step] is called SLICING in Python.

# if word=hello
# 🔹 word[1:4] → 'ell'
# Starts at index 1 (e), stops before index 4 (o), so you get e, l, l.

# 🔹 word[::2] → 'hlo'
# Starts from beginning, goes to end, takes every 2nd letter.

# 🔹 word[::-1] → 'olleh'
# Step is -1, so it reverses the string.



# Question 6

num=(1,2,3,4,5,6,7,8,9,10,11)
even=0
odd=0
for i in num:
    if(i%2==0):
        even+=1
    else:
        odd+=1

print(f'Number of even numbers: {even} \nNumber of odd numbers: {odd}')    



# Question 7

sample list
datalist=[1452,11.23,1+2j,True,'w3resourse',(0,-1),[5,12],{"Class":'V',"Section":'A'}]
for i in datalist:
    print(f'Type of {i} is {type(i)}')



# Question 8

for i in range(0,7):
    if(i==3 or i==6):
        continue
    print(i)



# Question 9-part1
# Fibonancy series 


a=0
b=1
while a<50:
    print(a, end=" ")
    a,b= b,a+b        # a=b and b=a+b must perform in one step 

# Question 9-part2

for i in range(0,51):
    if(i%3==0 and i%5==0):  # must check fizzbuzz condition first
        print("FizzBuzz")
    elif (i%3==0):
        print("Fizz")
    elif (i%5==0):
        print("Buzz")
    else:
        print(i)   



# Question 10

Rows=int(input("Enter number of rows: "))
Cols=int(input("Enter number of columns: "))

array_list=[]

for i in range(Rows):
    row_list=[]
    for j in range(Cols):
        row_list.append(i*j)      #The append() method is used with lists in Python to add a new element at the end of the list
    array_list.append(row_list)

print(array_list)



# Question 11

print("Enter strings (blank string to stop line):")

line=[]

while True:
    string=input()
    if string== "":
        break
    line.append(string.lower())

print(" ".join(line))  


# "separator".join(iterable) 
# to join elements of an iterable (like a list or tuple) into a single string, with a separator in between



# Question 12

binary_input = input("Enter comma-separated 4-digit binary numbers: ")

binary_num=binary_input.split(",")     # break input string into list items use , to split in string 

divisible_by_5=[]

for i in binary_num:
    decimal=int(i,2)
    if decimal % 5 == 0:
        divisible_by_5.append(i)

print(",".join(divisible_by_5))



# Question 13

text=input("Enter a string:")

Digits=0
Letters=0
for i in text:
     if i.isdigit():
         Digits+=1
     elif i.isalpha():
         Letters+=1 

print(f"Digits= {Digits} , Letters= {Letters}")
#       or
# print("Letters=", Letters)
# print("Digits=", Digits)



# Question 14

import re

def validate_password(password):
      if len(password)<6 or len(password)>16:
            return "Length of your password must be in between 6 and 16"
      if not re.search("[a-z]",password):
            return "Your Password must contain atleast one lower case letter"
      if not re.search("[A-Z]" ,password):
            return "Your Password must contain atleast one upper case letter"
      if not re.search("[@#$]",password):
             return "Your Password must contain at least one special character from [$#@]."
      if not re.search("[0-9]",password):
            return "Your password must contain atleast one digit"
      return "Valid Password!"

password=input("Enter your password:")
print(validate_password(password))


