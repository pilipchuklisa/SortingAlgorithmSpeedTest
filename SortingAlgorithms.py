async def bubble_sort_async(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


async def selection_sort_async(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


async def insertion_sort_async(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert


async def heap_sort_async(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        await heapify_async(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        await heapify_async(nums, i, 0)


async def heapify_async(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        await heapify_async(nums, heap_size, largest)


async def merge_sort_async(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = await merge_sort_async(nums[:mid])
    right_list = await merge_sort_async(nums[mid:])
    return await merge_async(left_list, right_list)


async def merge_async(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


async def quick_sort_async(nums):
    async def _quick_sort_async(items, low, high):
        if low < high:
            split_index = await partition_async(items, low, high)
            await _quick_sort_async(items, low, split_index)
            await _quick_sort_async(items, split_index + 1, high)

    await _quick_sort_async(nums, 0, len(nums) - 1)


async def partition_async(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

sorting_algorithms = [bubble_sort_async, selection_sort_async, insertion_sort_async, heap_sort_async, merge_sort_async, quick_sort_async]
sorting_names = ['bubble sort', 'selection sort', 'insertion sort', 'heap sort', 'merge sort', 'quick sort']
