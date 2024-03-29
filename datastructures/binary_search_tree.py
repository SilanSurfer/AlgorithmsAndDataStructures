"""
Implementation of binary search tree
"""
from __future__ import annotations
from typing import Tuple


class Node():
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
        self._parent = None

    def __str__(self):
        return f"{self._data}"

    def insert(self, data) -> bool:
        if data == self._data:
            return False
        elif data < self._data:
            if not self._left:
                new_node = Node(data)
                new_node._parent = self
                self._left = new_node
                return True
            else:
                return self._left.insert(data)
        else:  # data > self._data
            if not self._right:
                new_node = Node(data)
                new_node._parent = self
                self._right = new_node
                return True
            else:
                return self._right.insert(data)

    def max(self) -> Node:
        current_node = self
        while current_node._right:
            current_node = current_node._right
        return current_node

    def min(self) -> Node:
        current_node = self
        while current_node._left:
            current_node = current_node._left
        return current_node

    def find(self, value) -> Node:
        if value == self._data:
            return self
        elif value < self._data:
            if not self._left:
                return None
            else:
                return self._left.find(value)
        else:  # value > self._data
            if not self._right:
                return None
            else:
                return self._right.find(value)

    def delete(self, key) -> bool:
        node = self.find(key)
        if node:
            if node.left and node.right:  # 2 children
                successor = node.right.min()
                successor_data = successor.data
                node.delete(successor_data)
                node.data = successor_data
                return True
            elif node.left and not node.right:  # 1 child
                if node.parent.data < node.data:  # node is right child
                    node.parent.right = node.left
                else:  # node is left child
                    node.parent.left = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
                return True
            elif node.right and not node.left:  # 1 child
                if node.parent.data < node.data:  # node is right child
                    node.parent.right = node.right
                else:  # node is left child
                    node.parent.left = node.right
                node.right.parent = node.parent
                node.parent = None
                node.right = None
                return True
            else:  # no children
                temp_parent = node.parent
                if temp_parent.right is node:
                    temp_parent.right = None
                elif temp_parent.left is node:
                    temp_parent.left = None
                else:  # this shouldn't happen
                    pass
                node.parent = None
                return True
        else:
            return False

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(str(root))
            result = result + self.inorder_traversal(root.right)
        return result

    def inorder_traversal_non_recursive(self, root):
        node_stack = []
        result = []
        current_node = root
        while current_node or len(node_stack) != 0:
            while current_node:
                node_stack.append(current_node)
                current_node = current_node.left

            current_node = node_stack.pop()
            result.append(str(current_node))
            current_node = current_node.right
        return result

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node):
        self._left = left_node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node):
        self._right = right_node

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        self._parent = node


class BinarySearchTree():
    def __init__(self):
        self._root = None

    def __contains__(self, value) -> bool:
        if self.empty():
            return False
        else:
            node = self._root.find(value)
            return node is not None

    def empty(self):
        return self._root is None

    def insert(self, data) -> bool:
        if self.empty():
            self._root = Node(data)
            return True
        else:
            return self._root.insert(data)

    def find(self, key) -> bool:
        if self.empty():
            return False
        else:
            node = self._root.find(key)
            return node is not None

    def min(self):
        if self.empty():
            return None
        else:
            return self._root.min()

    def max(self):
        if self.empty():
            return None
        else:
            return self._root.max()

    def delete(self, key) -> bool:
        if self.empty():
            return False
        else:
            return self._root.delete(key)

    def print_inorder(self):
        if not self.empty():
            print(" ".join(self._root.inorder_traversal(self._root)))

    def print_inorder_non_recursive(self):
        print(" ".join(self._root.inorder_traversal_non_recursive(self._root)))

if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst.insert(20))
    print(bst.insert(10))
    print(bst.insert(30))
    print(bst.insert(-5))
    print(bst.insert(40))
    print(bst.insert(24))
    bst.print_inorder()
    bst.print_inorder_non_recursive()
    print(bst.min())
    print(bst.max())
    print(-5 in bst)
    print(100 in bst)
    print(bst.delete(-5))
    bst.print_inorder()
    print(bst.insert(-5))
    print(bst.insert(-6))
    bst.print_inorder()
    print(bst.delete(10))
    bst.print_inorder()
    print(bst.insert(45))
    bst.print_inorder()
    print(bst.delete(40))
    bst.print_inorder()
    print(bst.delete(30))
    bst.print_inorder()
    print(bst.insert(44))
    print(bst.insert(43))
    print(bst.insert(47))
    print(bst.insert(46))
    print(bst.insert(48))
    bst.print_inorder()
    print(bst.delete(45))
    bst.print_inorder()
