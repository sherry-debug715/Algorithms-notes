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