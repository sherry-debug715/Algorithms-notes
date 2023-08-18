class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1 

        while start < end: 
            mid = (start + end) // 2 
            if nums[mid] < target: 
                start = mid + 1 
                continue 
            if nums[mid] > target:
                end = mid - 1
                continue 
            return mid

        if start < len(nums) and nums[start] == target:
            return start 
        return -1 