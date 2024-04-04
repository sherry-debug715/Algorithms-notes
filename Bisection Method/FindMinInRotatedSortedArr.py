# Leetcode problem 153: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Time: O(logN) where N is the length of input nums
# Space: O(1) 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid 
        return min(nums[left], nums[right])

#  if nums[m] > nums[l]:
#     if nums[m] < nums[r]:
#       m is in the rotated portion
#       l = m
#     else:
#.      m is in the non rotated portion
#.      r = m
#  else:
#.    if nums[m] > nums[r]:
#.       m is in the rotated portion
#.       l = m
#.    else:
#       m is in the non rotated portion
#       r = m

