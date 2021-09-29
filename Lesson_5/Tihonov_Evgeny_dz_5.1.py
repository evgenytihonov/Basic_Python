def odd_num_generator(end):
    end = int(end)
    for num in range(1, end + 1):
        if num % 2:
            yield num


n = int(input('До какого числа считать нечетные числа? '))
print(*odd_num_generator(n))
