from typing import (
    List,
)
from lintcode import (
    Point,
)

import math, heapq
"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        x2, y2 = origin.x, origin.y

        min_distance = []
        heapq.heapify(min_distance)
        # res = []

        for point in points: # O(nlogn)
            x1, y1 = point.x, point.y
            euclidean = -self.distance(x1, x2, y1, y2)
            heapq.heappush(min_distance, (euclidean, -x1, -y1, point))
            if len(min_distance) > k:
                heapq.heappop(min_distance)

        # for _ in range(len(min_distance)):
        #     _,_,_,point = heapq.heappop(min_distance)
        #     res.append(point)
        # return res[::-1]
        return [heapq.heappop(min_distance)[3] for _ in range(len(min_distance))][::-1]
    
    def distance(self, x1, x2, y1, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

