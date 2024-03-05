A = [
      [1, 2],
      [5, 3]
    ]

ans = []
for i in range(len(A)):
    for j in range(len(A[0])):
        ans.append((A[i][j], i, j))

ans.sort()
print(ans)
