#!/usr/bin/python
import time
import random

#Selects a pivot element

def quick_sort(array, begin, end):
    
    if end - begin > 1:
        p = partition(array, begin, end)
        quick_sort(array, begin, p)
        quick_sort(array, p + 1, end)
 
 
def partition(array, begin, end):
    pivot = array[begin]
    i = begin + 1
    j = end - 1
 
    while True:
        while (i <= j and array[i] <= pivot):
            i = i + 1
        while (i <= j and array[j] >= pivot):
            j = j - 1
 
        if i <= j:
           array[i], array[j] = array[j], array[i]
        else:
            array[begin], array[j] = array[j], array[begin]
            return j
 
# The main function is called when the code block is executed.
 
def main():
    array=[]
    for _ in range(100):
        temp = random.randint(0, 500)
        array.append(temp)
        
    tbefore = time.time()
    quick_sort(array, 0, len(array))
    tafter = time.time()

    print('Sorted Array: ', end='')
    print(array)
    print('Execution Time [Quick sort algorithm] :', tafter - tbefore)

if __name__ == '__main__':
    main()