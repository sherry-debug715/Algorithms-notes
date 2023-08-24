# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.

# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.

# You may assume that the input tree is non-empty.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def all_tree_paths(root):
#   if root is None:
#     return []
  
#   if root.left is None and root.right is None:
#     return [[root.val]]
  
#   all_path = []
#   left = all_tree_paths(root.left)
#   right = all_tree_paths(root.right)
  
#   for sub in left:
#     all_path.append([root.val, *sub])
#   for sub in right:
#     all_path.append([root.val, *sub])

  
#   return all_path

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# Time O(N)
# Space O(N)
def all_tree_paths(root):
  all_paths = []
  _all_tree_paths(root, [root], all_paths) 
  return all_paths

def _all_tree_paths(root, cur_path, all_paths): 
  if root is None:
    return 
  
  if root.left is None and root.right is None:
    all_paths.append([node.val for node in cur_path]) 
    return 
  
  cur_path.append(root.left) 
  _all_tree_paths(root.left, cur_path, all_paths) 
  cur_path.pop() 
  
  cur_path.append(root.right) 
  _all_tree_paths(root.right, cur_path, all_paths) 
  cur_path.pop()
  
  
  