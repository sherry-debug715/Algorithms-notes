# Lintcode Problem 486: https://www.lintcode.com/problem/486/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    # Time: O(Nlogk) where N is the total number of integers across all arrays, and 
    # K is the number of input arrays. 
    def mergek_sorted_arrays(self, arrays: List[List[int]]) -> List[int]:
        if not arrays:
            return None 
        
        while len(arrays) != 1:
            merged_list = []
            for i in range(0, len(arrays), 2):
                list1 = arrays[i]
                list2 = arrays[i + 1] if i + 1 < len(arrays) else [] 
                merged_list.append(self.merge(list1, list2))
            arrays = merged_list 
        
        return arrays[0] 

    def merge(self, list1, list2):
        cur_list = []
        p1, p2 = 0, 0
        while p1 < len(list1) and p2 < len(list2):
            if list1[p1] < list2[p2]:
                cur_list.append(list1[p1])
                p1 += 1
            else:
                cur_list.append(list2[p2])
                p2 += 1
        
        if p1 == len(list1) and p2 < len(list2):
            for i in range(p2, len(list2)):
                cur_list.append(list2[i])
        elif p2 == len(list2) and p1 < len(list1):
            for i in range(p1, len(list1)):
                cur_list.append(list1[i])
        return cur_list
        
        

