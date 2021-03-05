#!/usr/bin/python

# 3 median quick sort
import time
import random

# Sort and return min, middle and max elements.

def Median_03(a, b, c):
    x = [a, b, c]
    insertion(x, 0, 2)
    small = x[0]
    middle = x[1]
    big = x[2]
    return small, middle, big

def insertion(array, low, high):
    for i in range(low+1, high+1):
        x = array[i]
        j = i
        while j > low and x < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = x


# Partition method is used to select pivot element and then the smaller 
# and greater elements are placed accordingly.


def partition(array, low, high):
    min, median, max = Median_03(
        array[low], array[high], array[((low+high)//2)+1])
    pivot = median
    array[low] = min
    array[((low+high)//2)+1] = max
    i = low + 1
    j = high - 1
    while i <= j:
        if array[i] < pivot:
            i += 1
        else:
            if array[j] > pivot:
                j -= 1
            else:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
    array[high] = array[i]
    array[i] = pivot
    return i


def quicksort(array, low, high):
    if high - low < 3:
        insertion(array, low, high)
    else:
        index = partition(array, low, high)
        quicksort(array, low, index-1)
        quicksort(array, index+1, high)

# The main function is called when the code block is executed.

def main():
    array = []
    for _ in range(100):
        x = random.randint(0, 500)
        array.append(x)

    tBefore = time.time()
    quicksort(array, 0, len(array)-1)
    tAfter = time.time()
    
    print('Sorted Array :', array)
    print('Execution Time [Quick sort(03 medians) algorithm]:', tAfter - tBefore)


if __name__ == '__main__':
    main()
