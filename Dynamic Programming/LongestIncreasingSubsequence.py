#User function Template for python3

#Question : Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

#References: https://www.youtube.com/watch?v=on2hvxBXJH4 Using Binary Search

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        
        '''since the output is in sorted form, we will use binary search to insert 
        an element when it is smaller than output[-1],
        we will replace it with the element in output which is just greater than a[i] 
        
        Note : the array that gets returned has one of the subsequence 
        not the exact subsequence'''
        
        output = [a[0]]
        
        for i in range(1,n):
            
            if a[i] > output[-1]:
                output.append(a[i])
            else:
                #Look for the element that is just above a[i] in output and replace it
                #with that element
                left, right = 0, len(output)-1
                
                while left <= right:
                    mid = (left + right) // 2
                    if output[mid] > a[i]:
                        right = mid-1
                    else:
                        left = mid+1
                
                output[left] = a[i]
        
        #Return the length of one of the longest common subsequence
        return len(output)
        
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