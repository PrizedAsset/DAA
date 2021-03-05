# Patel, Rutu Tarakbhai
# 100-175-1189

import time
import random
# 3 median quick sort
# Insertion sort implementation called when
# size is less then cutoff


def insertionSort(array, low, high):
    for i in range(low+1, high+1):
        temp = array[i]
        j = i
        while j > low and temp < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = temp

# method which uses insertionsort to sort
# three elements and then return min, middle, max
# in order


def medianOfThree(a, b, c):
    temp = [a, b, c]
    insertionSort(temp, 0, 2)
    min_ = temp[0]
    middle = temp[1]
    max_ = temp[2]
    return min_, middle, max_

# '''Partition method is used to select pivot element and then
# arrange it in such a way that pivot is in its place and then
# arrange it in such as '''


def partition(array, low, high):
    min, median, max = medianOfThree(
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

#'''function to implement quick sort algorithm'''


def quicksort(array, low, high):
    if high - low < 3:
        insertionSort(array, low, high)
    else:
        index = partition(array, low, high)
        quicksort(array, low, index-1)
        quicksort(array, index+1, high)

#'''Main method called when code is executed'''


def main():
    array = []
    # array = input('Enter space separeted array elements : ')
    # array = array.split()
    # array = [int(i) for i in array]
    for i in range(50000):
        temp = random.randint(0, 1000)
        array.append(temp)
    timeBefore = time.time()
    quicksort(array, 0, len(array)-1)
    timeAfter = time.time()
    print(f'Sorted Array : {array}')
    print(f'Time for the sorting algorithm : {timeAfter - timeBefore}')


if __name__ == '__main__':
    main()
