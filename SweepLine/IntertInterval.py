# Lintcode problem 57: https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            curInterval = intervals[i]
            # curInterval is before newInterval 
            if curInterval[0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            elif curInterval[1] < newInterval[0]: 
                output.append(curInterval)
            else:
                 newInterval[0] = min(curInterval[0], newInterval[0])
                 newInterval[1] = max(curInterval[1], newInterval[1])

        # if last interval from intervals is part of the newInterval
        # such as [[1,2],[3,5],[6,7],[8,10]], newInterval = [4, 8],
        # if the function doesn't return on line 9.
        output.append(newInterval)
        return output 
