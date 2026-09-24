# 1. self
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} говорит Гав!"

d1 = Dog("Рекс")
d2 = Dog("Шарик")
print(d1.bark())
print(d2.bark())

# 2. super()
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def info(self):
        return f"{self.name}, {self.age} мес."

p = Puppy("Бим", 3)
print(p.info())
print(p.bark())   # унаследованный метод

# 3. try/except
try:
    x = int("не число")
except ValueError as e:
    print(f"Ошибка: {e}")
finally:
    print(f"надоело чуток")