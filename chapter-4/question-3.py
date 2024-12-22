# Implement a Stack based Queue
class StackBasedQueue:
    def __init__(self):
        # create initial inbound and outbound stack
        self._InboundStack = []
        self._OutboundStack = []

        self._size = 0

    def __repr__(self):
        plural = "" if self._size == 1 else "s"
        values = [str(c) for c in self._InboundStack]
        values.extend([str(c) for c in self._OutboundStack][::-1])
        return (
            f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'
        )

    def enqueue(self, data):

        # insert element at first index
        self._InboundStack.insert(0, data)
        self._size += 1

    def dequeue(self):

        if not self._OutboundStack:
            while self._InboundStack:
                self._OutboundStack.append(self._InboundStack.pop())

        if len(self._OutboundStack) > 0:
            val = self._OutboundStack.pop(0)
            self._size -= 1
        else:
            val = None

        return val
