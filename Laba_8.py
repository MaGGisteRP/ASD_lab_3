def bitwise_sort(sequence):
    max_num = max(sequence)
    num_bits = max_num.bit_length()  # Количество битов, необходимых для представления max_num

    for bit_index in range(num_bits):
        # сортировка последовательности на основе текущего бита с помощью счетной сортировки
        zeros = []
        ones = []

        for num in sequence:
            if (num >> bit_index) & 1:  # Извлекаем бит по текущему индексу
                ones.append(num)
            else:
                zeros.append(num)

        # Обновляем последовательность отсортированными числами
        sequence = zeros + ones

    return sequence

sequence = [1,2, 35, 6, 45, 46, 4, 56, 0, 56, 234]
print(bitwise_sort(sequence))