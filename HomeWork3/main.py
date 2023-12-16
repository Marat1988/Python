import pickle

class Car:
    def __init__(self, model, year_release, manufacturer, engine_capacity, color, price):
        self.__model = model
        self.__year_release = year_release
        self.__manufacturer = manufacturer
        self.__engine_capacity = engine_capacity
        self.__price = price
        self.__color = color

    # Сетеры
    def set_model(self, new_model):
        self.__model = new_model

    def set_year_release(self, new_year_release):
        self.__year_release = new_year_release

    def set_manufacturer(self, new_manufacturer):
        self.__manufacturer = new_manufacturer

    def set_engine_capacity(self, new_engine_capacity):
        self.__engine_capacity = new_engine_capacity

    def set_price(self, new_price):
        self.__price = new_price

    def set_color(self, new_color):
        self.__color = new_color

    def get_model(self):
        return self.__model

    # Гетеры
    def get_year_release(self):
        return self.__year_release

    def get_manufacturer(self):
        return self.__manufacturer

    def get_engine_capacity(self):
        return self.__engine_capacity

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    # Сохранение объекта в файл. Сериализация и десериализация

    def serialize(self):
        with open("data.pickle", "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def deserialize():
        with open("data.pickle", "rb") as f:
            car = pickle.load(f)
        print(car)

    # toString
    def __str__(self):
        return (f"Модель: {self.__model} \nГод выпуска: {self.__year_release}"
                f"\nПроизводитель: {self.__manufacturer} \nОбъем двигателя: {self.__engine_capacity}"
                f"\nЦена: {self.__price} \nЦвет: {self.__color}")


car1 = Car("Mercedes-Benz C-Класс AMG 43 AMG", 2016, "Mersenes", 3, "Серый", 4000000)
car1.serialize()
car1.deserialize()

