'''
Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers.
'''
#Expected Time Complexity: O(n1* n2)
#Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        def getNumber(s1):
            number = 0
            isNegative = False
            i = 0
            
            if s1[0]=='-':
                isNegative = True
                i+=1
            
            while i < len(s1):
                number = number*10 + ord(s1[i])-ord('0')
                i+=1
                
            if isNegative:
                number = -number
            
            return number
            
        num1 = getNumber(s1)
        num2 = getNumber(s2)
                
        return num1*num2


'''
Sample Test cases :
Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66
Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253
'''


Constraints:
1 ≤ length of s1 and s2 ≤ 103

