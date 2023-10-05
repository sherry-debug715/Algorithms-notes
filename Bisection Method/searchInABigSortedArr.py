"""
LintCode problem 447: https://www.lintcode.com/problem/447/?fromId=161&_from=collection
"""

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # find the end pointer in the big array. 
        # end pointer start at 1, increment by end pointer * 2 each time 
        # check if big array[end_pointer] >= target: binary search 
        # else keep on incrementing 

        end = 1
        while reader.get(end) <= target:
            end *= 2
        
        return self.binary_search(0, end, reader, target)
    
    def binary_search(self, start, end, reader, target):
        if reader.get(start) == target:
            return start 
        
        while start + 1 < end:
            mid = (start + end) // 2 
            if reader.get(mid) < target:
                start = mid 
            else:
                end = mid 
        
        if reader.get(end) == target:
            return end 
        if reader.get(start) == target:
            return start 
        return -1
        