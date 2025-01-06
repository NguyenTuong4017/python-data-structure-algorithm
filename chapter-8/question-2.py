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

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """

        index = self._size - 1
        parent = 0

        while 2 * parent + 1 < self._size:
            right = parent * 2 + 2
            left = parent * 2 + 1
            smallest = left

            if right < self._size and self._heap[right] < self._heap[left]:
                smallest = right

            if self._heap[parent] <= self._heap[smallest]:
                break

            if self._heap[parent] > self._heap[smallest]:
                temp = self._heap[parent]
                self._heap[parent] = self._heap[smallest]
                self._heap[smallest] = temp

            parent = smallest


h = Heap()
h._heap = [8, 9]
h._size = 2
h._sink()
print(h._heap)
