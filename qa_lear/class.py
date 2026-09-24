class User:
    #класс описывающий пользователя

    def __init__(self, name, age, mail):
        """Конструктор — вызывается при создании объекта."""
        self.name = name   #атрибут объекта 
        self.age = age
        self.mail = mail

    def is_adult(self):
        """Метод — функция внутри класса."""
        return self.age >=18

    def greet(self):
        return(f"Привет {self.name}")

    def mail1(self):
        return(self.mail)

    # Создаём объект (экземпляр класса)
user1 = User("Костя", 21, "kostya@example.com")

print(user1.name)
print(user1.is_adult())
print(user1.greet())
print(user1.mail1())

class Admin(User): # Admin наследуется от User. Дочерний класс получает все методы и атрибуты родителя
    def __init__(self, name, age, mail, permissions):
        super().__init__(name, age, mail)   # вызываем конструктор родителя User
        self.permissions = permissions

    def ban_user(self, user):
        """Только у админа есть этот метод"""
        return f"{user.name} забанен"   

admin = Admin("Пётр", "25", "petr@mail.ru", ["ban", "delete"])
print(admin.greet())
print(admin.ban_user(user1))
print(user1.age)  


class Animal:
    def make_sound(self):
        return "звук"

class Dog(Animal):
    def make_sound(self):
        return "гав"

class Cat(Animal):
    def make_sound(self):
        return "мяу"

# Один и тот же вызов — разный результат
for animal in [Dog(), Cat()]:
    print(animal.make_sound())