'''
Question : 
Given a Binary Search Tree of size N, find the Median of its Node values.
'''
#TC : O(n)
#SC : O(n)

#Naive Approach:
#User function Template for python3

def findMedian(root):
    # code here
    #Get the array of elements
    def inOrder(node,elements):
        if node:
            inOrder(node.left,elements)
            elements.append(node.data)
            inOrder(node.right,elements)
    
    elements = []
    inOrder(root,elements)
    
    n = len(elements)
    if n%2 == 0: #For even length
        median_value =  (elements[n//2] + elements[n//2 - 1]) / 2
    #For odd length
    else:
        median_value = elements[n//2]
        
    if median_value == int(median_value):
        return int(median_value) #int
    return median_value #float

''' Sample Test cases :

Example 1:

Input:
       6
     /   \
   3      8   
 /  \    /  \
1    4  7    9
Output: 6
Explanation: Inorder of Given BST will be:
1, 3, 4, 6, 7, 8, 9. So, here median will 6.
'''
