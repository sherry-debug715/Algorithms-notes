# Lintcode problem 76: https://www.lintcode.com/problem/76/?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    """
    dp[i]表示以第i个数结尾的最长单增子序列有多长
                      i
    nums = [4,2,4,5,3,7]
                    j

                  i
    dp = [1,1,2,3,2,4]

    Time: O(N^2)
    Space: O(N)
    """
    def longest_increasing_subsequence(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n 

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)

