def binary_search(arr, t):
    l, r = 0, len(arr)
    steps = 0
    
    while l < r:
        steps += 1
        mid = int((l+r)/2)

        if arr[mid] == t:
            print('steps: ', steps)
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            r = mid
    return -1
        
arr_a = [1, 2, 3, 4, 5]
arr_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

binary_search(arr_a, 3)
binary_search(arr_b, 3)
binary_search(arr_c, 3)
