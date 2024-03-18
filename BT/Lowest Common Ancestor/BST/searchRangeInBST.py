# Lintcode problem 11: https://www.lintcode.com/problem/search-range-in-binary-search-tree/description

from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        if not root:
            return []

        results = [] 

        self.in_order(root, k1, k2, results)
        return results
    
    def in_order(self, root, k1, k2, results):
        if not root:
            return 
        if root.val < k1:
            self.in_order(root.right, k1, k2, results)
        elif root.val > k2:
            self.in_order(root.left, k1, k2, results)
        else:
            self.in_order(root.left, k1, k2, results)
            results.append(root.val)
            self.in_order(root.right, k1, k2, results)
