#!/usr/bin/env python
# coding: utf-8

# # Python build-in Data Type

# | Type            | Function                                                                   |
# | :-------------  |:---------------------------------------------------------------------------|
# | Text            | `str`                                                                      |
# | Numeric         | `int`  `float` `complex`                                                   |
# | Sequence        | `list` `tuple` `range`                                                     |
# | Mapping         | `dictionary`                                                               |
# | Set             | `set`  `frozenset`                                                         |
# | Boolean         | `bool`                                                                     |
# | Binary          | `bytes` `bytearray` `memoryview`                                           |

# <font color = red>
#     
# * Immutable：Numeric(int/float/complex),Boolean,String,Tuple；
# * Mutable：List,Dictionary,Set

# # Setting the Data Type

# |Example|Data Type|
# | :-------------  |:---------------------------------------------------------------------------|
# |str	|x = "Hello World"
# |int	|x = 20	
# |float	|x = 20.5	
# |complex	|x = 1j	
# |list |x = ["apple", "banana", "cherry"]	
# |tuple |x = ("apple", "banana", "cherry")		
# |range	|x = range(6)	
# |dict |x = {"name" : "John", "age" : 36}		
# |set	|x = {"apple", "banana", "cherry"}	
# |frozenset	|x = frozenset({"apple", "banana", "cherry"})	
# |bool	|x = True	
# |bytes	|x = b"Hello"	
# |bytearray	|x = bytearray(5)	
# |memoryview |x = memoryview(bytes(5))	

# # String
# 

#  <div class="alert alert-block alert-info">
#  * Strings are identified as a contiguous set of characters represented in the quotation marks
#  * Substrings can be taken using slice operator **<font color=blue>[ ]</font>** with indexes starting at **<font color=blue>0</font> in the beginning of the string ** and working their way from **<font color=blue>-1</font> at the end **.
#  * Strings can be concatenated using **<font color=blue>+</font>**
#  * Useful string functions: **<font color=blue>strip, lstrip, rstrip, split, lower, upper, find, rfind, replace</font>**

# #### Create a string

# In[6]:


s0 =''               # an empty string
s = 'Hello World!'
print('An empty string:',s0)
print('_______________________ \n')
print('This is a non-empty string:',s)


# #### Slicing a string

# In[11]:


print(s)          # Prints complete string
print('_______________________ \n')


print(s[0])       # Prints first character of the string
print('_______________________ \n')


print(s[2:5])     # Prints characters starting from 3rd to 5th
print('_______________________ \n')


print(s[2:] )     # Prints string starting from 3rd character
print('_______________________ \n')


print(s[-1])      # Prints the last character 
print('_______________________ \n')


print(s[-3:])     #get the last three characters
print('_______________________ \n')


print(s[0:10:2])   # step-wise slicing; [start,end,step]


# # List

# <div class="alert alert-info" style="margin: 20px">
#     
# * Items in a list can be of **different data type** e.g. numbers, strings, lists, tuples, dictionaries
# * Values in a list can be accessed using slice operator **<font color=blue>[ ]</font>** with indexes starting at **<font color=blue>0</font> for the first element ** and working their way from **<font color=blue>-1</font> at the end **.
# 
# * Lists can be concatenated using **<font color=blue>+</font>**
# * A string is actually a list of characters without commas!
# 

# In[61]:


list0 = [ 'welcome', "to" , "my", 'notebook' ]
list1 = ['welcome to my notebook']
print(list1)
print('________________________ \n')
print(list2)


# #### length of a lsit

# In[62]:


print(f'the length of list0 is {len(list0)}, and length of list1 is {len(list1)}')


# #### List indexing

# In[63]:


print (list0)          # Prints complete list
print('_______________________ \n')



print (list0[0])       # Prints first element of the list
print('_______________________ \n')



print (list0[1:3])     # Prints elements starting from 2nd till 3rd 
print('_______________________ \n')



print (list0[2:])      # Prints elements starting from 3rd element
print('_______________________ \n')



print (list0[-1])      # Prints the last element
print('_______________________ \n')

# concatenate elements in a list
print ("+".join(list0))# join elements into a single string with " " as the separator

