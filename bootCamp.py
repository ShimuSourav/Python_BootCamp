
# coding: utf-8

# In[2]:


#1 - enter length in centimeter and convert it to meter and kilometer

len_cm = input("Enter the length in centimeter: ")
len_m = int(len_cm) / 100
len_km = int(len_cm) / 100000
print(str(len_cm) + " = " + str(len_m) + " meter and " + str(len_km) + " kilometer")


# In[3]:


#2 - enter temperature in celsius and convert it to fahrenheit

temp_cel = float(input("Enter temp in celsius: "))
temp_f = temp_cel * 9 / 5 + 32
print(str(temp_cel) + " celsius = " + str(temp_f) + " fahrenheit")


# In[4]:


#3 - python program to find power of any number

print("Enter two numbers: ")

x = int(input())
y = int(input())
print(str(x) + " to the power " + str(y) + " = " + str(x ** y))


# In[5]:


#4 - checking a number is even or odd

#using modulus operator
a = int(input("Enter a number: "))
if a % 2 == 0:
    print(str(a) + " is Even")
else:
    print(str(a) + " is Odd")
    
#using bitwise operator
if(a & 1 == 1):
    print(str(a) + " is Odd")
else:
    print(str(a) + " is Even") 


# In[6]:


#5 - checking wheather a character is alphabet or not

char = input("Enter a character: ")
char.isalpha()


# In[7]:


#6 - finding maximum between three numbers

a = input()
b = input()
c = input()

print("Maximum between these three: " + str(max(a, b, c)))


# In[8]:


#7 - counting number of digits in a number

num = input("Enter a number: ")
len(num)


# In[9]:


#8 - checking palindrome (string)

my_str = input("Enter a string: ")

if (my_str == my_str[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


# In[10]:


#9 - count total number of vowels and consonants in a string

string = "Trust me, I'm a liar"
vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")

v = 0
c = 0

for i in string:
    if i in vowels:
        v += 1
    elif i in consonants:
        c += 1
        
print("Total no. of Vowel = " + str(v) + " and Consonant = " + str(c))


# In[1]:


#10 - declare a variable without breaking any of the rules

a = 100
print(a)


# In[1]:


#11 - declare this variable “break = 50”. Which rule does it break ?

print("There are some keywords in Python we can't use them as variables. \nBecause Python uses them for other purposes.")


# In[2]:


#12 - Make changes to these variables so that they no longer break the rules to 1. phone$number = 12345 2. 123Name = “Benny”

phone_number = 12345
name = "Benny"
print(name)
print(phone_number)


# In[ ]:


#13


# In[ ]:


#14


# In[5]:


#15-16-17 

#program to create a tuple of 4 elements
my_tuple = (10, "py", 12, "rock")
print(my_tuple)

##converting this tuple into a list
my_list = list(my_tuple)
print(my_list)

#deleting the first element in this list and converting it back to tuple
del my_list[0]
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)


# In[6]:


#18

"""Solve this equation manually.
            2 + 3 * 4
      	Now write a program to solve this.
         	Did you get the same answer?"""

2 + 3 * 4

a = int(input())
b = int(input())
c = int(input())

res = a + b * c
print(str(res))

if (2 + 3 * 4 == res):
    print("same answer")
else:
    print("not same")


# In[7]:


#19 - use a logical operator in between two comparison operators and return the value as true

(8 > 7) and ('a' != 'b')


# In[8]:


#20

#a program to create a list of 5 elements Update the value at 3rd element of the list Create another list of 3 elements. 
#now creating a final result as a concatenation of the first two lists

aList = [1, 2, 3, "hello", 10]
bList = ["hi", "py", 3]
aList[2] = bList

print(aList)


# In[9]:


#21 

#a program to create a dictionary with 5 key-value pairs 
aDic = {"C" : 2, "Python" : 3, "R" : 4, "Java" : 5, "PHP" : 1}
print(aDic)

#Updating the value of a key
aDic["PHP"] = 6
print(aDic)

#Copy this dictionary to another dictionary and clear the first dictionary
bDic = aDic.copy()
print(bDic)

aDic.clear()
print(aDic)


# In[10]:


#22 - a program to check if a number is less than 10

a = int(input("Enter a number: "))
if a < 10:
    print(str(a) + " is less than 10")
else: 
    print(str(a) + " is not less than 10")


# In[11]:


#23

""" a program to check if a number is divisible by both 10 as well as 50. 
    If it is divisible by 30 as well, print “This number is divisible by 10, 50 and 30”. 
    If not, print “This number divisible by 10 and 50 but not 30”
"""

a = int(input("Enter a number: "))
if (a % 10 == 0 and a % 50 == 0):
    if (a % 30 == 0):
        print("This number is divisible by 10, 50 and 30")
    else:
        print("This number divisible by 10 and 50 but not 30")


# In[12]:


#24 - a program to calculate factorial number(manually)

n = int(input("Enter a number: "))
fact = 1
while n > 0:
    fact = fact * n
    n = n - 1

print("Factorial of the given number: " + str(fact))


# In[13]:


#24 - a program to calculate factorial number(using function)

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return (n * factorial(n-1))

n = int(input("Enter a number: "))
print("Factorial of the given number: " + str(factorial(n)))


# In[14]:


#25 - a program to print Fibonacci series up to n terms (without recursion)

n = int(input())

# first two terms
n1 = 0
n2 = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence upto",n,":")
   while count < n:
       print(n1, end='  ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[16]:


#25 - a program to print Fibonacci series up to n terms (using recursion)

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms: "))
print("Fibonacci sequence upto: " + str(n))
for i in range(n):
    print (fibonacci(i), end = '  ')


# In[ ]:


#26


# In[17]:


#27

"""Star Line
Print as many stars as given in input
Sample input:
6
Sample output
******
"""

num_stars = int(input("Enter the number of stars to be printed: "))
count = 0

while num_stars > 0:
    print("*", end = " ")
    num_stars -= 1


# In[18]:


#28

"""Rectangle using solution of PROBLEM 1) Star Line
Sample input:
4
6
Sample output
******
******
******
******
 
Hint: 4 and 6 means 4 lines of stars having 6 stars in each line.
"""

r = int(input()) #row
c = int(input()) #column

for i in range(r): 
  for j in range(c):  
    print("* ", end='')
  print() 


# In[28]:


#29

"""
Triangle - Left Justified
Draw right angled triangle of given height
Sample input:
4
Sample output
*
**
***
****
 
Hint: One loop for lines, another loop for printing i number of starts when it is line i.
"""

rows = int(input())
for i in range(rows):
        print('*' * (i+1))


# In[22]:


#30

"""Triangle - Right Justified
Draw right angled triangle of given height
Sample input:
4
Sample output
   *
  **
 ***
****
Hint: Count and print appropriate number of spaces in front of stars. 
Notice that there is one less space and one more star in each line.
"""

rows = int(input())
for i in range(rows):
        print((rows - i) * " " + '*' * (i+1))


# In[27]:


#31

"""
Triangle - Isosceles
Draw triangle of given height
Sample input 1:
3
Sample output 1:
  *
 ***
*****
"""

n = int(input())

for i in range(n):
    print((n-i) * ' ' + (2*i+1) * '*')


# In[25]:


#32

"""
Triangle - Isosceles
Just draw the image of the above triangle once.  And then, the opposite, once.
Sample input:
3
Sample output
  *
 ***
*****
 ***
  *
"""


n = int(input())

for i in range(n-1):
    print((n-i) * ' ' + (2*i+1) * '*')
for i in range(n-1, -1, -1):
    print((n-i) * ' ' + (2*i+1) * '*')

