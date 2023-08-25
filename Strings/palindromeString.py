'''
Question : 
Given a string S, check if it is palindrome or not.

Expected Time Complexity: O (Length of S)
Expected Auxiliary Space: O(1)
'''

class Solution:
	def isPalindrome(self, S):
		# code here
		n = len(S)
		j = n-1
		isPalindrome = True
		for i in range(0,n//2):
		    if S[i]!=S[j]:
		        isPalindrome = False
		        break
		    j-=1
		            
		return 1 if isPalindrome else 0

'''
Sample test cases :
Example 1:

Input: S = "abba"
Output: 1
Explanation: S is a palindrome
Example 2:

Input: S = "abc" 
Output: 0
Explanation: S is not a palindrome
'''
