s = "aba"
n = len(s) # 3
is_palindrome = [[False] * n for _ in range(n)]
for i in range(n):
    is_palindrome[i][i] = True
for i in range(1, n):
    is_palindrome[i][i-1] = True
# [[True, False, False], [True, True, False], [False, True, True]]

start, longest = 0, 1
for length in range(2, n + 1): # 2, 3
    for i in range(n - length + 1): # 0, 1
        j = i + length - 1 # 1 3
        is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

print(is_palindrome)