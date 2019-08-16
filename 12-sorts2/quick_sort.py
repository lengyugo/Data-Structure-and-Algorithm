"""
    quick_sort
    快速排序
"""

from typing import List
import numpy as np

def quick_sort(a:List[int]):
    quick_sort_c(a,0,len(a) - 1)

##
def quick_sort_c(a:List[int],low:int,high:int):

    if low < high:

        #k = random.randint(low,high)
        #a[low],a[k] = a[k],a[low]

        q = partition(a,low,high)
        #print(q)
        quick_sort_c(a,low,q - 1)
        quick_sort_c(a,q + 1,high)

##没理解？
def partition(a:List[int],low:int,high:int):

    pivot,i= a[low],low

    for j in range(low+1,high+1):

       if a[j] <= pivot:

            i += 1

            a[i],a[j] = a[j],a[i]

    a[low],a[i] = a[i],a[low]
    return i

if __name__ == "__main__":

    a1 = [3, 9, -6, 4, 10]
    a2 = [2, 3, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = np.random.randint(1,100,size=50)
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)



