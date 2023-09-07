from typing import (
    List,
)

class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def __init__(self):
        self.minCost = float("inf") 

    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        graph = self.find_neighbors(n, roads)
        self.dfs(n, roads, graph, [1], {1}, 1, 0)
        return self.minCost
    
    def dfs(self, num_city, roads, graph, path, visited, city, cost):
        if len(visited) == num_city:
            self.minCost = min(self.minCost, cost)
        
        for next_city in graph[city]:
            if next_city in visited:
                continue 
            if self.not_good_path(path, next_city, graph):
                continue 
            visited.add(next_city) 
            path.append(next_city)
            self.dfs(num_city, roads, graph, path, visited, next_city, cost + graph[city][next_city])
            visited.remove(next_city)
            path.pop()
        
    def not_good_path(self, path, new_city, graph):
        #     |
        # [1, 2, 3, 4, 5] -> city
        for i in range(1, len(path)):
            # using the above example, supposely i is 1
            # check if w(1 -> 2) + w(5 -> city) > w(1 -> 5) + w(3 -> city)
            # keep on checking as i increment, looking for cheaper way than adding city directly to the end of path, which is the left side logic. 
            if graph[path[i - 1]][path[i]] + graph[path[-1]][new_city] > graph[path[i - 1]][path[-1]] + graph[path[i]][new_city]:
                return True 
        return False

    def find_neighbors(self, num_city, roads):
        graph = {i: {j: float("inf") for j in range(1, num_city + 1)} for i in range(1, num_city + 1)} 

        for city1, city2, cost in roads:
            graph[city1][city2] = min(graph[city1][city2], cost)
            graph[city2][city1] = min(graph[city2][city1], cost)
            
        return graph

