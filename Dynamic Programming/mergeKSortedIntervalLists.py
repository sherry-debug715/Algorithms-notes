# Lintcode problem 577: https://www.lintcode.com/problem/577/description?fromId=161&_from=collection

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    """
    首先，对于所有区间，按左端点从小到大排序。
    然后对所有区间依次进行处理，
    若答案序列为空 或者 答案序列的最后一个区间与当前区间无交点，压入当前序列；
    若答案序列的最后一个区间与当前区间有交点，则取二者右端点中较大的作为最后一个区间新的右端点。
           cur
  [(1,3),(1,2),(4,7),(6,8),(9,10)],
            prev
  output = [(1, 3), (4,8), (9,10)]
  Time: O(NlogN): sort function runs in O(NlogN) time
  Space: O(N)
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return [] 
        # iterate over intervals, and add all intervals into one list
        allIntervals = []
        output = []
        for row in range(len(intervals)):
            for interval in intervals[row]:
                allIntervals.append(interval) 
        
        # sort allIntervals by the start value of each interval 
        allIntervals.sort(key=lambda interval: interval.start)
        output.append(allIntervals[0]) 

        for idx in range(1, len(allIntervals)):
            prev_range = output[-1]
            cur_range = allIntervals[idx]
            # check if the interval overlap
            if prev_range.end < cur_range.start:
                output.append(cur_range)
            else:
                prev_range.start = min(prev_range.start, cur_range.start)
                prev_range.end = max(prev_range.end, cur_range.end)
                    
        
        return output 
