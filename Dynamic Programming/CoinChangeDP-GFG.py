'''
Question : Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin. And you can use any coin as many times as you want.
'''
#Reference Link : https://www.geeksforgeeks.org/coin-change-dp-7/

#TC : O(N*Sum)
#SC : O(Sum)

#User function Template for python3

class Solution:
    def count(self, coins, N, Sum):
        # code here 
        dp = [0] * (Sum+1)
        dp[0] = 1 #With sum 0 there is one way 
        
        #For every coin, go through different sum values.
        for i in range(0,N):
            for j in range(coins[i],Sum+1):
                dp[j] += dp[j-coins[i]]
        
        return dp[Sum]

'''
Sample Test cases :
Input:
N = 3, sum = 4
coins = {1,2,3}
Output: 4
Explanation: Four Possible ways are: {1,1,1,1},{1,1,2},{2,2},{1,3}.
'''