print('_______________________ \n')
# concatenate lists
print (list0 + list1)  # Prints concatenated lists


# In[52]:


list2 = ['My python notebook','List indexing']
list2


# In[60]:


print(list2[0])
print(list2[0][3:9]) 


# <font color= red> indexing always from 0. and the range of indexing always [start, end)

# #### append / extend/ remove

# In[39]:


list3 = [1,2,3,4,5,'a','b']
list3


# In[40]:


list3.append("c")     # append "c" to the end of the list
print (list3)


# In[41]:


list3.extend("d")     # extend "d" to the end of the list
print (list3)


# <font color = red> when it comes to a new list, a difference between append and extend will show

# In[42]:


list4 = ['11','22','33']
list3.append(list4)
print (list3)


# In[43]:


list5 =['aa','bb','cc']
list3.extend(list5) 
print (list3)


# In[36]:


list3.remove("a")     # remove the first "a" found in the list from the beginning
print (list3) 


# # Tuples 

# <div class="alert alert-info" style="margin: 20px">
#     
# * Tuples are enclosed within parentheses **<font color=blue>( )</font>**, while lists are enclosed in **<font color=blue>[ ]</font>**.
#     
# * A tuple, once declared, **<font color=blue>cannot be updated (read-only)</font>**, while the elements and size of a list can be changed

# In[103]:


tuple1 = ( 'welcome', "to" , "my", 'notebook' )
tuple2 = ('tuple(mynotebook)', 1994)

print (tuple1)          # Prints complete tuple
print('_______________________ \n')


print (tuple1[0])       # Prints first element of the tuple
print('_______________________ \n')



print (tuple1[1:3])     # Prints elements starting from 2nd till 3rd 
print('_______________________ \n')



print (tuple1[2:])      # Prints elements starting from 3rd element
print('_______________________ \n')



print (tuple1 + tuple2)  # Prints concatenated tuples


# In[84]:


# Make a list of tuple
# e.g. [(1,'Mary'),(2,'Tom'),(3, 'Joe')]

ids=(1,2,3)
names=('Mary','Tom','Joe')


# In[85]:


x=[(ids[0], names[0]),(ids[1], names[1]),(ids[2], names[2]) ]
print(x)


# In[86]:


# A efficient way: zip function - combine lists element-wise
# zip function in python 3 returns an iterator
# use list function to convert an iterator to list
zipped=list(zip(ids, names))   
print(zipped)


# In[98]:


# how to convert zipped back to unzipped? zip itself can also be an unzipped
idx, names = list(zip(*zipped))
print(idx, names)


# # Dictionary

# <div class="alert alert-info" style="margin: 20px">
# 
# *  A dictionary is made of key-value pairs, e.g. {1:'Mary Joe', 2:'David Johnson'} 
# *  Keys are **unique**
# *  A dictionary is enclosed by **curly braces { }** 
# *  Values can be assigned and accessed using **square braces [ ]**
# *  Keys are usually **numbers or strings**, but values can be of any python data types, e.g. numbers, strings, lists, tuples, dictionaries

# In[101]:


dict1 = {}                     # define an empty dictionary

dict1['one'] = "This is one"   # add  key-value pairs to the dictionary
dict1[2]     = "This is two"

dict1


# In[102]:


dict2 = {1:'Mary Joe', 2:'David Johnson'}  # a more compact way to define a dictionary
dict2


# In[177]:


# key must be unique, if duplicated key created, drop the old key-value pair
dic ={1:'Mary Joe', 2:'David Johnson', 2:'Mary Joe'} 
print(dic[2])
len(dic)


# In[2]:


Dictonary = {'key1':1,
             'key2':'value2',
             'key3':False,
             3:3,
             123.3:123.3,
             True:False,
             None:'not None',
             4:None,
             5:[12,32]
            }
# key can be str, int, float, bool, None, expect a list
# value can be every thing

Dictonary[None] # we can return the valye by calling the key

Dictonary.keys() # we can view keys by calling keys() function


# In[11]:


# searching by key
print('key1' in Dictonary)
print('value2' in Dictonary)
print(1 in Dictonary) # it is beacuse True can be seen as 1


# In[12]:


dic = {True:2}
print(1 in dic)


