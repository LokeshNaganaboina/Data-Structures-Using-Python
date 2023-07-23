#User function Template for python3

'''Question:

You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset 
is smaller than or equal to W. You cannot break an item, either pick the complete item or dont pick it (0-1 property).
'''

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        #Initialise a 2D array where rows belong to n items and columns belong to capacity
        dp = [[0] * (W + 1) for _ in range(n + 1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1] > j: # Exclude the current item
                    dp[i][j] = dp[i-1][j]
                else: # Calculate the maximum value by either including or excluding the current item
                    dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]] , dp[i-1][j])
        # Return the maximum value that can be put in the knapsack of capacity W
        return dp[n][W]

'''Sample Test Cases

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Example 2:

Input:
N = 3
W = 3
values[] = {1,2,3}
weight[] = {4,5,6}
Output: 0
'''