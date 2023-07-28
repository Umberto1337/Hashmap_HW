from Hashmap import HashMap
from employee import Employee

# Пример использования:
employee1 = Employee("AAA", 30)
print(hash(employee1))

hash_map = HashMap(4)
hash_map.put("+79005551122", "Александр")
hash_map.put("+79005551123", "Сергей")
hash_map.put("+79005551123", "Алексей")
hash_map.put("+79005551124", "Федя")
hash_map.put("+79005551125", "Антон")
hash_map.put("+79005551126", "Глеб")
hash_map.put("+79005551127", "Игорь")
hash_map.put("+79005551128", "Вася")

search_res = hash_map.get("+790055511221")

v = hash_map.remove("+79005551127")

# Используем метод items() для получения ключей и значений
for entry in hash_map.items():
    print(f"Ключ: {entry.key}, Значение: {entry.value}")

