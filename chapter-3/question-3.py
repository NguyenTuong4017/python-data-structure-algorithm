#Implement remove method for a Singly linked list with tail

class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'

class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if self._head is None:
            self._head = self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node
        
        # Update list's size
        self._size += 1

    def pop(self):
            """
        Removes the last node of the list
        
        Parameters: None
        
        Returns:
            The content of the removed node. If list is empty, returns None
            """
        #check if the list is empty then return None
            if self._head is None:
                return None
            else:
                current_node = self._head
                
                #check if the list has only one value
                if current_node.next is None:
                    val = current_node
                    
                    #delete the node
                    del(current_node)
                    
                    self._head = None
                    return val.data
                #if the next next node is None then get the node before the last node
                while current_node.next.next is not None:
                    current_node = current_node.next
                #assign last node to val
                val = current_node.next
                #change the pointer to None
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
            raise(ValueError('Index out of bounds'))

        # Prepare some variables to make the necessary changes
        # The new node will be inserted between previous_node and next_node
        previous_node = None
        next_node = self._head
        # Move to the given index and update pointer variables
        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        # Create new node. It's next pointer points to next node or None
        new_node = ListNode(value, next_node)

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

    def remove(self, index):
        """
        Remove a new node from the position given by the index

        Parameters:
        - 'index': The position where to insert the new node

        Returns: The value of the node being removed
        """
        #check if index is valid
        if index > self._size or index < 0:
            raise(ValueError('Index out of bounds'))
        
        #check if remove the last value
        if index == self._size-1:
            val = self._tail
            self.pop()
            return val.data
        
        #check if remove the first value
        if index == 0:
            val = self._head
            self._head = val.next
            self._size -= 1
            return val.data
        
        
        
        previous_node = None
        
        current_node = self._head
        
        #assign the previous node to the node before the deleted node, assign the current node to the removed node
        for _ in range(index):
            previous_node = current_node
            current_node = current_node.next
        
        #assign removed node to val
        val = current_node
        
        #update the pointer
        previous_node.next = current_node.next
        current_node = None
        
        #update list size
        self._size -= 1
        
        return val.data
        
        
        
        
        
        
mylist = SinglyLinkedList()

for i in range(1, 6):
    mylist.append(i*10)
val = mylist.remove(2)
print(val, mylist)
