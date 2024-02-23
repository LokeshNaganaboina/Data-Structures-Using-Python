'''
Question 787. Cheapest Flights Within K Stops:

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] 
indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
If there is no such route, return -1.
'''

#Code:
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Initialize a dist array
        dist = [float('inf')]*n
        dist[src] = 0

        #Relax edges k+1 times
        for _ in range(k+1):
            temp = dist.copy()
            for u,v,w in flights:
                if dist[u] + w < temp[v]:
                    temp[v] = dist[u] + w
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1

'''
Sample Test Cases:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
'''
