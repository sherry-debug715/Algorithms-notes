# Pramp: https://www.pramp.com/challenge/4E4NW7NjbnHQEx1AxoXE
# Time: O(NlogN)
# Space: O(N)
def absSort(arr):
  if not arr:
    return []
  
  n = len(arr)
  
  shadow_arr = [""] * n 
  merge_sort(0, n - 1, shadow_arr, arr)
  return arr 

def merge_sort(start, end, shadow_arr, arr):
  if start >= end:
    return 
  left, right = start, end
  pivot = (left + right) // 2
  merge_sort(left, pivot, shadow_arr, arr)
  merge_sort(pivot + 1, right, shadow_arr, arr)
  return merge(start, end, shadow_arr, arr)

def merge(start, end, shadow_arr, arr):
  pivot = (start + end) // 2
  left, right = start, pivot + 1
  index = start
  
  while left <= pivot and right <= end:
    if abs(arr[left]) < abs(arr[right]):
      shadow_arr[index] = arr[left]
      left += 1
      index += 1  
    elif abs(arr[right]) < abs(arr[left]):
      shadow_arr[index] = arr[right]
      right += 1 
      index += 1
    else:
      if arr[left] < arr[right]:
        shadow_arr[index] = arr[left]
        left += 1
      else:
        shadow_arr[index] = arr[right]
        right += 1
      index += 1
      
  while left <= pivot:
    shadow_arr[index] = arr[left]
    left += 1
    index += 1
  while right <= end:
    shadow_arr[index] = arr[right]
    right += 1
    index += 1

  for i in range(start, end + 1):
    arr[i] = shadow_arr[i]
    
      