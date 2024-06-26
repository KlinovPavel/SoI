# # Создаем матрицу N(6,6)
# матрица_6х6 = [
#     [1, 2, 3, 4, 5, 6],
#     [7, 8, 9, 10, 11, 12],
#     [13, 14, 15, 16, 17, 18],
#     [19, 20, 21, 22, 23, 24],
#     [25, 26, 27, 28, 29, 30],
#     [31, 32, 33, 34, 35, 36]
# ]
#
# # Задаем условия
# K = 2
#
# # Формируем одномерный массив Y
# новый_массив = []
#
# # for i in range(len(матрица_6х6)):
# #     for j in range(i + 1, len(матрица_6х6[i])):
# #         if матрица_6х6[i][j] <= K and матрица_6х6[i][j] > (i + j):
# #             новый_массив.append(матрица_6х6[i][j])
#
# for i in range(len(матрица_6х6)):
#     for j in range(len(матрица_6х6[i])):
#         print(f"Проверка для i={i}, j={j}: матрица_6х6[{i}][{j}] = {матрица_6х6[i][j]}")
#         if матрица_6х6[i][j] <= K and матрица_6х6[i][j] > (i + j):
#             новый_массив.append(матрица_6х6[i][j])
#
#
#
# # Выводим матрицу N
# print("\nМатрица N(6,6):")
# for строка in матрица_6х6:
#     print(строка)
#
# # Выводим одномерный массив Y
# print("\nОдномерный массив Y:")
# print(новый_массив)
#


# Создаем матрицу N(6,6)
матрица_6х6 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]

# Задаем условия
K = 2

# Формируем одномерный массив Y
новый_массив = []

for i in range(len(матрица_6х6)):
    for j in range(len(матрица_6х6[i])):
        print(f"Проверка для i={i}, j={j}: матрица_6х6[{i}][{j}] = {матрица_6х6[i][j]}")
        if j >= i and матрица_6х6[i][j] <= K and матрица_6х6[i][j] > (i + j):
            новый_массив.append(матрица_6х6[i][j])

# Выводим матрицу N
print("Матрица N(6,6):")
for строка in матрица_6х6:
    print(строка)

# Выводим одномерный массив Y
print("\nОдномерный массив Y:")
print(новый_массив)
