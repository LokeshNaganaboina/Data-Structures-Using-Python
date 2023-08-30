# Question : Given a singly linked list and an integer x.Delete xth node from the singly linked list.

# your task is to complete this function
# function should return new head pointer

#Code : 

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    
    if head is None:
        return None
    
    if k==1:
        head = head.next
        return head
        
        
    prev = head
    curr = head
    count = 1
    
    while count < k and curr.next:
        count+=1
        prev = curr
        curr = curr.next
    
    prev.next = curr.next

'''
Example 1:

Input: 1 -> 3 -> 4 
       x = 3
Output: 1 -> 3
Explanation:
After deleting the node at 3rd
position (1-base indexing), the
linked list is as 1 -> 3. 

Example 2:

Input: 1 -> 5 -> 2 -> 9 
x = 2
Output: 1 -> 2 -> 9
Explanation: 
After deleting the node at 2nd
position (1-based indexing), the
linked list is as 1 -> 2 -> 9.
'''
    return head
