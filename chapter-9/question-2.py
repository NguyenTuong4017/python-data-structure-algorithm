def sift_down(array, start, end):
    """
    This function sinks (if necessary) the given node of a MaxHeap structure
    Parameters:
    - array: The heap array
    - start: The index of the node that should be sunk.
    - end: The end of the heap inside the array. The index of the last node
    Returns: None
    """
    # Let's use a better variable name inside the function
    current = start
    # Loop while there is a left child to compare with
    while (left_child := 2 * current + 1) <= end:
        # Initialize swap var with current
        swap_index = current
        # If left child is smaller than current swap index, use it as swap index
        if array[swap_index] < array[left_child]:
            swap_index = left_child
        # If there is a right child and it is smaller than current swap index, use it asswap index
        right_child = 2 * current + 2
        if right_child <= end and array[swap_index] < array[right_child]:
            swap_index = right_child
        # If swap index has not changed, current element is bigger than its children and function can return
        if swap_index == current:
            return
        # Swap values at current and swap index
        array[current], array[swap_index] = array[swap_index], array[current]
        # Update current to be swap_index (left or right child)
        current = swap_index
