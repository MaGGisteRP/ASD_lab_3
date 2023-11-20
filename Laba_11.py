def quicksort(arr):
    # Если длина массива меньше или равна 1, то он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент
    pivot = arr[len(arr) // 2]

    # Разделяем массив на две части: элементы меньше опорного и элементы больше опорного
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортируем части массива
    return quicksort(left) + middle + quicksort(right)

sequence = [9, 3, 7, 5, 1, 6, 8, 2, 4]
sorted_sequence = quicksort(sequence)
print(sorted_sequence)