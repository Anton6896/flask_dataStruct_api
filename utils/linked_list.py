"""
for simplicity using single way list
"""


class Node:
    # will hol objects type User from server
    def __init__(self, data: {} = None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, node: Node = None):
        self.head = node
        self.last_node = None

    def insert_beginning(self, node: Node):
        if self.head is None:
            self.head = node
            self.last_node = self.head

        else:
            tmp = self.head
            self.head = node
            self.head.next_node = tmp

    def insert_to_end(self, node: Node):
        if self.head is None:
            self.insert_beginning(node)

        else:
            if self.last_node is None:
                # for this implementation will newer get here on running (theoretically)
                tmp = self.head
                while tmp.next_node:
                    tmp = tmp.next_node

                tmp.next_node = node
                self.last_node = tmp.next_node

            else:
                self.last_node.next_node = node
                self.last_node = self.last_node.next_node

    def find(self, data) -> bool:
        pass

    def delete(self, user_id) -> bool:
        node = prev = self.head
        if self.head.data["id"] is int(user_id):
            self.head = node.next_node
            return True

        while node:
            if node.data["id"] is int(user_id):
                prev.next_node = node.next_node  # take out current node
                return True

            prev = node  # order is important !!!
            node = node.next_node

        return False

    def print(self):
        if self.head is None:
            print('-- List is empty ...')

        tmp = self.head
        print("<>", end=" ")
        while tmp:
            print(tmp, end=" -> ")
            tmp = tmp.next_node
        print("|")

    def to_list(self):
        my_list = []
        if self.head:
            node = self.head
            while node:
                my_list.append(node.data)
                node = node.next_node
        return my_list

    def get_user_by_id(self, user_id: int):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
