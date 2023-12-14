begin = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона диапазона: "))
for i in range(min(begin, end + 1), max(begin, end + 1)):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
