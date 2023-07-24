# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        diff = len(nums) - k
        for n in range(diff):
            cur = heapq.heappop(nums)
        return nums[0]