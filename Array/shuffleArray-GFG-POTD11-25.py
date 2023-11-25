#GFG POTD - 11/25/2023
'''Question:
Given an array arr of n elements in the following format {a1, a2, a3, a4, ... , an/2, b1, b2, b3, b4, ... , bn/2}, the task is shuffle the array to {a1, b1, a2, b2, a3, b3, ... , an/2, bn/2} without using extra space.
Note that n is even.

Example Testcases:
Example 1:

Input: 
n = 4, arr = {1, 2, 9, 15}
Output:  
1 9 2 15
Explanation: 
a1=1, a2=2, b1=9, b2=15. So the final array will be: a1, b1, a2, b2 = {1,9,2,15}.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
'''
'''
Logic :
Two numbers x and y are combined into a single number z using the formula z = x * mx + y, 
where mx is a large number ensuring that x and y don't interfere with each other.

x and y can be retrieved from z by x = z / mx and y = z % mx.
'''

class Solution:
    def shuffleArray(self, arr, n):
    # Function to calculate the new position
        mx = 10000  # Equivalent to 1e4
        start, end = 1, n // 2
    
        # First pass: Combine two elements into one
        for i in range(1, n):
            if i % 2 == 1:  # Odd index
                arr[i] = (arr[end] % mx) * mx + (arr[i] % mx)
                end += 1
            else:  # Even index
                arr[i] = (arr[start] % mx) * mx + (arr[i] % mx)
                start += 1
    
        # Second pass: Separate the combined elements
        for i in range(1, n):
            arr[i] //= mx
            
        return arr