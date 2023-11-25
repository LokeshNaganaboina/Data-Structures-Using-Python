'''
Question : 
Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

TC : O(logn)
SC : O(1) '''

#Code:
#User function Template for python3
class Solution:

    def count(self,arr, n, x):
        # code here
        #first occuring index of a given element
        def firstOccurence(arr,n,x):
            left,right = 0,len(arr)-1
            index = n
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] >= x:
                    index =  mid
                    right = mid-1
                else:
                    left = mid+1
            return index

        #last occuring index of a given element
        def lastOccurence(arr,n,x):
            left,right = 0,len(arr)-1
            index = n
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] > x:
                    index = mid
                    right = mid-1
                else:
                    left = mid+1
        
            return index-1
             
        low = firstOccurence(arr,n,x)
        if low==n or arr[low]!=x:
            count = 0
        else:
            count = lastOccurence(arr,n,x) - firstOccurence(arr,n,x) + 1
        
        return count

'''
Sample Test Cases:
Example 1:
Input:
N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 4
Explanation: 2 occurs 4 times in the
given array.

Example 2:

Input:
N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
Output: 0
Explanation: 4 is not present in the
given array.
'''
