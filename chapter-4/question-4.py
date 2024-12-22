# Implement a Node based Queue


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<Node: {self.data}>"


class DoublyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        plural = "" if self._size == 1 else "s"
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = Node(value, next=None)

        # If list is empty, update head and tail pointers
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # In any other case, update tail node to point to the new element
            # and update tail pointer. The new node already points to its
            # previous element
            self._tail.next = new_node
            self._tail = new_node

        # update size
        self._size += 1

    def pop(self):
        """
        Removes the last node of the list

        Parameters: None

        Returns:
            The content of the removed node. If list is empty, returns None
        """
        # check if the list is empty then return None
        if self._head is None:
            return None
        else:
            current_node = self._head

            # check if the list has only one value
            if current_node.next is None:
                val = current_node

                # delete the node
                del current_node

                self._head = None
                return val.data
            # if the next next node is None then get the node before the last node
            while current_node.next.next is not None:
                current_node = current_node.next
            # assign last node to val
            val = current_node.next
            # change the pointer to None
            current_node.next = None

            return val.data

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        # Check if index is inside bounds
        if index < 0 or index > self._size:
            raise (ValueError("Index out of bounds"))

        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # Create new node. It's next pointer points to next node or None
        new_node = Node(value, next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node

        # If insert at the end, update tail
        if previous_node == self._tail:
            self._tail = new_node

        # Update list size
        self._size += 1


class Queue:
    def __init__(self):
        self.node_list = DoublyLinkedList()
        self._size = self.node_list._size

    def enqueue(self, data):
        self.node_list.insert(0, data)
        self._size += 1

    def __repr__(self):
        values = ""
        current_node = self.node_list._head

        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        plural = "" if self._size == 1 else "s"

        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def dequeue(self):

        if self._size > 0:
            val = self.node_list.pop()
            self._size -= 1
            return val

        return None


queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
val = queue.dequeue()
print(val, queue)
