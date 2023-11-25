'''
Question : 
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements
to its right side. The rightmost element is always a leader. '''

'''
Code :
class Solution:

    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        leader_arr = []
        leader = A[N-1] #Right most is always a leader
        leader_arr.append(leader)
        
        for i in range(N-2,-1,-1):
            if A[i] >= leader:
                leader = A[i]
                leader_arr.append(leader)
                
        leader_arr.reverse()
        return leader_arr
'''

'''
Sample Test cases :
Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
'''
