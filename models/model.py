class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def change_email(self, new_email):
        self.email = new_email
        return self.email

    def is_adult(self):
        return self.age >= 18

class Admin(User):
    def __init__(self, name, age, mail, permissions=None):
        super().__init__(name, age, mail)
        self.permissions = permissions if permissions is not None else []

    def has_permission(self, permission):
        return permission in self.permissions

    def is_adult(self):
        return self.age >= 18