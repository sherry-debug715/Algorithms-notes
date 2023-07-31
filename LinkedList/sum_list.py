# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

# a = Node(2)
# b = Node(8)
# c = Node(3)
# d = Node(-1)
# e = Node(7)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

# # 2 -> 8 -> 3 -> -1 -> 7

# sum_list(a) # 19

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def sum_list(head): #44ms
#   if head is None:
#     return 0
#   return head.val+sum_list(head.next)

def sum_list(head): #46ms
  sum = 0
  current = head
  while current is not None:
    sum += current.val
    current = current.next
  return sum


a = Node(2) 
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a)) # 19
