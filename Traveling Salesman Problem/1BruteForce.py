from typing import (
    List,
)


class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    # form adjacency list from roads. 
    # dfs traverse through the adjacency list compare costs
    # return the min cost 
    # the graph is undirected.
    def __init__(self):
        self.minCost = float("inf")

    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        neighbors = self.find_neighbors(n, roads) 
        self.dfs(n, neighbors, 0, 1, {1})
        return self.minCost
    
    def dfs(self, num_city, neighbors, cur_cost, next_city, visited):
        if len(visited) == num_city:
            self.minCost = min(cur_cost, self.minCost) 
            return
        
        for city in neighbors[next_city]:
            if city in visited:
                continue 
            
            visited.add(city)
            self.dfs(num_city, neighbors, cur_cost + neighbors[next_city][city], city, visited)
            visited.remove(city) 
    
    def find_neighbors(self, num_city, roads):
        neighbors = {
            i: {} for i in range(1, num_city + 1)
        } 

        for city1, city2, cost in roads:
            if city1 not in neighbors[city2]:
                neighbors[city2][city1] = cost
            else:
                neighbors[city2][city1] = min(neighbors[city2][city1], cost)

            if city2 not in neighbors[city1]:
                neighbors[city1][city2] = cost
            else:
                neighbors[city1][city2] = min(neighbors[city1][city2], cost)
        
        return neighbors 

# for i in range(1, 7):

# i == 1
# if g[path[0]][path[1]] + g[path[-1]][8] > g[path[0][path[-1]]] + graph[path[1]][8]

# check if 1->2 + 7->8 > 1->7 + 2->8