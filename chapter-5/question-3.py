class Node:
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ""
        right = self._right_child if self._right_child is not None else ""
        return f"{self.data}<{left}><{right}>#"


class Tree:
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f"<Tree: {self._root_node}>"

    def insert(self, data):
        """
        Inserts a new value in the BST

        Parameters:
        - 'data': Value or data to insert

        Returns: None
        """
        # Let's use a couple of pointers to traverse the tree
        # following BST rules and find the parent of the node
        # to be inserted
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        # After the loop, parent_node variable is parent node or None if Tree is empty
        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                # If tree is empty, just make the new node the root node
                self._root_node = new_node
            else:
                # If tree is not empty and parent_node is None,
                # probably is an error.
                raise (ValueError)
        elif new_node.data < parent_node.data:
            # If value of new node is smaller than parent's, add new node to its left
            parent_node._left_child = new_node
        else:
            # If value of new node is bigger than parent's, add new node to its right
            parent_node._right_child = new_node

    def _find(self, data):
        """
        Find the node containing the data.

        Parameters:
        - 'data': The data to be found

        Returns:
        - The node that contains such data or None if data is not found
        """
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None

    def _detach_node(self, node):
        """
        Detach a node from the tree. Node to be detached has one child at most.
        An error will be raised otherwise.
        """

        current_node = self._find(node.data)

        if current_node == self._root_node:
            if current_node._left_child == None and current_node._right_child == None:
                self._root_node = None
            else:
                raise ValueError

        else:

            pnode = current_node._parent

            if current_node._left_child == None and current_node._right_child == None:
                if current_node.data < pnode.data:
                    current_node._parent = None
                    pnode._left_child = None
                else:
                    current_node._parent = None
                    pnode._right_child = None
            else:
                if current_node._left_child == None:
                    child = current_node._right_child
                    current_node._right_child = None
                    current_node._parent = None

                    if child.data > pnode.data:
                        pnode._right_child = child
                    else:
                        pnode._left_child = child
                else:
                    child = current_node._left_child
                    current_node._left_child = None
                    current_node._parent = None
                    if child.data > pnode.data:
                        pnode._right_child = child
                    else:
                        pnode._left_child = child


tree = Tree()
tree.insert(50)
tree.insert(40)
tree.insert(60)
node = tree._find(50)
try:
    tree._detach_node(node)
except ValueError:
    pass
print(tree._root_node)
