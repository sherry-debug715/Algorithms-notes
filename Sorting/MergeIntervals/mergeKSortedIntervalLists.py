# Lintcode problem 577: https://www.lintcode.com/problem/577/

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return [] 

        res = []
        # construct heap by adding the first element from each sub array to heap
        heap = []
        for idx, arr in enumerate(intervals):
            if arr:
                heapq.heappush(heap, (arr[0].start, arr[0].end, idx, 0)) 
        
        while heap:
            start, end, arrIdx, val_idx = heapq.heappop(heap)
            self.push_back(res, intervals[arrIdx][val_idx])
            next_idx = val_idx + 1
            if next_idx < len(intervals[arrIdx]):
                next_interval = intervals[arrIdx][next_idx]
                heapq.heappush(heap, (next_interval.start, next_interval.end, arrIdx, next_idx)) 
        
        return res
    
    def push_back(self, res, interval):
        if not res:
            res.append(interval)
            return 

        prev = res[-1]
        if interval.start > prev.end:
            res.append(interval)
            return 
        
        prev.end = max(prev.end, interval.end)

