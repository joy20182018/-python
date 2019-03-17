# coding:utf-8

# 冒泡排序
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                # temp = alist[i]
                # alist[i] = alist[i+1]
                # alist[i+1] = temp
                alist[i], alist[i+1] = alist[i+1], alist[i]

            passnum = passnum-1

# 选择排序
def SelectSort(alist):
    for pushCount in range(len(alist) - 1, 0, -1):
        max = 0
        for value in range(1, pushCount+1):
            if alist[pushCount] > alist[max]:
                max = pushCount

        alist[max],alist[pushCount] = alist[pushCount], alist[max]

# 插入排序
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue

# 希尔排序
def shellsort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After incements of size", sublistcount, "the list is value", alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position-gap]
        alist[position] = currentvalue



# 归并排序
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    print("Merging ", alist)

# 快速排序
def quickSort(alist):
    quickSortHelper(alist, 0 , len(alist) - 1) # 定第一个点为枢纽值

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
             rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark




def quicksort(alist):
    spotmark = 0
    leftmark = 1
    rightmark = len(alist)-1
    while leftmark < rightmark:
        if alist[leftmark] > alist[spotmark]:
            if alist[rightmark] < alist[spotmark]:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
                done = True
            else:
                if rightmark > leftmark:
                    rightmark -= 1
        else:
            if rightmark > leftmark:
                leftmark += 1



















alist=[20,30,40,90,50,60,70,80,100,110]
# shortBubbleSort(alist)
# SelectSort(alist)
shellsort(alist)
print(alist)