'''
Question:
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct 
combinations to reach the given score.

Difficulty Level: Easy
'''

#Code:
class Solution:
    def count(self, n: int) -> int:
        #your code here
        scores = [3,5,10]
        dp = [0]*(n+1)
        dp[0] = 1 # There is atleast one way to reach score 0
        
        for score in scores:
            for i in range(score,n+1):
                dp[i]+=dp[i-score]
        
        return dp[n]

'''
Sample Test Cases:

Example 1:

Input
n = 10
Output
2
Explanation
There are two ways {5,5} and {10}.
Example 2:

Input
n = 20
Output
4
Explanation
There are four possible ways. {5,5,5,5}, {3,3,3,3,3,5}, {10,10}, {5,5,10}.

'''
