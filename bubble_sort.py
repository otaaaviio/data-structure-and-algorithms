def bubble_sort(nums):
    size = len(nums)

    for _ in range(size):
        print(nums)  # step validation
        is_sorted = True

        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                is_sorted = False

            if is_sorted:
                return nums

    return nums


# tests

# arr1 = [1, 3, 2, 4, 5]
# bubble_sort(arr1)  # [1, 3, 2, 4, 5]
# print('')
# arr2 = [5, 4, 3, 2, 1]
# bubble_sort(arr2)  # [5, 4, 3, 2, 1]

# tests
