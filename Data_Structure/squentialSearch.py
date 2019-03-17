# 顺序查找
def sequentialSearch(list, value):
    start = 0
    while len(list) > start:
        if list[start] == value:
            return True
        else:
            start += 1

            if start == len(list) - 1:
                return False

# 无序列表查找
def OrdersequentialSearch(alist, item):
    start = 0

    while len(alist) > start:
        if alist[start] == item:
            return True
        else:
            if alist[start] > item:
                return False
            else:
                start += 1

                if start == len(alist) - 1:
                    return False

# 二分搜索,针对顺序列表
def binarySearch(alist, item):
    low = 0
    high = len(alist) - 1

    while low <= high:


        mid = (low + high) // 2

        if alist[mid] < item:
            low = mid + 1

        elif alist[mid] > item:
            high = mid - 1

        else:
            return True

    return False

# 递归调用的二分搜索
def binarySearchRecursion(alist, item):
    low = 0
    high = len(alist) - 1
    count = 0

    while low <= high:

        mid = (low + high) // 2

        if alist[mid] < item:
            return binarySearchRecursion(alist[mid+1: ], item)

        elif alist[mid] > item:
            return binarySearchRecursion(alist[ : mid-1])

        else:
            return True
    return False















if __name__ == "__main__":
    l = [i for i in range(10000)]
    print(sequentialSearch(l, 123456))
    print(OrdersequentialSearch(l, 123456))
    print(binarySearch(l, 123456))
    print(binarySearchRecursion(l, 123456))