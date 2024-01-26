"""
Lintcode problem 628: https://www.lintcode.com/problem/628/?fromId=161&_from=collection
"""
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
# Time: O(N) Both the average and worst time is O(n) as the algorithmn visits each node exactly once,
# Space: O(H), where H is the height of the tree. For an unbalanced tree, the space complexity is O(N), however, for an balanced tree, the height of the tree would be logN, resulting in an O(logN) complexity.
class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    # use a helper function: function returns a tuple: 
    #   (cur_sum, max_sub_sum, root_of_subtree_with_max_sum) 
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        _, _, max_subtree_root = self._find_subtree(root) 
        return max_subtree_root 
    
    def _find_subtree(self, root): 
        # when traverse across leaf node, should hit this line 
        if root is None:
            return 0, float("-inf"), None 
        
        left_sum, left_max_sum, left_max_subtree = self._find_subtree(root.left) 
        right_sum, right_max_sum, right_max_subtree = self._find_subtree(root.right) 

        cur_sum = root.val + left_sum + right_sum 
        cur_max = max(cur_sum, left_max_sum, right_max_sum) 

        # decide which subtree has the largest sum 
        # first condition, when we are at leaf nodes, this situation apply
        if cur_max == cur_sum:
            return (cur_sum, cur_max, root) 
        elif cur_max == left_max_sum:
            return (cur_sum, cur_max, left_max_subtree) 
        else:
            return (cur_sum, cur_max, right_max_subtree)

