'''Question : You are given a connected undirected graph. Perform a Depth First Traversal of the graph. '''

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [False]*V
        result = []
        
        def dfs(v):
            visited[v] = True
            result.append(v)
            
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        #For disconnected graph
        for v in range(V):
            if not visited[v]:
                dfs(v)
        
        return result

''' Sample Test cases :
Input: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]

Output: 0 2 4 3 1
Explanation: 
0 is connected to 2, 3, 1.
1 is connected to 0.
2 is connected to 0 and 4.
3 is connected to 0.
4 is connected to 2.
so starting from 0, it will go to 2 then 4,
and then 3 and 1.
Thus dfs will be 0 2 4 3 1.
'''
        
