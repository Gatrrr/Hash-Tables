# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.size = 0
        self.storage = [None] * capacity


    def _hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum


    def _hash_djb2(self, key):
        hash = 5381
        for c in key:
            hash = (hash*33) + ord(c)
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        self.size += 1
        index = self._hash_mod(key)
        node = self.storage[index]
        if node is None:
            self.storage[index] = node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = node(key, value)



    def remove(self, key):
        index = self.hash(key)
        node = self.storage[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            return result


    def retrieve(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value


    def resize(self):
        new_storage = [None] * (self.capacity * 2)
        for i in range(self.capacity):
            #check for a key, value pair to rehash
            if self.storage[i] != None:
                key = self.storage[i].key
                value = self.storage[i].value
                #rehash using a new storage size
                index = self._hash(key) % (self.capacity * 2)
                new_storage[index] = LinkedPair(key, value)

        self.storage = new_storage
        print(self.storage)




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
