def interpolation_search(array, value, start=None, end=None):
    # Prepare the variables this way, so the user can call
    # the function with just the array and value to be searched.
    # If start and none are not defined, the search is conducted
    # in the whole array.
    if start is None:
        start = 0
    if end is None:
        end = len(array) - 1
    # Calculate a midpoint
    midpoint = start + int(
        (end - start) * ((value - array[start]) / (array[end] - array[start]))
    )
    # If the calculated midpoint is not within the search area, return
    if midpoint < start or midpoint > end:
        return None
    # If the value is found at the midpoint, return the index of midpoint

    if array[midpoint] == value:
        return midpoint
    # if the value being searched is smaller than the one in the midpoint
    # and there is at least one element left to the midpoint

    if value < array[midpoint] and midpoint >= start + 1:
        # Perform the search on the left part
        return interpolation_search(array, value, start=start, end=midpoint - 1)
    # if the value being searched is bigger than the one in the midpoint
    # and there is at least one element right to the midpoint

    if value > array[midpoint] and midpoint <= end - 1:
        # Perform the search on the right part
        return interpolation_search(array, value, start=midpoint + 1, end=end)
    return None


array = [1, 2, 3]
print(interpolation_search(array, 2))
