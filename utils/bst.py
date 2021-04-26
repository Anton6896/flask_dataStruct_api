class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, value, node: Node):
        if value < node.data:
            if node.left is None:
                node.left = Node(value)
                return
            else:
                self._insert(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = Node(value)
                return
            else:
                self._insert(value, node.right)
        else:
            return

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

        return self

    def _print_inorder(self, root):
        if root:
            self._print_inorder(root.left)
            print(root.data, end=" - ")
            self._print_inorder(root.right)

    def print(self):
        return self._print_inorder(self.root)


if __name__ == '__main__':
    bs = BST()
    bs.insert(2)
    bs.insert(1)
    bs.print()
