'''
Question: 
Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of 
k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the 
string. 
'''

#Code:

import heapq

class Solution:
    def minValue(self, s, k):
        # code here
        
        #counting the freq of each char in a string
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        #Initializing max heap (Min heap with negative counts)
        heap = [ -count for count in freq.values() ]
        heapq.heapify(heap)
        
        #Removing charcters 'k' times
        for i in range(k):
            if heap:
                #Pop the element with highest frequency, update its count 
                #and if it is not zero, push it back to the heap
                count = heapq.heappop(heap) + 1
                if count!=0:
                    heapq.heappush(heap,count)
                    
        value = sum(count ** 2 for count in heap)
        
        return value
      
'''
Sample Test cases:

Example 1:

Input: 
s = abccc, k = 1
Output: 
6
Explaination:
We remove c to get the value as 12 + 12 + 22

Example 2:

Input: 
s = aabcbcbcabcc, k = 3
Output: 
27
Explaination: 
We remove two 'c' and one 'b'. Now we get the value as 32 + 32 + 32.
'''
