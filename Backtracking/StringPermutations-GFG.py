# Question : Given a string S. The task is to find all permutations (need not be different) of a given string.

#Difficulty : Easy
#TC : O(n * n!)
#SC : O(n)

class Solution:
    def permutation(self,s):
        list1 = []
        def permute(s,start,end):
            if start == end:
                list1.append(''.join(s))
            else:
                for i in range(start,end):
                    s[start],s[i] = s[i], s[start]
                    permute(s,start+1,end)
                    s[start],s[i] = s[i], s[start] #Backtrack
                    
        s = list(s)
        permute(s,0,len(s))
        return sorted(list1) #Lexicographic order

''' Sample Test case :
Example 1:

Input:
S = AAA
Output: AAA AAA AAA AAA AAA AAA
Explanation: There are total 6 permutations, as given in the output.
'''
