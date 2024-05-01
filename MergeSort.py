import random

size = int(input("Please enter size of array:"))
array = []

for i in range(size):
    array.append(random.randint(0, 1000))

# print(array)


def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1
    # print("Merge:"+str(arr))


def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = []
    right = []

    for i in range(mid):
        left.append(arr[i])

    print("Left=" + str(left))
    for i in range(mid, len(arr)):
        right.append(arr[i])
    print("Right=" + str(right))
    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)


mergeSort(array)
# print(array)
