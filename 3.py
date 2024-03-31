# import random
# import timeit
#
# def сортировка_методом_пузырька(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
# def прямое_включение(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#
# def прямой_выбор(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
# def шейкерная_сортировка(arr):
#     n = len(arr)
#     swapped = True
#     start = 0
#     end = n - 1
#     while swapped:
#         swapped = False
#         for i in range(start, end):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swapped = True
#         if not swapped:
#             break
#         swapped = False
#         end = end - 1
#         for i in range(end - 1, start - 1, -1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swapped = True
#         start = start + 1
#
# def методом_шелла(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
# def метод_хоара(arr):
#     if len(arr) <= 1:
#         return arr
#     опорный_элемент = arr[len(arr) // 2]
#     left = [x for x in arr if x < опорный_элемент]
#     right = [x for x in arr if x > опорный_элемент]
#     return метод_хоара(left) + [опорный_элемент] + метод_хоара(right)
#
#
#
#
#
#
#
#
#
# def генерация_массива(size):
#     return [random.randint(0, 100) for _ in range(size)]  # генерация случайных чисел от 0 до 100
#
# def время_выполнения(func, arr):
#     return timeit.timeit(lambda: func(arr.copy()), number=1)
#
#
# if __name__ == "__main__":                    # Это условие проверяет, запущен ли скрипт напрямую (не импортирован как модуль). Если это условие выполняется, то код внутри этого блока будет выполнен.
#     размер_массива = 1000  # Размер массива
#
#     # Генерация случайного массива
#     генерация_массива = [random.randint(0, 100) for _ in range(размер_массива)]
#
#     # Измерение времени выполнения сортировки пузырьком
#     все_сортировки = [сортировка_методом_пузырька, прямое_включение, прямой_выбор, шейкерная_сортировка, методом_шелла, метод_хоара] # список различных функций сортировки
#
#     for сортировка in все_сортировки:
#         время = время_выполнения(сортировка, генерация_массива)
#         print(f"{сортировка.__name__}: {время} сек")



import random
import timeit

def сортировка_методом_пузырька(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def прямое_включение(arr):          # (вставками!!)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def прямой_выбор(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def шейкерная_сортировка(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1

def методом_шелла(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def метод_хоара(arr):
    if len(arr) <= 1:
        return arr
    опорный_элемент = arr[len(arr) // 2]
    left = [x for x in arr if x < опорный_элемент]
    right = [x for x in arr if x > опорный_элемент]
    return метод_хоара(left) + [опорный_элемент] + метод_хоара(right)

def генерация_массива(size):
    return [random.randint(0, 100) for _ in range(size)]  # генерация случайных чисел от 0 до 100

def время_выполнения(func, arr):
    return timeit.timeit(lambda: func(arr.copy()), number=1)

if __name__ == "__main__":
    размер_массива = 10000  # Размер массива
    кол_во_повторений = 1  # Количество повторений для каждой сортировки

    # Генерация случайного массива
    генерация_массива = генерация_массива(размер_массива)

    # Измерение времени выполнения для каждой сортировки
    все_сортировки = [сортировка_методом_пузырька, прямое_включение, прямой_выбор, шейкерная_сортировка, методом_шелла, метод_хоара]

    for сортировка in все_сортировки:
        время_выполнения_среднее = sum(время_выполнения(сортировка, генерация_массива) for _ in range(кол_во_повторений)) / кол_во_повторений
        print(f"{сортировка.__name__}: {время_выполнения_среднее} сек")


# Общий порядок временной сложности различных алгоритмов сортировки:
#
# Сортировка методом Хоара (быстрая сортировка) - O(n log n) в среднем случае
# Сортировка методом Шелла - O(n log^2 n)
# Прямое включение - O(n^2)
# Прямой выбор - O(n^2)
# Шейкерная сортировка - O(n^2)
# Сортировка методом пузырька - O(n^2)




# Быстрая сортировка (Сортировка Хоара):
# В среднем случае: O(n log n)
# В худшем случае: O(n^2)


# Сортировка методом Шелла:
# В среднем случае: О(n log^2 n) (но это сложно точно оценить, так как зависит от конкретной последовательности промежутков)


# Прямое включение (вставками!!):
# В среднем случае: O(n^2)
# В худшем случае: O(n^2)


# Прямой выбор (Selection Sort):
# В среднем случае: O(n^2)
# В худшем случае: O(n^2)


# Шейкерная сортировка (Cocktail Shaker Sort):
# В среднем случае: O(n^2)
# В худшем случае: O(n^2)


# Сортировка методом пузырька (Bubble Sort):
# В среднем случае: O(n^2)
# В худшем случае: O(n^2)



