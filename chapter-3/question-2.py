#Implementing pop method for a Singly linked list with tail
import time
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
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

        
    def pop(self):
        if self._tail is None:
            return None
        
        current_node = self._head
        
        if self._size == 1:
            val = self._tail
            self._head = None
            self._tail = None
            self._size -= 1
            return val.data
        else:
            val = self._tail
            while current_node is not None:
                if current_node.next == self._tail:
                    self._tail = current_node
                    current_node.next = None
                    self._size -= 1
                    return val.data
                current_node = current_node.next
                

        
        
 # Measure running time
def measure_pop_time(linked_list, num_operations):
    start_time = time.time()
    for _ in range(num_operations):
        linked_list.pop()
    end_time = time.time()
    return end_time - start_time           
        
                    
            
# Create a linked list and populate it with data
linked_list = SinglyLinkedList()
num_elements = 50000  # Number of elements to append
for i in range(num_elements):
    linked_list.append(i)
  
# Measure the time it takes to pop all elements
pop_time = measure_pop_time(linked_list, num_elements)
print(f"Time to pop {num_elements} elements: {pop_time:.6f} seconds")

# Time to pop 50000 elements: 36.523009 seconds

	
	
# mylist = SinglyLinkedList()
# for c in 'abc':
#     mylist.append(c)
# val = mylist.pop()
# mylist.append('c')
# mylist.append('d')
# val = mylist.pop()
# print(val, mylist)