# In[105]:


print (dict1['one'])       # Prints value for 'one' key
print('_______________________ \n')



print (dict1[2])           # Prints value for 2 key
print('_______________________ \n')



print (dict2)              # Prints complete dictionary
print('_______________________ \n')



print (dict2.keys())       # Prints all the keys
print('_______________________ \n')



print (dict2.values())     # Prints all the values
print('_______________________ \n')


# In[106]:


print (list(dict2.items()) ) # print key-value pair as a list of tuples


#  # Set

# <div class="alert alert-info" style="margin: 20px">
#     
# * set is for constructing and manipulating  collections of unique elements
# * set is unordered, indexing has no meaning. so, sets do not support indexing, slicing, or other sequence-like behavior.
# * set classes are implemented using dictionaries.
# 

# ### Creating a set

# In[179]:


a = {1,3}  # Dictionary ???????
print(type(a))


# In[180]:


a = {}  # you can't create a empty set
print(type(a))


a = set() # this is the only way to create a empty set
print(type(a))


# In[254]:


# difference?
import timeit
print(timeit.timeit('a = set([1,2,3])'))

print(timeit.timeit('a = {1, 2, 3}')) # Faster


# In[244]:


# set() only receive one argument

# list
a = set([1,2,2,2,2,2,'33',3,'33',3,4,5,6])
print(type(a),a)

# dictionary
a = set({1:1,'2':2,'2':3})
print(type(a),a)

# str
a = set('aaaaaaaaa and 123 or 1  or 2 or 22.31 ')
print(type(a),a)

# tuple
a = set((1,2,3,3,3,3,4,5,6,'6','6'))
print(type(a),a)


# In[214]:


# {} can be passed many values
# but not a list

a = {'a',2,('a','a'),3,3}
print(type(a),a)


# string
a = 'aaaaaa'
b = 'aaabbc'
c = {a,b}
print(type(c),c)


# int
a = 12345
b = 1234
c = {a,b}
print(type(c),c)


#float
a = 123.45
b = 123.4
c = {a,b}
print(type(c),c)


# In[259]:





# ### set addation

# In[263]:


# Set
Set = {1, 3}
print('initate:',Set)

Set.add(2)
print('add(2):',Set)

# add multiple elements
Set.update([2, 3, 4])
print('update multiple elements:',Set)

# add list and set
Set.update([4, 5], {1, 6, 8})
print('add list and set:',Set)

# update t
a = {1,2,3,4,5}
t = {5,6,7,8,9}
a |= t
print("|= t is equal to update",a)
# more details see operation chapter


# ### set deletion

# In[226]:


# discard / remove/ pop / clear 


# discard and remove
Set.discard(4)
print('discard 4:',Set)
Set.remove(5)
print('remove 5:',Set)




Set.pop()
print('pop 1st:',Set)
# pop will delete 1st left element in a set. Since set is generated in a random order, pop can be different.
# but once a set is generated, order is settled, pop always from left 1 to the right end.
Set.pop()
print('pop 2nd:',Set)



# The only difference is remove will raise an error when there is no such element
Set.discard(5)
Set.remove(4)


# In[228]:


# clear
Set.clear()
Set # empty set


# # Data type converting

# ### bool( )
# * Any data type can be converted to bool
# * Only empty type canbe translated to False, otherwise True

# In[51]:


a =  True
print(type(a),a)


# In[48]:


# str to bool
a = 'True'
a = bool(a)
print(type(a),a)

a = '1'
a = bool(a)
print(type(a),a)

a = '0' # not empty
a = bool(a)
print(type(a),a) # True

a = 'False' # not empty
a = bool(a)
print(type(a),a) # True

a = '' # empty
a = bool(a)
print(type(a),a) # False


# In[34]:


# int to bool
a = 1
a = bool(a)
print(type(a),a)

a = 123
a = bool(a)
print(type(a),a) # True

a = -3
a = bool(a)
print(type(a),a) #True

a = 0
a = bool(a)
print(type(a),a) # Only 0 canbe reconized as False


# In[50]:


# float to bool
a = 11.35
a = bool(a)
print(type(a),a)

a = -0.1
a = bool(a)
print(type(a),a)

