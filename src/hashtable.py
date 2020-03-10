# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, key):
        return hash

    def _hash_mod(self, key):
        return self._hash(key) % self.capacity  # gets the remainder
        #

    def insert(self, key, value):
        new_hash_index = LinkedPair(key, value)
        hash_index = self._hash_mod(key)
        if self.storage[hash_index] is not None:  # bucket exists already
            if self.storage[hash_index].key == key:  # check if first node in bucket is the key we are looking for
                self.storage[hash_index] = new_hash_index  # if it is then replace node w new node
                return
            current = self.storage[hash_index]  # first node in bucket is not the key we are looking for
            while current.next is not None:  # iterate through until we find the key
                if current.key == key:
                    current = new_hash_index  # update node to new node values (key,value)
                    break
                current = current.next  # lets us iterate
            current.next = new_hash_index  # bucket does not exist then add node to new bucket
        else:
            self.storage[hash_index] = new_hash_index

    def remove(self, key):
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            self.storage[index] = None  # if found the index then remove it
        else:
            print("warning:key not found")

    def retrieve(self, key):
        bucket_index = self._hash_mod(key)
        if self.storage[bucket_index] is not None:
            # if the first node at the bucket is equal to the key = there is only 1 node = return value
            if self.storage[bucket_index].key == key:
                return self.storage[bucket_index].value
            # if the first node doesn't equal to the key = iterate through bucket (linked list) until you get the bucket
            else:
                bucket = self.storage[bucket_index]
                while bucket.key is not key and bucket is not None:
                    bucket = bucket.next
                return bucket.value
        else:
            return None

    def resize(self):
        temp_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity
        for bucket in temp_storage:
            if bucket is None:
                pass
            elif bucket.next is None:
                self.insert(bucket.key, bucket.value)
            else:
                while bucket is not None:
                    self.insert(bucket.key, bucket.value)
                    bucket = bucket.next


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