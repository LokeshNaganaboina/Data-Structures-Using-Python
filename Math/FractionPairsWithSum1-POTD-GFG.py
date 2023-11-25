#Question : Given a list of N fractions, represented as two lists numerator and denominator, the task is to determine the count of pairs of fractions whose sum equals 1.
'''
Difficulty : Medium
Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(N)
'''

#User function Template for python3

class Solution:
    #Find the gcd of numerator(x) and denominator(y) and reduce the fractions
    #For every pair x,y look for y-x,y such pairs in the frequency map
    
    def countFractions(self, n, numerator, denominator):
        # Your code here
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        fraction_pairs = set()
        count = 0
        freq = {}
        
        for i in range(n):
            #For every pair reduce it to simplified form
            gcd_val = gcd(numerator[i], denominator[i])
            num = numerator[i] // gcd_val
            den = denominator[i] // gcd_val
            
            re_num, re_den = den-num, den
            #If y-x,y pair exists in the freq table, add the freq to count
            if re_num in freq and re_den in freq[re_num]:
                count += freq[re_num][re_den]
        
            if num in freq:
                freq[num][den] = freq[num].get(den,0) + 1 #Previous occurence+1
            else:
                freq[num] = {den: 1} #First occurence
            
        return count

'''
Sample Test Case:

Example 1:

Input:
N = 4
numerator = [1, 2, 2, 8]
denominator = [2, 4, 6, 12]
Output:
2
Explanation:
Fractions 1/2 and 2/4 sum to 1. Similarly fractions 2/6 and 8/12 sum to 1. So there are 2 pairs of fractions which sum to 1.
'''
