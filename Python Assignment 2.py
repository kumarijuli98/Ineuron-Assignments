#!/usr/bin/env python
# coding: utf-8

# In[1]:


#####Q- 1. Write a Python program to convert kilometers to miles?


# In[2]:


# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[3]:


### Q-2.Write a Python program to convert Celsius to Fahrenheit?


# In[4]:


### Formula----------fahrenheit = celsius * 1.8 + 32

celsius = 37.5

fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[5]:


##### Q-3. Write a Python program to display calendar?


# In[6]:


# importing calendar module

import calendar


# To take month and year input from the user

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))


print(calendar.month(yy, mm))


# In[7]:


###Q- 4. Write a Python program to solve quadratic equation?


# In[8]:


#  quadratic equation  is ax**2 + bx + c = 0

# import complex math module

import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[9]:


#### Q-5. Write a Python program to swap two variables without temp variable?


# In[10]:


x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'

x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:




