class Hero:
    # Конструкция класса
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # methods of the class
    def action(self):
        return print(f'{self.name} base action!!')

    def cast_spell(self):
        return print(f'Fire bool')

# за пределами класса def -> функция
# внутри класса def -> метод

kirito = Hero('Kirito', 100, 1000)
asuna = Hero('Asuna', 115, 900)

kirito.action()
asuna.cast_spell()

print(asuna.name)

