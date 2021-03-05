#!/usr/bin/python
import time
import random

# This function helps in swapping of numbers.

def numberSwap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)

# This function is used to implement bubblesort algorithm which 
# takes array as input and then makes necessary swaps into the original array.


def bubblesort(array):
    x = len(array)
    for i in range(x):
        for j in range(x -i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = numberSwap(array[j], array[j+1])

# This is the main method for the code. This is called when the code is 
# executed. This method takes string as a input and convert it into list of 
# integers and is called as bubblesort


def main():
    array = input('Enter Array : ')
    array = array.split()
    array = [int(i) for i in array]

    # bubblesort(array)
    tBefore = time.time()
    bubblesort(array)
    tAfter = time.time()
    
    print('Sorted Array: ' ,array)
    print('Execution Time [Bubble sort algorithm] : ' ,tAfter - tBefore)


if __name__ == '__main__':
    main()