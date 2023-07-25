def permutations(items):
  if not items:
    return [[]]
  
  first = items[0]
  without = permutations(items[1:])
  res = []
  
  for sub in without:
    for idx in range(len(sub) + 1):
      res.append([*sub[:idx], first, *sub[idx:]])
  return res

# print(permutations(['a', 'b', 'c']))