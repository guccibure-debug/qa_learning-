# числа 
age = 25  #int
price = 99.99  #float

#строки
name = "Костя"  #str
greeting = f"Привет, {name}!"  #f-строка (важно!)

#булевы
is_active = True 

#списки (изменяемые)
fruits = ["яблоко", "банан", "груша"]

#словари (ключ:значение)
user = {"name":"Костя", "age":25}

#Кортежи (неизменяемые)
coordinates = (10,20)

print(greeting)
print(fruits[0]) 
print(user["name"])


#условие 
age = 18
if (age>=18):
    print("Совершеннолетний")
else:
    print("ребёнок")

#цикл for
for fruit in fruits:
    print(fruit)

#цикл с диапазоном
for i in range(1,4):
    print(i)

#функции
def add(a,b):
    return a+b

def is_adult(age):
    return age>=18

print(add(2,3))
print(is_adult(19))

def multiply(a, b):
    return a*b
print (multiply(3,3))

def is_even(n):
    return n % 2 == 0
print (is_even(191))

def get_max(numbers):
    """Возвращает максимальное число в списке (без max())."""
    if not numbers:          # проверка на пустой список
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum
print (get_max([3,5,2,2,3,4,5]))

def count_vowels(text):
    vowels = "aeiouаоеу"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
print(count_vowels("hello world"))  #считает количество гласных

def reverse_string(text):
    return text[::-1]
print(reverse_string("какая-то строка")) #переворачивает строку 1 вариант

def reverse_string_1(text):
    result = ""
    for char in text:
        result = char + result
    return result
print(reverse_string_1("яблоко")) #переворачивает строку 2 вариант