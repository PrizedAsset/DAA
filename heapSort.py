# Patel, Rutu Tarakbhai     matangi
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

#'''This method is used to create a heap from the list'''


def heapify(array, length, root):
    maxElement = root
    leftElement = 2*root + 1
    rightElement = 2*root + 2
    # For Left subchild
    if leftElement < length and array[root] < array[leftElement]:
        maxElement = leftElement
    # For Right subchild
    if rightElement < length and array[maxElement] < array[rightElement]:
        maxElement = rightElement
    if maxElement != root:
        array[root], array[maxElement] = numberSwap(
            array[root], array[maxElement])
        heapify(array, length, maxElement)

# This method implements heapsort algorithm taking out
# Largest element and placing it in its correct place


def heapsort(x):
    length = len(x)
    for i in range(length, -1, -1):
        heapify(x, length, i)
    for i in range(length-1, 0, -1):
        x[i], x[0] = numberSwap(x[i], x[0])
        heapify(x, i, 0)

# Main method called when code is executed takes input
# and sets it to list and call heapsort algorithm


def main():

    array = []
    for i in range(50000):
        temp = random.randint(0, 1000)
        array.append(temp)
    timeBefore = time.time()
    heapsort(array)
    timeAfter = time.time()
    print(f'Sorted Array : {array}')
    print(f'Time Taken by Algorithm : {timeAfter - timeBefore}')


if __name__ == '__main__':
    main()
