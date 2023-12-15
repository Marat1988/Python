def drawSquare(length, symbol, fill=True):
    if not (isinstance(symbol, str)) or len(str(symbol)) > 1:
        raise Exception("Введен не символ. Введите символ, например *")
    for row in range(length):
        for col in range(length):
            if fill:
                print(symbol + " ", end='')
            else:
                if (row == 0) | (row == length - 1) | (col == 0) | (col == length - 1):
                    print(symbol + " ", end='')
                else:
                    print("  ", end='')
        print('')


drawSquare(5, '*', False)
print("\n")
drawSquare(5, '*', True)
