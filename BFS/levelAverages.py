# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque
def level_averages(root):
  if root is None:
    return []
  queue = deque([root])
  root.level = 0
  res = []
  mean = []
  while queue:
    cur = queue.popleft()
    
    if cur.level == len(res):
      res.append([cur.val])
    else:
      res[cur.level].append(cur.val)
    
    if cur.left:
      cur.left.level = cur.level + 1
      queue.append(cur.left)
    if cur.right:
      cur.right.level = cur.level + 1
      queue.append(cur.right)
  
  for sub in res:
    mean.append(cal_mean(sub))
  return mean

from statistics import mean
def cal_mean(ordered_collection):
  return mean(ordered_collection)

# def cal_mean(ordered_collection):
#   return sum(ordered_collection) / len(ordered_collection)

from collections import deque
def level_averages(root):  
  queue = deque([root]) 
  ave = [] 
  
  if root is None:
    return ave
  
  while queue:
    average = 0 
    cur_length = len(queue)
    for i in range(cur_length): 
      sum = 0
      cur_node = queue.popleft() 
      sum += cur_node.val
      average += (sum / cur_length)
      if cur_node.left:
        queue.append(cur_node.left) 
      if cur_node.right: 
        queue.append(cur_node.right) 
    ave.append(average)
  
  return ave 
  