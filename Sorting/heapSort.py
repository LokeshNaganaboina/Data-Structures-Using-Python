'''Question : 
Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() which are used to implement Heap Sort.
'''

#User function Template for python3
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        #Makes sure that parent is the largest
        largest,left,right = i, 2*i+1, 2*i+2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[largest],arr[i] = arr[i], arr[largest]
            self.heapify(arr,n,largest)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        #Check from last internal node
        for i in range( n-2 //2 , -1, -1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        #Swap first with last and call for n-1 nodes until root node
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr,i,0)

'''
Sample Test cases :
Example 1:

Input:
N = 5
arr[] = {4,1,3,9,7}
Output:
1 3 4 7 9
Explanation:
After sorting elements
using heap sort, elements will be
in order as 1,3,4,7,9.
'''
            
