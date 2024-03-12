# lintcode problem 547: https://www.lintcode.com/problem/547/description?fromId=161&_from=collection

from typing import (
    List,
)

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
             we will sort your return value in output
                          p
    nums1 = [1, 1, 2, 2]
                   p2
    nums2 = [2, 2]

    [2]
    """
    # Time: O(nlogn)
    # Space: O(N)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        p1, p2 = 0, 0
        nums1.sort()
        nums2.sort()
        output = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                p2 += 1
            else:
                if not output or nums1[p1] != output[-1]:
                    output.append(nums1[p1])
                p1 += 1
                p2 += 1
        return output

