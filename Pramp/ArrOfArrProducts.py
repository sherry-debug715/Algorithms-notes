# Pramp: https://www.pramp.com/challenge/7Lg1WA1nZqfoWgPbgM0M

def array_of_array_products(arr):
  if not arr or len(arr) == 1:
    return []
  arr_size = len(arr)
  prefix = [1] * arr_size
  suffix = [1] * arr_size 
  output = []
  
  for i in range(1, arr_size):
    prefix[i] = prefix[i - 1] * arr[i - 1]
  
  for i in range(arr_size - 2, -1, -1):
    suffix[i] = arr[i + 1] * suffix[i + 1]
  
  for i in range(arr_size):
    products = prefix[i] * suffix[i]
    output.append(products)
    
  return output 

