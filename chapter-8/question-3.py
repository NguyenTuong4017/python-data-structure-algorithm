def binary_search_iterative(array, value, start=None, end=None):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1

    midpoint = start + (end - start + 1) // 2

    if array[midpoint] == value:
        return midpoint
    else:
        if value < array[midpoint] and midpoint >= start + 1:
            return binary_search_iterative(array, value, start=start, end=midpoint - 1)
        if value > array[midpoint] and midpoint <= end - 1:
            return binary_search_iterative(array, value, start=midpoint + 1, end=end)

    return None


array = [0, 5, 8, 11, 14, 17, 29, 31, 31, 35, 39, 40, 47, 61, 68, 78, 85, 88, 95, 98]

print(binary_search_iterative(array, 85))
