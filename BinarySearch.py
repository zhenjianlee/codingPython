#        0 1 2 3 4 5 6 7
array = [1,2,3,4,5,6,7,8]

def binarySearch(arr,target):
    low = 0
    high = len(arr)-1

    while low<= high:
        mid = low+(high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            high=mid-1
        elif arr[mid]<target:
            low=mid+1



print(binarySearch(array,6))
print(binarySearch(array,2))
print(binarySearch(array,8))
print(binarySearch(array,1))