def isPalindrome(number):
    if not (isinstance(number, int)):
        raise Exception("Введено не целое число")
    else:
        number_as_string = str(number)
        return number_as_string[::-1] == number_as_string


print(isPalindrome(123321))
print(isPalindrome(546645))
print(isPalindrome(421987))
