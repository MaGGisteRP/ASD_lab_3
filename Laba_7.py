def shell_sort(sequence):
    n = len(sequence)
    gap = n // 2 #делим последовательность на две части

    while gap > 0: #сортируем методом вставки
        for i in range(gap, n):
            temp = sequence[i]
            j = i

            while j >= gap and sequence[j - gap] > temp:
                sequence[j] = sequence[j - gap]
                j -= gap

            sequence[j] = temp

        gap //= 2

    return sequence

sequence = [1,2, 35, 6, 45, 46, 4, 56, 0, 56, 234]
print(shell_sort(sequence))