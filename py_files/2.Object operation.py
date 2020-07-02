#!/usr/bin/env python
# coding: utf-8

# # Data type operation

# <div class="alert alert-block alert-info" style="margin: 20px">
#  
#  
# * **Operators** are used to perform operations on variables and values.
# * **Iterator** is an object that contains a countable number of values
# * **Generators** are used to create iterators, but with a different approach

# ## Operators

# ### Arithmetic Operators

# | Operator|	Name|	Example|
# |:--------|:----|:---------|
# |+	|Addition	|x + y	
# |-	|Subtraction	|x - y	
# |*	|Multiplication	|x * y	
# |/	|Division	|x / y	
# |%	|Modulus	|x % y	
# |**	|Exponentiation	|x ** y	
# |//	|Floor division	|x // y

# In[10]:


a, b=2,7
print ("a+b = ", a+b)             # addition/concatenation
print ("a-b = ", a-b )            # subtraction
print ("a*b = ", a*b )            # multiplication

# division. Notice that a,b are integers 
print ("b/a = ", b/a )   # in python3, b/a is a float 

# modulus, returns remainder
print ("b%a = ", b%a)    

# floor division, return quotient which is floored
print ("b//a = ", b//a )     

# exponent
print ("b**a = ", b**a )          


# ### Assignment Operators

# | Operator|	Name|	Equivalent|
# |:--------|:----|:---------|
# |=	|x = 5	|x = 5	
# |+=	|x += 3	|x = x + 3	
# |-=	|x -= 3	|x = x - 3	
# |*=	|x *= 3	|x = x * 3	
# |/=	|x /= 3	|x = x / 3	
# |%=	|x %= 3	|x = x % 3	
# | //=	|x //= 3	|x = x // 3	
# |**=	|x **= 3	|x = x ** 3	
# |&=	|x &= 3	|x = x & 3	
# ||=	|x \|= 3	|x = x \| 3|	
# |^=	|x ^= 3	|x = x ^ 3	
# |>>=	|x >>= 3	|x = x >> 3	
# |<<=	|x <<= 3	|x = x << 3

# In[13]:


# consise assignment 
a+=b

# a+=b is equivalent to a = a + b.
print ("after a+=b, a =", a) 
a*=b

# a*=b is equivalent to a= a*b. 
print ("after a*=b, a =",a) 


# | is or
x = 5
x |= 3 # x = x | 3 
print(x)

# 5 Bitwise is 0101，
# 3 Bitwise is 0011
# if there exist 1 then 1 
# then 3 or 5 is 0111, it is 7



# This concise assignment operator can be applied to other basic operators, check the tables above


# ### Comparison Operators

# | Operator|	Name|	Equivalent|
# |:--------|:----|:---------|
# |==	|Equal	|x == y	
# |!=	|Not equal	|x != y	
# |>	|Greater than	|x > y	
# |<	|Less than	|x < y	
# |>=	|Greater than or equal to	|x >= y	
# |<=	|Less than or equal to	|x <= y

# In[16]:


a, b = 2,7

print ("a==b ?", a==b)          # equal
print ("a!=b ?", a!=b )         # not Equal
print ("a>b ?",a>b)             # greater than
print ("a<b ?",a<b )            # less than
print ("a>=b ?",a>=b)           # greater than or equal
print ("a<=b ?",a<=b)           # less than or equal


# ### Logical Operators

# | Operator|	Name|	Equivalent|
# |:--------|:----|:---------|
# |and 	|Returns True if both statements are true	|x < 5 and  x < 10	
# |or	|Returns True if one of the statements is true	|x < 5 or x < 4	
# |not	|Reverse the result, returns False if the result is true	|not(x < 5 and x < 10)
# 

# In[18]:


a, b, c=2,7, [1,2,3]
# both conditions are true
print ("(a>b) and (a in c)? ——————>",(a>b) and (a in c))     
# either condition is true
print ("(a>b) or (a in c)? ——————>",(a>b) or (a in c))
# reverse the condition
print ("not (a>b)?  ——————>",not (a>b) )                    


# ### Membership Operators
# 

# | Operator|	Name|	Equivalent|
# |:--------|:----|:---------|
# |in 	|Returns True if a sequence with the specified value is present in the object	|x in y	
# |not in	|Returns True if a sequence with the specified value is not present in the object	|x not in y

# In[19]:


x = ["apple", "banana"]

print("banana" in x)


# ### Bitwise Operators

# |Operator	|Name	|Description|
# |:----------|:------|:---------|
# |& 	|AND	|Sets each bit to 1 if both bits are 1|
# |\|	|OR	|Sets each bit to 1 if one of two bits is 1|
# |^	|XOR	|Sets each bit to 1 if only one of two bits is 1
# |~ 	|NOT	|Inverts all the bits
# |<<	|Zero fill left shift	|Shift left by pushing zeros in from the right and let the leftmost bits fall off
# |>>	|Signed right shift	|Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# In[24]:


a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
print ("1 - c is：", c)
 
c = a | b;        # 61 = 0011 1101 
print ("2 - c is：", c)
 
c = a ^ b;        # 49 = 0011 0001
print ("3 - c is：", c)
 
c = ~a;           # -61 = 1100 0011
print ("4 - c is：", c)
 
c = a << 2;       # 240 = 1111 0000
print ("5 - c is：", c)
 
c = a >> 2;       # 15 = 0000 1111
print ("6 - c is：", c)


# #### <font color = blue> Operators Priority

# |Operator	|
# |:----------|
# |**	|
# |~ + -|
# |* / % //	
# |+ -	
# |>> <<	
# |&	
# |^ \|	
# |<= < > >=	
# |<> == !=	
# |= %= /= //= -= += \*=\**=	
# |is is not	
# |in not in	
# |not and or	

# # Iterator / Generator
# 

# <div class="alert alert-block alert-info" style="margin: 20px">
#     
# *  An iterator is simply an object that can be iterated upon. An iterator will return data, one element at a time.
# *  An iterator must implement two special methods, <font color=blue> iter</font> and  <font color=blue>next</font>.
# * An object is called **iterable** if we can get an iterator from it. *Iterable objects include lists, tuples, strings, dictionaries* etc. The <font color=blue>__iter__()</font> function returns an iterator from an iterable object.
# * An iterator object can be used **only once**. When we reach the end and there is no more data to be returned, it will raise the error *StopIteration*.
# 
# 
# * **A generator is a function that behaves like an iterator**

# ### Iterator

# In[25]:


# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
print(my_iter)

# similarly, you can convert the iterator object back to a list
print(list(my_iter))


# **Using next to make it iterable**

# In[26]:


## iterate through an iterable using next() 
my_iter = iter(my_list)

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

# loop through all remaining elements
for item in my_iter:
    print (item)
    
# raise StopIteration error if call next again since the for loop has reached the end of the iterator object
print(next(my_iter))


# ### Generator

# * Generator function contains one or more `yield` statements.
# * When called, it returns an `object (iterator)` but does not start execution immediately.
# * Methods like `__iter__()` and `__next__()` are implemented automatically. So we can iterate through the items using `next()`.
# * Once the function yields, the function is paused and the control is transferred to the caller.
# * Local variables and their states are remembered between successive calls.
# * Finally, when the function terminates, **StopIteration** is raised automatically on further calls.

# In[42]:


# A simple generator function
def my_gen(lst):
    for i in range(len(lst)):
    # Generator function contains yield statements
      yield lst[i]


# In[43]:


a = my_gen(my_list)


# In[48]:


next(a)


# # Advance operations

# ### subset (<=) / superset (>=)

# ![](https://raw.githubusercontent.com/devin19940107/My-Python-Notebook/master/supporting%20files/Images/subset.png)

# In[8]:


# list

a = [1,2,3,4]
b = [1,2,3,4,5]

a <= b
# a.issubset(b)# error


# In[11]:


# set
a = {1,2,3,4}
b = {1,2,3,4,5}

print(a <= b)
print(a.issubset(b)) # only works in set data type


# In[21]:


# dictionary
a = {'1':1,'2':2,'3':3}
b = {'1':1,'2':2,'3':3,'4':4}
# print(a <= b) # '<=' not supported between instances of 'dict' and 'dict'
print(a.items() <= b.items())
print(a.keys()<= b.keys())


# In[23]:


# tuple
a= (1,2,3,4)
b=(1,2,3,4,5)
print(a <= b)


# In[26]:


# string
a = '12345'
b = '123456'
print(a <= b)


# In[27]:


# int
a = 12345
b = 123456
print(a <= b)


# In[33]:


# bool
a = False # 0
b = True  # 1
print(a <= b)


# In[34]:


# float

a = 123.45
b = 123.456
print(a <= b)


# ### Union
# 
# - not appliacble type
#     * list
#     * string
#     * float

# ![](https://raw.githubusercontent.com/devin19940107/My-Python-Notebook/master/supporting%20files/Images/union.jpg)

# In[39]:


# set
a = {1,2,3,4}
b = {1,2,3,4,5}
print(a | b)
print(a.union(b))


# In[48]:


# dictionary
a = {'1':1,'2':2,'3':3}
b = {'1':1,'2':2,'3':3,'4':4}
print(a.items() | b.items())
print(a.keys() | b.keys())


# In[45]:


# int
a = 11
b = 13
print(a | b)
# check Bitwise Operators


# In[55]:


# bool
a = False # 0
b = True  # 1
print(a | b)


# ### Intersection
# 
# - not appliacble type
#     * list
#     * string
#     * float

# ![](https://raw.githubusercontent.com/devin19940107/My-Python-Notebook/master/supporting%20files/Images/Intersection.jpg)

# In[60]:


# set
a = {1,2,3,4}
b = {1,2,3,4,5}
print(a & b)
print(a.intersection(b))


# In[62]:


# dictionary
a = {'1':1,'2':2,'3':3}
b = {'1':1,'2':2,'3':3,'4':4}
print(a.items() & b.items())
print(a.keys() & b.keys())


# In[63]:


# int
a = 11
b = 13
# check Bitwise Operators
print(a & b)


# In[64]:


# bool
a = False # 0
b = True  # 1
print(a & b)


# ### Difference
# - not appliacble type
#     * list
#     * string

# ![](https://raw.githubusercontent.com/devin19940107/My-Python-Notebook/master/supporting%20files/Images/difference.jpg)

# In[70]:


# list

a = [1,2,3,4]
b = [1,2,3,4,5]

# str
a = '12345'
b = '123456'

print(a <= b)
a - b # unsupported operand
# but you can use a+b it returns:
# [1, 2, 3, 4, 1, 2, 3, 4, 5]
# 12345123456


# In[75]:


# float
a = 12.345
b = 12.3456
print(a - b)


# In[76]:


# int
a = 11
b = 13
# check Bitwise Operators
print(a - b)


# In[78]:


# set
a = {1,2,3,4,5,6}
b = {1,2,3,4,5}
print(a - b)
print(a.difference(b))


# In[85]:


# dictionary

a = {'1':1,'2':2,'3':3,'4':4}
b = {'1':1,'2':2,'3':3}

print(a.items() - b.items())

print(a.keys() - b.keys())


# In[86]:


# bool
a = False # 0
b = True  # 1
print(a - b)


# ### symmetric difference
# - not appliacble type
#     * list
#     * string
#     * float

# ![](https://raw.githubusercontent.com/devin19940107/My-Python-Notebook/master/supporting%20files/Images/symmetric-difference.jpg)

# In[90]:


# int
a = 11
b = 13
# check Bitwise Operators
print(a ^ b) # Sets each bit to 1 if only one of two bits is 1


# In[92]:


# set
a = {1,2,3,4,5,6}
b = {1,2,3,4,5,7}
print(a ^ b)
print(a.symmetric_difference(b))


# In[93]:


# dictionary

a = {'1':1,'2':2,'3':3,'4':4}
b = {'1':1,'2':2,'3':3}

print(a.items() ^b.items())


# In[94]:


# bool
a = False # 0
b = True  # 1
print(a ^ b)


# ### Sepcial discuss: 
#  bool value can be oeprated by any operator, but, why???
#  
#  I think it just a int with range(0,2)

# In[105]:


a = False # 0
b = True  # 1
print('bool opeartion：',a ^ b)

a = 0
b = 1
print(a ^ b)


# In[104]:


# bool
a = False # 0
b = True  # 1
print('bool operation：',a - b)

a = 0
b = 1
print(a - b)


# In[108]:


# bool
a = False # 0
b = True  # 1
print('bool operation：',a & b)


a = 0
b = 1
print(a & b)


# In[110]:


# bool
a = False # 0
b = True  # 1
print('bool operation：',a <= b)


a = 0
b = 1
print(a <= b)


# In[111]:


# bool
a = False # 0
b = True  # 1
a = False # 0
b = True  # 1
print('bool operation：',a | b)


print(a | b)


# In[1]:


print('codelines 112')


# In[ ]:




