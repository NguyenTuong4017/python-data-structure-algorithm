#delete the last value of linked list
import time
class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f'<ListNode: {self.data}>'
class SinglyLinkedList():
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'
     
    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node
    def pop(self):
        #check if the list is empty then return None
        if self._head is None:
            return None
        else:
            current_node = self._head
            
            #check if the list has only one value
            if current_node.next is None:
                val = current_node
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

#Time to pop 50000 elements: 67.143044 seconds [method 1] (use 2 while loops, first to get the last value, second to change the pointer)
# Time to pop 50000 elements: 15.605117 seconds

# list = SinglyLinkedList()
# for i in 'abc':
#     list.append(i)
# val = list.pop()
# print(val, list)