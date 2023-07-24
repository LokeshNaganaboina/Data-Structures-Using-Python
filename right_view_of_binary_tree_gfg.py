#Question :
'''Given a Binary Tree, find Right view of it. Right view of a Binary Tree is set of nodes visible when tree is viewed from right side.

Right view of following tree is 1 3 7 8.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8
    '''

class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        # code here
        #For each level get the last node of that level and add it to result.
        
        queue = deque([root])
        result = []
        
        while queue:
            #For each level
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            #At the end of level after adding it to result mark the right node null to 
            #get the next level right most node
            if rightNode:
                result.append(rightNode.data)
                rightNode = None
            
        return result

#Sample Test Cases:
'''Example 1:

Input:
       1
    /    \
   3      2
Output: 1 2'''
