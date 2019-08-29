"""
   二分查找变种
"""

from typing import List

##查找第一个值等于给定值的元素
def binary_search_1(a:List[int],value):

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)

        if a[mid] < value:
            low = mid + 1
        elif a[mid] > value:
            high = mid - 1
        else:

            if mid == 0 or a[mid - 1] != value: return mid
            else:
                high = mid - 1

    return -1

##查找最后一个值等于给定值的元素
def binary_search_2(a:List[int],value):

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)

        if a[mid] < value:
            low = mid + 1
        elif a[mid] > value:
            high = mid - 1
        else:

            if mid == len(a) - 1 or a[mid + 1] != value: return mid
            else:
                low = mid + 1

    return -1

##查找第一个值大于等于给定值的元素
def binary_search_3(a:List[int],value):

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        # print(mid)

        if a[mid] >= value:
            if mid == 0 or a[mid - 1] < value: return mid
            else:
                high = mid - 1

        else:
            low = mid + 1

    return -1

##查找第一个值小于等于给定值的元素
def binary_search_4(a:List[int],value):

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        # print(mid)

        if a[mid] > value:
            high = mid - 1

        else:
            if mid == len(a) - 1 or a[mid + 1] > value: return mid
            else:
                low = mid + 1

    return -1



if __name__ == "__main__":

    a = [1,5,9,6,3,4,9,9,12,45,8,59,20]
    a = sorted(a)
    print(a)
    print(binary_search_1(a, value=9))
    print(binary_search_2(a, value=9))
    print(binary_search_3(a, value=10))
    print(binary_search_4(a, value=10))
