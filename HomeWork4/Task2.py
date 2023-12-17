import time


def is_prime(number):
    if number < 2 and isinstance(number, int):
        raise Exception("Введенное число должно быть больше 2")
    if not (isinstance(number, int)):
        raise Exception("Введено не число!")
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def print_total_time(func):
    def wrapper():
        start_time = time.time()
        print("Список простых чисел", func())
        end_time = time.time()
        print("Затраченное время: ", end_time - start_time)

    return wrapper


@print_total_time
def findPrimeNumbers():
    list_prime_number = []
    for i in range(2, 1_0001):
        if is_prime(i):
            list_prime_number.append(i)
    return list_prime_number


findPrimeNumbers()
