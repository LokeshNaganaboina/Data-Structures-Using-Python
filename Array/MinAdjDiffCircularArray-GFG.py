#Question : Given an array Arr of n integers arranged in a circular fashion. Your task is to find the minimum absolute difference between adjacent elements.

#Diffivulty : Easy 
#TC : O(n)
#SC : O(1)

#Code :
#User function Template for python3

class Solution:
    #Complete this function
    #Function to find minimum adjacent difference in a circular array.
    def minAdjDiff(self,arr, n):
        ##Your code here
        min1 = 10000
        for i in range(1,len(arr)):
            min1 = min(min1, abs(arr[i]-arr[i-1]))
        min1 = min(min1,abs(arr[n-1]-arr[0]))
        return min1

'''
Sample Test cases :
Input:
n = 7
Arr[] = {8,-8,9,-9,10,-11,12}
Output: 4
Explanation: The absolute difference 
between adjacent elements in the given 
array are as such: 16 17 18  19 21 23 4
(first and last). Among the calculated 
absolute difference the minimum is 4.
'''
