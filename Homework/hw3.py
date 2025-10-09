class Car:
    def __init__(self, brand, fuel_level=0):
        self.brand = brand
        self._fuel_level = fuel_level
        self.__engine_status = False

    def start_engine(self):
        if self._fuel_level > 0:
            self.__engine_status = True
            print('Двигатель запущен!')
        else:
            print('Невозможно завести двигатель — нет топлива')

    def stop_engine(self):
        self.__engine_status = False

    def drive(self, distance):
        fuel_needed = distance * 0.1
        if self.__check_fuel(fuel_needed):
            self._fuel_level -= fuel_needed
            print(f'Проехали {distance} км, осталось {self._fuel_level}л топлива.')
        elif self._fuel_level < fuel_needed:
            print('Недостаточно топлива для поездки!')

    def refuel(self, amount):
        self._fuel_level += amount
        return self._fuel_level

    def get_status(self):
        if self.__engine_status:
            engine_status = 'Включен'
        else:
            engine_status = 'Выключен'
        return (f'Марка: {self.brand} | Топливо: {self._fuel_level} | '
                f'Двигатель: {engine_status}')

    def __check_fuel(self, fuel_needed):
        return self._fuel_level >= fuel_needed


car = Car('Lexus')
car.refuel(40)
car.start_engine()
car.drive(300)
print(car.get_status())



