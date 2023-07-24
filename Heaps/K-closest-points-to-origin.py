# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# https://leetcode.com/problems/k-closest-points-to-origin/description/

# Example:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # since we are returning the k closest coordinates to the origin of [0,0]
        # we can create a min-heap, ordered by the distance of each coordinates to the origin of [0,0], math.sqrt( (x-0)^2 + (y-0)^2 ), since we are only using the distance as a measurement to order points list into a min-heap, math.sqrt(x) is always > math.sqrt(y) if x > 0 and y > 0 and x > y

        for p in points:
            [x, y] = p
            # compute the distance to the origin, none sqaure root value 
            distance = x**2 + y**2
            p.insert(0, distance)

        heapq.heapify(points)

        res = []
        for n in range(k):
            cur_points = heapq.heappop(points)
            cur_points.pop(0)
            res.append(cur_points)

        # print("points", points)
        return res

