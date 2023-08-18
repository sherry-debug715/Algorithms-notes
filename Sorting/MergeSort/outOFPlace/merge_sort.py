# Time: O(nlogn)
# Space: O(nlogn)

def mergeSort(list):
    # Write your code here.
    # cover edge case of when list is empty 
    # cover base case, when list is length of one, return list 
    # divide the list into half and recursively call the left and right halves of the list.
    # pass both returned left and returned right into a helper function and return it.

    # helper function 
    # takes in two lists of numbers as argument 
    # sort these two lists into a new list in ascending order 
    # should return the newly created list of sorted numbers
    # the function need to cover cases where the length of left list is different from the length of 
    # right list. 

    if not list:
        return [] 

    if len(list) == 1:
        return list 

    pivot = len(list) // 2 

    left_list = mergeSort(list[:pivot])
    right_list = mergeSort(list[pivot:])

    return _mergeSort(left_list, right_list) 

def _mergeSort(left_list, right_list):
    left = 0 
    right = 0
    sorted = []

    while left < len(left_list) and right < len(right_list):
        if left_list[left] <= right_list[right]:
            sorted.append(left_list[left])
            left += 1 
        elif right_list[right] < left_list[left]:
            sorted.append(right_list[right])
            right += 1 
            
    if left == len(left_list):
        for idx in range(right, len(right_list)):
            sorted.append(right_list[idx])
    if right == len(right_list):
        for idx in range(left, len(left_list)):
            sorted.append(left_list[idx])

    return sorted





    
