# Patel, Rutu Tarakbhai
# 100-175-1189

import time
import random

# This is function tom implement numberSwap function
# This will take two arguments and return a swapped
# tupple of element which can be later used to assing the variables.


def numberSwap(x, y):
    temp = x
    x = y
    y = temp
    return (x, y)

# '''This function is used to implement bubblesort
# algorithm which takes array as input and then
# makes nessacary swaps to sort the original array'''


def bubblesort(array):
    lengthOfArray = len(array)
    for i in range(lengthOfArray):
        for j in range(lengthOfArray-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = numberSwap(array[j], array[j+1])

# '''This is the main method for the code. This is called
# when the code is executed this method takes space separeted
# string as a input convert it into list of ints and calls bubblesort'''


def main():
    array = input('Enter Array [Space Separated] : ')
    array = array.split()
    array = [int(i) for i in array]
    # array = []
    # for i in range(50000):
    #     temp = random.randint(0, 1000)
    #     array.append(temp)
    timeBefore = time.time()
    bubblesort(array)
    timeAfter = time.time()
    print(f'Sorted Array: {array}')
    print(f'Time Taken by Algorithm : {timeAfter - timeBefore}')


if __name__ == '__main__':
    main()
