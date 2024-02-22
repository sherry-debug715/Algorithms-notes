from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return [] 

        self.quickSelect(0, len(nums) - 1, nums, k)
        res = nums[:k]
        res.sort(reverse = True)
        return res

    
    def quickSelect(self, start, end, nums, k):
        if start >= end:
            return 
        l, r = start, end
        pivot = nums[(l + r) // 2]
        while l <= r:
            while l <= r and  nums[l] > pivot:
                l += 1
            while l <= r and  nums[r] < pivot:
                r -= 1 
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        if start + k - 1 >= l:
            return self.quickSelect(l, end, nums, k -  (l - start))
        if start + k - 1 <= r:
            return self.quickSelect(start, r, nums, k)

# start == 0
# end = 9
# k == 10

#             l                   
#           m
# [7,10,9,8,6,5,4,3,2,1]
#           r