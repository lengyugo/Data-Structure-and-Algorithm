"""
    merge_sort
    归并排序
"""

from typing import List

#分成两个数组
def merge_sort(a:List[int]):
    merge_sort_c(a,0,len(a)-1)

#对两组数据分别排序
def merge_sort_c(a:List[int],low:int,high:int):

    if low < high:
        q = low + (high - low) // 2
        merge_sort_c(a,low,q)  ##递归
        merge_sort_c(a,q+1,high)
        merge(a,low,q,high)

##将排序好的两组数据合并
def merge(a:List[int],low:int,q:int,high:int):
    i,j = low,q + 1
    tmp = []

    while i <= q and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

#将有剩余的数据加入到tmp末尾
    start = i if i <= q else j
    end = q if i <= q else high
    tmp.extend(a[start:end+1])
    a[low:high + 1] = tmp


if __name__ == "__main__":
    a1 = [3, 5, 9, 7, 8]
    a2 = [2, 2, 3, 2]
    a3 = [4, 5, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]

    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)



