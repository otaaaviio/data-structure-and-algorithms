def quick_sort(arr, left, right):
    if left < right:
        print(arr[left : right - 1])
        pi = partition(arr, left, right)
        quick_sort(arr, left, pi - 1)
        quick_sort(arr, pi + 1, right)


def median_of_three(arr, left, right):
    mid = (left + right) // 2
    if arr[left] > arr[mid]:
        arr[left], arr[mid] = arr[mid], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[mid] > arr[right]:
        arr[mid], arr[right] = arr[right], arr[mid]
    arr[mid], arr[right] = arr[right], arr[mid]
    return arr[right]


def partition(arr, left, right):
    pivot = median_of_three(arr, left, right)
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


# tests

# arr = [2,4,6,7,1,0,10]
# quick_sort(arr, 0, len(arr)-1)
# print(arr)

# tests
