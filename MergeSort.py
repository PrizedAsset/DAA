#!/usr/bin/python
import time
import random

# This function in mergesort algorithm divides the list into various sublists 
# and then sorts by later merging into give sorted array.


def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        leftArr = array[:mid]
        rightArr = array[mid:]
        mergeSort(leftArr)
        mergeSort(rightArr)
        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] <= rightArr[j]:
                array[k] = leftArr[i]
                i += 1
            else:
                array[k] = rightArr[j]
                j += 1
            k += 1
        while i < len(leftArr):
            array[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            array[k] = rightArr[j]
            j += 1
            k += 1
    return array

# The main function is called when the code block is executed.

def main():
    array = []
    
    for _ in range(100):
        temp = random.randint(0, 500)
        array.append(temp)

    tBefore = time.time()
    y = mergeSort(array)
    tAfter = time.time()
    print('Sorted Array   : ' ,y)
    totaltime = tAfter - tBefore
    print('Execution Time [Merge sort algorithm]: ',totaltime)


if __name__ == '__main__':
    main()
