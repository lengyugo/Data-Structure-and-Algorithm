"""
  二分查找
"""

from typing import List

def binary_search(a:List[int],value):

    ##非递归

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = int((low + high) / 2)
        #print(mid)
        if a[mid] == value:
            return mid
        elif a[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1



def bsearch(a:List[int],value):
    return recurrsion_binary_search(a,0,len(a)-1,value)

def recurrsion_binary_search(a:List[int],low,high,value):

    #递归实现

    if low > high:
        return -1

    mid = low + ((high - low) >> 1) ##为什么不用mid = int((low + high) / 2)，会陷入死循环

    if a[mid] == value:
        return mid
    elif a[mid] < value:
        return recurrsion_binary_search(a,mid+1,high,value)
    else:
        return recurrsion_binary_search(a,low,mid-1,value)


if __name__ == "__main__":

    a = [1,5,9,6,3,4,12,45,8,59,20]
    a = sorted(a)
    print(a)
    print(binary_search(a,value=9))

    b = [1, 5, 9, 6, 3, 4, 12, 45, 8, 59, 20]
    b = sorted(b)
    print(b)
    print(bsearch(b, value=9))