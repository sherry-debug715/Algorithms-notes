# Lintcode problem 1800: https://www.lintcode.com/problem/1800/?fromId=161&_from=collection

from typing import (
    List,
)
import math

class Solution:
    """
    @param a: A float array
    @param target: A non-negative integer
    @return: 
    """
    """
    A=[1.2, 1.7]
    i == 2
    ceil = 2 
    floor = 1 
    j = 3
[
    前0个数[0, float, float, float]
    前1个数[float, 0.2, 0.8, float]
    前2个数[float, float, float, 1]
]
[
    [-1, -1, -1, -1]
    [-1, 1, 0, -1]
    [-1, -1, -1, 1]
]
i == 1
target == 0
    A=[1, 2]
    """
    def get_array(self, a: List[float], target: int) -> List[int]:
        n = len(a)
        # dp[i][j] represents 前i个数能凑出和为j的最小代价 
        dp = [[float("inf")] * (target + 1) for _ in range(n + 1)]
        # prev[i][target] represents 在a list中能凑出和为target的最小代价的数是取上还是取下
        # 1 is ceil and 0 is floor
        dp[0][0] = 0
        prev = [[-1] * (target + 1) for _ in range(n + 1)] 

        for i in range(n + 1):
            ceil = math.ceil(a[i - 1])
            floor = math.floor(a[i - 1]) 
            for j in range(target + 1):
                # the price of taking ceil
                # dp[i - 1][j - ceil] represents第i - 1个数中能凑出和为j - current ceil 的
                # 最大代价
                # 加上 目前上取整的代价 
                if j >= ceil and dp[i - 1][j - ceil] + ceil - a[i - 1] < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - ceil] + ceil - a[i - 1]
                    prev[i][j] = 1
                # the price of takine floor
                if j >= floor and dp[i - 1][j - floor] + a[i - 1] - floor < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - floor] + a[i - 1] - floor
                    prev[i][j] = 0 

        answer = a[::]
        for i in range(n, 0, -1):
            if prev[i][target] == 1:
                answer[i - 1] = math.ceil(a[i - 1])
            else:
                answer[i - 1] = math.floor(a[i - 1])
            target -= answer[i - 1]
        
        return answer