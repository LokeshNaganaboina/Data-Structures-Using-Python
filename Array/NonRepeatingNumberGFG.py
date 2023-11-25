'''Question : Given an array A containing 2*N+2 positive numbers, out of which 2*N numbers exist in pairs whereas the other two number 
occur exactly once and are distinct. Find the other two numbers. Return in increasing order. '''

#Difficulty : Medium
#TC : O(n)
#SC : O(1)

#User function Template for python3

#Reference Link : https://www.youtube.com/watch?v=jPUMHoaiX60
#Use Xor operation , xor of two same numbers is 0, 
#xor of a number with zero is zero itself

class Solution:
	def singleNumber(self, nums):
		# Code here
		ans = []
		res = 0 
		
		for i in range(len(nums)):
		    res ^= nums[i] # sum of two distinct numbers
		    
		#Extract the last bit that is set to 1 of resulted sum
		res = res & ~(res-1)
		number1 = 0
		number2 = 0
		
		for i in range(len(nums)):
		    if res & nums[i]: #bit that results 1
		        number1 ^= nums[i]
		    else: #bit that results 0
		        number2 ^= nums[i]
		
		ans.append(number1)
		ans.append(number2)
		
		return sorted(ans)
        
'''
Sample Test case : 
Example 1:

Input: 
N = 2
arr[] = {1, 2, 3, 2, 1, 4}
Output:
3 4 
Explanation:
3 and 4 occur exactly once.
'''