#User function Template for python3

'''Question :

You are given an amount denoted by value. You are also given an array of coins. The array contains the denominations of the given coins.
You need to find the minimum number of coins to make the change for value using the coins of given denominations. Also, keep in mind that you have 
infinite supply of the coins.
'''

class Solution:
    #Function to find the minimum number of coins to make the change 
    #for value using the coins of given denominations.
    def minimumNumberOfCoins(self,coins,numberOfCoins,value):
        # your code here
        #Using Tabulation method (Bottom UP)
        minCoins = [float('inf')] * (value+1)
        minCoins[0] = 0 #Array of value+1 size
        #At each index value we have min number of coins for each index
        
        #For each index calculate min no of coins
        for i in range(1,value+1):
            for j in range(numberOfCoins):
                
                if coins[j] <= i:
                    sub = i - coins[j]
                    if minCoins[sub]!=float('inf'):
                        ''' Calculate the minimum number of coins needed for value 'i'
        by comparing the current value with previously calculated
        solution for 'sub' and adding 1 for the current coin used. '''
                        minCoins[i] = min(minCoins[i],minCoins[sub]+1)
                
        if minCoins[value] != float('inf'):
            ''' If minCoins[value] is not infinity, it means it's possible to make change
        for the given value using the available coin denominations. '''
            return minCoins[value]
        else:
            return -1
            
'''Sample Test Cases

Example 1:

Input:
value = 5
numberOfCoins = 3
coins[] = {3,6,3}
Output: Not Possible
Explanation:We need to make the change for
value = 5 The denominations are {3,6,3}
It is certain that we cannot make 5 using
any of these coins.
Example 2:

Input:
value = 10
numberOfCoins = 4
coins[] = {2 5 3 6}
Output: 2
Explanation:We need to make the change for
value = 10 The denominations are {2,5,3,6}
We can use two 5 coins to make 10. So
minimum coins are 2.

'''
        