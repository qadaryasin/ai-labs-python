# Comments in Python:(practice)

x=1
# the initial value of x is 1
if x>0:
   print("these are two comments") #print a string






#Multiple Statements on a Single Line:(practice)

print("Statement 1")
print("Statement 2")

# we can write both in a single line by using semicolon as:

print("Statement 1"); print("Statement 2")




#Indentation:(practice)

#no indentation 
#x=1
#if x>0:
#print("This statement has no indentation") #ERROR OCCURED (there must be indentation)
#print("This statement has no indentation")


#indentation is not fixed,but all statements have same indentation
# single space 
x=1
if x>0:
 print("This statement has a single space indentation") 
 print("This statement has a single space indentation")

# single tab 
x=1
if x>0:
    print("This statement has a single tab indentation") 
    print("This statement has a single tab indentation")

#single space + single tab 
x=1
if x>0:
     print("This statement has a single space+tab indentation") 
     print("This statement has a single space+tab indentation")






#Data types and Type casting

a=1452
print(type(a))

b=(-4578)
print(type(b))

c=0
print(type(c))

g=1.03
print(type(g))

h=-11.83
print(type(h))

i=.34
print(type (i))

j=2.12e-10
print(type(j))

k=5e220
print(type(j))



# complex number......

#___method 1(complex(x, y))
x=complex(1,2)
print(type (x))
print(x)

#___method 2((real + imagJ))
z=1+2j
print(type(z))

z=1+2J
print(type(z))



#Boolean (bool)
x=True
print (type(x))

y=False
print (type(y))




#Strings

#when string starts and ends with double quote
str1="String"
print (str1)

#when string starts and ends with single quote
str2='String'
print (str2)

#when string starts with double quote & ends with single quote 
#str3="String'   (SYNTAX ERROR OCCURED) 
#print (str3)

#when string starts with single quote & ends with double quote
##str4='String"  (SYNTAX ERROR OCCURED)
#print (str4)

#single quote within double quote
str5="Day's"
print (str5)

#double quote within single quote
str5='Day"s'
print (str5)



#special characters in strings
print("this is backlash (\\) mark")
print("this is a tab \t mark")
print("these are \'single quotes\' ")
print("these are \"double quotes\" ")
print("this is a newline\nNew line")



#string indeces and accessing string elements

str1="python tutorial"
print(str1[0]) #print first character
print(str1[-15])  #print first character
print(str1[1])  # print last character
print(str1[-11]) #print 4th character
#print(str1[16]) #out of index range (index ERROR)






#lists
my_list=[]
print(my_list)


my_list1=['red',12,112.12]
print(my_list1)


#list indices

color_list=['red' ,'blue' , 'green','black']
print(color_list[0]) #first element
print(color_list[-1])  #last element
print(color_list[-4])  #first element
