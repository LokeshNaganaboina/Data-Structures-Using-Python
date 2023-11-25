'''Question :
Given a BST, and a reference to a Node x in the BST. Find the Inorder Successor of the given node in the BST.
'''

class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        current = root
        successor = None

        while current:
            if current.data > x.data:
                successor = current
                current = current.left
            else:
                current = current.right

        return successor

'''
Sample Test case:

Example 1:

Input:
      2
    /   \
   1     3
K(data of x) = 2
Output: 3 
Explanation: 
Inorder traversal : 1 2 3 
Hence, inorder successor of 2 is 3.
'''
