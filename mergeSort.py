# Patel, Rutu Tarakbhai
# 100-175-1189

import time
import random

# '''This function is used to mergesort algorithm which
# divides the list into various sublists and then sorts those
# and later merging to give sorted array'''


def mergeSort(array):
    if len(array) > 1:
        middleItem = len(array)//2
        leftSubArray = array[:middleItem]
        rightSubArray = array[middleItem:]
        mergeSort(leftSubArray)
        mergeSort(rightSubArray)
        i = 0
        j = 0
        k = 0
        while i < len(leftSubArray) and j < len(rightSubArray):
            if leftSubArray[i] <= rightSubArray[j]:
                array[k] = leftSubArray[i]
                i += 1
            else:
                array[k] = rightSubArray[j]
                j += 1
            k += 1
        while i < len(leftSubArray):
            array[k] = leftSubArray[i]
            i += 1
            k += 1
        while j < len(rightSubArray):
            array[k] = rightSubArray[j]
            j += 1
            k += 1
    return array

#'''main method to called when code is executed'''


def main():
    array = []
    # array = input('Enter space separeted array elements : ')
    # array = array.split()
    # array = [int(i) for i in array]
    for i in range(50000):
        temp = random.randint(0, 1000)
        array.append(temp)
    timeBefore = time.time()
    y = mergeSort(array)
    timeAfter = time.time()
    print(f'Sorted Array   : {y}')
    totaltime = timeAfter - timeBefore
    print(f'Time taken by algorithm : {totaltime}')


if __name__ == '__main__':
    main()
