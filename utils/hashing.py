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

    def custom_hash(self, key) -> int:
        # hashing function implementation (for an example only)!! this func is full in collisions
        hash_value = 0
        for i in key:
            hash_value += ord(i)  # asii repr
            # modulo insure that size never bigger than table
            hash_value = (hash_value * ord(i)) % self.table_size
        return int(hash_value)

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:  # it is empty
            self.hash_table[hashed_key] = Node(Data(key, value))

        else:  # there is collision -> add ti linked list new Node with Data
            self.hash_table[hashed_key].next_node(Node(Data(key, value)))
