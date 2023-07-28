class HashMap:
    def __init__(self, init_bucket_count=16, load_factor=0.5):
        self.size = 0
        self.bucket_count = init_bucket_count
        self.load_factor = load_factor
        self.buckets = [None] * self.bucket_count

    class Entity:
        def __init__(self, key, value):
            self.key = key
            self.value = value

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

    def calculate_bucket_index(self, key):
        return hash(key) % self.bucket_count

    def recalculate(self):
        self.size = 0
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
        if not bucket:
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
        if not bucket:
            return None
        return bucket.get(key)

    def remove(self, key):
        index = self.calculate_bucket_index(key)
        bucket = self.buckets[index]
        if not bucket:
            return None
        res = bucket.remove(key)
        if res is not None:
            self.size -= 1
        return res

    def __iter__(self):
        return self.HashMapIterator()

    class HashMapIterator:
        def __init__(self):
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
            while self.bucket_index < len(self.buckets):
                bucket = self.buckets[self.bucket_index]
                if bucket and bucket.entries:
                    self.current_node = bucket.entries[0]
                    self.bucket_index += 1
                    return
                self.bucket_index += 1
            self.current_node = None

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Пример использования:
employee1 = Employee("AAA", 30)
print(hash(employee1))

hash_map = HashMap(4)

hash_map.put("+79005551122", "Александр")
hash_map.put("+79005551123", "Сергей")
hash_map.put("+79005551123", "Алексей")
hash_map.put("+79005551124", "Игорь")
hash_map.put("+79005551125", "Антон")
hash_map.put("+79005551126", "Федя")
hash_map.put("+79005551127", "Олег")
hash_map.put("+79005551128", "Глеб")

search_res = hash_map.get("+790055511221")

v = hash_map.remove("+79005551127")

for entry in hash_map:
    print(f"Ключ: {entry.key}, Значение: {entry.value}")
