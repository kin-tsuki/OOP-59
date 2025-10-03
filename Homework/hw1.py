class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def age(self):
        current_year = 2025
        span = current_year - self.year
        return print(f'Книга "{self.name}" была впервые опубликована {span} лет назад.')

m_and_m = Book('Мастер и Маргарита', 'Михаил Булгаков', 1967)
xmas_carol = Book('Рождественская песнь в прозе', 'Чарльз Диккенс', 1843)

m_and_m.age()
xmas_carol.age()

