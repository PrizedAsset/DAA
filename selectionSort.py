import time
import random

##website for comments https://www.programminginpython.com/selection-sort-algorithm-python/  <= REMOVE THIS FROM COMMENTS after insertion of the code comments

def selectionsort(arr):
    for i in range(len(arr)):
        smallest_element = min(arr[i:])
        index_of_smallest = arr.index(smallest_element)
        arr[i], arr[index_of_smallest] = arr[index_of_smallest], arr[i]
       


def main():
    arr=[]
   ## arr = input('Enter the list of numbers to be Sorted: ').split()
   # arr = [int(x) for x in arr]
    for i in range(50):
        temp = random.randint(0, 1000)
        arr.append(temp)
    tbefore = time.time()
    selectionsort(arr)
    tafter = time.time()
    print('Sorted list: ', end='')
    print(arr)
    print(f'Time for the sorting algorithm : {tafter - tbefore}')

if __name__ == '__main__':
    main()