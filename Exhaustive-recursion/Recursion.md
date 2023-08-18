## Recursion 

### Recursion depth 

- Recursion depth is a measure of how many times a recursive function calls itself before reaching the base case and starting to return.

### O(N) recursion depth, O(N) space 
```py
def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n
```

When n = 100, the recursion depth is 100. Because it recursively called itself 100 times (assuming there's no optimization like tail recursion in place). Generally speaking, we are more concerned about the order of magnitude of the recursion depth. In this factorial function, the recursion depth is O(n).

In bigO notation, which describes the upper bound of an algorithm in terms of its growth rate, the recursion depth of the factorial function is described as O(n). This is because, for an input of size n, the function recurses n times.

### O(N) recursion depth, O(1) space 
<strong style="color: orange">Optimize to use tail recursion</strong>

A function is tail-recursive if:

- The recursive call is the last action in the function. (like the above code example).
- The result of the recursive call is immediately returned and not used in any further computation. (the above example doesn't apply) 

```py
def factorial(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    else:
        return factorial(n-1, n * accumulator)
```

In this version, the recursive call to factorial is the last operation in the function, and there's no further computation with its result. The multiplication is done before the recursive call, using an accumulator to carry the intermediate result. When we hit the base case, the entire call stack pops. 






