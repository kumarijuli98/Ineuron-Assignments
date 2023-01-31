#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?


# In[2]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[3]:


### 2. Write a Python Program to Check if a Number is Odd or Even?


# In[4]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[6]:


### 3. Write a Python Program to Check Leap Year?


# In[7]:



year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))


# In[8]:


num = 29

flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:

    for i in range(2, num):
        if (num % i) == 0:
           
            flag = True
           
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# In[9]:


### 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[15]:


lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  


# In[ ]:




