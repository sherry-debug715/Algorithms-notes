# Lintcode problem 391: https://www.lintcode.com/problem/391/?showListFe=true&page=1&problemTypeId=2&tagIds=389&ordering=level&pageSize=50

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# Time: O(NlogN)
# Space: O(N)
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        time = []
        for interval in airplanes:
            time.append((interval.start, 1))
            time.append((interval.end, -1))
        # sort time list by taking off time, if same, sort by landing time.
        time.sort(key=lambda i : (i[0], i[1]))
        counter = 0
        flying = 0 

        for _, t in time:
            flying += t 
            counter = max(counter, flying)
        
        return counter
