# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Strategy
# If ordering stones list from max to min, we will come across a performance problem where when x != y and we need to add a new weight (y-x) if y > x, (x-y) if x > y to the sorted list, which will create another O(n) operation.

# using a heap to maintain the order of list could reduce the operation to O(logn) time. 

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq doesn't come with a function that would convert a list to max-heap
        convert_stones = [ele*-1 for ele in stones]

        heapq.heapify(convert_stones)

        while len(convert_stones) > 1:
            x = -1 * heapq.heappop(convert_stones)
            y = -1 * heapq.heappop(convert_stones)
            if x != y:
                if x < y:
                    heapq.heappush(convert_stones, (y - x)*-1)
                elif x > y:
                    heapq.heappush(convert_stones, (x - y)*-1)
        
        if not convert_stones:
            return 0
        else:
            return -1 * convert_stones[0]