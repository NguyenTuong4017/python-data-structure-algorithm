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


def heap_sort(array):
    # Heapify the array with a Max heap
    for start in range(len(array) // 2 - 1, -1, -1):
        sift_down(array, start, len(array) - 1)
    # As using a max heap, the heap will return the max values,
    # so they should be placed at the end of the array
    end = len(array) - 1  # Last position

    # Loop while heap is not empty
    while end > 0:
        # Swap root and end places
        array[0], array[end] = array[end], array[0]
        # Decrease end. Now heap is one element shorter
        end -= 1
        # Sink the value at the root to maintain the heap property
        sift_down(array, 0, end)
