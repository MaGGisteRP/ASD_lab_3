def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    l = 2 * i + 1  # Левый потомок
    r = 2 * i + 2  # Правый потомок

    # Если левый дочерний элемент существует и больше корня
    if l < n and arr[i] < arr[l]:
        largest = l

    # Если правый дочерний элемент существует и больше корня
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмен корня с наибольшим элементом

        # Рекурсивно строим пирамиду для поддерева
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Построение Max Heap (построение пирамиды)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из пирамиды по одному
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Обмен последнего элемента с корнем
        heapify(arr, i, 0)

    return arr


# Пример использования:
sequence = [5, 9, 3, 1, 8, 6, 4, 2, 7]
sorted_sequence = heap_sort(sequence)
print(sorted_sequence)