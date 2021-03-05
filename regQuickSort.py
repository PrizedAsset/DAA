import time
import random

##website for comments https://www.codespeedy.com/quicksort-in-python/  <= REMOVE THIS FROM COMMENTS after insertion of the code comments

def regquicksort(arr, begin, end):
    
    if end - begin > 1:
        p = partition(arr, begin, end)
        regquicksort(arr, begin, p)
        regquicksort(arr, p + 1, end)
 
 
def partition(arr, begin, end):
    pivot = arr[begin]
    i = begin + 1
    j = end - 1
 
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
 
        if i <= j:
           arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[begin], arr[j] = arr[j], arr[begin]
            return j
 
def main():
    arr=[]
   ## arr = input('Enter the list of numbers to be Sorted: ').split()
   # arr = [int(x) for x in arr]
    for i in range(100):
        temp = random.randint(0, 10000)
        arr.append(temp)
    tbefore = time.time()
    regquicksort(arr, 0, len(arr))
    tafter = time.time()
    print('Sorted list: ', end='')
    print(arr)
    print(f'Time for the sorting algorithm : {tafter - tbefore}')

if __name__ == '__main__':
    main()