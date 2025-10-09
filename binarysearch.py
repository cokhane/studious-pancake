def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = left + right
        print(mid)
        if targetVal == arr[mid]:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 2

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")