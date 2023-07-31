# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.

# You may assume that both input lists are non-empty.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# def zipper_lists(head_1, head_2):
#   if head_1 is None and head_2 is None:
#     return None
  
#   if head_1 is None:
#     return head_2
  
#   if head_2 is None:
#     return head_1
  
#   head1_next = head_1.next
#   head2_next = head_2.next

#   head_1.next = head_2
#   head_2.next = zipper_lists(head1_next, head2_next)
# it's important to return head_1 here, this step chains head_2.next to the next node, which is head1_next in the recursive function.
#   return head_1

# need a pointer to keep track of the last node of the shorter linked list

def zipper_lists(head_1, head_2):
  tail = head_1
  cur_1 = head_1.next
  cur_2 = head_2
  counter = 0
  
  while cur_1 is not None and cur_2 is not None:
    if counter % 2 == 0:
      tail.next = cur_2
      cur_2 = cur_2.next
    else:
      tail.next = cur_1
      cur_1 = cur_1.next
      
    tail = tail.next
    counter += 1
  
  if cur_2 is None:
    tail.next = cur_1
  elif cur_1 is None:
    tail.next = cur_2
  
  return head_1




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f

x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z

zipper_lists(a, x)
# a -> x -> b -> y -> c -> z -> d -> e -> f
