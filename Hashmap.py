class HashMap:
    class Entity:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    class Bucket:
        def __init__(self):
            self.entries = []

        def get(self, key):
            for entry in self.entries:
                if entry.key == key:
                    return entry.value
            return None

        def add(self, entity):
            for entry in self.entries:
                if entry.key == entity.key:
                    old_value = entry.value
                    entry.value = entity.value
                    return old_value
            self.entries.append(entity)
            return None

        def remove(self, key):
            for i in range(len(self.entries)):
                if self.entries[i].key == key:
                    return self.entries.pop(i).value
            return None

    def __init__(self, init_bucket_count=16, load_factor=0.5):
        self.size = 0
        self.bucket_count = init_bucket_count
        self.load_factor = load_factor
        self.buckets = [None] * self.bucket_count

    def calculate_bucket_index(self, key):
        return hash(key) % self.bucket_count

    def recalculate(self):
        old_buckets = self.buckets
        self.bucket_count *= 2
        self.buckets = [None] * self.bucket_count
        for bucket in old_buckets:
            if bucket:
                for entry in bucket.entries:
                    self.put(entry.key, entry.value)

    def put(self, key, value):
        if self.bucket_count * self.load_factor <= self.size:
            self.recalculate()

        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            bucket = self.Bucket()
            self.buckets[index] = bucket

        entity = self.Entity(key, value)
        res = bucket.add(entity)
        if res is None:
            self.size += 1
        return res

    def get(self, key):
        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            return None
        return bucket.get(key)

    def remove(self, key):
        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if bucket is None:
            return None
        res = bucket.remove(key)
        if res is not None:
            self.size -= 1
        return res

    def __iter__(self):
        return self.HashMapIterator(self)
    
    def items(self):
        entries = []
        for bucket in self.buckets:
            if bucket and bucket.entries:
                for entry in bucket.entries:
                    entries.append(entry)
        return entries

    class HashMapIterator:
        def __init__(self, hashmap):
            self.hashmap = hashmap
            self.bucket_index = 0
            self.current_node = None
            self.find_next_node()

        def __iter__(self):
            return self

        def __next__(self):
            if self.current_node is None:
                raise StopIteration
            entity = self.current_node.value
            self.current_node = self.current_node.next
            if self.current_node is None:
                self.find_next_node()
            return entity

        def find_next_node(self):
            while self.bucket_index < len(self.hashmap.buckets):
                bucket = self.hashmap.buckets[self.bucket_index]
                if bucket and bucket.entries:
                    self.current_node = bucket.entries[0]
                    self.bucket_index += 1
                    return
                self.bucket_index += 1
            self.current_node = None
