def binary_search(arr, t, l=0, r=None):
    if r is None:
        r = len(arr) - 1

    while l < r:
        mid = int((l + r) / 2)

        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            r = mid
    return -1


def exponential_search(arr, t):
    if arr[0] == t:
        return 0

    n = 1
    while n < len(arr) and arr[n] < t:
        n *= 2

    n = min(n, len(arr) - 1)

    if arr[n] == t:
        return n
    else:
        return binary_search(arr, t, n // 2, n)


# tests

# arr_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# print(exponential_search(arr_a, 9))
# print(exponential_search(arr_a, 11))

# tests
