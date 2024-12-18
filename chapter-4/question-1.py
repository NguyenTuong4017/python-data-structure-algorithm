#Implement push and pop methods for a Stack structure

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """
        new_node = Node(data)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """
        
        if self._size == 0:
            return None
        
        next_node = self._top.next
        
        val = self._top.data
        
        del(self._top)
        
        self._top = next_node
        
        self._size -= 1
        
        return val

    def __repr__(self):
        current_node = self._top
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

	
mystack = Stack()
for i in range(1,1000000001):
    mystack.push(i)
print(mystack)