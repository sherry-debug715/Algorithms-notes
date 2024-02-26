# Lintcode problem 545: https://www.lintcode.com/problem/545/description?fromId=161&_from=collection

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.nums = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        self.nums.append(num)

    """
    @return: Top k element
    """
    def topk(self):
        if not self.nums:
            return []
        
        self.quick_select(0, len(self.nums) - 1, self.k)
        res = self.nums[:self.k]
        res.sort(reverse = True)
        return res
    
    def quick_select(self, start, end, curK):

        if start >= end:
            return
        left, right = start, end
        mid = self.nums[(left + right) // 2]

        while left <= right:
            while left <= right and self.nums[left] > mid:
                left += 1
            while left <= right and self.nums[right] < mid:
                right -= 1 
            if left <= right:
                self.nums[left], self.nums[right] = self.nums[right], self.nums[left] 
                left += 1
                right -= 1
        
        if start + curK - 1 <= right:
            return self.quick_select(start, right, curK)
        if start + curK - 1 >= left:
            return self.quick_select(left, end, curK - left + start) 
