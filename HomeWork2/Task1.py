def countDigitInNumber(number):
    if not (isinstance(number, int)):
        raise Exception("Введено не целое число")
    else:
        number_as_string = str(number)
        return len(set(number_as_string))


print(countDigitInNumber(3456))
