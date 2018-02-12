
# coding: utf-8

# In[2]:


#enter length in centimeter and convert it to meter and kilometer

len_cm = input("Enter the length in centimeter: ")
len_m = int(len_cm) / 100
len_km = int(len_cm) / 100000
print(str(len_cm) + " = " + str(len_m) + " meter and " + str(len_km) + " kilometer")


# In[3]:


#enter temperature in celsius and convert it to fahrenheit

temp_cel = float(input("Enter temp in celsius: "))
temp_f = temp_cel * 9 / 5 + 32
print(str(temp_cel) + " celsius = " + str(temp_f) + " fahrenheit")


# In[4]:


#python program to find power of any number

print("Enter two numbers: ")

x = int(input())
y = int(input())
print(str(x) + " to the power " + str(y) + " = " + str(x ** y))


# In[5]:


#checking a number is even or odd

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


#checking wheather a character is alphabet or not

char = input("Enter a character: ")
char.isalpha()


# In[7]:


#finding maximum between three numbers

a = input()
b = input()
c = input()

print("Maximum between these three: " + str(max(a, b, c)))


# In[8]:


#counting number of digits in a number

num = input("Enter a number: ")
len(num)

