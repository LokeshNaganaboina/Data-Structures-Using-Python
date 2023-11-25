#User function Template for python3

class Solution:
    #Function to find the nth fibonacci number using top-down approach.
    def findNthFibonacci(self,number, dp):
        # Your Code Here
        #Memoization technique 
        #It uses Top Down approach
        #Memoization uses recursion to compute overlapping sub problems
        
        if dp[number] == 0:
            if number<=2: #Base case
                return dp[number]
            else:
                res = self.findNthFibonacci(number-1,dp) + self.findNthFibonacci(number-2,dp)
                dp[number] = res
        return dp[number] 
            