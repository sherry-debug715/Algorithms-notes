# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


# def longest_streak(head): #42ms
#   count = 0
#   count_collect = []
#   current = head
#   if head is None:
#     return count
  
#   while current is not None:
#     print('this is current', current.val)
#     count += 1
#     if current.next is None or current.val != current.next.val:
#       print('this is current different', current.val)
#       count_collect.append(count)
#       count = 0
      
#     current = current.next
  
#   return max(count_collect)

def longest_streak(head): 
  count = 1
  max_streak = 0
  prev_val = None
  current = head
  
  while current is not None:
    print('this is current val', current.val)
    print('this is prev val', prev_val)
    
    if current.val == prev_val:
      count += 1
    else:
      count = 1
      
    if max_streak < count:
      max_streak = count
    prev_val = current.val
    current = current.next
    
  return max_streak 



a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 9 -> 9 -> 1 -> 9 -> 9 -> 9

print(longest_streak(a)) # 3