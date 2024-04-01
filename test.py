  #  012345678 
s = "abcdzdcab"
n = len(s)
is_palindrome = [[False] * n for _ in range(n)]
for i in range(n):
    is_palindrome[i][i] = True
for i in range(1, n):
    is_palindrome[i][i - 1] = True
print(is_palindrome)
length = 1
i = 8
j = 9

[
    [True, False, False, False, False, False, False, False, False], 
    [True, True, False, False, False, False, False, False, False],
    [False, True, True, False, False, False, False, False, False], 
    [False, False, True, True, False, False, False, False, False], 
    [False, False, False, True, True, False, False, False, False], 
    [False, False, False, False, True, True, False, False, False], 
    [False, False, False, False, False, True, True, False, False], 
    [False, False, False, False, False, False, True, True, False], 
    [False, False, False, False, False, False, False, True, True]
]
