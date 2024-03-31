from collections import deque

queue = deque() # очередь
queue.append(1)
queue.append(2)
queue.append(3)


print(queue)

первый_элемент = queue[0]
print(первый_элемент)

удалить_элемент = queue.popleft()
print(queue)

размер = len(queue)
print(размер)

# Проверка, является ли очередь пустой
проверка_очереди = len(queue) == 0
print(проверка_очереди)