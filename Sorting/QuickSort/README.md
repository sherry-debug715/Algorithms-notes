```py
def _quickSort(start, end, array):
    if start >= end:
        return
    # key point 1: pivot is the value, not the index
    pivot = array[(start + end) // 2] 
    left, right = start, end 

    while left <= right:
        while left <= right and array[left] < pivot:
            left += 1 
        while left <= right and array[right] > pivot: 
            right -= 1 

        if left <= right:
            swap(left, right, array) 
            left += 1 
            right -= 1  
            
    _quickSort(start, right, array) 
    _quickSort(left, end, array)
```

- In the divide and conquer function, it's very important that every time we compare left & right, it should be left <= right not left < right. We need to avoid the following situation 
```py
while left < right:
    while left < right and array[left] < pivot:
        left += 1 
    while left < right and array[right] > pivot: 
        right -= 1 

    if left < right:
        swap(left, right, array) 
        left += 1 
        right -= 1 

_quickSort(start, right, array) 
_quickSort(left, end, array)

       #P
       #L
[3, 4, 6, 8, 10]
       #R
```

we break out of while loop because now left == right and enter the following situation.
```py
_quickSort(0, 2, array)
_quickSort(2, 4, array)
```
