import random
maxItems = 20
listBeginRange = -10
listEndRange = 10
list1 = []
list2 = []
for i in range(maxItems):
    list1.append(random.randrange(listBeginRange, listEndRange, 1))
    list2.append(random.randrange(listBeginRange, listEndRange, 1))
list3 = list1 + list2
print("Первый список: ", list1)
print("Второй список: ", list2)
print("Элементы обоих списков: ", list3)
print("Элементы обоих списков без повторений: ", list(set(list3)))
print("Общие для двух списков: ", list(set(list1) & set(list2)))
print("Уикальные элементы каждого из списков: ", list(set(list1)) + list(set(list2)))
list3.clear()
list3.append(min(list1))
list3.append(max(list1))
list3.append(min(list2))
list3.append(max(list2))
print("Минимальное и максимальное значение каждого из списка: ", list3)

