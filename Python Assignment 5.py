#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python Program to Find LCM?


# In[2]:


def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


# In[3]:


### 2. Write a Python Program to Find HCF?


# In[4]:


# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))


# In[5]:


### 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?


# In[10]:


dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[7]:


### 4. Write a Python Program To Find ASCII value of a character?


# In[11]:


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[12]:


### 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?


# In[14]:


num1 = float(input("enter 1st number"))
num2 = float(input("enter 2nd number"))

sum = num1 + num2
dif = num1 - num2
mult = num1 * num2
div = num1 / num2


print("The sum is ", sum)
print("The Dif is ", dif)
print("The mult is ", mult)
print("The div is ", div)


# In[ ]:




