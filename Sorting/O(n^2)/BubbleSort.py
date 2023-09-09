# Initialize a boolean, no_swap, set it to False
# Initialize a integer, numOfIteration, set it to 0 
# WHILE not swap:
#     swap = True 
#     iterate over the array from 1 to length of array - numOfIteration, using i:
#         if array[i] > array[i - 1]:
#             swap position
#             swap = False
            
#     numOfIteration += 1
# return array

def bubbleSort(array):
    no_swap = False 
    numOfIterations = 0 

    while not no_swap:
        no_swap = True 
        for i in range(1, len(array) - numOfIterations):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                no_swap = False
                
        numOfIterations += 1

    return array 