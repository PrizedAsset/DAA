#!/usr/bin/python
import time
import random

#Find the smallest element in the array

def selectionsort(array):
    for i in range(len(array)):
        small_num = min(array[i:])

        #Swap the position of first element and smallest element

        idx_small = array.index(small_num)
        array[i], array[idx_small] = array[idx_small], array[i]
       
# The main function is called when the code block is executed.

def main():
    array=[]
    for _ in range(100):
        temp = random.randint(0, 500)
        array.append(temp)

    tbefore = time.time()
    selectionsort(array)
    tafter = time.time()

    print('Sorted Array: ' ,end='')
    print(array)
    print('Execution Time [Selection sort algorithm] :' ,tafter - tbefore)

if __name__ == '__main__':
    main()