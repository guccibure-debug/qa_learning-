class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def change_email(self, new_email):
        self.email = new_email
        return self.email