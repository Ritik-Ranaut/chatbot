def binary_search(arr, key):
    """Performs binary search on a sorted list."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid].lower() == key.lower():
            return mid
        elif arr[mid].lower() < key.lower():
            left = mid + 1
        else:
            right = mid - 1

    return -1
