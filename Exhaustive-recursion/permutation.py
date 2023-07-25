def permutations(items):
  if not items:
    return [[]]
  
  first = items[0]
  without = permutations(items[1:])
  res = []
  
  for sub in without:
    # this is key logic in creating a permutation, using the length of each subset to insert value of first in different idx of the new permutation sub list.
    for idx in range(len(sub) + 1):
      res.append([*sub[:idx], first, *sub[idx:]])
  return res

# print(permutations(['a', 'b', 'c']))