def selection_sort(sequence):
    for i in range(len(sequence)):
        min_index = i #пусть первый элемент минимален

        for j in range(i+1, len(sequence)): #если найдется такой индекс минимальнее минимального зменим
            if sequence[j] < sequence[min_index]:
                min_index = j

        sequence[i], sequence[min_index] = sequence[min_index], sequence[i] #обмен значениями между минимальным элементом и элементом с текущим индексом.u

    return sequence
sequence = [1,2, 35, 6, 45, 46, 4, 56, 0, 234]
print(selection_sort(sequence))