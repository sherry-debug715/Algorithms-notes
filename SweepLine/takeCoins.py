# Lintcode problem 1399: https://www.lintcode.com/problem/1399/?showListFe=true&page=1&problemTypeId=2&tagIds=389&ordering=level&pageSize=50

from typing import (
    List,
)

class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    # Time: O(N)
    # Space: O(N)
    def take_coins(self, list: List[int], k: int) -> int:
        n = len(list)
        presum = [0] * (n + 1)

        # populate presum with sum(list[:i+1])
        for i in range(n):
            presum[i + 1] = presum[i] + list[i] 
        # print("presum", presum)

        ans = float("-inf")
        # 枚举左边拿的硬币个数，记录最优答案 
        for i in range(k + 1):
            # for example, if taking 0 from left, then we should take k coins from right
            left = i
            right = k - i

            cur_amount = presum[n] + presum[left] - presum[n - right]
            ans = max(ans, cur_amount)
        
        return ans 
