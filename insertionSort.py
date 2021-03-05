# Patel, Rutu Tarakbhai
# 100-175-1189

import time
import random

# '''this function is used to implement insertion sort
# algorithm'''


def insertionsort(array):
    for i in range(1, len(array)):
        this = array[i]
        pos = i
        while pos > 0 and array[pos - 1] > this:
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = this

#'''main method called when the code is executed'''


def main():
    array = []
    # array = input('Enter space separeted array elements : ')
    # array = array.split()
    # array = [int(i) for i in array]
    for i in range(50000):
        temp = random.randint(0, 1000)
        array.append(temp)
    timeBefore = time.time()
    insertionsort(array)
    timeafter = time.time()
    print(array)
    print(f'Time taken for the algorithm : {timeafter - timeBefore}')


if __name__ == '__main__':
    main()
