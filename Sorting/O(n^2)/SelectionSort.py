# Initialize an Integer, tail, set it to 0
# Initialize an Integer, minIndex, set it to 0
# WHILE tail < length of array:
#     Iterate over array from tail + 1 to length of array, using i.
#         check if array[i] <= array[tail]:
#             minIndex = i
#     swap minIndex with tail
#     tail += 1
#     minIndex = tail
# return array

def selectionSort(array):
    tail = 0
    min_index = 0

    while tail < len(array):
        for i in range(tail + 1, len(array)):
            if array[i] <= array[min_index]:
                min_index = i 

        array[min_index], array[tail] = array[tail], array[min_index]
        tail  += 1
        min_index = tail 

    return array
