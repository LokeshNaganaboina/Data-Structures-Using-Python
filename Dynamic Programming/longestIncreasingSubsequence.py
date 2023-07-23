#User function Template for python3

#Question : Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        
        '''since the dp is in sorted form, we will use binary search to insert 
        an element when it is smaller than dp[-1],
        we will replace it with the element in dp which is just greater than a[i] 
        
        Note : the array that gets returned has one of the subsequence 
        not the exact subsequence'''
        
        dp = [a[0]]
        
        for i in range(1,n):
            
            if a[i] > dp[-1]:
                dp.append(a[i])
            else:
                #Look for the element that is just above a[i] in dp and replace it
                #with that element
                left, right = 0, len(dp)-1
                
                while left <= right:
                    mid = (left + right) // 2
                    if dp[mid] > a[i]:
                        right = mid-1
                    else:
                        left = mid+1
                
                dp[left] = a[i]
        
        #Return the length of one of the longest common subsequence
        return len(dp)
        
'''
Test Cases :

1.
Input:
N = 16
A = {0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15}
Output: 
6
Explanation:
There are more than one LIS in this array. One such Longest increasing subsequence is {0,2,6,9,13,15}.

2.

Input:
N = 6
A[] = {5,8,3,7,9,1}
Output: 
3
Explanation:
There are more than one LIS in this array.  One such Longest increasing subsequence is {5,7,9}.

'''
