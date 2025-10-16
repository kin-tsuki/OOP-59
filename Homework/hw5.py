# Задание №1

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return (f'Название книги: {self.title} Автор: {self.author} '
                f'Количество страниц: {self.pages}')

    def __add__(self, other):
        if self.author == other.author:
            return self.pages + other.pages
        else:
            return 'Нельзя сложить книги разных авторов.'

book1 = Book('Маленькая жизнь', 'Ханья Янагихара', 688)
book2 = Book('Аэропорт', 'Артур Хейли', 640)
book3 = Book('Отель', 'Артур Хейли', 512)

print(book1)
print(book1 + book2)
print(book2 + book3)

# Задание №2

# 4. Реализуйте @classmethod с именем from_birth_year,
# который принимает имя и год рождения,
# а затем создает объект Person, вычисляя возраст на основе текущего года (2025).
# 5. Протестируйте все методы.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f'Имя: {self.name}, Возраст:{self.age}'

    @staticmethod
    def is_adult(age):
        if  age >= 18:
            return True
        else:
            return False

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = 2025 - birth_year
        return cls(name,age)

person1 = Person('Mirai', 27)
print(person1.info)
print(Person.is_adult(23))
print(Person.is_adult(12))
person2 = Person.from_birth_year('Rei', 2000)
print(person2.info)
