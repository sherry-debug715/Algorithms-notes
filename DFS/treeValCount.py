# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# def tree_value_count(root, target):
#   if root is None:
#     return 0
  
#   # if root.val == target:
#   #   return 1
#   match = 1 if root.val == target else 0
  
#   return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)

# depth first iterative
# def tree_value_count(root, target):
#   stack = [root]
#   count = 0
  
#   if not root:
#     return count
  
#   while len(stack):
#     cur = stack.pop()
#     if cur.val == target:
#       count += 1
      
#     if cur.right:
#       stack.append(cur.right)
#     if cur.left:
#       stack.append(cur.left)
#   return count


# breadth first 
# from collections import deque
# def tree_value_count(root, target):
#   queue = deque([ root ])
#   count = 0
  
#   if root is None:
#     return count
  
#   while queue:
#     cur = queue.popleft()
#     if cur.val == target:
#       count += 1
      
#     if cur.right:
#       queue.append(cur.right)
#     if cur.left:
#       queue.append(cur.left)
  
#   return count

def tree_value_count(root, target):
  if not root:
    return 0
  
  counter = 1 if root.val == target else 0

  return counter + tree_value_count(root.left, target) + tree_value_count(root.right, target)
  

















