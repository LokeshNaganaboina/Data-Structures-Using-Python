'''
Question : Given n integer ranges, the task is to find the maximum occurring integer in these ranges. If more than one such integer exists, find the smallest one. The ranges are given as two arrays L[] and R[].  L[i] consists of starting point of range and R[i] consists of corresponding end point of the range.

For example consider the following ranges.
L[] = {2, 1, 3}, R[] = {5, 3, 9)
Ranges represented by above arrays are.
[2, 5] = {2, 3, 4, 5}
[1, 3] = {1, 2, 3}
[3, 9] = {3, 4, 5, 6, 7, 8, 9}
The maximum occurred integer in these ranges is 3.

'''
#Difficulty : Easy
#TC : O(n+maxx)
#SC : O(maxx)
#-maxx is maximum element in R[]


#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,L,R,N,maxx):
        ##Your code here
        
        # Create an array and initialize it with size (maxx+1)
        arr = [0] * (maxx + 2)

        # Run a loop from 0 to n-1 and update the endpoints
        for i in range(N):
            arr[L[i]] += 1
            arr[R[i] + 1] -= 1
            
        #Initialize the max_frequency element as 1st element of the array and 
        # initialize its index to max frequency index
        maximum = arr[0]
        res = 0
        for j in range(1, maxx + 2):
             #Prefix sum to get the frequency of array
            arr[j] += arr[j - 1]
            '''update the frequency of the element and compare with max freq 
        acheived till now'''
            if arr[j] > maximum:
                maximum = arr[j]
                res = j

        return res

'''
Sample Test case :
Input:
n = 4
L[] = {1,4,3,1}
R[] = {15,8,5,4}
Output: 4
Explanation: The given ranges are [1,15]
 [4, 8] [3, 5] [1, 4]. The number that 
is most common or appears most times in 
the ranges is 4.
'''
        
