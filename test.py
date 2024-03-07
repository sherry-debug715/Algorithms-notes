s = "abbcdebdde"  
t = "bde" 
# cur = [i if x == t[0] else None for i, x in enumerate(s)]

#         0    1     2    3     4    5   6     7    8 
# cur = [None, 1, None, None,  None, 5, None, None, None] 

# cur = [None, None, None, None, 1, None, 5, 5, None]
#                                      5              8
# cur = [None, None, None, None, None, 1, None, None, 5]

ans = 0, len(s)
for e, st in enumerate(cur):
    if st and st >= 0 and e - st < ans[1] - ans[0]:
        ans = st, e
