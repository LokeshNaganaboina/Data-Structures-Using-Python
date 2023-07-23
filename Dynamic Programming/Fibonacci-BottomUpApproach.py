#User function Template for python3

'''Question:
One of the rudimentary problems to understand DP is finding the nth Fibonacci number. Here, we will solve the problem using a bottom-up approach.
You are given a number N. You need to find the Nth Fibonacci number. The first two number of the series are 1 and 1.
'''

class Solution:
    #Function to find the nth fibonacci number using bottom-up approach.
    def findNthFibonacci(self,number):
        # Your Code Here
        #Tabulatiom technique 
        #It uses Bottom Up approach
        #Tabulation uses array or table to compute overlapping sub problems
        
        memo = [-1]* (number+1)
        memo[0] = 0
        memo[1] = 1
        
        for i in range(2,number+1):
            memo[i] = memo[i-1] + memo[i-2]
            
        return memo[number]

'''
Sample Test Cases
Example 1:

Input:
N = 5
Output: 5
Example 2:

Input:
N = 7
Output: 13
Explanation: Some of the numbers of the
Fibonacci numbers are 1, 1, 2, 3, 5, 8,13
..... (N stars from 1).
'''