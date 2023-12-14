try:
    meters = int(input("Введите количество метров: "))
    print("Мили: ", meters * 0.00062)
    print("Дюймы ", meters * 10)
    print("Ядра ", meters * 1.09)
except Exception as err:
    print("Сведения об исключении: ", err)

