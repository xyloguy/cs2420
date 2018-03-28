class Node:
    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None

    def get(self):
        return self.item

    def set(self, item):
        self.item = item

    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return not self < other and not other < self

    def __gt__(self, other):
        return not self <= other

    @property
    def left(self):
        return self.left_child

    @property
    def right(self):
        return self.right_child

    @property
    def val(self):
        return self.get()

    @val.setter
    def val(self, val):
        self.set(val)

    @right.setter
    def right(self, node):
        self.right_child = node

    @left.setter
    def left(self, node):
        self.left_child = node

    # TODO: delete method
    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """

        if self.val == key:
            # found the node we need to delete

            if self.right and self.left:

                # get the successor node and its parent
                [psucc, succ] = self.right.__find_min(self)

                # splice out the successor
                # (we need the parent to do this)
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor
                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                # "easier" case
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.val > key:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                    # else the key is not in the tree

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

    def __find_min(self, parent):
        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the
        # call can return both the parent to the successor and the successor

        if self.left:
            return self.left.__find_min(self)
        else:
            return [parent, self]