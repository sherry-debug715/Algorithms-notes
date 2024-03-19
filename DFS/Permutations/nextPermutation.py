# Lintcode problem 52: https://www.lintcode.com/problem/52/

from typing import (
    List,
)
"""
从末尾往左走，如果一直递增，例如 {...9,7,5} ，那么下一个排列一定会牵扯到左边更多的数，直到一个非递增数为止，例如 {...6,9,7,5} 。
对于原数组的变化就只到 6 这里，和左侧其他数再无关系。6 这个位置会变成6右侧所有数中比 6 大的最小的数，而 6 会进入最后 3 个数中，
且后 3 个数必是升序数组。

所以算法步骤如下:
从右往左遍历数组 nums，直到找到一个位置 i ，满足 nums[i] > nums[i - 1] 或者 i 为 0 。
i 不为 0 时，用j再次从右到左遍历 nums ，寻找第一个 nums[j] > nums[i - 1] 。而后交换 nums[j] 和 nums[i - 1] 。
注意，满足要求的 j 一定存在!! 且交换后 nums[i] 及右侧数组仍为降序数组。
最后: 将 nums[i] 及右侧的所有数组翻转，使其升序。
Q: i为0怎么办？
A: i为0说明整个数组是降序的，直接翻转整个数组即可。

Q: 有重复元素怎么办？
A: 在遍历时只要严格满足 nums[i] > nums[i - 1] 和 nums[j] > nums[i - 1] 就不会有问题。

Q: 元素过少是否要单独考虑？
A: 当元素个数小于等于1个时，可以直接返回。
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def next_permutation(self, nums: List[int]) -> List[int]:        
        n = len(nums)
        if n <= 1:
            return nums
        
        i = n - 1
        while i >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i != 0:        
            j = n - 1
            while j >= 0 and nums[j] <= nums[i - 1]:
                j -= 1 
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
        self.swap(nums, i, n - 1)
        return nums 
    
    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
