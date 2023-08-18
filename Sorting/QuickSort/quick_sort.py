# Time O(nlogn)
# Space O(N)
def quickSort(array):
    # Write your code here.
    if not array:
        return 

    if len(array) == 1:
        return array 

    _quickSort(0, len(array) - 1, array) 
    return array


def _quickSort(start, end, array):
    if start >= end:
        return
    # key point 1: pivot is the value, not the index
    pivot = array[(start + end) // 2] 
    left, right = start, end 
    # key point 2: explained in the README.
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

def swap(index1, index2, array):
    array[index1], array[index2] = array[index2], array[index1]
            
    
