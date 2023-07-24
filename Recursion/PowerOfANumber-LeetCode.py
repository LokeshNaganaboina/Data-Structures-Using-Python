#Question : Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#TC : O(logn)
#SC : O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n==0:
                return 1
            if x==0:
                return 0
            
            result = helper(x, n//2)
            return result*result if n%2==0 else result*result*x

        output = helper(x,abs(n))
        return output if n>=0 else 1/output

'''Sample Test Case:
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000 '''
