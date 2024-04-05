# Leetcode problem 33: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m
                else:
                    r = m
            # right portion
            else:
                # [5, 0, 1, 3] target = 0 if mid is 2 
                if target < nums[m] or target > nums[r]:
                    r = m
                else:
                    l = m
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r 
        return -1