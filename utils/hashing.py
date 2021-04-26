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
        # hashing function implementation (for an example only)!!
        # this func is full in collisions
        hash_value = 0
        for i in key:
            hash_value += ord(i)  # asii repr
            # modulo insure that size never bigger than table
            hash_value = (hash_value ** 2) % self.table_size
        return int(hash_value)

    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:  # it is empty
            self.hash_table[hashed_key] = Node(Data(key, value))

        else:  # there is collision -> add ti linked list new Node with Data
            node = self.hash_table[hashed_key]
            while node.next_node:  # traverse to eng
                node = node.next_node
            node.next_node = Node(Data(key, value))

    def get_value(self, key):
        hashed_key = self.custom_hash(key)

        if self.hash_table[hashed_key]:
            node = self.hash_table[hashed_key]
            while node:
                if node.data.key == key:
                    return node.data.value
                node = node.next_node

        return None

    def print(self):
        for i, val in enumerate(self.hash_table):
            if val:
                print(f" place {i} ---")
                node = val
                while node:
                    print(
                        f"[ key:{node.data.key},"
                        f" hashed_key:{self.custom_hash(node.data.key)},"
                        f" value:{node.data.value} ] ")
                    node = node.next_node
                print("==============================")


if __name__ == '__main__':
    hs = HashTable(4)
    hs.add_key_value("aa", "aa")
    hs.add_key_value("bb", "bb")
    hs.add_key_value('7', '4')
    hs.print()
    print(f"get value 7 : {hs.get_value('7')}")
