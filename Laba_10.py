def merge_sort(arr):
    # Базовый случай: если длина массива <= 1, то он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две части
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно(функция вызывает себя) применяем сортировку к двум половинам
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Объединяем отсортированные половины
    merged_arr = merge(left_half, right_half)

    return merged_arr


def merge(left, right):
    # Создаем итоговый массив для объединения двух половин
    merged = []

    # Инициализируем указатели на начало каждой половины
    i = j = 0

    # Объединяем элементы из каждой половины, сравнивая их значения
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левой половины
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из правой половины
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Пример использования
sequence = [9, 3, 7, 5, 1, 6, 8, 2, 4]
sorted_sequence = merge_sort(sequence)
print(sorted_sequence)