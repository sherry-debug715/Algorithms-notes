# Average/Worst Time O(nLogn)
# Space O(N)
def mergeSort(list):
    # Write your code here.
    if not list:
        return list
    
    shadow_list = [""] * len(list)
    _mergeSort(0, len(list) - 1, shadow_list, list)
    return list 

def _mergeSort(start, end, shadow_list, list):
    if start >= end:
        return  
    left, right = start, end
    pivot = (start + end) // 2

    # divide the left side 
    _mergeSort(left, pivot, shadow_list, list)
    # divide the right side
    _mergeSort(pivot + 1, right, shadow_list, list)
    # sort and merge
    do_merge(start, pivot, end, shadow_list, list)

def do_merge(start, mid, end, shadow_list, list):
    left, right = start, mid + 1 
    index = start 
    while left <= mid and right <= end:
        if list[left] < list[right]:
            shadow_list[index] = list[left]
            index += 1
            left += 1 
        else:
            shadow_list[index] = list[right]
            index += 1 
            right += 1 
            
    while left <= mid:
        shadow_list[index] = list[left] 
        left += 1 
        index += 1 
        
    while right <= end:
        shadow_list[index] = list[right] 
        right += 1 
        index += 1 

    for i in range(start, end + 1):
        list[i] = shadow_list[i]
    
    
    
