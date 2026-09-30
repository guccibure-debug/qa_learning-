import pytest

def add(x, y):
  if x+y==False:
    raise TypeError("некорректно")
  else:
    return x + y

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email

  def change_email(self, new_email):
    if "@" not in new_email:
      raise ValueError("не тот email")
    self.email = new_email

