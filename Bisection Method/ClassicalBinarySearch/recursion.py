class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        return self.binary_search(0, len(nums) - 1, target, nums) 
    
    def binary_search(self, start, end, target, nums):
        if start > end:
            return -1 
        
        if start == end:
            if nums[start] == target:
                return start 
            else:
                return -1
        
        mid = (start + end) // 2 
        if nums[mid] == target:
            return mid 
        elif nums[mid] > target: # left 
            return self.binary_search(start, mid - 1, target, nums) 
        else:
            return self.binary_search(mid + 1, end, target, nums) 
        
        