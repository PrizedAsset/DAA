#!/usr/bin/python
import time
import random

#Insertion sort Code block

def insertionsort(array):
    for i in range(1, len(array)):
        a = array[i]
        key = i
        while key > 0 and array[key - 1] > a:
            array[key] = array[key - 1]
            key -= 1
        array[key] = a

# Main method executes when the function is called

def main():
    array = input('Enter Array : ')
    array = array.split()
    array = [int(i) for i in array]

    
    tBefore = time.time()
    insertionsort(array)
    tAfter = time.time()
    
    print('Sorted Array:' ,array)
    print('Execution Time [Insertion sort algorithm] :', tAfter - tBefore)


if __name__ == '__main__':
    main()
