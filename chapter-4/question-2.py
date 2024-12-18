# Write function to check the brackets balance


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

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

        val = self._top.value

        del self._top

        self._top = next_node

        self._size -= 1

        return val

    def __repr__(self):
        current_node = self._top
        values = ""
        while current_node:
            values += f", {current_node.value}"
            current_node = current_node.next
        plural = "" if self._size == 1 else "s"
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'


def check_balance(text):
    # create a dictionary for brackets
    brackets = {"[": "]", "{": "}", "(": ")"}

    # create initial count and stack
    count = 0
    stack = Stack()

    for index, char in enumerate(text):
        # if char is one of the open brackets then push into stack
        if char in brackets.keys():

            # if char is one of the open brackets but at the end of the string then return the error
            if index == len(text) - 1:
                return f"Match error at position {index}"

            # push the char into the stack
            stack.push(char)

        # if char is one of the close brackets
        elif char in brackets.values():

            # if the stack is empty(no open bracket included in the stack) then return the error
            if stack._size == 0:
                return f"Match error at position {index}"

            # if the close bracket char match the open brackets char in the stack then increase count by 1 then pop the open bracket char in the stack
            if char == brackets[stack._top.value]:
                count += 1
                stack.pop()

            # if the close bracket char doesn't match the open brackets char in the stack then return error
            else:
                return f"Match error at position {index}"

    return f"Ok - {count}"


print(check_balance("a[b}c"))
