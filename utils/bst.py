"""
tree will be in use by the server.BlogPost().id for as comparison obj
for test porpoise only, for practice and remember how to !!
"""


class Node:
    def __init__(self, data=None):
        # data = BlogPost() obj  == dict
        self.data = data
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def _insert(self, data_blog: dict, node: Node):
        # data = BlogPost() obj == dict
        if data_blog["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data_blog)
                return
            else:
                self._insert(data_blog, node.left)
        elif data_blog["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data_blog)
                return
            else:
                self._insert(data_blog, node.right)
        else:
            return

    def insert(self, data_blog):
        if not self.root:
            self.root = Node(data_blog)
        else:
            self._insert(data_blog, self.root)
        return self

    def _print_inorder(self, root):
        if root:
            self._print_inorder(root.left)
            print(root.data["id"], end=" - ")
            self._print_inorder(root.right)

    def print(self):
        return self._print_inorder(self.root)

    def search(self, blog_id) -> dict or bool:
        blog_id = int(blog_id)

        if not self.root:
            return False

        return self._search(blog_id, self.root)

    def _search(self, id, node: Node) -> bool:
        if id == node.data["id"]:
            return node.data

        if id < node.data["id"] and node.left:
            return self._search(id, node.left)

        if id > node.data["id"] and node.right:
            return self._search(id, node.right)

        return False


if __name__ == '__main__':
    bs = BST()
    bs.insert({"id": 1}).insert({"id": 10}).insert({"id": 4})
    bs.print()
    print()
    print(bs.search(10))
