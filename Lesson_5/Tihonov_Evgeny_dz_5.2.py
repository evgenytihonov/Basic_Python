def odd_num():
    upper = 1 + int(input('До какого числа считать нечетные числа? '))
    lower = 1

    for i in range(lower, upper):
        if i % 2:
            print(i)


odd_num()
