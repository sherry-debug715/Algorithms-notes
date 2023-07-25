# Write a function, create_combinations, that takes in a list and a length as arguments. The function should return a 2D list representing all of the combinations of the specifized length.

# The items within the combinations and the combinations themselves may be returned in any order.

# You may assume that the input list contains unique elements and 1 <= k <= len(items).

# Examples:
# create_combinations(["a", "b", "c"], 2); # ->
# # [
# #   [ 'a', 'b' ],
# #   [ 'a', 'c' ],
# #   [ 'b', 'c' ]
# # ]

# create_combinations(['q', 'r', 's', 't'], 3)); # ->
# # [
# #   [ 'q', 'r', 's' ],
# #   [ 'q', 'r', 't' ],
# #   [ 'q', 's', 't' ],
# #   [ 'r', 's', 't' ]
# # ]

# method 1:
def create_combinations(items, k):
  if k == 0:
    return [[]]
  if k > len(items):
    return []
  
  first = items[0]
  without = items[1:]
  decrement_k = create_combinations(without, k-1)
  not_decrement = create_combinations(without, k)
  
  perm = []
  for sub in decrement_k:
    perm.append([first, *sub])
  
  return perm + not_decrement

print(create_combinations(["q", "r", "s", "t"], 3))

#method 2
from itertools import combinations
# combinations function from python itertools modules returns tuples
# it takes in a list and a certain length as arguments
def create_combinations(lst, length):
    return [list(combo) for combo in combinations(lst, length)]