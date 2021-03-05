#!/usr/bin/python
import time
import random

# This function helps in swapping of numbers.

def numberSwap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)

# This function is used to create heap from the list


def heapify(array, length, root):
    maxElement = root
    leftChild = 2*root + 1
    rightChild = 2*root + 2

    # Left child
    if leftChild < length and array[root] < array[leftChild]:
        maxElement = leftChild

    # Right child
    if rightChild < length and array[maxElement] < array[rightChild]:
        maxElement = rightChild

    
    if maxElement != root:
        array[root], array[maxElement] = numberSwap(array[root], array[maxElement])
        heapify(array, length, maxElement)

# This function performs heapsort algorithm by rearranging the largest element.

def heapsort(li):
    length = len(li)
    for i in range(length, -1, -1):
        heapify(li, length, i)
    for i in range(length-1, 0, -1):
        li[i], li[0] = numberSwap(li[i], li[0])
        heapify(li, i, 0)


def main():

    array = []
    for _ in range(100):
        temp = random.randint(0, 500) #Generates the random integer for the range and select the given number.
        array.append(temp)
    
    tBefore = time.time()
    heapsort(array)
    tAfter = time.time()

    print('Sorted Array :' , array)
    print('Execution Time [Heap sort algorithm] :', tAfter - tBefore)


if __name__ == '__main__':
    main()
