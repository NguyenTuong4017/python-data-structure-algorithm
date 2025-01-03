class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        curr_index = self._size - 1

        parent_index = (curr_index - 1) // 2

        while self._heap[curr_index] < self._heap[parent_index]:

            temp = self._heap[curr_index]
            self._heap[curr_index] = self._heap[parent_index]
            self._heap[parent_index] = temp

            curr_index = parent_index
            if curr_index == 0:
                break
            parent_index = (curr_index - 1) // 2


h = Heap()
h._heap = [3, 6, 5, 9, 7, 8, 2]
h._size = 7
h._float()
print(h._heap)
