def quicksort(L):
    qsort(L,0,leng(L)-1)

def qsort(L,first,last):
    if first < last:
        qsort(L,first,split-1)
        qsort(L,split+1,last)

def partition(L,first,last):
    # 选取第一个为 pivot
    pivot = L[first]
    leftmark = first+1
    rightmark = last
    while True:
        while L[leftmark]<=pivot:
            pass