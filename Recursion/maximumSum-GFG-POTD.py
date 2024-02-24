'''
Question: A number n can be broken into three parts n/2, n/3, and n/4 (consider only the integer part). Each number obtained in 
this process can be divided further recursively. Find the maximum sum that can be obtained by summing up the divided parts 
together.

Note: It is possible that we don't divide the number at all.

Time Complexity: O(n)
Space Complexity: O(n)
'''

#Code:
class Solution:
    def maxSum(self, n): 
        # code here
        memo = {}
        if n in memo:
            return memo[n]
        
        if n < 12:
            return n
        
        memo[n] = max(self.maxSum(n//2) + self.maxSum(n//3) + self.maxSum(n//4), n)
        return memo[n]

'''
Sample Test Cases:

Example 1:

Input:
n = 12
Output: 
13
Explanation: 
Break n = 12 in three parts {12/2, 12/3, 12/4} = {6, 4, 3}, now current sum is = (6 + 4 + 3) = 13. 
Further breaking 6, 4 and 3 into parts will produce sum less than or equal to 6, 4 and 3 respectively.

Example 2:

Input:
n = 24
Output: 
27
Explanation: 
Break n = 24 in three parts {24/2, 24/3, 24/4} = {12, 8, 6}, now current sum is = (12 + 8 + 6) = 26. 
But recursively breaking 12 would produce value 13. So our maximum sum is 13 + 8 + 6 = 27.
'''
