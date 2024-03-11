# Lintcode problem 521: https://www.lintcode.com/problem/521/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    """
                     i
     [1, 2, 3, 4, 3, 4]
                  j
    """
    def deduplication(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j 