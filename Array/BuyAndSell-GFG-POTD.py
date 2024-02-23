'''
In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make 
at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). 
The stock prices throughout the day are represented in the form of an array of prices. 
Given an array price of size n, find out the maximum profit that a share trader could have made.

Time Complexity : O(n)
Space Complexity : O(n)
'''

#Code:
class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        if n < 2:
            return 0
            
        #Array to store max profit after each day
        profit1 = [0] * n
        profit2 = [0] * n
        
        #First pass: forward pass to get the min price
        min_price = price[0]
        for i in range(1,n):
            min_price = min(min_price, price[i])
            profit1[i] = max(profit1[i-1], price[i]-min_price)
            
        #Second pass: Backward pass to get the max price
        max_price = price[-1]
        for i in range(n-2,-1,-1):
            max_price = max(max_price, price[i])
            profit2[i] = max(profit2[i+1], max_price - price[i])
        
        #Finding the max profit at atmost 2 transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, profit1[i] + profit2[i])
            
        return max_profit


'''
Sample test case:

Example 1:

Input:
n = 6
prices[] = {10,22,5,75,65,80}
Output:
87
Explanation:
Trader earns 87 as sum of 12, 75 Buy at 10, sell at 22, Buy at 5 and sell at 80.
Example 2:

Input:
n = 7
prices[] = {2,30,15,10,8,25,80}
Output:
100
Explanation:
Trader earns 100 as sum of 28 and 72 Buy at price 2, sell at 30, Buy at 8 and sell at 80,
'''
