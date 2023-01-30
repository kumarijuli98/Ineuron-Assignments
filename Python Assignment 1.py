#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Q-1. Write a Python program to print "Hello Python"?


# In[5]:


print ("Hello Python")


# In[6]:


### Q-2. Write a Python program to do arithmetical operations addition and division.?


# In[7]:


num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))

sum = num1 + num2

div = num1 / num2


# In[8]:


sum


# In[9]:


div


# In[10]:


#### Q- 3. Write a Python program to find the area of a triangle?


# In[17]:


a = float(input('Enter first side: '))
 
b = float(input('Enter second side: '))
     
c = float(input('Enter second side: '))
    
s = (a + b + c) / 2


area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[18]:


### Q-4. Write a Python program to swap two variables?


# In[19]:



x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[20]:


### Q-5. Write a Python program to generate a random number?


# In[22]:


# lets take random number between 0 and 9

# importing the random module
import random

print(random.randint(0,9))


# In[ ]:




