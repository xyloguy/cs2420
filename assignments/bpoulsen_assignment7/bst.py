from node import Node


class BST:
    def __init__(self):
        self.__root = None

    def insert(self, val):
        if self.find(val):
            return False
        self.__root = self.insert_node(self.__root, val)
        return True

    def insert_node(self, current_node, val):
        if current_node is None:
            current_node = Node(val)
        elif val < current_node.val:
            current_node.left = self.insert_node(current_node.left, val)
        else:
            current_node.right = self.insert_node(current_node.right, val)
        return current_node

    def find(self, val):
        return self.find_node(self.__root, val)

    def find_node(self, current_node, val):
        if current_node is None:
            return False
        elif val == current_node.val:
            return current_node
        elif val < current_node.val.key:
            return self.find_node(current_node.left, val)
        else:
            return self.find_node(current_node.right, val)

    def delete(self, val):
        node = self.find(val)
        node.delete(val)
