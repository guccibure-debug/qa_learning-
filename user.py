class User:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    def is_adult(self):
        return self.age >= 18
    
    def greet(self):
        return (f"Привет, меня зовут {self.name}")
        
    def change_email(self, new_email):
        if "@" in new_email:
            self.mail = new_email
            return(self.mail)
        else:
            raise ValueError("некорректный mail")
        
user1 = User("Костя", 21, "lmao@gmail.com")
print(user1.is_adult())
print(user1.mail)
print(user1.greet())
print(user1.change_email("new@mail.ru"))

class Admin(User):
    def __init__(self, name, age, mail, permissions ):
        super().__init__(name, age, mail)
        self.permissions = permissions if permissions is not None else []

    def has_permission(self, permission):
        """True, если право есть в списке permissions."""
        return permission in self.permissions

admin1 = Admin("Костя", 30, "lmao@gmail.com", ["read", "write", "delete"])

print(admin1.name)                          # Костя
print(admin1.is_adult())                    # True (унаследовано)
print(admin1.has_permission("delete"))      # True
print(admin1.has_permission("ban"))         # False
 