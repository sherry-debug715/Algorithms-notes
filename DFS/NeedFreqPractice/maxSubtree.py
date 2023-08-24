# Description
# Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.
# Input:
# {1,-5,2,0,3,-4,-5}
# Output:3
# Explanation:
# The tree is look like this:
#      1
#    /   \
#  -5     2
#  / \   /  \
# 0   3 -4  -5
# The sum of subtree 3 (only one node) is the maximum. So we return 3.
# Example 2:

# Input:
# {1}
# Output:1
# Explanation:
# The tree is look like this:
#    1
# There is one and only one subtree in the tree. So we return 1.

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    
    # Main function that will be called. This function calls the helper function
    # and returns the root of the subtree with the maximum sum.
    def find_subtree(self, root: TreeNode) -> TreeNode:
        _, _, max_subtree_root = self._find_subtree(root) 
        return max_subtree_root 
    
    # Helper function. For a given node (subtree root), it returns:
    # 1. The sum of the entire subtree rooted at the node.
    # 2. The maximum sum of all subtrees.
    # 3. The root of the subtree that has the maximum sum.
    def _find_subtree(self, root): 
        # Base case: If the node is None (i.e., we've reached past a leaf node or the tree is empty),
        # return 0 for the sum, negative infinity for the max sum, and None for the root.
        if root is None:
            return 0, float("-inf"), None 
        
        # Recursively compute the sum of the left and right subtrees, 
        # as well as their maximum subtree sums and the roots of those maximum subtrees.
        left_sum, left_max_sum, left_max_subtree = self._find_subtree(root.left) 
        right_sum, right_max_sum, right_max_subtree = self._find_subtree(root.right) 

        # Calculate the current sum for the subtree rooted at the current node.
        cur_sum = root.val + left_sum + right_sum 
        # Determine the maximum sum out of the current subtree and its left and right children.
        cur_max = max(cur_sum, left_max_sum, right_max_sum) 

        # Decide which subtree (current, left, or right) has the largest sum 
        # and return the appropriate values.
        if cur_max == cur_sum:
            return (cur_sum, cur_max, root) 
        elif cur_max == left_max_sum:
            return (cur_sum, cur_max, left_max_subtree) 
        else:
            return (cur_sum, cur_max, right_max_subtree)
