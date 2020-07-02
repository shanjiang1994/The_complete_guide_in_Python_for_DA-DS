#!/usr/bin/env python
# coding: utf-8

# # Two Sum

# In[21]:


# Question
# Check full description of question from LeetCode
nums = [2, 7, 11, 15]
target = 9 


# In[22]:


# Brute Force ----- O(N^2)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print([i,j])


# In[23]:


# Hash Map ----- O(N)
dct = {}
for i, n in enumerate(nums):
    if target - n in dct:
        print([dct[target - n], i]) 
    dct[n] = i
    


# # Merge Two Sorted Lists

# In[55]:


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# In[56]:


L1 = [1,2,4]
l1 = ListNode(L1)
L2 = [1,3,4]
l2 = ListNode(L2)


# In[57]:


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    curr = dummy = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
            
    curr.next = l1 or l2
    return(dummy.next)


# In[58]:


mergeTwoLists(l1,l2)


# In[1]:


get_ipython().run_cell_magic('', 'pixie_debugger', '')


# In[ ]:




