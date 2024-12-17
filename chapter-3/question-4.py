#Implement insert method for a Doubly linked list
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
        # If list is empty, returns None
        if not self._size:
            return None
        
        # Locate previous_node (the node just before last node)
        node_to_remove = self._tail
        previous_node = node_to_remove.prev

        # If node to remove is first node, then update head pointer
        if node_to_remove == self._tail:
            self._head = None
        else:
            # If not, update the pointer of the previous node
            previous_node.next = None   # It is now the last node

        # Update tail pointer
        self._tail = previous_node

        # Update size, remove node and return its content
        self._size -= 1
        value = node_to_remove.data
        del(node_to_remove)
        return value

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

    def insert(self, index, value):
        """
        Insert a new node with value in the position given by the index

        Parameters:
        - 'index': The position where to insert the new node
        - 'value': The value of the new node

        Returns: None
        """
        
        #check if index is valid
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))
            
        
        #create a new node 
        new_node = ListNode(value, next=None,prev=None)
        
        #check if the list is empty
        if self._head == None:
            self._head = new_node
            self._size += 1
        #if insert the new node at the beginning
        elif index == 0:
            #change the pointer of new node
            new_node.next = self._head
            
            #change the pointer of old head
            self._head.prev = new_node
            
            #set the head as the new node
            self._head = new_node
            
            #update the size
            self._size += 1
        #if insert at the ending
        elif index == self._size:
            #change the pointer of new node to the tail
            new_node.prev = self._tail
            
            #change the pointer of tail from None to new node
            self._tail.next = new_node
            
            #set the tail as the new node
            self._tail = new_node
            
            #update the size
            self._size += 1
        else:
            #create a node to get the node at the inputted index
            current_node = self._head
            for _ in range(index):
                current_node = current_node.next
            
            #change the new node pointer, change the next from None to the current node
            new_node.next = current_node
            
            #change the new node pointer, change the prev from None to the current node prev
            new_node.prev = current_node.prev
            
            #change the node before the current node pointer, change the next from current node to new node
            current_node.prev.next = new_node 
            
            #change the current node pointer, change the prev from old prev to the new prev
            current_node.prev = new_node
            
            self._size += 1
            
            
                
def measure_insert_time(dll, index, value):
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
    dll.insert(index, value)          # Call the insert method
    end_time = time.perf_counter()    # Stop the timer
    
    execution_time = end_time - start_time  # Calculate the elapsed time
    return execution_time

	
	
# mylist = DoublyLinkedList()
# for i in range(1, 70001):
#     mylist.append(i)
# mylist.insert(45967, 55)
# mylist.insert(53256, 25)
# mylist.insert(70000, 5)
# print(mylist)


# Run time test
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    for i in range(1, 1000001):  # Populate the list
        mylist.append(i)

    # Measure time for different insertions
    time1 = measure_insert_time(mylist, 45967, 55)
    time2 = measure_insert_time(mylist, 53256, 25)
    time3 = measure_insert_time(mylist, 994576, 5)

    print(f"Time to insert at index 45967: {time1:.6f} seconds")
    print(f"Time to insert at index 53256: {time2:.6f} seconds")
    print(f"Time to insert at index 994576: {time3:.6f} seconds")
    
    print("Value at index 45967:", mylist.__getitem__(45967))
    print("Value at index 53256:", mylist.__getitem__(53256))
    print("Value at index 994576:", mylist.__getitem__(994576))
    
    

