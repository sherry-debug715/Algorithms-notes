import heapq
class Solution:
    """
    @param: k: An integer
    """
    # Space: O(k)
    def __init__(self, k):
        self.nums = []
        self.k = k
        heapq.heapify(self.nums)

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num): # Time(O(logK))
        # check if capacity is below k
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num) 
            return 
        # else, compare the value of num to index0 of the self.nums, if it's bigger, 
        # remove the smallest number and insert num
        if self.nums[0] < num:
            heapq.heappushpop(self.nums, num)

    """
    @return: Top k element
    """
    def topk(self): # Time: O(KlogK)
        return sorted(self.nums, reverse = True)
