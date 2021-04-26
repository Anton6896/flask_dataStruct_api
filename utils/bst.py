class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, value, node):
        if not node:
            node = Node(value)

        # small will be left other right
        # let assume that data is comparable obj (if value same -> do nothing)
        if node.data < value:
            self._insert(value, node.left)
        else:
            self._insert(value, node.right)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
