'''
Question:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
'''

'''
Algorithm:

1. Initialize an empty string "filtered-string"
2. For each character in the given string, check if it is alpha-numeric or not and if it is alpha-num, convert
   it to lower case and add it to the filtered-string.
3. Check if filtered-string is same as the reversed string
'''

#Code:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char.lower() for char in s if char.isalnum())
        return True if new_string == new_string[::-1] else False

'''
Sample Test cases:

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:
'''
