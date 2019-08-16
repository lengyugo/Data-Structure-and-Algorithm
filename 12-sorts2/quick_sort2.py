import random
import numpy as np



def QuickSort(a):

    if a is None or len(a) < 1:
        return a

    def swap(a,low,upper):
        tmp = a[low]
        a[low] = a[upper]
        a[upper] = tmp

        return a

    def quicksort_twoway(a,low,upper):

        if low >= upper:
            return a

        swap(a,low,int(random.uniform(low,upper)))
        tmp = a[low]
        i,j = low,upper
        while True:
            i += 1
            while i<= upper and a[i] <= tmp:
                i += 1
            while a[j] > tmp:
                j -= 1
            if i >= j:
                break
            swap(a,i,j)

        swap(a,low,j)
        quicksort_twoway(a,low,j-1)
        quicksort_twoway(a,j+1,upper)
        return a

    return quicksort_twoway(a,0,len(a)-1)

if __name__ == "__main__":

    a1 = [3, 9, -6, 4, 10]
    a2 = [2, 3, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = np.random.randint(1,100,size=50)
    QuickSort(a1)
    print(a1)
    QuickSort(a2)
    print(a2)
    QuickSort(a3)
    print(a3)
    QuickSort(a4)
    print(a4)
