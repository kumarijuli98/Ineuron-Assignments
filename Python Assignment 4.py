#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### 1. Write a Python Program to Find the Factorial of a Number?


# In[4]:



# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[5]:


### 2. Write a Python Program to Display the multiplication Table?


# In[6]:


# To take input from the user

num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10

for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[8]:


### 3. Write a Python Program to Print the Fibonacci sequence?


# In[9]:


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[10]:


### 4. Write a Python Program to Check Armstrong Number?


# In[11]:


# take input from the user

num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10


if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[12]:


### 5. Write a Python Program to Find Armstrong Number in an Interval?


# In[28]:




lower = 100
upper = 2000

for num in range(lower, upper + 1):

   
   order = len(str(num))
    
   
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


# In[29]:


### 6. Write a Python Program to Find the Sum of Natural Numbers?


# In[30]:


num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)


# In[ ]:




