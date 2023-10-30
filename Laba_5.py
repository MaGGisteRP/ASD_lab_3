def vstavka_sort(sequence):
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1 # предыдущий элемент отсортированной части

        while j >= 0 and sequence[j] > key: # сравниваю след. элемент с отсортированной частью
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j + 1] = key

    return sequence

sequence = [1,2, 35, 6, 46, 4, 56]
print(vstavka_sort(sequence))