#
# num1 = int(input("Введите четыре целых числа: "))
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
#
# max_num = max(num1, num2, num3, num4)
# min_num = min(num1, num2, num3, num4)
#
# third_largest = None # Переменная принимает "пустоту", то есть не содержит какого либо значения
#
# # Проходим по числам и ищем число, которое не равно ни максимальному, ни минимальному
# for num in (num1, num2, num3, num4):
#     if num != max_num and num != min_num:
#         third_largest = num
#         break
#
# #Третье максимальное число с конца
#
# if third_largest is not None:
#     print("Третье по величине число:", third_largest)
# else:
#     print("Третье по величине число не существует, так как все числа равны.")
#

# Запрашиваем у пользователя четыре целых числа
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
num3 = int(input("Введите третье целое число: "))
num4 = int(input("Введите четвертое целое число: "))

# Ищем максимальное число
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
if num4 > max_num:
    max_num = num4

# Ищем минимальное число
min_num = num1
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4

# Ищем третье по величине число
third_largest = None
for num in (num1, num2, num3, num4):
    if num != max_num and num != min_num:
        if third_largest is None or num > third_largest:
            third_largest = num

# Выводим результат
if third_largest is not None:
    print(f"Третье по величине число: {third_largest}")
else:
    print("Третье по величине число не существует, так как все числа равны.")