vowels = ["a", "o", "e", "i", "u", "y"]
file = open("task1.txt", "r")
arr = file.read().split("\n")
str = ' '.join(arr)
print(arr)
print(str)
countVowel = 0
countConsonant = 0
countNumber = 0
for char in str:
    if char.lower() in vowels:
        countVowel += 1
    if char.isdigit():
        countNumber += 1
    if char.lower().isalpha() and char.lower() not in vowels and not (char.isdigit()):
        countConsonant += 1

fileStatistic = open("task1_statistic.txt", "w", encoding="utf-8")
fileStatistic.write(f"Количество символов: {len(str)}")
fileStatistic.write(f"\nКоличество строк: {len(arr)}")
fileStatistic.write(f"\nКоличество гласных: {countVowel}")
fileStatistic.write(f"\nКоличество согласных: {countConsonant}")
fileStatistic.write(f"\nКоличество цифр: {countNumber}")
print("Статистика записана в файл task1_statistic.txt")

file.close()
fileStatistic.close()