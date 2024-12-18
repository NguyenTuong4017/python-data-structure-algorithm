import time
import random

class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def __iter__(self):
        self._iter_index = self._head
        return self

    def __next__(self):
        if self._iter_index:
            value = self._iter_index.data
            self._iter_index = self._iter_index.next
            return value
        else:
            raise StopIteration
            
    def __getitem__(self, index):
        """
        Return value at index
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        
        # Return the value
        return current_node.data

    def __setitem__(self, index, value):
        """
        set value at index k with val
        """
        # Check if index is inside bounds
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        # Move to the given index
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        # Set the value
        current_node.data = value

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value. This is the last node, so next is None,
        # but there can be already some node in the list, hence the prev value
        new_node = ListNode(value, next=None, prev=self._tail)

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

        # Create new node with right value and pointers
        new_node = ListNode(value, prev=previous_node, next=next_node)

        # If insert at front, update head
        if previous_node is None:
            self._head = new_node
        else:
            # If not, update previous node
            previous_node.next = new_node
        
        # If insert at the end, update tail
        if next_node is None:
            self._tail = new_node
        else:
            # If not, update next node
            next_node.prev = new_node

        # Update list size
        self._size += 1

    def remove_by_value(self, value):
        """
        Remove first node with given value and return its position
        """
        # Find if there is a node with given value
        current_node = self._head
        index = 0
        while current_node and current_node.data != value:
            current_node = current_node.next
            index += 1
        
        # If value was not found, current_node is None
        if not current_node:
            return None

        previous_node = current_node.prev
        next_node = current_node.next

        # If node to remove is the first node, update head
        if previous_node is None:
            self._head = next_node
        else:
            # If not, update previous node
            previous_node.next = next_node

        # If node to remove is last node, update tail
        if next_node is None:
            self._tail = previous_node
        else:
            # If not, update next node
            next_node.prev = previous_node

        # Update size, remove the node and return its index
        self._size -= 1
        del(current_node)
        return index

    def contains(self, value):
        """
        Returns True if value if found in the list and False if not
        """
        for node_value in self:
            if value == node_value:
                return True
        return False

    def clear(self):
        """
        Clear the list
        """
        # Remove all nodes
        current_node = self._head
        while current_node:
            next = current_node.next
            del(current_node)
            current_node = next

        # Update pointers and size
        self._head = self._tail = None
        self._size = 0

    def remove(self, index):
        """
        Remove a new node from the position given by the index

        Parameters:
        - 'index': The position where to insert the new node

        Returns: The value of the node being removed
        """

        #check if index is valid
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))
        
        #check if the list is empty
        if self._size == 0:
            raise ValueError("Cannot remove from an empty list.")
        
        #if remove the last index using pop method
        if index == self._size - 1:
            val = self.pop()
            self._size -= 1
            return val
        
        #if remove the first index 
        elif index == 0:
            val = self._head.data
            
            #create the next node 
            next_node = self._head.next
            
            #change the pointer of next node to None (same as old head node)
            next_node.prev = None
            
            #delete the old head node
            del(self._head)
            
            #assign the next node as the new head node
            self._head = next_node
            
            #update the size
            self._size -= 1
            
            return val
        
        #if remove the node in the middle
        else:
            #find the node at the inputted index
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next
            
            #create the previous and next node of the current node
            next_node = current_node.next
            prev_node = current_node.prev
            
            #update the pointer of the next node and previous node to link to each other
            next_node.prev = prev_node
            prev_node.next = next_node
            
            #create the return value (removed node)
            val = current_node.data
            
            #delete the removed node
            del(current_node)
            
            #update the size
            self._size -= 1
            
            return val

	
	
	
def measure_remove_time(dll, index):
    """
    Measure the execution time of the insert function.

    Parameters:
    - dll: The DoublyLinkedList object
    - index: The position where to insert the new node
    - value: The value to insert

    Returns:
    - Execution time in seconds
    """
    start_time = time.perf_counter()  # Start the timer
    dll.remove(index)          # Call the insert method
    end_time = time.perf_counter()    # Stop the timer
    
    execution_time = end_time - start_time  # Calculate the elapsed time
    return execution_time

	
	


# Run time test
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    for i in range(1, 1000001):  # Populate the list
        mylist.append(i)

    # Measure time for different insertions
    time1 = measure_remove_time(mylist, 45967)
    time2 = measure_remove_time(mylist, 53256)
    time3 = measure_remove_time(mylist, 994576)

    print(f"Time to remove at index 45967: {time1:.6f} seconds")
    print(f"Time to remove at index 53256: {time2:.6f} seconds")
    print(f"Time to remove at index 994576: {time3:.6f} seconds")
    
    print("Value at index 45967:", mylist.__getitem__(45967))
    print("Value at index 53256:", mylist.__getitem__(53256))
    print("Value at index 994576:", mylist.__getitem__(994576))