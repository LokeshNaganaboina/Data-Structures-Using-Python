'''
Question : Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. 
Return 1 if the number is Perfect otherwise return 0.

Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)

Sample Test cases :
Example 1:

Input:
N = 6
Output:
1 
Explanation:
Factors of 6 are 1, 2, 3 and 6.
Excluding 6 their sum is 6 which
is equal to N itself. So, it's a
Perfect Number.
Example 2:

Input:
N = 10
Output:
0
Explanation:
Factors of 10 are 1, 2, 5 and 10.
Excluding 10 their sum is 8 which
is not equal to N itself. So, it's
not a Perfect Number.
'''

#Code:
#User function Template for python3
import math
class Solution:
    def isPerfectNumber(self, N):
        # code here 
        def factorsSum(N):
            i=2
            factSum = 1
            while i <= math.sqrt(N):
                if N%i == 0:
                    if N//i == i:
                        factSum += i
                    else:
                        factSum += i
                        factSum += N//i
                i += 1
            return factSum
            
        if N>1 and N == factorsSum(N):
            return 1
        else:
            return 0
