"""
    计数排序
"""

from typing import List
import numpy as np

def counting_sort(a:List[int]):
    length = len(a)
    if length <= 1: return

    max_data = a[0]
    for i in range(length):
        if max_data < a[i]:
            max_data = a[i]

## 将每个数字的个数存起来
    c = []
    #print(max_data)
    for j in range(max_data+1):
        c.append(0)

    for i in a:
        c[i] += 1

    for j in range(1,max_data+1):
        c[j] = c[j - 1] + c[j]

## 定义一个r列表来存储排序好的数据
    r = [1] * length
    d = list(range(length))[::-1]

    for i in d:
        index = c[a[i]] -1
        r[index] = a[i]
        c[a[i]] -= 1

    for i in range(len(r)):
        a[i] = r[i]


    return a

if __name__ == "__main__":
    a = np.random.randint(1,100,size=50)
    # a = [2,5,3,0,2,3,0,3]
    print(a)
    print(counting_sort(a))


