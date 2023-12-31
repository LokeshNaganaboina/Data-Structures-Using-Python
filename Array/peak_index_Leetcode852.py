'''Question : An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1] '''


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right = 0, len(arr)-1
        while left < right:
            mid = (left+right) // 2
            if arr[mid] > arr[mid+1]: #descending peak
                right = mid  
            else: #ascending peak
                left = mid+1
        #return left or right
        return left 

'''
Sample Test cases:
Example 1:

Input: arr = [0,1,0]
Output: 1

Example 2:

Input: arr = [0,2,1,0]
Output: 1
'''
