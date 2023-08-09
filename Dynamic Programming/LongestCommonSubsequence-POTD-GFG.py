#Given two strings, find the length of longest subsequence present in both of them. Both strings are in uppercase Latin alphabets.

#Code :
#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        #Using Tabulation
        # code here

        dp = [[-1] * (y + 1) for _ in range(x + 1)]

        # dp[i][j] is the length of LCS of s1 till i-1 and s2 till j-1
        for i in range(x + 1):
            dp[i][0] = 0  # Fill first column with zero

        for j in range(y + 1):
            dp[0][j] = 0  # Fill first row with zero

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1] #Add diagonal
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) #Max of previous row or col

        return dp[x][y]

''' 
TC : O(len(s1) * len(s2))
SC : O(len(s1) * len(s2))

Sample Test cases :- 
Example 1: 

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input strings “ABCDGH” and “AEDFHR” is “ADH” of length 3.
'''
        