a = -0.0
a = bool(a)
print(type(a),a)

a = 0.0
a = bool(a)
print(type(a),a)


# In[64]:


# None type to bool
a = None
a = bool(a)
print(type(a),a)


# In[70]:


# list  to bool
a = [1,2,3]
a = bool(a)
print(type(a),a)

a = [0]
a = bool(a)
print(type(a),a)


a = []
a = bool(a)
print(type(a),a)


# In[82]:


# dic to bool
a = {'key1':11,'key2':12}
a = bool(a) 
print(type(a),a)

a = {}
a = bool(a) 
print(type(a),a)


# ### int( ) 
# * True = 1 , False = 0
# * Float only reamin integer part
# * Only integer in string can be convert to integer

# In[53]:


a = 11
print(type(a),a)


# In[54]:


# bool to int
a = True 
a = int(a)
print(type(a),a) # True =1. False =0

a = False 
a = int(a)
print(type(a),a)


# In[ ]:


# 


# In[55]:


# float to int
a = 11.35
a = int(a) # direct cut off the decimals, only reamin interger part. No round, cilling or floor
print(type(a),a)

a = -11.35
a = int(a) # direct cut off the decimals, only reamin interger part. No round, cilling or floor
print(type(a),a)


# In[60]:


# str to int
a = '11' 
a = int(a)
print(type(a),a)


a = '11.35' 
a = int(a)
print(type(a),a) # ValueError 

a = 'Hello, World'
a = int(a)
print(type(a),a) # ValueError 


# In[63]:


# None type to int
a = None
a = int(a)
print(type(a),a)


# In[72]:


# list to int
a = [1]
a = int(a)
print(type(a),a)


# In[85]:


a = {'key1':123}
a = int(a) 
print(type(a),a)


# ### str( )
# * every data type can be converted to str

# In[12]:


# str
a = '1223.26'
print(type(a),a)


# In[36]:


# int to str
a = 11
a = str(a)
print(type(a),a)


# In[20]:


# bool to str
a = True
a = str(a)
print(type(a),a)


# In[37]:


# float to str
a = 11.35
a = str(a)
print(type(a),a)


# In[61]:


# empty type to str
a = None
a = str(a)
print(type(a),a)


# In[67]:


# list to str
a = [1,2,3]
a = str(a)
print(type(a),a)


# In[79]:


# dictonary to str
a = {'key1':11,'key2':12}
a = str(a) 
print(type(a),a)
a[0]


# ### float( )
# * rules are similar to int

# In[13]:


# str to float
a = float(a)
print(type(a),a)


# In[19]:


# bool to float
a = True
a = float(a)
print(type(a),a)


# In[35]:


# int to float
a = 11
a = float(a)
print(type(a),a)


# In[87]:


# empty type to flot
a = None
a = float(a)
print(type(a),a) #TypeError


# In[88]:


# list to int
a = [1]
a = int(a)
print(type(a),a )# TypeError


# In[89]:


a = {'key1':123}
a = float(a) 
print(type(a),a) #TypeError


# # Mutable vs Inmutable?

# ### Mutable
# 
# * List
# * Dictionary
# * Set

# In[231]:


# List
List = [4,2,1,3,4]
print(type(List),List)

List[0]

List[0]=99999
List # 1st element changed

# More expample check List chapter


# In[120]:


# Dictonary

Dictonary = {'key1':1,
             'key2':'value2',
             'key3':False,
             3:3,
             123.3:123.3,
             True:False,
             None:'not None',
             4:None,
             5:[12,32]
            }

Dictonary[None] = 'now it changed to None'
Dictonary[None]


# In[232]:


# Set
a = {4,2,1,3,4}
a.pop()
a


# ### Inmutable
# * Numeric(int/float/complex)
# * Boolean
# * String
# * Tuple；

# In[235]:


a = '123'
a[1]
a[1]='1'


# In[237]:


a = (1,2,3)
a[1]
a[1]= 1


# In[238]:


a = True
# you can assign a to a new value
a = False
a[1] # but you can not indexing or slicing


# In[239]:


# same as boolean
a = 123
a[1]


# In[27]:


print('code lines 264' )


# In[ ]:




