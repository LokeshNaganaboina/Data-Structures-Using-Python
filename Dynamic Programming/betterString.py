'''
Better String

Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.

Example 1:

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 7 distinct subsequences whereas "ggg" have 4 distinct subsequences. 
Example 2:

Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence. 

'''

#Difficulty: Hard
#TC: O(n)
#SC: O(n)
#Code:

#User function Template for python3

class Solution:
    def countDistinctSubsequences(s):
        n = len(s)
        last = [-1] * 256  # Stores the last occurrence of characters
        dp = [0] * (n + 1) # dp[i] will store the count of distinct subsequences till s[i]
    
        dp[0] = 1  # An empty string has 1 subsequence
    
        for i in range(1, n + 1):
            dp[i] = 2 * dp[i - 1]  # If the current character hasn't appeared before
    
            if last[ord(s[i - 1])] != -1:
                dp[i] -= dp[last[ord(s[i - 1])]]  # Remove count of subsequences formed without the last occurrence of s[i]
    
            last[ord(s[i - 1])] = i - 1  # Update the last occurrence of s[i]
    
        return dp[n] - 1
    def betterString(self, str1, str2):
        # Code here
        count1 = Solution.countDistinctSubsequences(str1)
        count2 = Solution.countDistinctSubsequences(str2)
    
        if count1 == count2:
            return str1
        return str1 if count1 > count2 else str2