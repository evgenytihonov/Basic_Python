def run():
    numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print("Старый список: ", numbers)
    print("Обработанный список: ", [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]])


run()
