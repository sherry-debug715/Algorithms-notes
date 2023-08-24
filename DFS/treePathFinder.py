# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

# METHOD 1
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def path_finder(root, target):
#   if root is None:
#     return None
#   stack = [ root ]
#   path = [ [root.val] ]
  
#   while len(stack):
#     cur_node = stack.pop()
#     cur_path = path.pop()
    
#     target_node_val = cur_path[-1]
#     if target_node_val == target:
#       return cur_path
    
#     if cur_node.right:
#       path.append([*cur_path, cur_node.right.val])
#       stack.append(cur_node.right)
#     if cur_node.left:
#       path.append([*cur_path, cur_node.left.val])
#       stack.append(cur_node.left)
      
#   return None

# METHOD 2
# def path_finder(root, target):
#   if root is None:
#     return None
  
#   if root.val == target:
#     return [root.val]
  
#   left = path_finder(root.left, target)
#   if left is not None:
#     return [root.val, *left]
  
#   right = path_finder(root.right, target)
#   if right is not None:
#     return [root.val, *right]

#METHOD 3
# Time: O(N + E) N is the number of node, E represent number of edges visited 
# Space: O(D + S) D is the depth of BT, S is the depth of the stack.
def path_finder(root, target):
  return _path_finder(root, target, []) 

def _path_finder(root, target, cur_path): 
  if root is None:
    return 
  
  cur_path.append(root.val)
  
  if root.val == target:
    return cur_path

  left = _path_finder(root.left, target, cur_path) 
  if left:
    return left

  right = _path_finder(root.right, target, cur_path)
  if right:
    return right
  
  cur_path.pop()
  