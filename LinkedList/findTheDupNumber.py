# Leetcode problem 287: https://leetcode.com/problems/find-the-duplicate-number/description/

# Time: O(N)
# Space: O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        # find the cycle 
        while True:
            slow = nums[slow] # 
            fast_pos1 = nums[fast] # 
            fast = nums[fast_pos1] # 
            if slow == fast:
                break
        # locate the entrance of the cycle 
        new = nums[0]
        while nums[slow] != new:
            slow = nums[slow]
            new = nums[new]

        return new