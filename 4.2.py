# def search_substring(строка, поиск_подстроки):
#     return поиск_подстроки in строка
#
# строка = "Привет, меня зовут Паша!"
# поиск_подстроки = "студент"
#
# if search_substring(строка, поиск_подстроки):
#     print("Подстрока найдена")
# else:
#     print("Подстрока не найдена")


def поиск_подстроки(строка_поиска, подстрока_для_поиска):
    длина_строки_поиска = len(строка_поиска)
    длина_подстроки = len(подстрока_для_поиска)

    i = 0
    while i + длина_подстроки <= длина_строки_поиска:         # цикл, который продолжается до тех пор, пока значение i + "строка_поиска" не выходит за границы строки. Это нужно, чтобы осталось достаточное кол-во символов в строке, чтобы сравнивать с подстрокой
        совпадение = True                                     # используется для отслеживания совпадения подстроки с текущим фрагментом строки.
        for j in range(длина_подстроки):                      # цикл, который бежит по символам подстроки
            if строка_поиска[i + j] != подстрока_для_поиска[j]:
                совпадение = False                            # если хотя бы одна пара символов не совпадает, устанавливаем флаг "совпадение" в False и прерываем вложенный цикл.
                break

        if совпадение:                            # если флаг "совпадение" остается True после завершения вложенного цикла, значит, все символы подстроки совпали с соответствующими символами строки.
            return i, i + длина_подстроки - 1  # Возвращаем диапазон индексов подстроки в строке

        i += 1                      # если совпадения не найдено, то увеличиваем i и продолжаем поиск.

    return -1, -1                    # Вхождение не найдено

# Пример использования
строка_для_поиска = "на дворе трава, на траве дрова"
подстрока_поиска = "траве"
начало, конец = поиск_подстроки(строка_для_поиска, подстрока_поиска)

if начало != -1:
    print(f"Вхождение подстроки найдено с {начало} по {конец}")
else:
    print("Вхождение подстроки не найдено")