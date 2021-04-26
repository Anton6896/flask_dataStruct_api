class Data:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value


class Node:
    def __init__(self, data: Data = None, next_node=None):
        self.data = data
        self.next_node = next_node


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * self.table_size
